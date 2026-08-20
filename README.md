# Site do Nimo Chat

Site institucional do **Nimo Chat**, em onze idiomas: página inicial, Termos
de Uso, Política de Privacidade e a página de exclusão de conta que a Google
Play exige.

Estático puro. Sem framework, sem Node, sem nada rodando no servidor — são
arquivos HTML, CSS e imagens. O gerador em Python roda só na sua máquina,
antes do commit.

**No ar em:** https://mondaine25.github.io/NimoChat/

## Idiomas

Os mesmos onze do aplicativo: **en** (raiz do site), **pt**, es, de, tr, ru,
ar, he, hi, ja, ko. Árabe e hebraico são renderizados da direita para a
esquerda.

```
/                     inglês — raiz e hreflang x-default
/privacy.html  /terms.html  /delete-account.html
/pt/           português — inclui os três documentos legais traduzidos
/es/ /de/ /tr/ /ru/ /ar/ /he/ /hi/ /ja/ /ko/      página inicial traduzida
```

Os documentos legais existem por inteiro em **inglês e português**. Nos
outros nove idiomas, os links legais apontam para a versão em inglês — que é
exatamente o que a própria Política de Privacidade define como versão de
referência fora do Brasil. Se um dia quiser traduzir os documentos para mais
algum idioma, crie `conteudo/<idioma>/`, acrescente o idioma em `COM_LEGAL`
(em `textos.py`) e registre os nomes de arquivo em `ARQ_LEGAL` e
`FONTE_LEGAL` (em `construir.py`).

## Estrutura

```
construir.py          o gerador: HTML, SEO, navegação entre idiomas
textos.py             textos de en e pt + carregador dos demais
traducoes/<xx>.py     um arquivo por idioma
conteudo/pt/*.md      documentos legais em português   ← edite aqui
conteudo/en/*.md      documentos legais em inglês      ← e aqui
assets/estilo.css     a folha de estilo inteira
assets/icone.png      ícone do app
assets/capa.png       imagem de compartilhamento (Open Graph, 1200x630)
servir.bat            sobe um servidor local em http://localhost:8080
```

Tudo o que está na raiz com extensão `.html`, mais `sitemap.xml` e
`robots.txt`, é **gerado**. Não edite: é sobrescrito a cada build.

## Rodar

```bash
pip install markdown
python3 construir.py
```

Para ver no navegador, dê dois cliques em `servir.bat` (ou rode
`python -m http.server 8080` na pasta) e abra http://localhost:8080.

Abrir o `index.html` direto pelo Explorer também funciona, mas pelo servidor
os caminhos ficam iguais aos de produção — vale a pena.

| Quero mudar | Mexo em |
|---|---|
| Um texto legal | `conteudo/<idioma>/*.md` |
| Qualquer texto da home | `textos.py` (en/pt) ou `traducoes/<xx>.py` |
| Cor, espaçamento, tipografia | `assets/estilo.css` |
| Domínio, e-mails, links das lojas | as constantes no topo do `construir.py` |

O build **falha de propósito** se um idioma tiver uma chave a mais ou a menos
que o português, ou se uma lista tiver um número diferente de itens. Com onze
idiomas, esse é o erro que realmente acontece.

## Links das lojas

No topo do `construir.py`:

```python
LINK_PLAY  = ''   # cole aqui o endereço da ficha na Google Play
LINK_APPLE = ''   # e aqui o da App Store
```

Enquanto uma delas estiver vazia, aquele selo aparece apagado, com a tarja
"em breve", e não é clicável. Assim que você preencher e rodar o build, ele
vira um botão de verdade — nos onze idiomas de uma vez.

**Antes de lançar, troque os selos pelas artes oficiais.** Os que estão aqui
são reproduções em SVG, feitas para o site não depender de imagem externa.
As duas empresas exigem a arte oficial nas suas diretrizes de marca, e elas
vêm prontas nos onze idiomas:

- Google: https://play.google.com/intl/en_us/badges/
- Apple: https://developer.apple.com/app-store/marketing/guidelines/

## SEO

O que já está no site:

- **`hreflang` completo** entre os onze idiomas, com `x-default` no inglês —
  é o que impede o Google de tratar as versões como conteúdo duplicado e o
  que faz cada país receber a sua.
