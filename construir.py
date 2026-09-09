#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Constrói o site do Nimo Chat, nos onze idiomas do aplicativo.

    pip install markdown
    python3 construir.py

Estrutura gerada:

    index.html                inglês — a raiz do site e o x-default
    privacy.html  terms.html  delete-account.html
    pt/index.html  pt/privacidade.html  pt/termos.html  pt/excluir-conta.html
    es/index.html  de/index.html  tr/index.html  ru/index.html
    ar/index.html  he/index.html  hi/index.html  ja/index.html  ko/index.html
    404.html  sitemap.xml  robots.txt

Os textos vêm de `textos.py` (+ `traducoes/*.py`). Os documentos legais vêm
de `conteudo/<idioma>/*.md`. Este arquivo cuida só do HTML, do SEO e da
navegação entre os idiomas.

Site estático puro: sem framework, sem Node, sem nada rodando no servidor.
"""
import pathlib
import re
import sys
from datetime import date

try:
    import markdown
except ImportError:
    sys.exit('Falta a biblioteca markdown. Rode:  pip install markdown')

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from textos import IDIOMAS, ORDEM, COM_LEGAL, conferir   # noqa: E402

RAIZ = pathlib.Path(__file__).parent
CONTEUDO = RAIZ / 'conteudo'

# ===========================================================================
# Configuração — é aqui que você mexe
# ===========================================================================

# Endereço final do site, SEM barra no fim. Entra em todo link canônico, em
# todo hreflang e no sitemap. Ao registrar o domínio, troque esta linha por
# 'https://chatnimo.com', crie o arquivo CNAME com o domínio dentro, e rode
# o build de novo.
SITE = 'https://chatnimo.com'

NOME = 'Nimo Chat'
EMAIL_SUPORTE = 'suporte@chatnimo.com'
EMAIL_ABUSO = 'abuso@chatnimo.com'

# Preencha quando cada loja aprovar o app. Enquanto estiver vazio, o botão
# daquela loja aparece apagado, com a tarja "em breve", e não é clicável.
LINK_PLAY = 'https://play.google.com/store/apps/details?id=com.leonardomondaine.nimo'
LINK_APPLE = ''

IDIOMA_RAIZ = 'en'

# Nome do arquivo de cada documento legal, por idioma. Nomes diferentes por
# idioma são melhores para busca do que um /pt/privacy.html.
ARQ_LEGAL = {
    'en': {'privacidade': 'privacy.html',
           'termos': 'terms.html',
           'excluir': 'delete-account.html',
           'seguranca': 'child-safety.html'},
    'pt': {'privacidade': 'privacidade.html',
           'termos': 'termos.html',
           'excluir': 'excluir-conta.html',
           'seguranca': 'seguranca-infantil.html'},
}
FONTE_LEGAL = {
    'en': {'privacidade': 'en/privacy-policy.md',
           'termos': 'en/terms-of-use.md',
           'excluir': 'en/delete-account.md',
           'seguranca': 'en/child-safety-standards.md'},
    'pt': {'privacidade': 'pt/politica-de-privacidade.md',
           'termos': 'pt/termos-de-uso.md',
           'excluir': 'pt/excluir-conta.md',
           'seguranca': 'pt/padroes-de-seguranca-infantil.md'},
}


# ===========================================================================
# Blog -- só em inglês e português por enquanto. Fica fora do textos.py de
# propósito: aquele sistema exige as mesmas chaves nos onze idiomas
# (conferir() falha se faltar uma só), e o blog ainda não existe nos outros
# nove. BLOG_TEXTOS é um dicionário pequeno e paralelo, só para os dois
# idiomas que têm posts -- não mexe em nada do textos.py.
# ===========================================================================
BLOG_IDIOMAS = ['en', 'pt']

MESES_PT = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
            'julho', 'agosto', 'setembro', 'outubro', 'novembro',
            'dezembro']
MESES_EN = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December']


def data_extenso(cod, d):
    if cod == 'pt':
        return f'{d.day} de {MESES_PT[d.month - 1]} de {d.year}'
    return f'{MESES_EN[d.month - 1]} {d.day}, {d.year}'


BLOG_TEXTOS = {
    'en': {
        'nav': 'Blog',
        'titulo_index': 'Blog — Nimo Chat',
        'descricao_index': ('Guides and articles about anonymous chat, '
                             'online safety, and how Nimo Chat works.'),
        'h1': 'The Nimo Chat blog',
        'sub': ('Notes on anonymous chat, online safety, and how the app '
                'is built.'),
        'ler_mais': 'Read more',
        'voltar': 'Back to blog',
        'publicado': 'Published on',
        'cta_titulo': 'Curious to try it?',
        'cta_sub': 'Nimo Chat is free, with no sign-up required.',
    },
    'pt': {
        'nav': 'Blog',
        'titulo_index': 'Blog — Nimo Chat',
        'descricao_index': ('Guias e artigos sobre chat anônimo, segurança '
                             'online e como o Nimo Chat funciona.'),
        'h1': 'O blog do Nimo Chat',
        'sub': ('Notas sobre chat anônimo, segurança online e como o app '
                'é construído.'),
        'ler_mais': 'Leia mais',
        'voltar': 'Voltar para o blog',
        'publicado': 'Publicado em',
        'cta_titulo': 'Curioso para experimentar?',
        'cta_sub': 'O Nimo Chat é grátis, sem precisar de cadastro.',
    },
}

# Cada post: uma data e, por idioma, título/descrição/arquivo-fonte/imagem.
# As imagens são screenshots reais do app (assets/blog/), e os arquivos-
# fonte ficam em conteudo/blog/<idioma>/, junto dos documentos legais.
BLOG_POSTS = [
    {
        'data': date(2026, 9, 8),
        'en': {
            'arquivo': 'blog-anonymous-chat-no-signup.html',
            'titulo': 'Anonymous Chat With No Sign-Up: How Does It Work?',
            'descricao': ('No email, no password, no phone number. How '
                           'Nimo Chat matches you with strangers and what '
                           '"safe" actually means with no account at all.'),
            'fonte': 'blog/en/anonymous-chat-no-signup.md',
            'imagem': 'assets/blog/privacidade-en.png',
            'alt': 'Nimo Chat profile screen showing no email, no password, and no personal data stored, with automatic location removal and one-tap account deletion.',
        },
        'pt': {
            'arquivo': 'blog-chat-anonimo-sem-cadastro.html',
            'titulo': 'Chat anônimo sem cadastro: como funciona e é seguro usar?',
            'descricao': ('Sem e-mail, sem senha, sem telefone guardado. '
                           'Como o pareamento do Nimo Chat funciona e o '
                           'que "seguro" quer dizer sem conta nenhuma.'),
            'fonte': 'blog/pt/chat-anonimo-sem-cadastro.md',
            'imagem': 'assets/blog/privacidade-pt.png',
            'alt': 'Tela de perfil do Nimo Chat mostrando sem e-mail, sem senha e nenhum dado pessoal guardado, com remoção automática de localização e exclusão da conta em um toque.',
        },
    },
    {
        'data': date(2026, 9, 8),
        'en': {
            'arquivo': 'blog-the-board-meet-new-people.html',
            'titulo': "The Board: How to Meet New People Even When Nobody's Online",
            'descricao': ('What happens when live matching finds no one? '
                           'Inside the Board, the public 24-hour icebreaker '
                           "space in Nimo Chat's Discover tab."),
            'fonte': 'blog/en/the-board-meet-new-people.md',
            'imagem': 'assets/blog/buscar-en.png',
            'alt': "Nimo Chat's search screen showing live matching in progress, with the number of people currently in the queue to chat.",
        },
        'pt': {
            'arquivo': 'blog-mural-conhecer-gente-nova.html',
            'titulo': 'O Mural: como conhecer gente nova mesmo sem ninguém online',
            'descricao': ('O que acontece quando o pareamento não encontra '
                           'ninguém? Conheça o Mural, o espaço público de '
                           '24h da aba Buscar do Nimo Chat.'),
            'fonte': 'blog/pt/mural-conhecer-gente-nova.md',
            'imagem': 'assets/blog/buscar-pt.png',
            'alt': 'Tela de busca do Nimo Chat mostrando o pareamento em andamento, com o número de pessoas na fila para conversar agora.',
        },
    },
    {
        'data': date(2026, 9, 8),
        'en': {
            'arquivo': 'blog-safety-tips-anonymous-chat.html',
            'titulo': '5 Safety Tips for Using Anonymous Chat Without the Headaches',
            'descricao': ('Five practical habits for chatting with '
                           'strangers safely, and how Nimo Chat was built '
                           'around each one of them.'),
            'fonte': 'blog/en/safety-tips-anonymous-chat.md',
            'imagem': 'assets/blog/seguranca-en.png',
            'alt': "Nimo Chat conversation screen showing a view-once photo, deleted from the server as soon as it's opened.",
        },
        'pt': {
            'arquivo': 'blog-dicas-seguranca-chat-anonimo.html',
            'titulo': '5 dicas de segurança pra usar chat anônimo sem dor de cabeça',
            'descricao': ('Cinco práticas para conversar com estranhos com '
                           'mais segurança, e como o Nimo Chat foi '
                           'construído em volta de cada uma delas.'),
            'fonte': 'blog/pt/dicas-seguranca-chat-anonimo.md',
            'imagem': 'assets/blog/seguranca-pt.png',
            'alt': 'Tela de conversa do Nimo Chat mostrando uma foto de visualização única, apagada do servidor assim que é aberta.',
        },
    },
    {
        'data': date(2026, 9, 8),
        'en': {
            'arquivo': 'blog-private-feed-for-friends.html',
            'titulo': 'The Private Feed: The Space That Exists Only Between You and Your Friends',
            'descricao': ('Random matching is anonymous and public. The '
                           'Feed is the opposite: private, friends-only, '
                           'and invisible to everyone else.'),
            'fonte': 'blog/en/private-feed-for-friends.md',
            'imagem': 'assets/blog/feed-en.png',
            'alt': "Nimo Chat's private Feed screen, showing posts visible only to accepted friends.",
        },
        'pt': {
            'arquivo': 'blog-feed-privado-entre-amigos.html',
            'titulo': 'O Feed privado: o espaço que só existe entre você e seus amigos',
            'descricao': ('O pareamento aleatório é público e anônimo. O '
                           'Feed é o oposto: privado, só entre amigos, e '
                           'invisível para todo o resto.'),
            'fonte': 'blog/pt/feed-privado-entre-amigos.md',
            'imagem': 'assets/blog/feed-pt.png',
            'alt': 'Tela do Feed privado do Nimo Chat, mostrando publicações visíveis só para amigos aceitos.',
        },
    },
]


# ===========================================================================
# Caminhos e URLs
# ===========================================================================
def pasta(cod):
    """'' para o idioma da raiz, 'pt/' para os demais."""
    return '' if cod == IDIOMA_RAIZ else f'{cod}/'


def caminho(cod, arquivo='index.html'):
    return f'{pasta(cod)}{arquivo}'


def url(cod, arquivo='index.html'):
    return f'{SITE}/{caminho(cod, arquivo)}'


def subir(cod):
    """Prefixo relativo para chegar na raiz a partir de uma página."""
    return '' if cod == IDIOMA_RAIZ else '../'


def link(de, para_cod, arquivo='index.html'):
    """Link relativo de uma página em `de` para uma página em `para_cod`."""
    return f'{subir(de)}{caminho(para_cod, arquivo)}'


def link_legal(de, qual):
    """Legal no idioma da página quando existe; senão, na versão em inglês."""
    alvo = de if de in COM_LEGAL else IDIOMA_RAIZ
    return link(de, alvo, ARQ_LEGAL[alvo][qual])


# ===========================================================================
# Ícones — traço de 1,7px, cor herdada do texto
# ===========================================================================
def svg(d, t=24):
    return (f'<svg viewBox="0 0 24 24" width="{t}" height="{t}" fill="none" '
            f'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{d}</svg>')


I_CHECK = svg('<path d="M20 6 9 17l-5-5"/>')
I_CHECK_P = svg('<path d="M20 6 9 17l-5-5"/>', 15)
I_ESCUDO = svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/>'
               '<path d="m9 12 2 2 4-4"/>')
I_ESCUDO_P = svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/>'
                 '<path d="m9 12 2 2 4-4"/>', 18)
I_OLHO = svg('<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7-10-7-10-7Z"/>'
             '<circle cx="12" cy="12" r="3"/><path d="m3 3 18 18"/>')
I_RAIO = svg('<path d="M13 2 4.1 13.4a.7.7 0 0 0 .5 1.1H11l-1 8.5 8.9-11.4a'
             '.7.7 0 0 0-.5-1.1H12l1-8.5Z"/>')
I_MIC = svg('<rect x="9" y="2" width="6" height="11" rx="3"/>'
            '<path d="M5 11a7 7 0 0 0 14 0"/><path d="M12 18v4"/>')
I_CORACAO = svg('<path d="M12 20.5S3.5 15 3.5 9.2A4.7 4.7 0 0 1 12 6.4a4.7 '
                '4.7 0 0 1 8.5 2.8c0 5.8-8.5 11.3-8.5 11.3Z"/>')
I_RELOGIO = svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>')
I_GLOBO = svg('<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/>'
              '<path d="M12 3a15 15 0 0 1 0 18 15 15 0 0 1 0-18Z"/>', 17)
I_ENVIAR = svg('<path d="M4 12h15"/><path d="m13 6 6 6-6 6"/>', 17)
I_SETA_ESQ = svg('<path d="M19 12H5"/><path d="m11 6-6 6 6 6"/>', 15)

ICONES_RECURSO = [I_OLHO, I_MIC, I_CORACAO, I_RELOGIO, I_RAIO, I_ESCUDO]


# ===========================================================================
# Selos das lojas
# ===========================================================================
# Reproduções em SVG, para o site não depender de imagem externa e ficar
# nítido em qualquer tela. Antes de lançar, vale trocar pelas artes oficiais
# — as duas empresas exigem isso nas suas diretrizes de marca, e as artes
# vêm traduzidas para os onze idiomas:
#   Google:  https://play.google.com/intl/en_us/badges/
#   Apple:   https://developer.apple.com/app-store/marketing/guidelines/

LOGO_APPLE = """<svg viewBox="0 0 24 24" width="25" height="25" aria-hidden="true">
<path fill="currentColor" d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 14.25 3.51 5.32 9.05 5.05c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.34zM12.03 4.99C11.88 2.71 13.73.83 15.85.7c.29 2.64-2.4 4.6-3.82 4.29z"/>
</svg>"""


# Idiomas com arte oficial da Google Play baixada em assets/badges/; os
# demais caem no badge em ingles.
BADGE_PLAY_IDIOMAS = {'en', 'pt', 'es', 'de', 'tr', 'ru', 'ar'}


def selo_play(cod, href, breve, rotulo):
    """Selo oficial da Google Play (assets/badges/). A propria arte ja traz
    o fundo escuro e o texto -- so falta o link em volta."""
    variante = cod if cod in BADGE_PLAY_IDIOMAS else 'en'
    img = (f'<img src="{subir(cod)}assets/badges/google-play-{variante}.svg" '
           f'alt="" width="169" height="50" loading="lazy">')
    if href:
        return (f'<a class="loja-oficial" href="{href}" aria-label="{rotulo}" '
                f'rel="noopener">{img}</a>')
    return (f'<span class="loja-oficial loja-oficial--breve" role="img" '
            f'aria-label="{rotulo} — {breve}">{img}'
            f'<i class="breve">{breve}</i></span>')


def selo_loja(logo, linha1, linha2, href, breve, rotulo):
    """Um selo de loja. Sem link, vira uma tarja apagada de 'em breve'."""
    miolo = (f'<span class="loja-i">{logo}</span>'
             f'<span class="loja-t"><small>{linha1}</small>'
             f'<b>{linha2}</b></span>')
    if href:
        return (f'<a class="loja" href="{href}" aria-label="{rotulo}" '
                f'rel="noopener">{miolo}</a>')
    return (f'<span class="loja loja--breve" role="img" aria-label="'
            f'{rotulo} — {breve}">{miolo}<i class="breve">{breve}</i></span>')


def lojas(t, cod):
    return (
        '<div class="lojas">'
        + selo_play(cod, LINK_PLAY, t['em_breve'], f'{NOME} — Google Play')
        + selo_loja(LOGO_APPLE, 'Download on the', 'App Store', LINK_APPLE,
                    t['em_breve'], f'{NOME} — App Store')
        + '</div>'
    )


# ===========================================================================
# Moldura comum
# ===========================================================================
def alternates(arquivo_por_idioma):
    """As tags hreflang de um grupo de páginas equivalentes."""
    saida = []
    for cod, arq in arquivo_por_idioma.items():
        saida.append(f'<link rel="alternate" hreflang="'
                     f'{IDIOMAS[cod]["html_lang"]}" href="{url(cod, arq)}">')
    raiz = arquivo_por_idioma.get(IDIOMA_RAIZ)
    if raiz:
        saida.append(f'<link rel="alternate" hreflang="x-default" '
                     f'href="{url(IDIOMA_RAIZ, raiz)}">')
    return '\n'.join(saida)


def og_alternates(cod):
    return '\n'.join(
        f'<meta property="og:locale:alternate" content="'
        f'{IDIOMAS[c]["og_locale"]}">'
        for c in ORDEM if c != cod)


def seletor_idioma(cod, arquivo_por_idioma, t):
    """Trocador de idioma em <details> — nativo, sem JavaScript."""
    itens = []
    for c in ORDEM:
        arq = arquivo_por_idioma.get(c, 'index.html')
        atual = ' aria-current="true"' if c == cod else ''
        itens.append(f'<a href="{link(cod, c, arq)}" lang="'
                     f'{IDIOMAS[c]["html_lang"]}"{atual}>'
                     f'{IDIOMAS[c]["idioma"]}</a>')
    return f"""<details class="seletor">
  <summary aria-label="{t['idioma_label']}">{I_GLOBO}
    <span>{IDIOMAS[cod]['idioma']}</span></summary>
  <div class="seletor-lista">{''.join(itens)}</div>
