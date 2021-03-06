import nextcord

pause_embed = nextcord.Embed(
    title="Pause  :pause_button:",
    description="a música agora está pausada",
    color=0x3b88c3
)
pause_embed.set_footer(text="use o comando /resume para despausar")

resume_embed = nextcord.Embed(
    title="Resume  :arrow_forward:",
    description="a música agora está despausada",
    color=0x3b88c3
)
resume_embed.set_footer(text="use o comando /pause para pausar")

loop_embed = nextcord.Embed(
    title="Loop ON  :repeat_one:",
    description="a música agora irá repetir",
    color=0x3b88c3
)
loop_embed.set_footer(text="use o comando /loop novamente para desativar")

unloop_embed = nextcord.Embed(
    title="Loop OFF  :arrow_right:",
    description="a música não irá mais repetir",
    color=0x3b88c3
)
unloop_embed.set_footer(text="use o comando /loop novamente para ativar")

stop_embed = nextcord.Embed(
    title="Stop  :stop_button:",
    description="o bot parou de tocar música e limpor a queue",
    color=0x3b88c3
)
stop_embed.set_footer(text="use o comando /play tocar e adicionar músicas novamente")

connect_first = nextcord.Embed(
    title="Ops ...",
    description="Você não está conectado(a) a nenhum canal de voz.\nPara usar os comandos de música conecte-se a um primeiro",
    color=0xe42a44
)
connect_first.set_footer(text="no caso de dúvidas use /help")

no_music_playing = nextcord.Embed(
    title="Ops ...",
    description="Parece que o bot não está tocando nenhuma música no momento",
    color=0xe42a44
)
no_music_playing.set_footer(text="no caso de dúvidas use /help")

command_not_in_same_vc = nextcord.Embed(
    title="Ops ...",
    description="Você não pode usar comandos de música estando em um canal de voz diferente do bot",
    color=0xe42a44
)
command_not_in_same_vc.set_footer(text="no caso de dúvidas use /help")

play_not_in_same_vc = nextcord.Embed(
    title="Ops ...",
    description="Parece que o bot está ocupado em outro canal de voz.\nVocê pode esperar o bot ficar livre ou pode se juntar ao canal de voz onde o bot está.",
    color=0xe42a44
)
play_not_in_same_vc.set_footer(text="no caso de dúvidas use /help")

music_already_playing = nextcord.Embed(
    title="Ops ...",
    description="A música não está pausada para você precisar despausa-la",
    color=0xe42a44
)
music_already_playing.set_footer(text="no caso de dúvidas use /help")

music_already_paused = nextcord.Embed(
    title="Ops ...",
    description="Não tem nenhuma música tocando no momento para que você possa pausa-la",
    color=0xe42a44
)
music_already_paused.set_footer(text="no caso de dúvidas use /help")

no_next_songs = nextcord.Embed(
    title="Acabaram as músicas..",
    description="Não existe nenhuma próxima música para tocar, você pode usar `/play` para adicionar novas músicas à queue ou `/stop` caso queira parar a música atual.",
    color=0xe42a44
)
no_next_songs.set_footer(text="no caso de dúvidas use /help")

music_is_looping = nextcord.Embed(
    title="Ops ...",
    description="a música atual está em loop, desative o loop para usar este comando",
    color=0xe42a44
)
music_is_looping.set_footer(text="no caso de dúvidas use /help")

check_your_dm = nextcord.Embed(
    title="Dê uma olhada nas suas mensagens privadas   <a:PingoBongo:905962919727091752> ",
    color=0x3b88c3
)

use_use_the_panel = nextcord.Embed(
    description="um painel de música está aberto, use-o para controlar a música ou feche o painel e use os comandos",
    color=0xe42a44
)



panel_embed= nextcord.Embed(
    title="Painel de Música",
    description="use este painel para controlar o bot\nㅤ",
    color=0xc18568
)
panel_embed.set_thumbnail(url="https://i.imgur.com/spntYMz.gif")

panel_embed_updated= nextcord.Embed(
    description="o painel de controle foi atualizado",
    color=0x3b88c3
)