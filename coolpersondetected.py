import discord

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_message(message):
  if message.author.id == 917860693934506054:
    # Create an embed message
    embed = discord.Embed(title='Hot person detected', color=0xFF0000)
    # Set the thumbnail of the embed message to the person's profile picture
    # Add a spicy footer to the embed message
    embed.set_footer(text='This message is spicy! 🔥')
    # Send the embed message
    await message.channel.send(embed=embed)
  elif message.author.id == 873298756529971201:
    # Create an embed message
    embed = discord.Embed(title='Cool person detected', color=0x00FF00)
    # Set the thumbnail of the embed message to the person's profile picture
    # Add a spicy footer to the embed message
    embed.set_footer(text='This message is spicy! 🔥')
    # Send the embed message
    await message.channel.send(embed=embed)


client.run('YOUR_BOT_TOKEN')