</details>"""


def moldar(cod, arquivo, titulo, descricao, corpo, grupo, jsonld='',
           tipo_og='website', imagem_og=None):
    """Envolve o corpo no <head>, no cabeçalho e no rodapé."""
    t = IDIOMAS[cod]
    base = subir(cod)
    inicio = link(cod, cod, 'index.html')

    nav = t['nav']
    menu = ''.join(
        f'<a href="{inicio}#{ancora}">{nav[chave]}</a>'
        for ancora, chave in [('como', 'como'), ('recursos', 'recursos'),
                              ('privacidade', 'privacidade'),
                              ('duvidas', 'duvidas')])
    if cod in BLOG_IDIOMAS:
        menu += (f'<a href="{link(cod, cod, "blog.html")}">'
                 f'{BLOG_TEXTOS[cod]["nav"]}</a>')

    rodape_blog_li = ''
    if cod in BLOG_IDIOMAS:
        rodape_blog_li = (f'<li><a href="{link(cod, cod, "blog.html")}">'
                          f'{BLOG_TEXTOS[cod]["nav"]}</a></li>')

    return f"""<!DOCTYPE html>
<html lang="{t['html_lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#080B0A">
<title>{titulo}</title>
<meta name="description" content="{descricao}">
<meta name="keywords" content="{t['palavras']}">
<link rel="canonical" href="{url(cod, arquivo)}">
{alternates(grupo)}
<link rel="icon" type="image/png" href="{base}assets/icone.png">
<link rel="apple-touch-icon" href="{base}assets/icone.png">
<meta property="og:type" content="{tipo_og}">
<meta property="og:site_name" content="{NOME}">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descricao}">
<meta property="og:url" content="{url(cod, arquivo)}">
<meta property="og:image" content="{imagem_og or f'{SITE}/assets/capa.png'}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{t['og_locale']}">
{og_alternates(cod)}
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{base}assets/estilo.css">
{jsonld}
</head>
<body>
<a class="pular" href="#conteudo">{t['pular']}</a>
<div class="atmosfera" aria-hidden="true"></div>

