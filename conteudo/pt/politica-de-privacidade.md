# Política de Privacidade — Nimo Chat

**Última atualização:** 13 de agosto de 2026

O Nimo Chat é operado por **Leonardo Mondaine**, pessoa física, estabelecido
na R. Presidente João Goulart, 675, Cascavel, Paraná, Brasil ("nós").

Esta política explica, sem enrolação, o que o aplicativo coleta, por quê, com
quem compartilha e o que você pode exigir de nós.

Seguimos a **Lei Geral de Proteção de Dados** (Lei 13.709/2018 — LGPD). Para
quem usa o app na Europa e no Reino Unido, seguimos também o **GDPR**; para
residentes da Califórnia, a **CCPA/CPRA**.

Ao usar o Nimo Chat você concorda com esta política e com os
[Termos de Uso](termos.html). Se não concordar, não use o aplicativo.

> **Idioma.** Esta política é publicada em onze idiomas. A versão em inglês é
> a de referência para usuários fora do Brasil. **Se você está no Brasil, vale
> este texto em português** — é o seu direito pelo Código de Defesa do
> Consumidor, e não abrimos mão dele.

---

## 1. O que o Nimo Chat **não** coleta

Começamos por aqui porque é o que mais distingue este app:

- **Não pedimos e-mail nem telefone.** Não existe cadastro com e-mail.
- **Não pedimos senha.** Não há senha para vazar.
- **Não pedimos sua idade nem data de nascimento.** Você declara ter 18 anos
  ou mais ao aceitar os termos, e paramos por aí.
- **Não pedimos seu nome real.**
- **Não coletamos sua localização.** Mais que isso: **removemos os metadados
  EXIF de toda foto antes de enviá-la**, o que apaga a coordenada de onde ela
  foi tirada. É um dado que quase todo aplicativo esquece de limpar.
- **Não acessamos sua agenda de contatos.**
- **Não usamos publicidade nem rastreadores de anúncio.** Não há SDK de
  publicidade no aplicativo.

---

## 2. O que coletamos

### 2.1 Identificação da conta
Ao abrir o app pela primeira vez, criamos uma **conta anônima** com um
identificador aleatório gerado pelo Firebase Authentication. Esse
identificador não está ligado a você, ao seu aparelho ou a qualquer serviço
externo.

### 2.2 Dados de perfil, informados por você
| Dado | Obrigatório | Quem vê |
|---|---|---|
| Apelido | sim | qualquer pessoa com quem você conversar |
| Gênero (masculino/feminino) | sim | usado no pareamento; visível na conversa |
| Interesses | não | quem conversa com você |
| Frase de apresentação (bio) | não | quem conversa com você |
| Foto de perfil | não | **somente pessoas que aceitaram sua amizade** |

A foto de perfil merece destaque: o servidor **não entrega** sua foto para
estranhos. Ela só passa a ser visível depois que as duas pessoas aceitam a
amizade. Antes disso, todos veem um avatar desenhado pelo aplicativo.

### 2.3 Conteúdo que você cria
Mensagens de texto, fotos, vídeos, áudios, figurinhas, publicações no feed,
Status de 24 horas e recados no mural. Guardamos esse conteúdo para entregá-lo
à outra pessoa e para você reencontrá-lo depois.

**Fotos e vídeos de visualização única** são tratados de forma diferente: o
arquivo é **apagado do nosso servidor assim que é aberto**, e apagado
automaticamente em 24 horas se nunca for aberto.

### 2.4 Dados de funcionamento
- **Presença:** o horário do seu último acesso, para mostrarmos quantas
  pessoas estão online. Essa informação é agregada — ninguém consegue
  consultar quem especificamente está online.
- **Fila de pareamento:** enquanto você procura alguém, seu identificador,
  gênero e interesses ficam numa fila temporária, apagada assim que o
  pareamento acontece ou você desiste.
- **Token de notificação:** um código do Firebase Cloud Messaging para
  conseguirmos avisar você de mensagens novas. Você pode desligar as
  notificações a qualquer momento nas configurações.
- **Amizades, bloqueios e denúncias.**
- **Hash do código de recuperação:** quando você gera um código de
  recuperação, guardamos apenas uma impressão digital dele — nunca o código
  em si. Nem nós conseguimos descobrir qual é o seu código.

### 2.5 Chamadas de voz
Este ponto é importante: **o áudio das chamadas não passa pelos nossos
servidores e não é gravado.** A conversa vai diretamente de um aparelho para
o outro (tecnologia WebRTC).

