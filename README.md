# DEUTERA — Site Institucional V1

Site estático em português brasileiro para apresentar a DEUTERA como empresa de Dados e Inteligência Computacional. Preserva fundo verde-preto, tipografia de sistema, branco suave, verde-claro e o símbolo de Feynman do logotipo oficial.

## Arquitetura e rotas

Sem framework, dependências de frontend ou pacotes para instalar. HTML, CSS, JavaScript progressivo e SVG. As páginas geradas ficam versionadas, prontas para GitHub Pages e hospedagem estática com domínio próprio.

- `/` → `index.html`: Início, segmentos potenciais, Quem somos, fundadores, Produtos e Contato.
- `/#quem-somos`, `/#produtos`, `/#contato`: seções institucionais.
- `/produtos/midia-instagram/` → `produtos/midia-instagram/index.html`: página completa da proposta Mídia Instagram, com acesso direto e atualização sem roteador JavaScript.

Os links locais são relativos; não há domínio fixado no código. Nenhuma configuração de DNS, HTTPS, domínio ou GitHub Pages foi alterada. Não há `CNAME` neste checkout; configurações externas existentes devem ser preservadas.

## Arquivos

```text
index.html                           # página inicial gerada
produtos/midia-instagram/index.html   # página de produto gerada
assets/
  logo_oficial.png                    # imagem oficial existente, preservada
  Edson.png, Lucas1.png               # fotos dos fundadores fornecidas pelo responsável
  favicon.svg                        # símbolo vetorial da identidade
  site.css                           # estilos compartilhados e responsividade
  site.js                            # menu, ano e ativação futura do contato
  contact-config.js                  # configuração única do WhatsApp
scripts/
  build.py                           # gerador, biblioteca padrão do Python
  check.py                           # verificação do site gerado (Python + Node)
templates/
  base.html                          # documento e metadados SEO/Open Graph
  home.html                          # seções institucionais
  product.html                       # conteúdo Mídia Instagram
  components/
    header.html, footer.html          # navegação e identidade compartilhadas
    hero.html, diagram.svg           # hero e propagador animado
    founder.html, contact.html        # cards e contato
    segments.html, about.html         # segmentos e apresentação institucional
    products.html                    # categoria e produto inicial
```

O gerador simples evita divergência de cabeçalhos, rodapés e outros blocos. O HTML essencial e os links funcionam sem JavaScript. Nesse caso, a navegação mobile permanece expandida e o ano usa seu fallback de 2026.

## Editar e visualizar

Edite os templates, estilos e scripts; gere os HTMLs após alterações:

```bash
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Abra `http://127.0.0.1:8000/` e `http://127.0.0.1:8000/produtos/midia-instagram/`.

Também é possível abrir `index.html` diretamente no navegador. Os links entre páginas apontam explicitamente para os arquivos `index.html`, evitando listagem de diretórios ao navegar por `file://`.

Não é necessário executar Python no GitHub Pages: ele publica os HTMLs já gerados. O gerador não altera configurações de publicação.

## Contato

`assets/contact-config.js` centraliza `whatsappNumber`, inicialmente vazio. O botão é nativamente desabilitado e informa “Atendimento via WhatsApp — Em breve”. Não há formulário, backend simulado ou número fictício.

Quando houver número oficial confirmado, preencha somente dígitos (código do país + DDD + número). Um valor de 10 a 15 dígitos ativa o link `wa.me` via JavaScript e atualiza a mensagem de disponibilidade. A checagem atual exige o contato vazio, conforme o escopo da V1; atualize essa expectativa ao disponibilizar o canal real.

## Conteúdo e pendências editoriais

