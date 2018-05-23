from main import client
import discord


@client.command()
async def git():
    embed = discord.Embed(
        title='GitHub Tibagel',
        description='Bad code and shit',
        colour=discord.Colour.magenta()
    )
    embed.set_footer(text='penchez vous tous')
    embed.set_image(url='https://i.imgur.com/hBYEPoB.png')
    embed.set_author(name='Le Dindon', icon_url='https://i.imgur.com/jGZ3fX1.png')
    embed.add_field(name='Le hub du petit matin', value='https://github.com/tibagel/DiscordBot', inline=True)
    await client.say(embed=embed)
