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
connect_first.set_footer(text="no caso de dúvidas procure usar o comando /help")

no_music_playing = nextcord.Embed(
    title="Ops ...",
    description="Parece que o bot não está tocando nenhuma música no momento",
    color=0xe42a44
)
no_music_playing.set_footer(text="no caso de dúvidas procure usar o comando /help")

command_not_in_same_vc = nextcord.Embed(
    title="Ops ...",
    description="Você não pode usar comandos de música estando em um canal de voz diferente do bot",
    color=0xe42a44
)
command_not_in_same_vc.set_footer(text="no caso de dúvidas procure usar o comando /help")

play_not_in_same_vc = nextcord.Embed(
    title="Ops ...",
    description="Parece que o bot está ocupado em outro canal de voz.\nVocê pode esperar o bot ficar livre ou pode se juntar ao canal de voz onde o bot está.",
    color=0xe42a44
)
play_not_in_same_vc.set_footer(text="no caso de dúvidas procure usar o comando /help")