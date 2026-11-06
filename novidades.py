# -*- coding: utf-8 -*-
"""
Novidades de nov/2026 no site: Discussão em grupo, recado nos Stories e
reações no Mural.

Só ACRESCENTA. Os três cartões novos entram antes do último cartão de
recursos (o de denúncia e bloqueio, que fecha o bento), e as duas perguntas
novas entram no fim das dúvidas. Nada do texto que já existia muda.

Os nomes seguem os do app em cada idioma (Mural, Wall, Muro, Pinnwand...),
que é o que a pessoa vai ver ao abrir o Nimo.
"""

RECURSOS = {
    'pt': [
        ('Discussão em grupo no Mural',
         'Marque "Discussão em grupo" ao escrever seu recado e quem responder '
         'entra numa conversa com todo mundo. Até 15 pessoas, só texto, e ela '
         'termina sozinha em 24 horas. Gostou de alguém? Continue no privado.'),
        ('Seu recado nos Stories',
         'Compartilhe seu recado ou sua discussão nos Stories do Instagram ou '
         'no WhatsApp. Quem tocar no link cai direto no Nimo para te '
         'responder.'),
        ('Reações no Mural',
         'Um toque em 👋 😂 ❤️ mostra que você viu o recado. E quem postou '
         'pode te chamar para conversar.'),
    ],
    'en': [
        ('Group discussions on the Wall',
         'Pick "Group discussion" when you write your note and whoever replies '
         'joins one chat with everyone. Up to 15 people, text only, and it '
         'ends on its own after 24 hours. Liked someone? Keep talking '
         'privately.'),
        ('Your note in Stories',
         'Share your note or your discussion to Instagram Stories or WhatsApp. '
         'Anyone who taps the link lands right in Nimo to reply.'),
        ('Reactions on the Wall',
         'One tap on 👋 😂 ❤️ shows you saw the note. And whoever posted it '
         'can invite you to chat.'),
    ],
    'es': [
        ('Discusión en grupo en el Muro',
         'Marca "Discusión en grupo" al escribir tu mensaje y quien responda '
         'entra en una charla con todos. Hasta 15 personas, solo texto, y '
         'termina sola en 24 horas. ¿Te cayó bien alguien? Sigue en privado.'),
        ('Tu mensaje en las Historias',
         'Comparte tu mensaje o tu discusión en las Historias de Instagram o en '
         'WhatsApp. Quien toque el enlace llega directo a Nimo para '
         'responderte.'),
        ('Reacciones en el Muro',
         'Un toque en 👋 😂 ❤️ muestra que viste el mensaje. Y quien lo publicó '
         'puede invitarte a hablar.'),
    ],
    'de': [
        ('Gruppendiskussionen an der Pinnwand',
         'Wähle beim Schreiben „Gruppendiskussion" und wer antwortet, kommt in '
         'einen Chat mit allen. Bis zu 15 Personen, nur Text, nach 24 Stunden '
         'ist sie von selbst vorbei. Jemand war sympathisch? Schreibt privat '
         'weiter.'),
        ('Deine Nachricht in der Story',
         'Teile deine Nachricht oder deine Diskussion in Instagram-Storys oder '
         'auf WhatsApp. Wer auf den Link tippt, landet direkt in Nimo und kann '
         'antworten.'),
        ('Reaktionen an der Pinnwand',
         'Ein Tipp auf 👋 😂 ❤️ zeigt, dass du die Nachricht gesehen hast. Und '
         'wer sie gepostet hat, kann dich zum Chat einladen.'),
    ],
    'tr': [
        ('Duvar\'da grup tartışması',
         'Notunu yazarken "Grup tartışması"nı seç; yanıt veren herkes aynı '
         'sohbete katılır. En fazla 15 kişi, sadece yazı ve 24 saat sonra '
         'kendiliğinden biter. Birini sevdin mi? Özelden devam et.'),
        ('Notun Hikâyelerde',
         'Notunu ya da tartışmanı Instagram Hikâyeleri\'nde veya WhatsApp\'ta '
         'paylaş. Bağlantıya dokunan doğrudan Nimo\'ya gelir ve sana cevap '
         'verir.'),
        ('Duvar\'da tepkiler',
         '👋 😂 ❤️ ile tek dokunuşta notu gördüğünü göster. Notu paylaşan da '
         'seni sohbete çağırabilir.'),
    ],
    'ru': [
        ('Групповые обсуждения на Стене',
         'Выбери «Групповое обсуждение», когда пишешь записку, и все, кто '
         'ответит, попадут в общий чат. До 15 человек, только текст, и через '
         '24 часа обсуждение закончится само. Кто-то понравился? Продолжайте '
         'в личке.'),
        ('Твоя записка в историях',
         'Делись запиской или обсуждением в историях Instagram или в WhatsApp. '
         'Кто нажмёт на ссылку, сразу попадёт в Nimo и сможет ответить.'),
        ('Реакции на Стене',
         'Одно нажатие на 👋 😂 ❤️ показывает, что ты увидел(а) записку. А '
         'автор может позвать тебя пообщаться.'),
    ],
    'ar': [
        ('نقاش جماعي على الحائط',
         'اختر "نقاش جماعي" عند كتابة رسالتك، وكل من يرد يدخل محادثة واحدة مع '
         'الجميع. حتى 15 شخصًا، نص فقط، وينتهي تلقائيًا بعد 24 ساعة. أعجبك '
         'أحدهم؟ تابعا على الخاص.'),
        ('رسالتك في القصص',
         'شارك رسالتك أو نقاشك في قصص إنستغرام أو على واتساب. من يضغط على '
         'الرابط يصل مباشرة إلى Nimo ليرد عليك.'),
        ('تفاعلات على الحائط',
         'لمسة واحدة على 👋 😂 ❤️ تُظهر أنك رأيت الرسالة. ويمكن لصاحبها أن '
         'يدعوك للدردشة.'),
    ],
    'he': [
        ('דיון קבוצתי בלוח',
         'בחרו "דיון קבוצתי" כשאתם כותבים הודעה, וכל מי שעונה נכנס לשיחה אחת '
         'עם כולם. עד 15 אנשים, טקסט בלבד, והדיון נגמר לבד אחרי 24 שעות. '
         'מישהו מצא חן בעיניכם? המשיכו בפרטי.'),
        ('ההודעה שלכם בסטורי',
         'שתפו את ההודעה או הדיון שלכם בסטורי של אינסטגרם או בוואטסאפ. מי '
         'שמקיש על הקישור מגיע ישר ל-Nimo כדי לענות.'),
        ('תגובות בלוח',
         'נגיעה אחת ב-👋 😂 ❤️ מראה שראיתם את ההודעה. ומי שפרסם אותה יכול '
         'להזמין אתכם לשיחה.'),
    ],
    'hi': [
        ('दीवार पर ग्रुप चर्चा',
         'संदेश लिखते समय "ग्रुप चर्चा" चुनें, और जो भी जवाब देगा वह सबके '
         'साथ एक बातचीत में आ जाएगा। अधिकतम 15 लोग, सिर्फ़ टेक्स्ट, और 24 '
         'घंटे बाद अपने आप खत्म। कोई पसंद आया? निजी में बात जारी रखें।'),
        ('आपका संदेश स्टोरी में',
         'अपना संदेश या चर्चा Instagram स्टोरी या WhatsApp पर शेयर करें। '
         'लिंक पर टैप करने वाला सीधे Nimo में आकर आपको जवाब देता है।'),
        ('दीवार पर रिएक्शन',
         '👋 😂 ❤️ पर एक टैप से दिखाएँ कि आपने संदेश देखा। और पोस्ट करने '
         'वाला आपको बातचीत के लिए बुला सकता है।'),
    ],
    'ja': [
        ('ウォールでグループディスカッション',
         'メッセージを書くときに「グループディスカッション」を選ぶと、返信した'
         '人はみんなと同じチャットに参加します。最大15人、テキストのみ、24時間'
         'で自動的に終了。気になる人がいたら個別に話せます。'),
        ('メッセージをストーリーズに',
         'メッセージやディスカッションをInstagramのストーリーズやWhatsAppで'
         'シェア。リンクをタップした人はそのままNimoで返信できます。'),
        ('ウォールでリアクション',
         '👋 😂 ❤️ をタップするだけで、メッセージを見たことが伝わります。'
         '投稿した人はあなたをチャットに誘えます。'),
    ],
    'ko': [
        ('담벼락 그룹 토론',
         '메시지를 쓸 때 "그룹 토론"을 선택하면 답장한 사람은 모두와 같은 '
         '대화에 들어와요. 최대 15명, 텍스트만, 24시간 후 자동으로 끝나요. '
         '마음에 드는 사람이 있다면 1:1로 이어가세요.'),
        ('내 메시지를 스토리에',
         '메시지나 토론을 인스타그램 스토리나 WhatsApp에 공유하세요. 링크를 '
         '누른 사람은 바로 Nimo로 와서 답장할 수 있어요.'),
        ('담벼락 반응',
         '👋 😂 ❤️ 한 번만 눌러도 메시지를 봤다는 걸 알릴 수 있어요. 글쓴 '
         '사람은 나를 대화에 초대할 수 있어요.'),
    ],
}

