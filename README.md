# Deutera — página em construção

Página institucional provisória da Deutera, empresa de tecnologia e inteligência artificial. Avisa que o site está em construção, sem apresentar serviços, preços ou datas de lançamento ainda não definidos.

## Arquivos

```text
webpage/
├── index.html   # página completa, com CSS incorporado
└── README.md    # instruções de edição e publicação
```

O HTML está em português brasileiro, é responsivo e não depende de JavaScript, fontes externas, frameworks ou instalação de pacotes. Não contém formulários, rastreamento, pagamentos ou dados pessoais. A assinatura tipográfica “deutera.” é texto, não um logotipo oficial.

## Visualizar e editar

Abra `index.html` diretamente no navegador. Para servir localmente, a partir desta pasta:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Acesse `http://127.0.0.1:8000`. Encerre com `Ctrl+C`.

Textos e estilos ficam no próprio `index.html`. As cores principais são definidas em `:root`. Depois de editar, confira desktop e celular, contraste, legibilidade e ausência de rolagem horizontal.

## GitHub e publicação

Organização indicada pelo usuário: https://github.com/deutera-ai

Repositório sugerido para o site da organização: **deutera-ai/deutera-ai.github.io**. Usando GitHub Pages, o endereço padrão será `https://deutera-ai.github.io/` após habilitação e conclusão da publicação. Não foi configurado domínio próprio.

**Estado atual:** arquivos locais criados; publicação ainda não realizada. A consulta pública não mostrou repositórios na organização e o executor não possui autenticação GitHub utilizável. Isso não comprova ausência de repositórios privados ou permissão para criá-los.

### Primeira publicação pelo terminal normal

São necessários Git, GitHub CLI (`gh`), identidade de commit configurada por você e uma conta com permissão para criar/publicar repositórios na organização. Autentique-se pelo fluxo do GitHub; não coloque tokens neste diretório ou no chat:

```bash
gh auth login
gh repo list deutera-ai
```

Se o repositório sugerido **ainda não existir**, execute a partir de `deutera/webpage/`, somente para a primeira publicação:

```bash
git init -b main
git add index.html README.md
git commit -m "Adiciona página Deutera em construção"
gh repo create deutera-ai/deutera-ai.github.io --public --source=. --remote=origin --push
```

Não execute esses passos novamente sobre um repositório já configurado. Se o destino já existir, inspecione-o antes e preserve seus arquivos; não use push forçado.

Depois, no GitHub, abra **Settings → Pages**, selecione publicação por branch, **main** e pasta **/ (root)**. Ou, caso Pages ainda não esteja habilitado e sua conta possua permissão:

```bash
gh api --method POST repos/deutera-ai/deutera-ai.github.io/pages \
  -f 'build_type=legacy' \
  -f 'source[branch]=main' \
  -f 'source[path]=/'
```

Confira o resultado em Settings → Pages e abra o endereço informado pelo GitHub. Um push não comprova, por si só, que o site já está disponível; a publicação pode levar alguns minutos ou ser limitada por políticas da organização.

### Atualizações posteriores

Com este diretório já conectado ao repositório correto:

```bash
git add index.html README.md
git commit -m "Atualiza página institucional"
git push
```

## O que pode ir para o repositório público

Somente `index.html` e este README. O repositório do site deve permanecer separado do restante do projeto. Não publicar `finance/`, comprovantes, configurações locais, tokens, históricos de clientes ou arquivos de trabalho privados. Evite `git add .` a partir da raiz do projeto.

Nenhuma API financeira, configuração de cron ou conteúdo dos clientes foi alterado para criar esta página.