<header class="topo">
  <div class="topo-i">
    <a class="marca" href="{inicio}">
      <img src="{base}assets/icone.png" alt="" width="34" height="34">
      <b>{NOME}</b>
    </a>
    <nav class="nav" aria-label="{nav['como']}">{menu}</nav>
    {seletor_idioma(cod, grupo, t)}
    <a class="btn btn--menta btn--pequeno" href="{inicio}#baixar">
      {nav['baixar']}</a>
  </div>
</header>
{corpo}
<footer class="rodape">
  <div class="env">
    <div class="rodape-grade">
      <div>
        <a class="marca" href="{inicio}">
          <img src="{base}assets/icone.png" alt="" width="34" height="34">
          <b>{NOME}</b>
        </a>
        <p class="sobre">{t['rodape_sobre']}</p>
      </div>
      <div>
        <h4>{t['rodape_app']}</h4>
        <ul>
          <li><a href="{inicio}#como">{nav['como']}</a></li>
          <li><a href="{inicio}#recursos">{nav['recursos']}</a></li>
          <li><a href="{inicio}#premium">{t['rodape_premium']}</a></li>{rodape_blog_li}
          <li><a href="{inicio}#baixar">{nav['baixar']}</a></li>
        </ul>
      </div>
      <div>
        <h4>{t['rodape_legal']}</h4>
        <ul>
          <li><a href="{link_legal(cod, 'termos')}">{t['legal']['termos']}</a></li>
          <li><a href="{link_legal(cod, 'privacidade')}">{t['legal']['privacidade']}</a></li>
          <li><a href="{link_legal(cod, 'seguranca')}">{t['legal']['seguranca']}</a></li>
          <li><a href="{link_legal(cod, 'excluir')}">{t['legal']['excluir']}</a></li>
        </ul>
      </div>
      <div>
        <h4>{t['rodape_contato']}</h4>
        <ul>
          <li><a href="mailto:{EMAIL_SUPORTE}">{EMAIL_SUPORTE}</a></li>
          <li><a href="mailto:{EMAIL_ABUSO}">{EMAIL_ABUSO}</a></li>
          <li><a href="{inicio}#duvidas">{t['rodape_duvidas']}</a></li>
        </ul>
      </div>
    </div>
    <nav class="idiomas" aria-label="{t['idioma_label']}">
      {''.join(f'<a href="{link(cod, c, grupo.get(c, "index.html"))}" '
               f'lang="{IDIOMAS[c]["html_lang"]}" hreflang="'
               f'{IDIOMAS[c]["html_lang"]}">{IDIOMAS[c]["idioma"]}</a>'
               for c in ORDEM)}
    </nav>
    <div class="rodape-fim">
      <span class="tag-idade">18+</span>
      <span>&copy; {date.today().year} {NOME}. {t['direitos']}</span>
      <span>{t['feito']}</span>
    </div>
  </div>
