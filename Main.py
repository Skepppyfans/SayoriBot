import random
from tokenize import Triple
from unittest.loader import VALID_MODULE_NAME
from urllib import response
import embedlinks
import discord
from discord.ext import commands
import asyncio

import json
import os

intents = discord.Intents.all()
bot=commands.Bot(command_prefix='s.', help_command=None)


# main commands

@bot.event
async def on_ready():
    activity = discord.Game(name="s.commands ┃ Lets Hang OUT.", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")

@bot.command()
async def Help(ctx):
    embed = discord.Embed(title="**Help**", description="Need any help? Type s.info", color = 16705372)
    embed.add_field(name="Fun", value="``Poems``,")
    embed.add_field(name="ㅤ", value="``Food``,")
    embed.add_field(name="ㅤ", value="``Motivation``.")
    embed.add_field(name="ㅤ", value="``Bread``")
    embed.add_field(name="ㅤ", value="``Memes``")
    embed.add_field(name="ㅤ", value="ㅤ")
    embed.add_field(name="Bot", value="``Botinfo``,")
    embed.add_field(name="ㅤ", value="``Info``,")
    embed.add_field(name="ㅤ", value="``Help``,")
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="**Help**", description="Need any help? Type s.info", color = 16705372)
    embed.add_field(name="Fun", value="``Poems``,")
    embed.add_field(name="ㅤ", value="``Food``,")
    embed.add_field(name="ㅤ", value="``Motivation``.")
    embed.add_field(name="ㅤ", value="``Bread``")
    embed.add_field(name="ㅤ", value="``Memes``")
    embed.add_field(name="ㅤ", value="ㅤ")
    embed.add_field(name="Bot", value="``Botinfo``,")
    embed.add_field(name="ㅤ", value="``Info``,")
    embed.add_field(name="ㅤ", value="``Help``,")
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command()
async def Info(ctx):
    embed = discord.Embed(title="Info", url="https://discord.gg/", description="How to use!", color = 16705372)
    embed.add_field(name="General use", value="prefix is s.<command>")
    embed.add_field(name="Development", value="``Bot is currently in beta stages! Any bugs? Report to the offical discord server``", inline=True)
    embed.set_footer(text="Join the offical discord! <coming soon>")
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Info", url="https://discord.gg/", description="How to use!", color = 16705372)
    embed.add_field(name="General use", value="prefix is s.<command>")
    embed.add_field(name="Development", value="``Bot is currently in beta stages! Any bugs? Report to the offical discord server``", inline=True)
    embed.set_footer(text="Join the offical discord! <coming soon>")
    await ctx.send(embed=embed)

@bot.command()
async def Botinfo(ctx):
    embed = discord.Embed(title="Bot Info", rl="https://discord.gg/", description="Info about Sayori!", color = 16705372)
    embed.add_field(name="Creators", value="Im.Lewis#2294")
    embed.add_field(name="Made with", value="Discord.py ``3.10.5``", inline=True)
    embed.add_field(name="ㅤ", value="Python ``3.10.5``", inline=True)
    embed.set_footer(text="Join the offical discord!")
    await ctx.send(embed=embed)

@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(title="Bot Info", rl="https://discord.gg/", description="Info about Sayori!", color = 16705372)
    embed.add_field(name="Creators", value="Im.Lewis#2294")
    embed.add_field(name="Made with", value="Discord.py ``3.10.5``", inline=True)
    embed.add_field(name="ㅤ", value="Python ``3.10.5``", inline=True)
    embed.set_footer(text="Can you find all the easter eggs?")
    await ctx.send(embed=embed)

# Main Commands

@bot.command()
async def motivation(ctx):
  response= ['Life is here to be hugging your friends all round.', 'You only got one life. Enjoy as you can!', 'Life has got all those twists and turns. You have got to hold on tight and off you go.', 'Keep your face always toward the sunshine, and shadows will fall behind you.', 'Be courageous. Challenge orthodoxy. Stand up for what you believe in. When you are in your rocking chair talking to your grandchildren many years from now, be sure you have a good story to tell.', 'Success is not final, failure is not fatal: it is the courage to continue that counts.', 'You define your own life. Dont let other people write your script.', 'You are never too old to set another goal or to dream a new dream.', 'At the end of the day, whether or not those people are comfortable with how you are living your life doesnt matter. What matters is whether you are comfortable with it.', 'Spread love everywhere you go.', 'Do not allow people to dim your shine because they are blinded. Tell them to put some sunglasses on.', 'You can be everything. You can be the infinite amount of things that people are.', 'I want to be in the arena. I want to be brave with my life. And when we make the choice to dare greatly, we sign up to get our asses kicked. We can choose courage or we can choose comfort, but we cant have both. Not at the same time.', 'Im going to be gone one day, and I have to accept that tomorrow isnt promised. Am I OK with how I’m living today? Its the only thing I can help. If I didnt have another one, what have I done with all my todays? Am I doing a good job?', 'elief creates the actual fact.', 'I am experienced enough to do this. I am knowledgeable enough to do this. I am prepared enough to do this. I am mature enough to do this. I am brave enough to do this.', 'Im not going to continue knocking that old door that doesnt open for me. Im going to create my own door and walk through that.', 'Just dont give up trying to do what you really want to do. Where there is love and inspiration, I dont think you can go wrong.']
  await ctx.reply(f"{random.choice(response)}")