FAQ = {
    'pt': [
        ('O que é a Discussão em grupo?',
         ['É um recado do Mural que vira bate-papo em grupo: todo mundo que '
          'responde entra na mesma conversa. Cabem até 15 pessoas, só texto, e '
          'ela termina sozinha em 24 horas — aí as mensagens somem.',
          'Quem criou pode remover quem passar dos limites, e todo apelido tem '
          'denúncia e bloqueio. Gostou de alguém? Toque no apelido para '
          'continuar no privado ou pedir amizade.']),
        ('Como compartilho meu recado nos Stories?',
         ['No seu recado do Mural, toque em <b>Compartilhar nos Stories</b>. O '
          'Nimo monta a imagem e copia o link. No Instagram, cole o link no '
          'adesivo de link; no WhatsApp ele já vai junto. Quem tocar no link '
          'cai direto no seu recado — ou dentro da sua discussão.']),
    ],
    'en': [
        ('What is a group discussion?',
         ['It is a Wall note that turns into a group chat: everyone who replies '
          'joins the same conversation. Up to 15 people, text only, and it ends '
          'on its own after 24 hours — then the messages are gone.',
          'The creator can remove anyone who crosses the line, and every '
          'nickname has report and block. Liked someone? Tap their nickname to '
          'keep talking privately or add them as a friend.']),
        ('How do I share my note to Stories?',
         ['On your Wall note, tap <b>Share to Stories</b>. Nimo builds the '
          'image and copies the link. On Instagram, paste the link into the '
          'link sticker; on WhatsApp it goes along automatically. Anyone who '
          'taps the link lands right on your note — or inside your '
          'discussion.']),
    ],
    'es': [
        ('¿Qué es la discusión en grupo?',
         ['Es un mensaje del Muro que se convierte en charla en grupo: todos '
          'los que responden entran en la misma conversación. Hasta 15 '
          'personas, solo texto, y termina sola en 24 horas — luego los '
          'mensajes desaparecen.',
          'Quien la creó puede quitar a quien se pase de la raya, y cada apodo '
          'tiene denuncia y bloqueo. ¿Te cayó bien alguien? Toca su apodo para '
          'seguir en privado o pedir amistad.']),
        ('¿Cómo comparto mi mensaje en las Historias?',
         ['En tu mensaje del Muro, toca <b>Compartir en Historias</b>. Nimo '
          'arma la imagen y copia el enlace. En Instagram, pega el enlace en el '
          'sticker de enlace; en WhatsApp va incluido. Quien toque el enlace '
          'llega directo a tu mensaje — o dentro de tu discusión.']),
    ],
    'de': [
        ('Was ist eine Gruppendiskussion?',
         ['Eine Pinnwand-Nachricht, die zum Gruppenchat wird: Alle, die '
          'antworten, landen im selben Chat. Bis zu 15 Personen, nur Text, und '
          'nach 24 Stunden ist sie von selbst vorbei — dann sind die '
          'Nachrichten weg.',
          'Wer sie erstellt hat, kann Leute entfernen, die zu weit gehen, und '
          'jeder Spitzname hat Melden und Blockieren. Jemand war sympathisch? '
          'Tippe auf den Spitznamen, um privat weiterzuschreiben oder eine '
          'Freundschaftsanfrage zu senden.']),
        ('Wie teile ich meine Nachricht in der Story?',
         ['Tippe bei deiner Pinnwand-Nachricht auf <b>In Storys teilen</b>. '
          'Nimo erstellt das Bild und kopiert den Link. Auf Instagram fügst du '
          'den Link in den Link-Sticker ein, auf WhatsApp geht er automatisch '
          'mit. Wer auf den Link tippt, landet direkt bei deiner Nachricht — '
          'oder in deiner Diskussion.']),
    ],
    'tr': [
        ('Grup tartışması nedir?',
         ['Grup sohbetine dönüşen bir Duvar notudur: yanıt veren herkes aynı '
          'sohbete katılır. En fazla 15 kişi, sadece yazı ve 24 saat sonra '
          'kendiliğinden biter — sonra mesajlar silinir.',
          'Tartışmayı açan kişi sınırı aşanları çıkarabilir; her takma adda '
          'şikâyet ve engelleme vardır. Birini sevdin mi? Takma adına dokunup '
          'özelden devam et ya da arkadaşlık iste.']),
        ('Notumu Hikâyelerde nasıl paylaşırım?',
         ['Duvar\'daki notunda <b>Hikâyede paylaş</b>\'a dokun. Nimo görseli '
          'hazırlar ve bağlantıyı kopyalar. Instagram\'da bağlantıyı bağlantı '
          'çıkartmasına yapıştır; WhatsApp\'ta kendiliğinden eklenir. '
          'Bağlantıya dokunan doğrudan notuna — ya da tartışmanın içine — '
          'gelir.']),
    ],
    'ru': [
        ('Что такое групповое обсуждение?',
         ['Это записка на Стене, которая превращается в групповой чат: все, кто '
          'ответил, попадают в одну беседу. До 15 человек, только текст, и '
          'через 24 часа обсуждение заканчивается само — сообщения исчезают.',
          'Автор может удалить тех, кто переходит границы, а у каждого ника '
          'есть жалоба и блокировка. Кто-то понравился? Нажми на ник, чтобы '
          'продолжить в личке или добавить в друзья.']),
        ('Как поделиться запиской в историях?',
         ['В своей записке на Стене нажми <b>Поделиться в историях</b>. Nimo '
          'сделает картинку и скопирует ссылку. В Instagram вставь ссылку в '
          'стикер «Ссылка», в WhatsApp она добавится сама. Кто нажмёт на '
          'ссылку, сразу попадёт к твоей записке — или в твоё обсуждение.']),
    ],
    'ar': [
        ('ما هو النقاش الجماعي؟',
         ['رسالة على الحائط تتحول إلى دردشة جماعية: كل من يرد يدخل المحادثة '
          'نفسها. حتى 15 شخصًا، نص فقط، وينتهي تلقائيًا بعد 24 ساعة — ثم '
          'تختفي الرسائل.',
          'يمكن لمن أنشأه إزالة من يتجاوز الحدود، ولكل اسم خيار الإبلاغ '
          'والحظر. أعجبك أحدهم؟ اضغط على اسمه لتكمل على الخاص أو ترسل طلب '
          'صداقة.']),
        ('كيف أشارك رسالتي في القصص؟',
         ['في رسالتك على الحائط، اضغط <b>شارك في القصص</b>. يجهّز Nimo الصورة '
          'وينسخ الرابط. في إنستغرام الصق الرابط في ملصق الرابط، وفي واتساب '
          'يُرسل معها تلقائيًا. من يضغط على الرابط يصل مباشرة إلى رسالتك — أو '
          'إلى داخل نقاشك.']),
    ],
    'he': [
        ('מה זה דיון קבוצתי?',
         ['הודעה בלוח שהופכת לצ׳אט קבוצתי: כל מי שעונה נכנס לאותה שיחה. עד 15 '
          'אנשים, טקסט בלבד, והדיון נגמר לבד אחרי 24 שעות — ואז ההודעות '
          'נמחקות.',
          'מי שפתח את הדיון יכול להסיר מי שחוצה את הגבול, ולכל כינוי יש דיווח '
          'וחסימה. מישהו מצא חן בעיניכם? הקישו על הכינוי כדי להמשיך בפרטי או '
          'לשלוח בקשת חברות.']),
        ('איך משתפים את ההודעה בסטורי?',
         ['בהודעה שלכם בלוח, הקישו על <b>שיתוף בסטורי</b>. Nimo מכין את '
          'התמונה ומעתיק את הקישור. באינסטגרם הדביקו את הקישור במדבקת הקישור; '
          'בוואטסאפ הוא נשלח יחד איתה. מי שמקיש על הקישור מגיע ישר להודעה '
          'שלכם — או לתוך הדיון.']),
    ],
    'hi': [
        ('ग्रुप चर्चा क्या है?',
         ['यह दीवार का एक संदेश है जो ग्रुप चैट बन जाता है: जवाब देने वाले सभी '
          'लोग एक ही बातचीत में आ जाते हैं। अधिकतम 15 लोग, सिर्फ़ टेक्स्ट, और '
          '24 घंटे बाद यह अपने आप खत्म हो जाती है — फिर संदेश मिट जाते हैं।',
          'चर्चा शुरू करने वाला हद पार करने वालों को हटा सकता है, और हर नाम '
          'पर रिपोर्ट और ब्लॉक है। कोई पसंद आया? उसके नाम पर टैप करके निजी '
          'में बात करें या दोस्ती का अनुरोध भेजें।']),
        ('मैं अपना संदेश स्टोरी में कैसे शेयर करूँ?',
         ['दीवार पर अपने संदेश में <b>स्टोरी में शेयर करें</b> पर टैप करें। '
          'Nimo तस्वीर बनाता है और लिंक कॉपी कर देता है। Instagram में लिंक को '
          'लिंक स्टिकर में पेस्ट करें; WhatsApp में यह अपने आप साथ जाता है। '
          'लिंक पर टैप करने वाला सीधे आपके संदेश पर — या आपकी चर्चा के अंदर '
          '— पहुँचता है।']),
    ],
    'ja': [
        ('グループディスカッションとは？',
         ['グループチャットになるウォールのメッセージです。返信した人はみんな'
          '同じ会話に参加します。最大15人、テキストのみ、24時間で自動的に終了'
          'し、メッセージは消えます。',
          '作成した人は度を越した人を削除でき、すべてのニックネームに通報と'
          'ブロックがあります。気になる人がいたら、ニックネームをタップして'
          '個別に話したり友だち申請したりできます。']),
        ('メッセージをストーリーズでシェアするには？',
         ['ウォールの自分のメッセージで<b>ストーリーズでシェア</b>をタップ。'
          'Nimoが画像を作り、リンクをコピーします。Instagramではリンク'
          'スタンプにリンクを貼り付け、WhatsAppでは自動で一緒に送られます。'
          'リンクをタップした人は、あなたのメッセージ（またはディスカッション）'
          'に直接届きます。']),
    ],
    'ko': [
        ('그룹 토론이 뭔가요?',
         ['그룹 채팅이 되는 담벼락 메시지예요. 답장한 사람은 모두 같은 대화에 '
          '들어와요. 최대 15명, 텍스트만, 24시간 후 자동으로 끝나고 메시지는 '
          '사라져요.',
          '토론을 만든 사람은 선을 넘는 사람을 내보낼 수 있고, 모든 닉네임에 '
          '신고와 차단이 있어요. 마음에 드는 사람이 있다면 닉네임을 눌러 1:1로 '
          '대화하거나 친구 신청을 보내세요.']),
        ('메시지를 스토리에 어떻게 공유하나요?',
         ['담벼락의 내 메시지에서 <b>스토리에 공유</b>를 누르세요. Nimo가 '
          '이미지를 만들고 링크를 복사해 줘요. 인스타그램에서는 링크 스티커에 '
          '붙여 넣고, WhatsApp에서는 자동으로 함께 보내져요. 링크를 누른 '
          '사람은 바로 내 메시지로 — 또는 토론 안으로 — 들어와요.']),
    ],
}


def aplicar(idiomas):
    """Acrescenta as novidades em todos os idiomas (sem tirar nada)."""
    for cod, d in idiomas.items():
        novos = RECURSOS.get(cod) or RECURSOS['en']
        rec = list(d['recursos'])
        # O último cartão (denúncia e bloqueio) fecha o bento: os novos entram
        # antes dele.
        d['recursos'] = rec[:-1] + list(novos) + rec[-1:]
        d['faq'] = list(d['faq']) + list(FAQ.get(cod) or FAQ['en'])
