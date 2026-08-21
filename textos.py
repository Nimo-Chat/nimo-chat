# -*- coding: utf-8 -*-
"""
Fonte única dos textos do site, nos onze idiomas do aplicativo.

Mesma ideia do `tools/traducoes.py` do app: com onze idiomas, o risco não é
traduzir mal — é uma chave existir num idioma e faltar noutro. Aqui cada
idioma é um dicionário com exatamente as mesmas chaves, e o `construir.py`
confere isso antes de gerar qualquer página.

Idiomas: pt (base), en, es, de, tr, ru, ar, he, hi, ja, ko
`ar` e `he` são escritos da direita para a esquerda ('dir': 'rtl').

Ao mexer num texto, mexa no mesmo lugar dos onze — ou rode o build, que
avisa o que ficou faltando.
"""

IDIOMAS = {}

# Ordem em que os idiomas aparecem no seletor. `en` primeiro porque é a raiz
# do site (x-default); `pt` segundo porque é o mercado de casa.
ORDEM = ['en', 'pt', 'es', 'de', 'tr', 'ru', 'ar', 'he', 'hi', 'ja', 'ko']

# Idiomas que têm os documentos legais traduzidos por inteiro. Os demais
# apontam para a versão em inglês, que é a de referência fora do Brasil —
# exatamente o que a própria Política de Privacidade diz.
COM_LEGAL = ['en', 'pt']