</footer>
</body>
</html>
"""


# ===========================================================================
# Dados estruturados — é o que faz a busca entender o que o site é
# ===========================================================================
def jsonld_home(cod, t):
    import json

    def esc(s):
        return re.sub(r'<[^>]+>', '', s)

    grafo = [
        {
            '@type': 'SoftwareApplication',
            '@id': f'{SITE}/#app',
            'name': NOME,
            'description': t['descricao'],
            'applicationCategory': 'SocialNetworkingApplication',
            'operatingSystem': 'Android, iOS',
            'inLanguage': [IDIOMAS[c]['html_lang'] for c in ORDEM],
            'contentRating': '18+',
            'offers': {'@type': 'Offer', 'price': '0',
                       'priceCurrency': 'USD'},
        },
        {
            '@type': 'WebSite',
            '@id': f'{SITE}/#site',
            'url': f'{SITE}/',
            'name': NOME,
            'inLanguage': t['html_lang'],
        },
        {
            '@type': 'Organization',
            '@id': f'{SITE}/#org',
            'name': NOME,
            'url': f'{SITE}/',
            'logo': f'{SITE}/assets/icone.png',
            'email': EMAIL_SUPORTE,
        },
        {
            '@type': 'FAQPage',
            '@id': f'{url(cod)}#faq',
            'mainEntity': [
                {'@type': 'Question', 'name': esc(p),
                 'acceptedAnswer': {'@type': 'Answer',
                                    'text': esc(' '.join(rs))}}
                for p, rs in t['faq']
            ],
        },
    ]
    corpo = json.dumps({'@context': 'https://schema.org', '@graph': grafo},
                       ensure_ascii=False, indent=1)
    return f'<script type="application/ld+json">\n{corpo}\n</script>'


# ===========================================================================
# Página inicial
# ===========================================================================
def pagina_inicial(cod):
    t = IDIOMAS[cod]
    c = t['chat']
    inicio_priv = link_legal(cod, 'privacidade')

    metricas = ''.join(
        f'<div class="metrica"><b>{v}</b><span>{r}</span></div>'
        for v, r in t['metricas'])

    notas = ''.join(f'<li>{I_CHECK_P} {n}</li>' for n in t['notas'])

    passos = ''.join(
        f'<div class="passo"><div class="n" aria-hidden="true"></div>'
        f'<h3>{tit}</h3><p>{txt}</p></div>'
        for tit, txt in t['passos'])

    cartoes = []
    for i, (tit, txt) in enumerate(t['recursos']):
        classe = 'cartao'
        if i == 0:
            classe += ' cartao--largo'
        if i == len(t['recursos']) - 1:
            classe += ' cartao--total'
        cartoes.append(
            f'<article class="{classe}"><div class="icone">'
            f'{ICONES_RECURSO[i]}</div><h3>{tit}</h3><p>{txt}</p></article>')

    priv = ''.join(
        f'<li>{I_CHECK} <span><b>{forte}</b> {resto}</span></li>'
        for forte, resto in t['priv_itens'])

    plano = ''.join(f'<li>{I_CHECK} {x}</li>' for x in t['plano_itens'])

    faq = ''.join(
        '<details><summary>' + p + '</summary><div class="resposta">'
        + ''.join(f'<p>{r}</p>' for r in rs) + '</div></details>'
        for p, rs in t['faq'])

    corpo = f"""