Guardamos apenas os dados necessários para a ligação acontecer e para você
ver o histórico: quem ligou para quem, quando, se foi atendida e quanto
durou. Os dados técnicos de conexão são apagados assim que a chamada termina.

Em algumas redes a conexão direta não é possível, e o áudio precisa passar
por um servidor intermediário (TURN). Esse servidor **apenas repassa** os
pacotes: não grava, não armazena e não consegue ler o conteúdo.

### 2.6 Diagnóstico
Quando o aplicativo trava, o Firebase Crashlytics registra o erro, o modelo
do aparelho e a versão do sistema. Serve exclusivamente para corrigirmos
falhas.

---

## 3. Por que tratamos seus dados (bases legais)

| Finalidade | Base legal (LGPD) |
|---|---|
| Criar sua conta e entregar suas mensagens | execução de contrato (art. 7º, V) |
| Parear você com outra pessoa | execução de contrato |
| Impedir abuso, spam e assédio | legítimo interesse (art. 7º, IX) |
| Analisar falhas do aplicativo | legítimo interesse |
| Enviar notificações | consentimento (art. 7º, I) — revogável |
| Atender ordem judicial | cumprimento de obrigação legal (art. 7º, II) |

---

## 4. Com quem compartilhamos

Não vendemos, não alugamos e não trocamos seus dados. O compartilhamento se
limita a fornecedores que executam o serviço por nós:

| Fornecedor | Para quê | Onde processa |
|---|---|---|
| **Google Firebase** (Google LLC) | autenticação, banco de dados, arquivos, notificações e relatórios de falha | Estados Unidos e outros |
| **Apple App Store / Google Play** | distribuição e, quando houver, pagamento de assinaturas | conforme cada loja |
| **RevenueCat** | validar recibos de assinatura, quando as assinaturas estiverem ativas | Estados Unidos |
| **Servidor TURN** | repassar áudio de chamadas quando a conexão direta falha | a definir — ainda não contratamos servidor TURN |

Todos são obrigados contratualmente a usar os dados apenas para nos prestar o
serviço.

**Divulgação por obrigação legal:** podemos revelar dados diante de ordem
judicial ou requisição de autoridade competente. Analisamos cada pedido,
recusamos os que forem genéricos ou desproporcionais, e entregamos o mínimo
necessário.

**Transferência de negócio:** em caso de fusão, aquisição ou venda, seus
dados podem ser transferidos ao sucessor, que ficará obrigado a esta mesma
política.

---

## 5. Transferência internacional

Nossos fornecedores mantêm servidores fora do Brasil, principalmente nos
Estados Unidos. A transferência acontece com base no art. 33 da LGPD e, para
dados vindos da Europa, em Cláusulas Contratuais Padrão aprovadas pela
Comissão Europeia. Os dados trafegam sempre criptografados.

---

## 6. Por quanto tempo guardamos

| Dado | Prazo |
|---|---|
| Perfil e conversas | enquanto a conta existir |
| Foto/vídeo de visualização única | até ser aberta, ou 24 horas |
| Status | 24 horas |
| Recado no mural | 24 horas |
| Fila de pareamento | minutos |
| Dados técnicos da chamada | apagados ao fim da chamada |
| Denúncias | até 2 anos, para reincidência e defesa |
| Registros exigidos por lei | conforme o prazo legal |

---

## 7. Como excluir sua conta

Em **Perfil → Conta → Excluir minha conta**. Não pedimos justificativa e não
há período de espera: a exclusão começa no mesmo instante.

O que acontece: seu perfil e sua foto são apagados imediatamente; o banco de
dados do seu aparelho é zerado; e um processo automático remove, em seguida,
suas mensagens, publicações, status e arquivos dos nossos servidores.

**Duas coisas honestas sobre isso:**

1. Mensagens que você enviou para outra pessoa podem permanecer na conversa
   dela, como acontece em qualquer aplicativo de mensagens.
2. Se alguém tirou print ou salvou algo que você enviou, isso está fora do
   nosso alcance.

Excluir a conta **não cancela assinaturas**. O cancelamento é feito na App
Store ou no Google Play.

---

## 8. Seus direitos

Pela LGPD (art. 18), você pode a qualquer momento: confirmar se tratamos seus
dados; acessá-los; corrigir dados incompletos ou desatualizados; pedir
anonimização, bloqueio ou eliminação; pedir a portabilidade; saber com quem
compartilhamos; revogar consentimento; e se opor a um tratamento.