- Os dados acadêmicos e profissionais dos fundadores foram fornecidos pelo responsável pelo site. Não foram criados clientes, métricas, depoimentos, prêmios ou fotografias.
- Os cards usam as fotos fornecidas em `Edson.png` e `Lucas1.png`, com recorte via CSS, dimensões reservadas, texto alternativo e carregamento adiado.
- As etapas do produto são uma proposta de funcionamento; benefícios são potenciais, sem garantias de alcance, seguidores ou desempenho.
- A coordenação de pós-graduação em Ciência de Dados mencionada no briefing não foi confirmada. Por isso, a versão pública apresenta Edson Otoniel apenas como professor da UFCA, sem essa função de coordenação.
- Fonte oficial consultada: [UFCA — Conheça os cursos de graduação: Banco de Dados](https://www.ufca.edu.br/noticias/conheca-os-cursos-de-graduacao-da-ufca-banco-de-dados/). Ela identifica Otoniel como coordenador de graduação em Banco de Dados, com ênfase em Ciência de Dados. Isso não confirma coordenação de pós-graduação. Confirmar com o responsável antes de acrescentar a atribuição solicitada.

## Acessibilidade e movimento

HTML semântico, link para pular ao conteúdo, foco visível, menu mobile com `aria-expanded`, fechamento por Escape, botões com área de interação adequada, texto alternativo e dimensões da marca. Os elementos decorativos usam `aria-hidden` e não capturam eventos.

O propagador SVG tem pulso de três segundos, sem GIF/vídeo. Com `prefers-reduced-motion`, o pulso e a rolagem suave são desativados. O hero limita o recorte do SVG à sua própria área.

## Validação realizada

`python3 scripts/check.py` passou com:

- Build reproduzível das duas páginas.
- 42 referências locais verificadas, incluindo arquivos e âncoras entre páginas.
- Um h1 por página, hierarquia de títulos sem saltos e imagens com alt/dimensões.
- SVGs bem formados e IDs sem duplicidade.
- Sintaxe de `site.js` e `contact-config.js` validada pelo Node.
- WhatsApp vazio e botão desabilitado; ausência da mensagem antiga de construção.

`git diff --check` passou.

Também foi verificada a sintaxe do CSS com tinycss2. Os pares de cores de texto principais sobre os dois fundos sólidos têm contraste calculado de pelo menos 9,15:1; isso não substitui a revisão visual das composições sobre o SVG.

**Limitação real:** a inspeção visual e os testes de interação no navegador não foram concluídos. Neste ambiente, Chromium/Chrome falharam por restrições de operações do sistema e o Firefox encerrou ao iniciar. Não foi validada navegação real por teclado, console, animação ou ausência de overflow por medição no navegador.

Antes de publicar, conferir ambas as rotas em 320, 390, 768 e 1440 px: menu aberto/fechado, Tab/Escape, recarga direta do produto, todos os CTAs, legibilidade do hero, ausência de rolagem horizontal e preferência de movimento reduzido. Repetir sem JavaScript para conferir o fallback. Os breakpoints foram implementados em CSS, mas não substituem essa conferência.

## Publicação

O remoto configurado é `https://github.com/deutera-ai/deutera-ai.github.io.git`. Preservar o método atual de publicação. Nenhum push foi realizado nesta entrega.

Depois de revisar e validar localmente, os arquivos públicos desta V1 são:

```bash
git add index.html README.md produtos/midia-instagram/index.html \
  assets/logo_oficial.png assets/favicon.svg assets/site.css assets/site.js \
  assets/Edson.png assets/Lucas1.png \
  assets/contact-config.js scripts/build.py scripts/check.py templates/
git commit -m "Implementa site institucional Deutera V1"
git push
```

Revisar `git diff --cached` antes do commit. Não adicionar arquivos do projeto pai, documentos privados ou outras imagens de trabalho de `assets/` que não sejam usadas no site. Um push não comprova o término da implantação; verificar o resultado no GitHub Pages e no domínio configurado.

A apresentação dos fundadores está temporariamente comentada em `templates/components/about.html`. A seção Quem somos continua visível; nomes, biografias, fotos e links dos fundadores não são renderizados. Recursos originais foram preservados. Para restaurar, remover o comentário e executar `python3 scripts/build.py`.