<main id="conteudo">

<section class="env hero">
  <div class="hero-grade">
    <div>
      <span class="selo"><span class="ponto"></span> {t['selo']}</span>
      <h1 class="h-mega">{t['h1_a']}
        <em class="destaque">{t['h1_destaque']}</em></h1>
      <p class="subtitulo">{t['hero_sub']}</p>
      {lojas(t, cod)}
      <p class="ver-como"><a class="btn btn--fantasma" href="#como">
        {t['btn_como']}</a></p>
      <ul class="hero-notas">{notas}</ul>
    </div>

    <div class="palco">
      <div class="celular">
        <div class="celular-tela">
          <div class="entalhe"></div>
          <div class="tela-topo">
            <div class="av">{c['nome'][0]}</div>
            <div><div class="quem">{c['nome']}</div>
              <div class="estado">{c['estado']}</div></div>
          </div>
          <div class="conversa">
            <div class="balao balao--deles" style="animation-delay:.25s">{c['b1']}</div>
            <div class="balao balao--meus" style="animation-delay:.85s">{c['b2']}</div>
            <div class="balao balao--deles" style="animation-delay:1.5s">{c['b3']}</div>
            <div class="cartao-unica" style="animation-delay:2.1s">{I_OLHO}
              <div><b>{c['unica_t']}</b><span>{c['unica_s']}</span></div>
            </div>
            <div class="digitando" style="animation-delay:2.7s">
              <i></i><i></i><i></i></div>
          </div>
          <div class="tela-base">
            <div class="campo">{c['campo']}</div>
            <div class="enviar">{I_ENVIAR}</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="metricas">{metricas}</div>
