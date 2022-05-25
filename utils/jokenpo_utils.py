import nextcord



### ROCK ###

player_win_prock_bscissors = nextcord.Embed(
    title=f"E o resultado é <a:loading:747680523459231834>",
    description=f"Você **ganhou**!",
    color=0xfebcbb
)
player_win_prock_bscissors.set_image(url="https://c.tenor.com/O15KXmvG3X8AAAAd/opm-one-punch-man.gif")
player_win_prock_bscissors.set_footer(
    text=f"Você escolheu Pedra, Eu escolhi Tesoura.",
    icon_url="https://i.imgur.com/M6rbN5i.png"
)

player_lose_prock_bpaper = nextcord.Embed(
    title=f"E o resultado é <a:loading:747680523459231834>",
    description=f"Você **perdeu**!",
    color=0xfebcbb
)
player_lose_prock_bpaper.set_image(url="https://c.tenor.com/O15KXmvG3X8AAAAd/opm-one-punch-man.gif")
player_lose_prock_bpaper.set_footer(
    text=f"Você escolheu Pedra, Eu escolhi Papel.",
    icon_url="https://i.imgur.com/M6rbN5i.png"
)

player_draw_prock_brock = nextcord.Embed(
    title=f"E o resultado é <a:loading:747680523459231834>",
    description=f"Nós **espatamos**!",
    color=0xfebcbb
)
player_draw_prock_brock.set_image(url="https://c.tenor.com/O15KXmvG3X8AAAAd/opm-one-punch-man.gif")
player_draw_prock_brock.set_footer(
    text=f"Você escolheu Pedra, Eu escolhi Pedra também.",
    icon_url="https://i.imgur.com/M6rbN5i.png"
)



### PAPER ###

player_win_ppaper_brock = nextcord.Embed(
    title=f"E o resultado é <a:loading:747680523459231834>",
    description=f"Você **ganhou**!",
    color=0xfebcbb
)
player_win_ppaper_brock.set_image(url="https://c.tenor.com/O15KXmvG3X8AAAAd/opm-one-punch-man.gif")
player_win_ppaper_brock.set_footer(
    text=f"Você escolheu Papel, Eu escolhi Pedra.",
    icon_url="https://i.imgur.com/M6rbN5i.png"
)

player_lose_ppaper_bscissors = nextcord.Embed(
    title=f"E o resultado é <a:loading:747680523459231834>",
    description=f"Você **perdeu**!",
    color=0xfebcbb
)
player_lose_ppaper_bscissors.set_image(url="https://c.tenor.com/O15KXmvG3X8AAAAd/opm-one-punch-man.gif")
player_lose_ppaper_bscissors.set_footer(
    text=f"Você escolheu Papel, Eu escolhi Tesoura.",
    icon_url="https://i.imgur.com/M6rbN5i.png"
)

player_draw_ppaper_bpaper = nextcord.Embed(
    title=f"E o resultado é <a:loading:747680523459231834>",
    description=f"Nós **espatamos**!",
    color=0xfebcbb
)
player_draw_ppaper_bpaper.set_image(url="https://c.tenor.com/O15KXmvG3X8AAAAd/opm-one-punch-man.gif")
player_draw_ppaper_bpaper.set_footer(
    text=f"Você escolheu Papel, Eu escolhi Papel também.",
    icon_url="https://i.imgur.com/M6rbN5i.png"
)


### SCISSORS ###

player_win_pscissors_bpaper = nextcord.Embed(
    title=f"E o resultado é <a:loading:747680523459231834>",
    description=f"Você **ganhou**!",
    color=0xfebcbb
)
player_win_pscissors_bpaper.set_image(url="https://c.tenor.com/O15KXmvG3X8AAAAd/opm-one-punch-man.gif")
player_win_pscissors_bpaper.set_footer(
    text=f"Você escolheu Tesoura, Eu escolhi Papel.",
    icon_url="https://i.imgur.com/M6rbN5i.png"
)

player_lose_pscissors_brock = nextcord.Embed(
    title=f"E o resultado é <a:loading:747680523459231834>",
    description=f"Você **perdeu**!",
    color=0xfebcbb
)
player_lose_pscissors_brock.set_image(url="https://c.tenor.com/O15KXmvG3X8AAAAd/opm-one-punch-man.gif")
player_lose_pscissors_brock.set_footer(
    text=f"Você escolheu Tesoura, Eu escolhi Pedra.",
    icon_url="https://i.imgur.com/M6rbN5i.png"
)

player_draw_pscissors_bscissors = nextcord.Embed(
    title=f"E o resultado é <a:loading:747680523459231834>",
    description=f"Nós **espatamos**!",
    color=0xfebcbb
)
player_draw_pscissors_bscissors.set_image(url="https://c.tenor.com/O15KXmvG3X8AAAAd/opm-one-punch-man.gif")
player_draw_pscissors_bscissors.set_footer(
    text=f"Você escolheu Tesoura, Eu escolhi Tesoura também.",
    icon_url="https://i.imgur.com/M6rbN5i.png"
)