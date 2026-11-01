#!/usr/bin/env python3
"""Verifica páginas geradas, assets, âncoras, headings e build determinístico."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PAGES = [ROOT / 'index.html', ROOT / 'produtos/midia-instagram/index.html']


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids, self.references, self.headings = set(), [], []
        self.h1_count = 0
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'ID duplicado: {attrs["id"]}'
            self.ids.add(attrs['id'])
        for attr in ('href', 'src'):
            if attr in attrs:
                self.references.append(attrs[attr])
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            level = int(tag[1])
            previous = self.headings[-1] if self.headings else 0
            assert level <= previous + 1, f'Hierarquia de headings: {previous} → {level}'
            self.headings.append(level)
            self.h1_count += tag == 'h1'
        if tag == 'img':
            assert 'alt' in attrs and 'width' in attrs and 'height' in attrs, 'Imagem sem alt/dimensões'


def check():
    original = {path: path.read_bytes() for path in PAGES}
    subprocess.run([sys.executable, str(ROOT / 'scripts/build.py')], check=True)
    for path in PAGES:
        assert path.read_bytes() == original[path], f'Página desatualizada: {path}'
    documents = {path: Document(path.read_text(encoding='utf-8')) for path in PAGES}
    count = 0
    for path, document in documents.items():
        assert document.h1_count == 1, f'{path}: deve haver exatamente um h1'
        assert {'site-nav', 'conteudo', 'inicio', 'propagator'} <= document.ids
        for reference in document.references:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                assert url.scheme == 'https', f'Protocolo externo inesperado: {reference}'
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            assert target.is_relative_to(ROOT), f'Referência fora do site: {reference}'
            if target.is_dir():
                target /= 'index.html'
            assert target.is_file(), f'{path.name}: destino ausente: {reference}'
            if url.fragment:
                target_document = documents.get(target)
                assert target_document, f'Âncora para documento desconhecido: {reference}'
                assert unquote(url.fragment) in target_document.ids, f'Âncora ausente: {reference}'
            count += 1
        print(f'OK: {path.relative_to(ROOT)} — h1 único, hierarquia, imagens e links locais')
    ET.parse(ROOT / 'assets/favicon.svg')
    ET.parse(ROOT / 'templates/components/diagram.svg')
    for script in ('site.js', 'contact-config.js'):
        subprocess.run(['node', '--check', str(ROOT / 'assets' / script)], check=True)
    contact = (ROOT / 'assets/contact-config.js').read_text()
    assert "whatsappNumber: ''" in contact, 'Revisar configuração de contato antes de disponibilizar'
    home = PAGES[0].read_text(encoding='utf-8')
    assert 'disabled data-whatsapp' in home
    assert 'Site em construção' not in home
    print(f'OK: {count} referências locais; SVGs válidos; sintaxe JS; WhatsApp indisponível; build reproduzível')


if __name__ == '__main__':
    check()
