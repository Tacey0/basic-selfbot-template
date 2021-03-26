import discord
import json
import time

from discord.ext import commands

whatever = discord.Client
whatever = commands.Bot(description="whatever selfbot", command_prefix="x" , self_bot=True)
whatever.remove_command("help")

@whatever.command(pass_context=True)
async def help(ctx, *, type):
  await ctx.message.delete()
  if type == 'util':
    embed = discord.Embed(
      title = '*whatever sb ig*',
      color = 000000
    )
    embed.add_field(name=f'🎸**ping**', value='**⭐ shows the latecny between the bot and shit dip shit**', inline=False)
    embed.set_thumbnail(url=whatever.user.avatar_url)
    await ctx.send(embed=embed, delete_after=10)

@help.error
async def help_error(ctx, error):
  embed = discord.Embed(
    title = '*whatever sb ig*',
    color = 000000,
    description = f'''
   \n🎸 `help util` \n **⭐ for util shit**
    ''')
  if isinstance(error, discord.ext.commands.MissingRequiredArgument):
    await ctx.message.delete()
  embed.set_thumbnail(url=whatever.user.avatar_url)
  embed.set_footer(text="whatever sb")
  await ctx.send(embed=embed, delete_after=10)

@whatever.command()
async def ping(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title = 'whatever sb ig',
        color = 000000,
        description = f'''
        Latency: {round(whatever.latency * 1000)}ms
        '''    
    )
    embed.set_thumbnail(url=whatever.user.avatar_url)
    embed.set_footer(text="whatever sb")
    await ctx.send(embed=embed, delete_after=10)



whatever.run('', bot=False)