@bot.command()
async def Motivation(ctx):
  response= ['Life is here to be hugging your friends all round.', 'You only got one life. Enjoy as you can!', 'Life has got all those twists and turns. You have got to hold on tight and off you go.', 'Keep your face always toward the sunshine, and shadows will fall behind you.', 'Be courageous. Challenge orthodoxy. Stand up for what you believe in. When you are in your rocking chair talking to your grandchildren many years from now, be sure you have a good story to tell.', 'Success is not final, failure is not fatal: it is the courage to continue that counts.', 'You define your own life. Dont let other people write your script.', 'You are never too old to set another goal or to dream a new dream.', 'At the end of the day, whether or not those people are comfortable with how you are living your life doesnt matter. What matters is whether you are comfortable with it.', 'Spread love everywhere you go.', 'Do not allow people to dim your shine because they are blinded. Tell them to put some sunglasses on.', 'You can be everything. You can be the infinite amount of things that people are.', 'I want to be in the arena. I want to be brave with my life. And when we make the choice to dare greatly, we sign up to get our asses kicked. We can choose courage or we can choose comfort, but we cant have both. Not at the same time.', 'Im going to be gone one day, and I have to accept that tomorrow isnt promised. Am I OK with how I’m living today? Its the only thing I can help. If I didnt have another one, what have I done with all my todays? Am I doing a good job?', 'elief creates the actual fact.', 'I am experienced enough to do this. I am knowledgeable enough to do this. I am prepared enough to do this. I am mature enough to do this. I am brave enough to do this.', 'Im not going to continue knocking that old door that doesnt open for me. Im going to create my own door and walk through that.', 'Just dont give up trying to do what you really want to do. Where there is love and inspiration, I dont think you can go wrong.']
  await ctx.reply(f"{random.choice(response)}")

@bot.command()
async def Food(ctx):
  chosen_image = random.choice(embedlinks.food)

  embed = discord.Embed(color = 16705372)
  embed.set_image(url=chosen_image)
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

  await ctx.send(embed=embed)

@bot.command()
async def Bread(ctx):

  embed = discord.Embed(color = 16705372)
  embed.add_field(name="Bread", value="👍")
  embed.set_image(url="https://cdn.discordapp.com/attachments/995028958234038342/995703664742244352/0cee3adc861b7b397c19f70abe5e0f8d.png")
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

  await ctx.send(embed=embed)  

@bot.command()
async def bread(ctx):

  embed = discord.Embed(color = 16705372)
  embed.add_field(name="Bread", value="👍")
  embed.set_image(url="https://cdn.discordapp.com/attachments/995028958234038342/995703664742244352/0cee3adc861b7b397c19f70abe5e0f8d.png")
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

  await ctx.send(embed=embed)  

@bot.command()
async def food(ctx):
  chosen_image = random.choice(embedlinks.food)

  embed = discord.Embed(color = 16705372)
  embed.set_image(url=chosen_image)
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

  await ctx.send(embed=embed)

@bot.command()
async def memes(ctx):
  chosen_image = random.choice(embedlinks.memes)

  embed = discord.Embed(color = 16705372)
  embed.set_image(url=chosen_image)
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

  await ctx.send(embed=embed)

@bot.command()
async def Memes(ctx):
  chosen_image = random.choice(embedlinks.memes)

  embed = discord.Embed(color = 16705372)
  embed.set_image(url=chosen_image)
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

  await ctx.send(embed=embed)


# Poems commands

@bot.command()
async def Poems(ctx):
  chosen_image = random.choice(embedlinks.poems)

  embed = discord.Embed(color = 16705372)
  embed.set_image(url=chosen_image)
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

  await ctx.send(embed=embed)

@bot.command()
async def Poem(ctx):
  chosen_image = random.choice(embedlinks.poems)

  embed = discord.Embed(color = 16705372)
  embed.set_image(url=chosen_image)
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
  await ctx.send(embed=embed)

@bot.command()
async def poem(ctx):
  chosen_image = random.choice(embedlinks.poems)

  embed = discord.Embed(color = 16705372)
  embed.set_image(url=chosen_image)
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

  await ctx.send(embed=embed)

@bot.command()
async def poems(ctx):
  chosen_image = random.choice(embedlinks.poems)

  embed = discord.Embed(color = 16705372)
  embed.set_image(url=chosen_image)
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

  await ctx.send(embed=embed)

# slash commands

# @Tree.command(guild = discord.Object(id=995023718751408219), name = 'tester', description='testing') #guild specific slash command
# async def slash2(interaction: discord.Interaction):
#     await interaction.response.send_message(f"I am working! I was made with Discord.py!", ephemeral = True)




# @bot.command()
# async def poem_monika(ctx):
#   chosen_image = random.choice(embedlinks.monikapoems)


#   embed = discord.Embed(color = 16705372)
#   embed.set_image(url=chosen_image)
#   embed.set_footer(text="Made by Im.Lewis#2294")

#   await ctx.send(embed=embed)



# @bot.command()
# async def poem_sayori(ctx):
#   chosen_image = random.choice(embedlinks.sayoripoems)


#   embed = discord.Embed(color = 16705372)
#   embed.set_image(url=chosen_image)
#   embed.set_footer(text="Made by Im.Lewis#2294")

#   await ctx.send(embed=embed)

# @bot.command()
# async def poem_natsuki(ctx):
#   chosen_image = random.choice(embedlinks.natsukipoems)


#   embed = discord.Embed(color = 16705372)
#   embed.set_image(url=chosen_image)
#   embed.set_footer(text="Made by Im.Lewis#2294")

#   await ctx.send(embed=embed)


# @bot.command()
# async def poem_yuri(ctx):
#   chosen_image = random.choice(embedlinks.yuripoems)

#   embed = discord.Embed(color = 16705372)
#   embed.set_image(url=chosen_image)
#   embed.set_footer(text="Made by Im.Lewis#2294")

#   await ctx.send(embed=embed)

bot.run('TOKEN')
