import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord import Option, slash_command
import requests
import json
import random
import asyncio
from discord.ui import View
from discord import guild_only

with open('URL.json', mode='r', encoding='utf8') as jfile:
    url = json.load(jfile)

json6 = requests.get(url['odate'])
odate = json6.json()

class CogName(commands.Cog):
    def init(self, bot:commands.Bot):
        self.bot = bot

    @slash_command(description = "🟩每日一抽，運勢在手")
    @guild_only()
    async def ouo運勢(self, ctx):

        await ctx.response.defer()

        if (str(ctx.author.id)) not in (odate['people']):
            random_pic = random.choice(odate['pic'])
            await ctx.followup.send(f'emmm...本ouo幫你抽好了~!喵~~~')
            await ctx.send(f'{random_pic}')
            await asyncio.sleep(1)
            odate['people'].append(str(ctx.author.id))
            requests.put(url['odate'], json=odate)
        else:
            await ctx.followup.send(f'emmm...本ouo發現你今天已經抽過喵!明天再來吧!`(GMT+8)00:00後`')

    @commands.command()
    @guild_only()
    async def set(self, ctx):
        if (str(ctx.author.id)) in ['833717980633628732', '761967543698980866', '763012970686316544', '606991251098566684']:
            odate['people'] = ["1"]
            requests.put(url['odate'], json=odate)
            await ctx.channel.send(f'好了~')

    @slash_command(description = "🟩多多認識我吧!")
    @guild_only()
    async def 陽光(self, ctx):

        await ctx.response.defer()
        
        embed=discord.Embed(title="陽光自製機器人", url="https://discord.com/api/oauth2/authorize?client_id=977899499324317698&permissions=8&scope=bot%20applications.commands", description="任何youtube、twitch主播開台時，會自動發布通知", color=0xffff00)
        embed.set_author(name="陽光", icon_url="https://cdn.discordapp.com/attachments/978285960414502982/1076551250700669019/-.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1077934515793698816/21.png")
        embed.add_field(name="☀️請我喝杯奶茶增加動力吧", value="[綠界](https://p.ecpay.com.tw/1733398)", inline=False)
        embed.add_field(name="☀️訂閱一下啦", value="[Youtube](https://www.youtube.com/channel/UC5YWYeE-ZQpCUma4WWH6jQg)", inline=False)
        embed.add_field(name="☀️追隨一下嘛", value="[Twitch](https://www.twitch.tv/sunlight_nikko_ouo)", inline=False)
        embed.add_field(name="☀️進來一下齁", value="[社團-Cozy Box_discord](https://discord.gg/MwQvTREWKm)", inline=False)
        embed.add_field(name="☀️過來一下喔", value="[個人_discord](https://discord.gg/2g4Te4XXpv)", inline=False)
        embed.add_field(name="姓名:", value="陽光-Nikko Sun_Ch.", inline=True)
        embed.add_field(name="暱稱:", value="陽光", inline=True)
        embed.add_field(name="性別:", value="男", inline=True)
        embed.add_field(name="星座:", value="金牛", inline=True)
        embed.add_field(name="年齡:", value="18歲(太陽年)", inline=True)
        embed.add_field(name="生日:", value="4/22", inline=True)
        embed.add_field(name="身高:", value="181.4cm", inline=True)
        embed.add_field(name="體重:", value="56kg", inline=True)
        embed.add_field(name="喜歡:", value="奶茶&閃粉", inline=True)
        embed.add_field(name="討厭:", value="所有昆蟲", inline=True)
        embed.add_field(name="興趣:", value="追動漫、寫程式", inline=True)
        embed.add_field(name="語言:", value="太陽語>貓語>中文>日文>英文", inline=True)
        embed.set_footer(text="🌞背景： 自從8歲離開太陽後，就的銀河各處去旅行了。在經過地球時，剛好看見了貓貓，ouo就對他一見鐘情了ww所以吵著要來地球。為了找尋那隻貓貓而成為了VTUBER~\n🌞近況： 因為被地球上有個叫動漫的東西給深深吸引住了，所以天天都不出門，在家追漫，所以服裝走的都是居家風~ 一邊追動漫，一邊喝奶茶，真是光生一大享受吖！！")
        await ctx.followup.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))