</section>

<hr class="linha">

<section class="secao" id="como">
  <div class="env">
    <p class="olho">{t['olho_como']}</p>
    <h2 class="h-secao">{t['h_como']}</h2>
    <p class="subtitulo">{t['sub_como']}</p>
    <div class="passos">{passos}</div>
  </div>
</section>

<hr class="linha">

<section class="secao" id="recursos">
  <div class="env">
    <p class="olho">{t['olho_recursos']}</p>
    <h2 class="h-secao">{t['h_recursos']}</h2>
    <div class="bento">{''.join(cartoes)}</div>
  </div>
</section>

<hr class="linha">

<section class="secao" id="privacidade">
  <div class="env">
    <div class="painel">
      <div>
        <p class="olho">{t['olho_priv']}</p>
        <h2 class="h-secao">{t['h_priv']}</h2>
        <p class="subtitulo">{t['sub_priv']}</p>
        <p class="painel-btn"><a class="btn btn--fantasma"
          href="{inicio_priv}">{t['btn_priv']}</a></p>
      </div>
      <ul class="nao-lista">{priv}</ul>
    </div>
  </div>
</section>

<hr class="linha">

<section class="secao" id="premium">
  <div class="env centro">
    <p class="olho">{t['olho_prem']}</p>
    <h2 class="h-secao">{t['h_prem']}</h2>
    <p class="subtitulo">{t['sub_prem']}</p>
    <div class="plano">
      <div class="titulo">{t['plano_titulo']}</div>
      <ul>{plano}</ul>
      <p class="rodape-nota">{t['plano_nota']}</p>
    </div>
  </div>
</section>

<hr class="linha">

<section class="secao" id="duvidas">
  <div class="env">
    <div class="centro">
      <p class="olho">{t['olho_faq']}</p>
      <h2 class="h-secao">{t['h_faq']}</h2>
    </div>
    <div class="faq">{faq}</div>
  </div>
</section>

<section class="secao" id="baixar">
  <div class="env">
    <div class="chamada">
      <p class="olho">{t['olho_baixar']}</p>
      <h2 class="h-secao">{t['h_baixar']}</h2>
      <p class="subtitulo centro">{t['sub_baixar']}</p>
      {lojas(t, cod)}
      <p class="chamada-priv"><a class="btn btn--fantasma" href="{inicio_priv}">
        {I_ESCUDO_P} {t['btn_priv']}</a></p>
    </div>
  </div>
</section>

