#!/usr/bin/env python3
"""Renderiza as duas páginas estáticas; usa apenas a biblioteca padrão."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FOUNDER_PHOTOS = {
    'EO': ('Edson.png', 1122, 1402),
    'LS': ('Lucas1.png', 1198, 1313),
}
FOUNDER_LINKEDIN = {
    'EO': 'https://www.linkedin.com/in/edson-otoniel-b877a5115/',
    'LS': 'https://www.linkedin.com/in/lucas-alves-souza/',
}


def render(template_name, **values):
    source = (ROOT / 'templates' / template_name).read_text(encoding='utf-8')
    def substitute(match):
        key = match[1]
        if key not in values:
            raise ValueError(f'{template_name}: valor ausente para {key}')
        return str(values[key])
    return re.sub(r'\{\{\s*(\w+)\s*\}\}', substitute, source)


def build():
    for product in (False, True):
        assets = '../../assets/' if product else 'assets/'
        home = '../../index.html' if product else ''
        values = dict(assets=assets, home=home, home_url='../../index.html' if product else 'index.html')
        header = render('components/header.html', **values,
                        home_current='' if product else ' aria-current="page"',
                        products_current=' aria-current="page"' if product else '')
        footer = render('components/footer.html', **values)
        diagram = render('components/diagram.svg')
        hero = render('components/hero.html', diagram=diagram,
            eyebrow='Mídia Digital / Mídia Instagram' if product else 'Dados e Inteligência Computacional',
            title='Sua marca merece uma presença digital <span>à altura do seu potencial.</span>' if product else 'Tecnologia, dados e <span>inteligência artificial.</span>',
            description='Produção inteligente de conteúdo para Instagram, combinando automação, criatividade e inteligência artificial para ajudar sua marca a se comunicar melhor e com mais consistência.' if product else 'Unimos ciência, tecnologia e criatividade para desenvolver soluções inteligentes que fortalecem marcas, automatizam processos e ampliam oportunidades de crescimento.',
            primary_link='../../index.html#contato' if product else '#produtos',
            primary_label='Entre em contato' if product else 'Conheça nossas soluções',
            secondary_link='#como-funciona' if product else '#quem-somos',
            secondary_label='Como funciona' if product else 'Quem somos',
            hero_class='hero--product' if product else '',
            caption='Criatividade, tecnologia e supervisão humana.' if product else 'Ciência de dados · Machine Learning · IA & automação')
        contact = render('components/contact.html') if not product else ''
        founders = ''
        for initials, name, bio in [
            ('EO', 'Edson Otoniel', '<p>Doutor em Física Nuclear pelo Instituto Tecnológico de Aeronáutica (ITA).</p><p>Professor da Universidade Federal do Cariri (UFCA). Sua trajetória acadêmica e científica contribui para o desenvolvimento de soluções fundamentadas em modelagem, análise de dados, inteligência artificial e Machine Learning.</p>'),
            ('LS', 'Lucas Souza', '<p>Doutor em Física Nuclear pelo Instituto Tecnológico de Aeronáutica (ITA).</p><p>Cientista de dados com vários anos de experiência profissional, atuando com análise de dados, modelos computacionais, Machine Learning e inteligência artificial.</p><p>Sua experiência reúne conhecimento científico e aplicação prática de soluções baseadas em dados.</p>')]:
            photo, photo_width, photo_height = FOUNDER_PHOTOS[initials]
            founders += render('components/founder.html', name=name, bio=bio,
                photo=assets + photo, photo_width=photo_width, photo_height=photo_height,
                linkedin=FOUNDER_LINKEDIN[initials])
        content = render('product.html' if product else 'home.html', hero=hero, contact=contact,
            segments=render('components/segments.html'),
            about=render('components/about.html', founders=founders),
            products=render('components/products.html'))
        page = render('base.html', **values, header=header, footer=footer, content=content,
            title='Mídia Instagram | DEUTERA' if product else 'DEUTERA | Dados e Inteligência Computacional',
            description='Conheça a proposta de Mídia Instagram da DEUTERA: conteúdo, planejamento e inteligência artificial com supervisão humana para a sua marca.' if product else 'Dados, ciência e inteligência artificial para fortalecer marcas e tornar negócios mais eficientes. Conheça a DEUTERA e suas soluções em mídia digital.',
            page_class='product-page' if product else 'home-page')
        destination = ROOT / ('produtos/midia-instagram/index.html' if product else 'index.html')
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(page, encoding='utf-8')
        print(f'Gerado: {destination.relative_to(ROOT)}')


if __name__ == '__main__':
    build()
