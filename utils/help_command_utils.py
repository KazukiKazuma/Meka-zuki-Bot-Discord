import nextcord

help_music = nextcord.Embed(
    title="Help | Música",
    color=0xffffff
)
help_music.set_thumbnail(url="https://i.imgur.com/JIFYQW6.gif")
help_music.add_field(
    name="\u200b",
    value="\u200b",
    inline=False
)
help_music.add_field(
    name="/play `música`",
    value="Usado para fazer com que o bot conecte no canal e comece a tocar a música que você forneceu. Caso alguma música já esteja tocando, este comando assume a função de adicionar a música especificada à queue. O campo de `música` deste comando aceita tanto o `nome de uma música` quanto um `link da música no YouTube`;",
    inline=False
)
help_music.add_field(
    name="/remove `música`",
    value="Usado para remover uma música da queue, fornecendo dentro do campo `música` ou o nome ou a posição na queue da música que quer remover",
    inline=False
)
help_music.add_field(
    name="/stop  &  /leave",
    value="O __/stop__ faz com que o bot pare de tocar música, limpe a queue, mas continue no canal de voz. Já o __/leave__ faz o mesmo mas também desconecta o Meka-zuki do canal de voz;",
    inline=False
)
help_music.add_field(
    name="/pause  &  /resume",
    value="O __/pause__ pausa a música que está tocando no momento que o comando foi usado. Já o __/resume__ faz com que ela volte a tocar.",
    inline=False
)
help_music.add_field(
    name="/skip",
    value="Pula para a próxima música de acordo com a posição na queue;",
    inline=False
)
help_music.add_field(
    name="/queue",
    value="Mostra a lista de músicas que foram adicionadas e estão na fila de espera para serem tocadas;",
    inline=False
)
help_music.add_field(
    name="/loop",
    value="Faz com que a música tocando no momento continue repetindo indefinidamente. O comando é usado tanto para ativar a repetição quanto desativar.",
    inline=False
)
help_music.add_field(
    name="/nowplaying",
    value="Envia uma mensagem contendo o nome e mais algumas informações da música que está tocando no momento que o comando foi usado.",
    inline=False
)
help_music.add_field(
    name="/link_da_musica_no_pv",
    value="Envia o link da música que está tocando no momento nas suas mensagens privadas para que você possa se lembrar da música mais tarde caso queira.",
    inline=False
)
help_music.add_field(
    name="/painel",
    value="Cria um painel interativo no canal para você controlar as músicas tocadas pelo Meka-zuki em um lugar só.",
    inline=False
)
help_music.add_field(
    name="\u200b",
    value="\u200b",
    inline=False
)
help_music.set_footer(text="Caso ainda tenha dúvidas fique a vontade para perguntar aos outros membors da Guilda", icon_url="https://i.imgur.com/M6rbN5i.png")





help_dice = nextcord.Embed(
    title="Help | Rolagem de Dados",
    color=0xffffff
)
help_dice.set_thumbnail(url="https://i0.wp.com/www.richardhughesjones.com/wp-content/uploads/2019/01/dice-gif.gif?fit=480%2C480&ssl=1")
help_dice.add_field(
    name="\u200b",
    value="\u200b",
    inline=False
)
help_dice.add_field(
    name="/rolagem `quantidade` `tipo`",
    value="Te possibilita fazer uma rolagem de dados fornecendo a `quantidade` de dados que quer rolar, e qual `tipo` de dado quer rolar.\nCaso queira fazer uma rolagem bônus, ou seja, ter um resultado de outra rolagem somada à sua rolagem base, você pode usar os campos __opcionais__ de `quantidade-de-dados-bônus` e `tipo-do-dado-bônus` para especificar quantos dados e de qual tipo você quer adicionar o valor à sua rolagem..",
    inline=False
)
help_dice.add_field(
    name="\u200b",
    value="segue um exemplo da resposta do bot para o uso do comando /rolagem `quantidade`: **__1__** `tipo`: **__d20__** `quantidade-de-dados-bônus`: **__1__** `tipo-do-dado-bônus`: **__d4__**",
    inline=False
)
help_dice.set_image(url="https://i.imgur.com/r9me3Ab.jpg")
help_dice.set_footer(text="\u200b \nCaso ainda tenha dúvidas fique a vontade para perguntar aos outros membors da Guilda", icon_url="https://i.imgur.com/M6rbN5i.png")