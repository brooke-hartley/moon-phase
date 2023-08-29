import discord
import requests

def run_discord_bot():
    TOKEN = 'MTEzNDE1MzEwODM1Njg1NzkxNg.G6LUbf.mb2adhHn_w53UCGVU9133Y4zfNbPw6HoRUpzXo'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    all_url = "https://moon-phase.p.rapidapi.com/advanced"

    # API keys
    headers = {
	    "X-RapidAPI-Key": "217c706ddcmshde2e2c82feb0878p17922ejsn35ab177e0b18",
	    "X-RapidAPI-Host": "moon-phase.p.rapidapi.com"
    }

    all = requests.get(all_url, headers=headers)
    all_data = all.json()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        # If the users uses '!help' command
        if message.content == '!help':
            channel = message.channel
            emoji = all_data['moon']['emoji']
            embed = discord.Embed(
                title=emoji + "  Moon Phase Bot Commands  " + emoji,
                description="List of commands",
            )

            fields_list = [
                ("!moonphase", "The current moon phase"),
                ("!newmoon", "Checks the status of a New Moon"),
                ("!fullmoon", "Checks the status of a Full Moon"),
            ]

            # Add fields from the list
            for name, value in fields_list:
                embed.add_field(name=name, value=value, inline=False)
            
            # Sends the embed message
            await channel.send(embed=embed)

        # If the users uses '!moonphase' command
        elif message.content == '!moonphase':
            phase = all_data['moon']['phase_name']
            emoji = all_data['moon']['emoji']
            embed = discord.Embed(title=emoji + "  Moon Phase  " + emoji,description="Today's Moon Phase: "+f"**{phase}**",color=None)
            await message.channel.send(embed=embed)

         # If the users uses '!newmoon' command
        elif message.content == '!newmoon':
            current = all_data['moon_phases']['new_moon']['current']
            next = all_data['moon_phases']['new_moon']['next']
            emoji = all_data['moon']['emoji']
            zodiac = all_data['moon']['zodiac_sign']
            new_moon_emoji = "\U0001F311"

            # Removes the timestamp at the end of the date
            formatted_datestamp1 = current['datestamp'][:-15]
            formatted_datestamp2 = next['datestamp'][:-15]

            fields_list = [
                ("Last New Moon", "The last New Moon was " + str(current['days_ago']) + f' days ago on {formatted_datestamp1}'),
                ("Next New Moon", "The next New Moon is going to be in " + str(next['days_ahead']) + f' days on {formatted_datestamp2}'),
            ]
            
            if current['days_ago'] == 0:
                embed = discord.Embed(
                    title=f"{new_moon_emoji}  New Moon  {new_moon_emoji}",
                    description=f'There is a New Moon today in {zodiac}!',
                    color=None)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=f"{new_moon_emoji}  New Moon  {new_moon_emoji}",
                    description=f"Today is **NOT** a New Moon",
                    color=None)
                # Add fields from the list
                for name, value in fields_list:
                    embed.add_field(name=name, value=value, inline=False)
                await message.channel.send(embed=embed)

        # If the users uses '!fullmoon' command
        elif message.content == '!fullmoon':
            current = all_data['moon_phases']['full_moon']['current']
            next = all_data['moon_phases']['full_moon']['next']
            emoji = all_data['moon']['emoji']
            zodiac = all_data['moon']['zodiac_sign']
            full_moon_emoji = "\U0001F315"

            # Removes the timestamp at the end of the date
            formatted_datestamp1 = current['datestamp'][:-15]
            formatted_datestamp2 = next['datestamp'][:-15]

            fields_list = [
                ("Last Full Moon", "The last Full Moon was " + str(current['days_ago']) + f' days ago on {formatted_datestamp1}'),
                ("Next Full Moon", "The next Full Moon is going to be in " + str(next['days_ahead']) + f' days on {formatted_datestamp2}'),
            ]
            
            if current['days_ago'] == 0:
                embed = discord.Embed(
                    title=f"{full_moon_emoji}  Full Moon  {full_moon_emoji}",
                    description=f'There is a Full Moon today in {zodiac}!',
                    color=None)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=f"{full_moon_emoji}  Full Moon  {full_moon_emoji}",
                    description=f"Today is **NOT** a Full Moon",
                    color=None)
                # Add fields from the list
                for name, value in fields_list:
                    embed.add_field(name=name, value=value, inline=False)
                await message.channel.send(embed=embed)

    client.run(TOKEN)
