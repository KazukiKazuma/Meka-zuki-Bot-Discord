import nextcord

command_modules = {
    "Music Player":"On",
    "Stream Alerts":"On",
    "Dice Rolling":"On",
    "Jokenpo":"On",
}

module_disabled_message = nextcord.Embed(
    description="Este módulo de comandos se encontra temporariamente desabilitado",
    color=0xffb11a
)