# ===========================================================================
# PORTUGUÊS — o texto de origem. Todos os outros são traduções deste.
# ===========================================================================
IDIOMAS['pt'] = {
    'idioma': 'Português',
    'html_lang': 'pt-BR',
    'og_locale': 'pt_BR',
    'dir': 'ltr',

    'titulo': 'Nimo Chat — chat anônimo e aleatório, sem cadastro',
    'descricao': ('Chat anônimo e aleatório. Converse com estranhos sem '
                  'cadastro, com foto que some depois de vista e chamada de '
                  'voz. Grátis, sem anúncios.'),
    'palavras': ('chat anônimo, bate-papo anônimo, chat aleatório, conversar '
                 'com estranhos, conhecer pessoas, chat sem cadastro'),

    'nav': {
        'como': 'Como funciona',
        'recursos': 'Recursos',
        'privacidade': 'Privacidade',
        'duvidas': 'Dúvidas',
        'baixar': 'Baixar',
    },

    'selo': 'Sem cadastro. Sério.',
    'h1_a': 'Converse com alguém novo',
    'h1_destaque': 'sem dizer quem você é',
    'hero_sub': ('O Nimo é um chat anônimo de verdade: não pedimos e-mail, '
                 'telefone, senha nem nome real. Você escolhe um apelido e, '
                 'em segundos, já está falando com uma pessoa que está online '
                 'agora.'),
    'btn_como': 'Ver como funciona',
    'notas': ['Grátis para usar', 'Sem anúncios', '11 idiomas'],
    'em_breve': 'Em breve',

    'chat': {
        'nome': 'Lira',
        'estado': 'online agora',
        'b1': 'oi! vi que a gente combinou em cinema',
        'b2': 'opa! qual foi o último que te marcou de verdade?',
        'b3': 'um japonês antigo, chorei uns 20 minutos',
        'unica_t': 'Foto de visualização única',
        'unica_s': 'some do servidor assim que você abrir',
        'campo': 'Mensagem',
    },

    'metricas': [
        ('0', 'dados pedidos no cadastro'),
        ('11', 'idiomas'),
        ('24 h', 'para revisar uma denúncia'),
        ('18+', 'só para maiores'),
    ],

    'olho_como': 'Como funciona',
    'h_como': 'Três toques até a primeira conversa',
    'sub_como': ('Não existe tela de cadastro, confirmação por e-mail ou '
                 'espera de código.'),
    'passos': [
        ('Escolha um apelido',
         'É a única coisa que pedimos. Nenhum e-mail, nenhum telefone, '
         'nenhuma senha para vazar depois.'),
        ('Marque o que te interessa',
         'Música, games, filmes, viagem, madrugada, desabafar. O pareamento '
         'passa a considerar o que vocês têm em comum.'),
        ('Toque em buscar',
         'O Nimo te apresenta a alguém online agora. Se combinou, continuem. '
         'Se não, é só procurar de novo.'),
    ],

    'olho_recursos': 'Recursos',
    'h_recursos': 'O que dá para fazer aqui',
    'recursos': [
        ('Foto que some depois de vista',
         'Envie uma foto de visualização única. No instante em que a outra '
         'pessoa abre, o arquivo é apagado do servidor — não fica cópia '
         'guardada, nem para você. No Android, a tela fica protegida contra '
         'captura enquanto a foto está aberta.'),
        ('Voz e vídeo',
         'Mensagem de áudio, vídeo, figurinhas — e chamada de voz entre '
         'amigos.'),
        ('De estranho a amigo',
         'Gostou da conversa? Mande um pedido de amizade. Aceito, a conversa '
         'vira permanente e vocês não dependem mais da fila.'),
        ('Status de 24 horas',
         'Some sozinho, como deve ser. Só quem é seu amigo vê.'),
        ('Mural para quando a fila está vazia',
         'Deixe uma frase. Quem entrar depois responde, e a conversa começa '
         'mesmo que vocês nunca estejam online ao mesmo tempo.'),
        ('Denúncia e bloqueio a um toque',
         'Toda mensagem, publicação e chamada tem denúncia e bloqueio. '
         'Analisamos as denúncias em até 24 horas, e quem aparenta ser menor '
         'de idade é suspenso imediatamente. Nada de nudez, assédio, golpe ou '
         'violência — quem faz isso perde a conta.'),
    ],

    'olho_priv': 'Privacidade',
    'h_priv': 'Anônimo não é só uma palavra na descrição',
    'sub_priv': ('A maioria dos aplicativos chama de anônimo o que é só um '
                 'apelido em cima de um cadastro completo. Aqui, o cadastro '
                 'não existe.'),
    'btn_priv': 'Ler a Política de Privacidade',
    'priv_itens': [
        ('Sem e-mail, sem telefone, sem senha.',
         'Não há cadastro para vazar.'),
        ('Não guardamos sua idade nem sua data de nascimento.',
         'Você declara ter 18 anos ao aceitar os termos, e paramos por aí.'),
        ('Removemos os metadados EXIF de toda foto',
         'antes do envio — o que apaga a coordenada de onde ela foi tirada.'),
        ('Nenhum SDK de publicidade, nenhum rastreador de anúncio.',
         'O app não é pago com a sua atenção.'),
        ('Um toque exclui a conta e todos os dados,',
         'de verdade — e você pode pedir isso por aqui também.'),
        ('Perdeu o celular?',
         'O código de recuperação traz a conta inteira de volta. Sem e-mail, '
         'sem SMS.'),
    ],

    'olho_prem': 'Premium',
    'h_prem': 'O Nimo funciona inteiro de graça',
    'sub_prem': ('A assinatura não desbloqueia conteúdo. Ela ajusta três '
                 'coisas para quem usa muito.'),
    'plano_titulo': 'Nimo Premium',
    'plano_itens': [
        'Escolher conversar só com homens ou só com mulheres',
        'Prioridade na fila de pareamento',
        'Amigos ilimitados',
    ],
    'plano_nota': ('Renova sozinha e pode ser cancelada quando quiser, direto '
                   'na loja do seu aparelho.'),

    'olho_faq': 'Dúvidas',
    'h_faq': 'Perguntas que todo mundo faz',
    'faq': [
        ('O Nimo é anônimo mesmo?',
         ['É. Não pedimos e-mail, telefone, senha nem nome real, e não '
          'guardamos sua idade. A conta é criada com um identificador '
          'aleatório que não está ligado a você, ao seu aparelho ou a '
          'qualquer serviço externo.',
          'Sua foto de perfil só é entregue para quem aceitou sua amizade. '
          'Antes disso, todo mundo é um avatar.']),
        ('A foto de visualização única some de verdade?',
         ['Sim. Assim que a outra pessoa abre, o arquivo é apagado do '
          'servidor e o endereço dele é zerado na conversa — inclusive para '
          'quem enviou. Se ninguém abrir, ela expira sozinha em 24 horas.',
          'No Android, a tela fica protegida contra captura enquanto a foto '
          'está aberta. Nenhum aplicativo do mundo consegue impedir que '
          'alguém fotografe a tela com outro celular, e nós não vamos fingir '
          'que conseguimos.']),
        ('Como funciona a chamada de voz?',
         ['Só entre amigos. O áudio vai direto de um aparelho para o outro '
          'sempre que a rede permite, e não é gravado em momento nenhum. '
          'Quando a rede não deixa a conexão direta acontecer, o áudio passa '
          'cifrado por um servidor de retransmissão, sem ficar guardado.']),
        ('Perdi meu celular. Perdi minha conta?',
         ['Não, se você guardou o <b>código de recuperação</b>. Ele fica em '
          'Ajustes, dentro do app. Com esse código, a conta volta inteira — '
          'conversas, amigos e feed — em qualquer aparelho.',
          'Sem e-mail e sem telefone, esse código é a única forma de provar '
          'que a conta é sua. Guarde num lugar seguro.']),
        ('Como eu excluo minha conta?',
         ['Ajustes → Excluir minha conta. Não há período de espera e não há '
          'como desfazer. A página de exclusão de conta explica exatamente o '
          'que é apagado, o que não é, e por quê.']),
        ('Tem anúncio? Vocês vendem meus dados?',
         ['Não e não. Não há nenhum SDK de publicidade no aplicativo, e nunca '
          'vendemos nem alugamos dados de usuário. O Nimo se paga com as '
          'assinaturas de quem quer o Premium.']),
        ('Qual a idade mínima?',
         ['18 anos. Conta que aparenta ser de menor de idade é suspensa '
          'imediatamente quando denunciada, antes mesmo da revisão humana.']),
    ],

    'olho_baixar': 'Baixar',
    'h_baixar': 'Uma conversa começa em segundos',
    'sub_baixar': ('Grátis, sem anúncios e sem cadastro. Para Android e '
                   'iPhone.'),

    'rodape_sobre': ('Conversas anônimas com pessoas novas. Sem e-mail, sem '
                     'telefone, sem nome real.'),
    'rodape_app': 'Aplicativo',
    'rodape_legal': 'Legal',
    'rodape_contato': 'Contato',
    'rodape_duvidas': 'Dúvidas frequentes',
    'rodape_premium': 'Premium',
    'direitos': 'Todos os direitos reservados.',
    'feito': 'Feito no Brasil.',
    'idioma_label': 'Idioma',

    'legal': {
        'termos': 'Termos de Uso',
        'privacidade': 'Política de Privacidade',
        'excluir': 'Excluir sua conta',
        'seguranca': 'Segurança Infantil',
    },
    'voltar': 'Voltar para o início',
    'atualizado': 'Última atualização',
    'nota_ingles': ('Este documento está disponível em português e em inglês. '
                    'A versão em inglês é a de referência para quem usa o app '
                    'fora do Brasil.'),

    'erro_t': 'Essa página não existe',
    'erro_s': 'O endereço mudou, ou o link estava errado desde o começo.',
    'erro_btn': 'Voltar para o início',
    'pular': 'Ir para o conteúdo',
}


