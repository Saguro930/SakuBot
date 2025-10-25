import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="ヘルプを表示します")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="ℹ️ヘルプ",
            color=discord.Color.green()
        )

        embed.add_field(
            name="💰 通貨・報酬システム",
            value=(
                "/daily … 20時間おきにログインボーナスを受け取る\n"
                "/give_coin user: price: … 指定ユーザーにコインを渡す\n"
                "/work … 仕事をしてコインと経験値を獲得（4時間ごと）\n"
                "/bank withdraw amount: … 銀行から出金（手数料あり）\n"
                "/profile … 所持金・銀行残高・職業レベルを確認\n"
                "/dollar … コインとドルのレート表示、交換可能"
            ),
            inline=False
        )

        embed.set_footer(text="SakuBor v0.1β対応")

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
