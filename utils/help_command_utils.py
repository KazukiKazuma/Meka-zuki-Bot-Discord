import nextcord

help_music = nextcord.Embed(
    title="Help | Música",
    color=0xffffff
)
help_music.set_thumbnail(url="https://i.imgur.com/JIFYQW6.gif")
help_music.add_field(
    name="ㅤ",
    value="ㅤ",
    inline=False
)
help_music.add_field(
    name="/play `música`",
    value="Usado para fazer com que o bot conecte no canal e comece a tocar a música que você forneceu. Caso alguma música já esteja tocando, este comando assume a função de adicionar a música especificada à queue. O campo de `música` deste comando aceita tanto o `nome de uma música` quanto um `link da música no YouTube`;",
    inline=False
)
help_music.add_field(
    name="/queue",
    value="Mostra a lista de músicas que foram adicionadas e estão na fila de espera para serem tocadas;",
    inline=False
)
help_music.add_field(
    name="/skip",
    value="Pula para a próxima música de acordo com a posição na queue;",
    inline=False
)
help_music.add_field(
    name="/pause",
    value="Pausa a música que está tocando no momento que o comando foi usado;",
    inline=False
)
help_music.add_field(
    name="/resume",
    value="Volta a tocar a música que estava tocando no momento que o comando de *pause* foi usado.",
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
    name="ㅤ",
    value="ㅤ",
    inline=False
)
help_music.set_footer(text="Caso ainda tenha dúvidas fique a vontade para perguntar aos outros membors da Guilda", icon_url="https://i.imgur.com/M6rbN5i.png")