# ===========================================================================
# INGLÊS — a raiz do site e o x-default. É a versão que mais gente vê.
# ===========================================================================
IDIOMAS['en'] = {
    'idioma': 'English',
    'html_lang': 'en',
    'og_locale': 'en_US',
    'dir': 'ltr',

    'titulo': 'Nimo Chat — anonymous random chat, no sign-up',
    'descricao': ('Anonymous random chat with strangers. No sign-up, '
                  'vanishing photos and voice calls. Free, no ads, no '
                  'trackers.'),
    'palavras': ('anonymous chat, random chat, talk to strangers, chat with '
                 'strangers, meet new people, chat without registration'),

    'nav': {
        'como': 'How it works',
        'recursos': 'Features',
        'privacidade': 'Privacy',
        'duvidas': 'FAQ',
        'baixar': 'Get the app',
    },

    'selo': 'No sign-up. Really.',
    'h1_a': 'Talk to someone new',
    'h1_destaque': 'without saying who you are',
    'hero_sub': ('Nimo is anonymous chat done properly: no email, no phone '
                 'number, no password, no real name. Pick a nickname and, '
                 'seconds later, you are talking to someone who is online '
                 'right now.'),
    'btn_como': 'See how it works',
    'notas': ['Free to use', 'No ads', '11 languages'],
    'em_breve': 'Coming soon',

    'chat': {
        'nome': 'Lira',
        'estado': 'online now',
        'b1': 'hey! saw we both picked movies',
        'b2': 'nice! which one actually stayed with you?',
        'b3': 'an old japanese one, cried for 20 minutes',
        'unica_t': 'View-once photo',
        'unica_s': 'erased from the server the moment you open it',
        'campo': 'Message',
    },

    'metricas': [
        ('0', 'details asked at sign-up'),
        ('11', 'languages'),
        ('24 h', 'to review a report'),
        ('18+', 'adults only'),
    ],

    'olho_como': 'How it works',
    'h_como': 'Three taps to your first conversation',
    'sub_como': ('There is no sign-up screen, no email confirmation and no '
                 'waiting for a code.'),
    'passos': [
        ('Pick a nickname',
         'It is the only thing we ask for. No email, no phone number, no '
         'password to leak later.'),
        ('Choose what you are into',
         'Music, games, movies, travel, late nights, venting. Matching starts '
         'to weigh what you have in common.'),
        ('Tap search',
         'Nimo introduces you to someone online right now. If it clicks, keep '
         'going. If not, just look again.'),
    ],

    'olho_recursos': 'Features',
    'h_recursos': 'What you can do here',
    'recursos': [
        ('Photos that vanish after one look',
         'Send a view-once photo. The moment the other person opens it, the '
         'file is erased from the server — no copy is kept, not even for you. '
         'On Android the screen is protected against capture while the photo '
         'is open.'),
        ('Voice and video',
         'Voice notes, video, stickers — and voice calls between friends.'),
        ('From stranger to friend',
         'Enjoyed the conversation? Send a friend request. Once accepted, the '
         'chat becomes permanent and you no longer depend on the queue.'),
        ('24-hour Status',
         'It disappears on its own, the way it should. Only your friends see '
         'it.'),
        ('A board for when the queue is empty',
         'Leave a line. Whoever comes along answers it, and the conversation '
         'starts even if you are never online at the same time.'),
        ('Report and block, one tap away',
         'Every message, post and call has report and block. We review '
         'reports within 24 hours, and anyone who appears to be a minor is '
         'suspended immediately. No nudity, harassment, scams or violence — '
         'do that and you lose the account.'),
    ],

    'olho_priv': 'Privacy',
    'h_priv': 'Anonymous is not just a word in the description',
    'sub_priv': ('Most apps call it anonymous when it is really a nickname on '
                 'top of a full account. Here, the account does not exist.'),
    'btn_priv': 'Read the Privacy Policy',
    'priv_itens': [
        ('No email, no phone number, no password.',
         'There is no account to leak.'),
        ('We do not store your age or date of birth.',
         'You declare you are 18 when you accept the terms, and we stop '
         'there.'),
        ('We strip EXIF metadata from every photo',
         'before upload — which erases the coordinates of where it was '
         'taken.'),
        ('No advertising SDK, no ad trackers.',
         'The app is not paid for with your attention.'),
        ('One tap deletes your account and all your data,',
         'for real — and you can request that here too.'),
        ('Lost your phone?',
         'The recovery code brings the whole account back. No email, no '
         'SMS.'),
    ],

    'olho_prem': 'Premium',
    'h_prem': 'Nimo works fully for free',
    'sub_prem': ('The subscription does not unlock content. It adjusts three '
                 'things for people who use the app a lot.'),
    'plano_titulo': 'Nimo Premium',
    'plano_itens': [
        'Choose to talk only to men or only to women',
        'Priority in the matching queue',
        'Unlimited friends',
    ],
    'plano_nota': ('It renews automatically and can be cancelled any time, '
                   'straight from your phone’s store.'),

    'olho_faq': 'FAQ',
    'h_faq': 'The questions everyone asks',
    'faq': [
        ('Is Nimo really anonymous?',
         ['It is. We do not ask for an email, a phone number, a password or a '
          'real name, and we do not store your age. The account is created '
          'with a random identifier that is not tied to you, to your phone or '
          'to any external service.',
          'Your profile picture is only delivered to people who accepted your '
          'friend request. Before that, everyone is an avatar.']),
        ('Does the view-once photo really disappear?',
         ['Yes. The moment the other person opens it, the file is erased from '
          'the server and its address is cleared from the conversation — '
          'including for the sender. If nobody opens it, it expires on its '
          'own after 24 hours.',
          'On Android the screen is protected against capture while the photo '
          'is open. No app in the world can stop someone from photographing '
          'the screen with another phone, and we are not going to pretend we '
          'can.']),
        ('How do voice calls work?',
         ['Between friends only. Audio goes straight from one phone to the '
          'other whenever the network allows, and it is never recorded. When '
          'the network blocks a direct connection, the audio passes '
          'encrypted through a relay server without being stored.']),
        ('I lost my phone. Did I lose my account?',
         ['Not if you kept your <b>recovery code</b>. It lives in Settings, '
          'inside the app. With that code the account comes back whole — '
          'chats, friends and feed — on any device.',
          'With no email and no phone number, that code is the only way to '
          'prove the account is yours. Keep it somewhere safe.']),
        ('How do I delete my account?',
         ['Settings → Delete my account. There is no waiting period and no '
          'undo. The account deletion page explains exactly what is removed, '
          'what is not, and why.']),
        ('Are there ads? Do you sell my data?',
         ['No and no. There is no advertising SDK in the app, and we never '
          'sell or rent user data. Nimo pays for itself with the '
          'subscriptions of people who want Premium.']),
        ('What is the minimum age?',
         ['18. An account that appears to belong to a minor is suspended '
          'immediately when reported, before human review even starts.']),
    ],

    'olho_baixar': 'Get the app',
    'h_baixar': 'A conversation starts in seconds',
    'sub_baixar': ('Free, no ads and no sign-up. For Android and iPhone.'),

    'rodape_sobre': ('Anonymous conversations with new people. No email, no '
                     'phone number, no real name.'),
    'rodape_app': 'App',
    'rodape_legal': 'Legal',
    'rodape_contato': 'Contact',
    'rodape_duvidas': 'Frequently asked questions',
    'rodape_premium': 'Premium',
    'direitos': 'All rights reserved.',
    'feito': 'Made in Brazil.',
    'idioma_label': 'Language',

    'legal': {
        'termos': 'Terms of Use',
        'privacidade': 'Privacy Policy',
        'excluir': 'Delete your account',
        'seguranca': 'Child Safety Standards',
    },
    'voltar': 'Back to home',
    'atualizado': 'Last updated',
    'nota_ingles': ('This document is available in English and Portuguese. '
                    'The English version is the reference for people using '
                    'the app outside Brazil.'),

    'erro_t': 'This page does not exist',
    'erro_s': 'The address changed, or the link was wrong to begin with.',
    'erro_btn': 'Back to home',
    'pular': 'Skip to content',
}