- **`canonical`** em toda página.
- **`title` e `description` escritos por idioma**, não traduzidos ao pé da
  letra. Cada um usa o termo que as pessoas realmente digitam naquele idioma
  (匿名チャット, анонимный чат, anonimer Chat, دردشة مجهولة…), porque
  "chat anônimo" traduzido literalmente às vezes não é o que se busca.
- **Dados estruturados** (JSON-LD): `SoftwareApplication`, `WebSite`,
  `Organization` e `FAQPage`. O `FAQPage` é o que pode render aquele bloco de
  perguntas expansíveis direto no resultado da busca.
- **`sitemap.xml` com alternates `xhtml:link`** por idioma.
- Open Graph e Twitter Card com imagem 1200x630.
- HTML semântico, um `<h1>` por página, imagens com dimensão declarada, zero
  JavaScript.

O que **você** precisa fazer depois de publicar, e sem isso o resto rende
pouco:

1. Cadastre o site no [Google Search Console](https://search.google.com/search-console)
   e envie o `sitemap.xml`.
2. Cadastre também no [Bing Webmaster Tools](https://www.bing.com/webmasters)
   — o Yandex, importante para o russo, também tem o
   [Yandex Webmaster](https://webmaster.yandex.com).
3. Ponha o endereço do site na ficha da Play Store e da App Store. Link de
   loja para site é um dos sinais mais fortes que existem para um app.
4. Espere. Site novo demora de semanas a meses para ranquear, e não há
   atalho honesto.

Uma expectativa realista: "chat" e "chat anônimo" são termos disputados por
gente com anos de domínio e milhares de links. O que um site novo ganha
primeiro são as buscas de cauda longa — "chat anônimo sem cadastro", "app de
conversa anônima", "登録不要 匿名チャット". É por isso que os textos foram
escritos em volta dessas frases, e não só da palavra solta.

## Publicar

O repositório já está pronto para o **GitHub Pages**:

1. Repositório → **Settings** → **Pages**
2. **Source:** Deploy from a branch
3. **Branch:** `main`, pasta `/ (root)` → Save

Em um ou dois minutos o site está em
`https://mondaine25.github.io/NimoChat/`.

O arquivo `.nojekyll` já está aqui: sem ele, o GitHub roda o Jekyll na pasta
e ignora arquivos e diretórios que começam com underscore.

### Quando o domínio chegar

1. Troque a constante no `construir.py`:
   ```python
   SITE = 'https://chatnimo.com'
   ```
2. Crie um arquivo `CNAME` na raiz, com uma linha só: `chatnimo.com`
3. Rode `python3 construir.py` e publique.
4. No seu provedor de domínio, crie um `CNAME` de `www` apontando para
   `mondaine25.github.io`, e os registros `A` da raiz para os IPs do GitHub
   Pages (`185.199.108.153`, `.109.153`, `.110.153`, `.111.153`).
5. Em Settings → Pages, preencha o **Custom domain** e marque
   **Enforce HTTPS**.
6. Atualize os dois endereços na Play Console e na App Store Connect.

Sem o passo 1, os `canonical` e o `sitemap.xml` continuam apontando para o
github.io e o Google indexa o endereço antigo.

## Endereços que a Google Play pede

Enquanto o domínio não chega:

- Política de Privacidade: `https://mondaine25.github.io/NimoChat/privacy.html`
  (ou `/pt/privacidade.html` na ficha em português)
- Solicitação de exclusão: `https://mondaine25.github.io/NimoChat/delete-account.html`

O revisor abre os dois. Confira que abrem antes de mandar o app para análise.

## Detalhes que valem saber

- **Uma fonte externa só:** Inter, pelo Google Fonts, com fallback para a do
  sistema. Nada mais é carregado de fora.
- **Zero JavaScript.** O acordeão das dúvidas e o seletor de idiomas são
  `<details>` nativo.
- **Tema escuro fixo**, com as cores de `app_theme.dart` no aplicativo.
- **Acessibilidade:** atalho "pular para o conteúdo", foco visível, contraste
  conferido, `prefers-reduced-motion` respeitado e `dir="rtl"` de verdade em
  árabe e hebraico.
