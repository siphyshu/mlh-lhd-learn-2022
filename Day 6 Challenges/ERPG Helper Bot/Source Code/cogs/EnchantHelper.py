import discord
from discord.ext import commands, tasks
import asyncio

enchantsList = ["NORMIE", "GOOD", "GREAT", "MEGA", "EPIC",
            "HYPER", "ULTIMATE", "PERFECT", "EDGY",
            "ULTRA-EDGY", "OMEGA", "ULTRA-OMEGA", "GODLY"]
enchantDb = {}


class EnchantHelper(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command() 
	async def setenchant(self, ctx, *, targetEnchant: str):
		if targetEnchant.upper() in enchantsList:
			await ctx.send(f"Alright, you'll be muted when you get :sparkles: **{targetEnchant}** :sparkles: or above.")
			targetEnchantIndex = enchantsList.index(targetEnchant.upper())
			targetEnchantList = enchantsList[targetEnchantIndex:]
			print(targetEnchantList)
			username = ctx.message.author.name
			userid = ctx.message.author.id

			enchantDb[username] = {"user":userid, "targetenchant":targetEnchantList}


		else:
			await ctx.send(f"That's not a valid enchant, please see `rpg help enchant` for valid enchants.")


	@commands.Cog.listener() # You use commands.Cog.listener() instead of bot.event
	async def on_ready(self):
		print("// enchant helper cog ready")


	@commands.Cog.listener()
	async def on_message(self, message):
		# print("hmmmmm")
		
		if message.author.id == self.bot.user.id:
			print("i ran lol")
			return

		# rpgmessage = message.content
		try:
			if (len(message.embeds) != 0):
				embedDict = message.embeds[0].to_dict()
				embedName = embedDict['author']['name']
				# print(embedDict)

				if "enchant" in embedName:
					username = embedName.replace("'s enchant", "")
					givenEnchant = embedDict["fields"][0]["name"].replace(":sparkles: ~-~> **", "").replace("** <~-~ :sparkles:", "").upper()
				else:
					return

				if username in enchantDb.keys():
					userid = enchantDb[username]["user"]
					targetenchant = enchantDb[username]["targetenchant"]
					if givenEnchant in targetenchant:
						await message.channel.send(f"<@{userid}>, MUTE!")
				else:
					return

				# print(embedDict)
				# print("I was run.")


		except Exception as e:
			await message.channel.send(e)
			pass


def setup(bot):
	bot.add_cog(EnchantHelper(bot))