</main>
"""
    grupo = {c2: 'index.html' for c2 in ORDEM}
    return moldar(cod, 'index.html', t['titulo'], t['descricao'], corpo,
                  grupo, jsonld_home(cod, t))


# ===========================================================================
# Páginas de texto
# ===========================================================================
def documento(cod, qual):
    t = IDIOMAS[cod]
    arquivo = ARQ_LEGAL[cod][qual]
    origem = CONTEUDO / FONTE_LEGAL[cod][qual]
    texto = origem.read_text(encoding='utf-8')

    titulo = t['legal'][qual]
    corpo_md = re.sub(r'^# .*\n', '', texto, count=1)

    quando = ''
    m = re.search(r'^\*\*(?:Última atualização|Last updated):\*\*\s*(.+)$',
                  corpo_md, re.M)
    if m:
        quando = m.group(1).strip()
        corpo_md = corpo_md.replace(m.group(0), '', 1)

    # Sem `nl2br` de propósito: os .md são quebrados em ~78 colunas para
    # ficarem legíveis no editor, e o nl2br viraria cada quebra dessas num
    # <br>, picotando o parágrafo na tela em vez de deixá-lo refluir.
    html = markdown.markdown(corpo_md,
                             extensions=['tables', 'sane_lists', 'attr_list'])
    html = html.replace('<table>', '<div class="rolavel"><table>')
    html = html.replace('</table>', '</table></div>')

    legenda = (f'<p class="quando">{t["atualizado"]}: {quando}</p>'
               if quando else '')

    corpo = f"""
<main id="conteudo" class="doc">
  <a class="voltar" href="{link(cod, cod)}">{I_SETA_ESQ} {t['voltar']}</a>
  <div class="doc-cabeca">
    <h1>{titulo}</h1>
    {legenda}
  </div>
  <div class="aviso"><p>{t['nota_ingles']}</p></div>
  <div class="doc-corpo">
{html}
  </div>
</main>
"""
    grupo = {c: ARQ_LEGAL[c][qual] for c in COM_LEGAL}
    descricao = f'{titulo} — {NOME}. {t["descricao"]}'[:158]
    return moldar(cod, arquivo, f'{titulo} — {NOME}', descricao, corpo, grupo)


# ===========================================================================
# Blog
# ===========================================================================
def jsonld_post(cod, post):
    import json

    p = post[cod]
    quando = post['data'].isoformat()
    grafo = [
        {
            '@type': 'BlogPosting',
            '@id': f'{url(cod, p["arquivo"])}#post',
            'headline': p['titulo'],
            'description': p['descricao'],
            'image': f'{SITE}/{p["imagem"]}',
            'datePublished': quando,
            'dateModified': quando,
            'inLanguage': IDIOMAS[cod]['html_lang'],
            'mainEntityOfPage': {'@type': 'WebPage',
                                 '@id': url(cod, p['arquivo'])},
            'author': {'@type': 'Organization', 'name': NOME,
                       'url': f'{SITE}/'},
            'publisher': {
                '@type': 'Organization', 'name': NOME,
                'logo': {'@type': 'ImageObject',
                         'url': f'{SITE}/assets/icone.png'},
            },
        },
    ]
    corpo = json.dumps({'@context': 'https://schema.org', '@graph': grafo},
                       ensure_ascii=False, indent=1)
    return f'<script type="application/ld+json">\n{corpo}\n</script>'


def pagina_blog_index(cod):
    t = IDIOMAS[cod]
    bt = BLOG_TEXTOS[cod]

    cartoes = []
    for post in BLOG_POSTS:
        p = post[cod]
        cartoes.append(f"""
<article class="post-cartao">
  <a href="{link(cod, cod, p['arquivo'])}">
    <img src="{subir(cod)}{p['imagem']}" alt="{p['alt']}" width="1200"
      height="630" loading="lazy">
    <div class="post-cartao-corpo">
      <span class="post-data">{data_extenso(cod, post['data'])}</span>
      <h2>{p['titulo']}</h2>
      <p>{p['descricao']}</p>
      <span class="post-ler">{bt['ler_mais']}</span>
    </div>
  </a>
</article>""")

    corpo = f"""
<main id="conteudo" class="doc">
  <a class="voltar" href="{link(cod, cod)}">{I_SETA_ESQ} {t['voltar']}</a>
  <div class="doc-cabeca">
    <h1>{bt['h1']}</h1>
    <p class="subtitulo">{bt['sub']}</p>
  </div>
  <div class="blog-grade">{''.join(cartoes)}</div>
</main>
"""
    grupo = {c: 'blog.html' for c in BLOG_IDIOMAS}
    return moldar(cod, 'blog.html', bt['titulo_index'], bt['descricao_index'],
                  corpo, grupo)


def pagina_blog_post(cod, post):
    t = IDIOMAS[cod]
    bt = BLOG_TEXTOS[cod]
    p = post[cod]

    origem = CONTEUDO / p['fonte']
    texto = origem.read_text(encoding='utf-8')
    corpo_md = re.sub(r'^# .*\n', '', texto, count=1)
    html = markdown.markdown(corpo_md,
                             extensions=['tables', 'sane_lists', 'attr_list'])

    corpo = f"""
<main id="conteudo" class="doc">
  <a class="voltar" href="{link(cod, cod, 'blog.html')}">{I_SETA_ESQ}
    {bt['voltar']}</a>
  <div class="doc-cabeca">
    <h1>{p['titulo']}</h1>
    <p class="quando">{bt['publicado']}: {data_extenso(cod, post['data'])}</p>
  </div>
  <img class="post-capa" src="{subir(cod)}{p['imagem']}" alt="{p['alt']}"
    width="1200" height="630">
  <div class="doc-corpo">
{html}
  </div>
  <div class="post-cta">
    <h3>{bt['cta_titulo']}</h3>
    <p>{bt['cta_sub']}</p>
    {lojas(t, cod)}
  </div>