Na Europa e no Reino Unido, o GDPR garante os mesmos direitos, mais o de
apresentar reclamação à autoridade do seu país. Na Califórnia, a CCPA/CPRA
garante saber, excluir, corrigir e não ser discriminado por exercer esses
direitos — e registramos que **não vendemos e não compartilhamos dados
pessoais** no sentido dado por essa lei.

**Como exercer:** escreva para suporte@chatnimo.com. Respondemos em até 15 dias
(LGPD) ou 30 dias (GDPR). Para proteger sua conta, podemos pedir que você
prove o controle dela — por exemplo, informando o código de recuperação ou
enviando o pedido de dentro do aplicativo. Não cobramos por isso.

Você também pode reclamar diretamente à **ANPD** (gov.br/anpd).

---

## 9. Idade mínima

O Nimo Chat é destinado a **maiores de 18 anos**. Não permitimos contas de
menores de idade, e a declaração é feita no aceite dos termos.

**Não tratamos dados de crianças e adolescentes.** Se descobrirmos que um
menor de idade está usando o aplicativo, excluímos a conta e todos os dados
imediatamente. Se você é responsável por um adolescente e quer que a conta
dele seja removida, escreva para abuso@chatnimo.com — agimos no mesmo dia,
sem exigir justificativa e sem pedir documento.

Denúncias de perfis que aparentam ser de menores recebem prioridade máxima e
entram em fluxo de suspensão imediata.

> **Por que 18 e não 16.** O aplicativo junta conversa aleatória com
> desconhecidos, filtro por gênero, foto, vídeo, chamada de voz e anonimato.
> Cada peça isolada é defensável; somadas, criam um ambiente em que a
> presença de adolescentes multiplica o risco. E o consentimento de um
> responsável não resolveria isso de verdade: num aplicativo anônimo,
> **nenhum dos dois lados tem como saber a idade real do outro**.

---

## 10. Segurança

Usamos criptografia em trânsito (HTTPS/TLS) em toda comunicação, criptografia
em repouso nos servidores do Firebase, e regras de acesso que limitam, no
próprio servidor, o que cada pessoa consegue ler.

Vale explicar uma decisão de arquitetura: **sua lista de amigos não é legível
por ninguém além de você** — nem pelos seus próprios amigos. O feed funciona
ao contrário do óbvio: em vez de perguntar "quem são os amigos dessa pessoa",
cada publicação pergunta "essa pessoa me tem como amigo". O resultado é que
não existe forma de mapear quem conhece quem.

**Sobre o que não podemos prometer:** nenhum sistema é inviolável. Não
oferecemos criptografia de ponta a ponta nas mensagens de texto — elas são
criptografadas em trânsito e em repouso, mas tecnicamente poderíamos acessá-las
para cumprir ordem judicial. Preferimos dizer isso a vender uma segurança que
não entregamos. As **chamadas de voz**, essas sim, não passam por nós.

Em caso de incidente de segurança, comunicaremos os afetados e a ANPD nos
prazos legais.

---

## 11. Conteúdo de outras pessoas

O Nimo Chat conecta desconhecidos. Não lemos suas conversas nem as
pré-analisamos. Você é responsável pelo que escreve e envia.

Existem ferramentas de denúncia e bloqueio em toda conversa. **Analisamos
toda denúncia em até 24 horas** e removemos quem violar as regras. Casos
graves — suspeita de menor de idade, nudez não consentida, violência —
resultam em suspensão automática e imediata.

---

## 12. Publicidade

Hoje o Nimo Chat **não exibe publicidade** e não possui nenhuma biblioteca de
anúncios instalada. Isso é uma decisão de produto sobre o estado atual do
aplicativo, não uma promessa permanente. Se um dia mudarmos, atualizaremos
esta política e avisaremos antes.

Seus dados **nunca** serão vendidos a anunciantes ou corretores de dados.

---

## 13. Alterações

Podemos atualizar esta política. Mudanças relevantes serão avisadas dentro do
aplicativo com pelo menos 15 dias de antecedência. A data no topo indica a
última revisão.

---

## 14. Contato

**Leonardo Mondaine**
R. Presidente João Goulart, 675 — Cascavel, Paraná, Brasil

| Assunto | E-mail |
|---|---|
| Dúvidas, dados pessoais e conta | suporte@chatnimo.com |
| Denúncias e segurança | abuso@chatnimo.com |

Encarregado de dados (DPO): Leonardo Mondaine — suporte@chatnimo.com

Respondemos em poucos dias úteis.
