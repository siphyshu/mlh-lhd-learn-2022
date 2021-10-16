import discord
from discord.ext import commands, tasks
import json

class MiscAdminSetup(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def setprefix(self, ctx, prefix):
        try:
            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            prefixes[str(ctx.guild.id)] = prefix

            with open("prefixes.json", "w") as f:
                json.dump(prefixes, f, indent=4)

            await ctx.send(f"Prefix changed to `{prefix}`")

        except:
            await ctx.send(f"You need administrator permissions for this!")


    @commands.command()
    async def prefix(self, ctx):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        guildPrefix = prefixes[str(ctx.guild.id)]
        sendMessage = f"The prefix for this server is `{guildPrefix}`\nChange the prefix by doing `{guildPrefix}setprefix [prefix]`"
        await ctx.send(sendMessage)


    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, name: str):
        try:
            self.bot.reload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(e)
        await ctx.send(f'**{name}** Cog reloaded.')


    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, name: str):
        try:
            self.bot.unload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(e)
        await ctx.send(f'**{name}** Cog unloaded.')


    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, name: str):
        try:
            self.bot.load_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(e)
        await ctx.send(f'**{name}** Cog loaded.')


    @commands.command()
    async def ping(self, ctx):
        try:
            await ctx.send(f"Pong! `{round(self.bot.latency, 3)}ms`")
        except:
            await ctx.send(f"Oops! Something went wrong.")


    # @commands.Cog.listener()
    # async def on_message(self):
    #     pass


def setup(bot):
    bot.add_cog(MiscAdminSetup(bot))