# ===========================================================================
# Os outros nove idiomas moram em `traducoes/<idioma>.py`, um arquivo cada.
# Assim dá para abrir um idioma sozinho sem rolar por um arquivo gigante, e
# o build confere se todos têm o mesmo conjunto de chaves.
# ===========================================================================
import importlib

for _cod in ORDEM:
    if _cod in IDIOMAS:
        continue
    IDIOMAS[_cod] = importlib.import_module(f'traducoes.{_cod}').DADOS


def conferir():
    """Devolve os problemas encontrados. Lista vazia = tudo certo."""
    base = set(IDIOMAS['pt'])
    problemas = []
    for cod in ORDEM:
        d = IDIOMAS.get(cod)
        if d is None:
            problemas.append(f'{cod}: idioma inteiro faltando')
            continue
        falta = base - set(d)
        sobra = set(d) - base
        if falta:
            problemas.append(f'{cod}: faltam as chaves {sorted(falta)}')
        if sobra:
            problemas.append(f'{cod}: chaves a mais {sorted(sobra)}')
        # o número de itens das listas tem que bater, senão a página sai torta
        for chave in ('notas', 'metricas', 'passos', 'recursos', 'priv_itens',
                      'plano_itens', 'faq'):
            if chave in d and len(d[chave]) != len(IDIOMAS['pt'][chave]):
                problemas.append(
                    f'{cod}: {chave} tem {len(d[chave])} itens, '
                    f'o português tem {len(IDIOMAS["pt"][chave])}')
    return problemas
