import discord
from discord.ext import commands
from discord import app_commands

class Analyse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="analyse", description="Mockanalyse van een coin")
    @app_commands.describe(coin="De coin die je wil analyseren")
    async def analyse(self, interaction: discord.Interaction, coin: str):
        await interaction.response.send_message(
            f"Mockanalyse voor {coin.upper()} uitgevoerd. (TA nog niet actief)"
        )

async def setup(bot):
    await bot.add_cog(Analyse(bot))