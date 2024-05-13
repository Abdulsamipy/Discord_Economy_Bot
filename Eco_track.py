import discord
from discord.ext import commands
import DiscordUtils
import json
import string
import pandas as pd
intents = discord.Intents.default()
intents.members = True
bot = commands.AutoShardedBot(command_prefix="!", intents=intents)
tracker = DiscordUtils.InviteTracker(bot)

def user_exist_in_file(user):
    with open('Data.json', "r+") as json_data:
        data = json.load(json_data)
    
    for d in data['Users']:
        if d['Name'].lower() == user.lower():
            return True
    return False

com = ['!Done', "!work", "!fun"]

@bot.event
async def on_message(message):
    channel = ["general"]
    if str(message.channel) in channel:
        if message.content in com:
            name = message.author.name  
            with open('Data.json', "r+") as json_data:
                data = json.load(json_data)
                data_user= data["Users"]

            check_user = user_exist_in_file(name)
            if check_user == False:
                data_user.append({
            "Name": name, 
            "Coins" : "1" 
            })
            
                with open('Data.json', "w+") as json_data_update:
                    json.dump(data, json_data_update, indent=4)
                print(str(message.author.name) + " is Awarded with a coin")
            else:
                with open("Data.json", 'r+', encoding='utf') as f:
                    json_data = json.load(f)

                #Look for the user in list
                for j in json_data['Users']:
                    if message.author.name.lower() == (j['Name'].lower()):
                        num = int(j['Coins']) + 1
                        j['Coins']=j['Coins'].replace(str(j['Coins']), str(num))
                    
                        with open("Data.json", 'w', encoding='utf') as f:
                            json.dump(json_data, f, indent=2)
                        print(str(message.author.name) + " is Awarded with a coin")
                        break

        if message.content ==  "/list":
            with open('Data.json', "r+") as json_data:
                data = json.load(json_data)


            sub_li = []
            for d in data['Users']:
                appe = [d['Name'], d['Coins']]
                sub_li.append(appe)

            #sub_li.sort(key = lambda x: x[-1])
            sub_lis = sorted(sub_li, key=lambda x: x)
            

            sub_li = []
            for d in data['Users']:
                appe = [d['Name'], d['Coins']]
                sub_li.append(appe)

            #sub_li.sort(key = lambda x: x[-1])
            
            sub_lis = sorted(sub_li, key=lambda x: x[-1], reverse=True)


            inv_name = []
            inv_amount = []

            for s in sub_lis:
                inv_amount.append(s[1])
                inv_name.append(s[0])

            df = pd.DataFrame(inv_name)
            df_invites = pd.DataFrame(inv_amount)

            embed = discord.Embed(title="User Ranks", description="Rank of Users With Most to Least Coins " +"\n", colour = discord.Colour.red()) #,color=Hex code
            embed.add_field(name="Names" + "\n", value=df.to_string(header=None, index=False), inline=True)
            embed.add_field(name="Coins" + "\n", value="\n" +"**"+ df_invites.to_string(header=None, index=False)+ "**", inline=True)
            embed.set_author(name = "Economy Bot")
            await message.channel.send(embed=embed)

bot.run("")