</main>
"""
    grupo = {c: post[c]['arquivo'] for c in BLOG_IDIOMAS}
    descricao = p['descricao'][:158]
    return moldar(cod, p['arquivo'], f"{p['titulo']} — {NOME}", descricao,
                  corpo, grupo, jsonld=jsonld_post(cod, post),
                  tipo_og='article', imagem_og=f'{SITE}/{p["imagem"]}')


# ===========================================================================
# 404
# ===========================================================================
def pagina_erro():
    cod = IDIOMA_RAIZ
    t = IDIOMAS[cod]
    corpo = f"""
<main id="conteudo" class="erro">
  <div>
    <div class="codigo">404</div>
    <h1 class="h-secao">{t['erro_t']}</h1>
    <p class="subtitulo centro">{t['erro_s']}</p>
    <p class="erro-btn"><a class="btn btn--menta" href="{link(cod, cod)}">
      {I_SETA_ESQ} {t['erro_btn']}</a></p>
  </div>
</main>
"""
    grupo = {c: 'index.html' for c in ORDEM}
    return moldar(cod, '404.html', f'404 — {NOME}', t['erro_s'], corpo, grupo)


# ===========================================================================
# Buscadores
# ===========================================================================
def sitemap(grupos):
    hoje = date.today().isoformat()
    linhas = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
              '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for grupo in grupos:
        alt = ''.join(
            f'\n    <xhtml:link rel="alternate" hreflang="'
            f'{IDIOMAS[c]["html_lang"]}" href="{url(c, a)}"/>'
            for c, a in grupo.items())
        if IDIOMA_RAIZ in grupo:
            alt += (f'\n    <xhtml:link rel="alternate" hreflang="x-default" '
                    f'href="{url(IDIOMA_RAIZ, grupo[IDIOMA_RAIZ])}"/>')
        for c, a in grupo.items():
            linhas.append(f'  <url>\n    <loc>{url(c, a)}</loc>'
                          f'\n    <lastmod>{hoje}</lastmod>{alt}\n  </url>')
    linhas.append('</urlset>')
    return '\n'.join(linhas) + '\n'


ROBOTS = f"""User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
"""


# ===========================================================================
# Execução
# ===========================================================================
def main():
    problemas = conferir()
    if problemas:
        print('  Os textos estao inconsistentes entre os idiomas:')
        for p in problemas:
            print(f'    {p}')
        sys.exit(1)

    grupos = [{c: 'index.html' for c in ORDEM}]
    contagem = 0

    for cod in ORDEM:
        destino = RAIZ / caminho(cod, 'index.html')
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(pagina_inicial(cod), encoding='utf-8')
        contagem += 1
    print(f'  {len(ORDEM)} paginas iniciais')

    for qual in ('privacidade', 'termos', 'excluir', 'seguranca'):
        grupos.append({c: ARQ_LEGAL[c][qual] for c in COM_LEGAL})
        for cod in COM_LEGAL:
            destino = RAIZ / caminho(cod, ARQ_LEGAL[cod][qual])
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(documento(cod, qual), encoding='utf-8')
            contagem += 1
    print(f'  {len(COM_LEGAL) * 4} paginas legais')

    grupos.append({c: 'blog.html' for c in BLOG_IDIOMAS})
    for cod in BLOG_IDIOMAS:
        destino = RAIZ / caminho(cod, 'blog.html')
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(pagina_blog_index(cod), encoding='utf-8')
        contagem += 1
    for post in BLOG_POSTS:
        grupos.append({c: post[c]['arquivo'] for c in BLOG_IDIOMAS})
        for cod in BLOG_IDIOMAS:
            destino = RAIZ / caminho(cod, post[cod]['arquivo'])
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(pagina_blog_post(cod, post), encoding='utf-8')
            contagem += 1
    print(f'  1 indice do blog + {len(BLOG_POSTS)} posts, em '
          f'{len(BLOG_IDIOMAS)} idiomas')

    (RAIZ / '404.html').write_text(pagina_erro(), encoding='utf-8')
    (RAIZ / 'sitemap.xml').write_text(sitemap(grupos), encoding='utf-8')
    (RAIZ / 'robots.txt').write_text(ROBOTS, encoding='utf-8')
    # GitHub Pages ignora a pasta se este arquivo nao existir e o repo tiver
    # nome comecando com underscore em algum lugar. Custa nada e evita dor.
    (RAIZ / '.nojekyll').write_text('', encoding='utf-8')
    print('  404.html + sitemap.xml + robots.txt + .nojekyll')

    print(f'\n  {contagem + 1} paginas geradas. Site em {SITE}')
    faltando = [n for n, v in (('LINK_PLAY', LINK_PLAY),
                               ('LINK_APPLE', LINK_APPLE)) if not v]
    if faltando:
        print(f'  Lembrete: {" e ".join(faltando)} vazio(s) — o selo daquela '
              f'loja aparece como "em breve".')


if __name__ == '__main__':
    main()
