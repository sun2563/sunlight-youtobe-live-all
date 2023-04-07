# -*- coding: UTF-8 -*-
import json
import time
import discord
from discord.ext import commands, tasks
import os,aiohttp
import asyncio
import requests
import re
from datetime import datetime
from discord import Option, slash_command
from discord.ui import View, Button, Modal, InputText
from discord import guild_only

intents = discord.Intents.all()

with open('URL.json', mode='r', encoding='utf8') as jfile:
    url = json.load(jfile)

json1 = requests.get(url['jdate'])
jdate = json1.json()
json3 = requests.get(url['tdate'])
tdate = json3.json()
json8 = requests.get(url['cdata'])
cdata = json8.json()
json9 = requests.get(url['bdata'])
bdata = json9.json()

#YT
json7 = requests.get(url['ndata'])
ndata = json7.json()
json2 = requests.get(url['data'])
data = json2.json()
json5 = requests.get(url['udate'])
udate = json5.json()
#YT

#TW
json4 = requests.get(url['wdata'])
wdata = json4.json()
#TW

bot = commands.Bot(command_prefix='$', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")
    activity = discord.Activity(type=discord.ActivityType.streaming, name="陽光", url = "https://www.twitch.tv/sunlight_nikko_ouo")
    await bot.change_presence(status=discord.Status.idle, activity=activity)

    channel = bot.get_channel(1039919671455006790)
    await channel.send(f'阿(。￣O￣)彌(。￣=￣)陀(。￣□￣)佛(。￣△￣)')
    await asyncio.sleep(5)
    if not checkforvideos.is_running():
        checkforvideos.start()
    jdate['ct1']="0"
    await asyncio.sleep(5)
    if not check_twitch_online_streamers.is_running():
        check_twitch_online_streamers.start()

#---------------------------------------------------------------------------------------------------

class ytid(View):
    def __init__(self):
        super().__init__(timeout=None)

        supportServerButton = Button(label='點我前往頁面!', style=discord.ButtonStyle.gray, url='https://commentpicker.com/youtube-channel-id.php')
        self.add_item(supportServerButton)

class update(Modal, View):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(InputText(label="標題"))
        self.add_item(InputText(label="內文", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="公告", color=0xc4302b)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1076550985146703932/a1e90c0977bcca94.png")
        embed.add_field(name=self.children[0].value, value=self.children[1].value, inline=False)
        await interaction.response.send_message(embeds=[embed], view=bupdate())
        jdate['update1']=(str(self.children[0].value))
        jdate['update2']=(str(self.children[1].value))
        
class bupdate(View):
    @discord.ui.button(label="確定發送", style=discord.ButtonStyle.green)
    async def button_callback(self, button, interaction):
        embed = discord.Embed(title="公告", color=0xffff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1076550985146703932/a1e90c0977bcca94.png")
        embed.add_field(name=jdate['update1'], value=jdate['update2'], inline=False)
        button.disabled = True
        await abupdate()
        await interaction.response.edit_message(content=f'公告已發送', embed=embed, view=no())


    @discord.ui.button(label="取消發送", style=discord.ButtonStyle.red)
    async def button_callback2(self, button, interaction):
        embed = discord.Embed(title="公告", color=0xc4302b)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1076550985146703932/a1e90c0977bcca94.png")
        embed.add_field(name=jdate['update1'], value=jdate['update2'], inline=False)
        button.disabled = True
        await interaction.response.edit_message(content=f'已取消發送', embed=embed, view=no())

async def abupdate():
    for c in cdata:
        if cdata[str(c)]['OX'] == 'T':
            embed = discord.Embed(title="公告", color=0xffff00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1076550985146703932/a1e90c0977bcca94.png")
            embed.add_field(name=jdate['update1'], value=jdate['update2'], inline=False)

            updatec_id=cdata[str(c)]['channel_id']
            updatec=bot.get_channel(int(updatec_id))
            await updatec.send(embed=embed)
        
        else:
            pass

class no(View):
    pass

class bug(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(InputText(label="標題", placeholder="ex.提問/建議/bug"))
        self.add_item(InputText(label="怎麼稱呼您?"))
        self.add_item(InputText(label="內文", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title=self.children[0].value, description="from."+self.children[1].value, color=0xc4302b)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1077577427561218109/1676984811869.png")
        embed.add_field(name=self.children[2].value, value="", inline=False)
        embed.set_footer(text="⚠️您的寶貴意見我收到了~稍後將給您回覆!\n等待期間請勿刪除此頻道或踢除此機器人，避免收不到回覆之事件發生!感謝配合!")
        await interaction.response.send_message(embeds=[embed])

        embed2 = discord.Embed(title=self.children[0].value, color=0xc4302b)
        embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1077577427561218109/1676984811869.png")
        embed2.add_field(name=self.children[1].value, value=interaction.channel.id, inline=False)
        embed2.add_field(name=self.children[2].value, value="", inline=False)
        channel = bot.get_channel(1077561962851991602)
        await channel.send(embeds=[embed2])

class reply(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(InputText(label="標題"))
        self.add_item(InputText(label="頻道id"))
        self.add_item(InputText(label="內文", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title=self.children[0].value, description=f"from.陽光_({self.children[1].value})", color=0xffff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1077933953345929330/1677069865321.png")
        embed.add_field(name=self.children[2].value, value="", inline=False)
        await interaction.response.send_message(embeds=[embed])

        embed2 = discord.Embed(title=self.children[0].value, description="from.陽光", color=0xffff00)
        embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1077933953345929330/1677069865321.png")
        embed2.add_field(name=self.children[2].value, value="", inline=False)
        embed2.set_footer(text="🌞如果還有其他問題，都可以來問我!\n祝您使用愉快!")
        channel = bot.get_channel(int(self.children[1].value))
        try:
            await channel.send(embeds=[embed2])
            await interaction.channel.send("發送成功!")
        except:
            await interaction.channel.send("發送失敗!")

class abug(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(InputText(label="標題"))
        self.add_item(InputText(label="內文", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.defer()

        n=(jdate['nbug'])
        n=(int(n))
        n=n+1
        jdate['nbug']=(str(n))
        requests.put(url['jdate'], json=jdate)

        bdata[str(n)]={}
        bdata[str(n)]["title"]=self.children[0].value
        bdata[str(n)]["content"]=self.children[1].value
        bdata[str(n)]["TF"]="T"
        requests.put(url['bdata'], json=bdata)

        embed=discord.Embed(title="bug", color=0x1E90FF)
        embed.set_author(name="陽光", icon_url="https://cdn.discordapp.com/attachments/978285960414502982/1076551250700669019/-.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1077577427561218109/1676984811869.png")
        bbug = 1
        for b in bdata:
            if str(bdata[b]["TF"]) == "T":
                tbug = str(bdata[b]["title"])
                cbug = str(bdata[b]["content"])
                embed.add_field(name=f"{b}.{tbug}", value=f"*{cbug}*", inline=False)
                bbug = 0
            else:
                pass

        if bbug == 1:
            embed.add_field(name="目前沒有bug", value="", inline=False)
        else:
            pass

        await interaction.followup.send(embed=embed)

class Sabout(View):
    async def on_timeout(self):
        for child in self.children:
            child.disabled = True

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
        await self.message.edit(content="下拉選單已失效，如還需要使用，則再次輸入此指令即可。", embed=embed, view=self)

    @discord.ui.select(
        placeholder="選擇類別",
        options=[
            discord.SelectOption(
                label="首頁",
                emoji="🌞",
            ),
            discord.SelectOption(
                label="Youtube",
                emoji="🟥",
                description="關於youtube的所有指令"
            ),
            discord.SelectOption(
                label="Twitch",
                emoji="🟪",
                description="關於twitch的所有指令"
            ),
            discord.SelectOption(
                label="功能",
                emoji="🟨",
                description="關於功能類的所有指令"
            ),
            discord.SelectOption(
                label="娛樂",
                emoji="🟩",
                description="關於娛樂類的所有指令"
            ),
            discord.SelectOption(
                label="待修bug",
                emoji="🟦",
                description="關於目前已知的bug"
            )
        ]
    )
    async def select_callback(self, selsct, interaction):
        if selsct.values[0] == "首頁":
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
            await interaction.response.edit_message(embed=embed)

        elif selsct.values[0] == "Youtube":
            embed=discord.Embed(title="Youtube", color=0xc4302b)
            embed.set_author(name="陽光", icon_url="https://cdn.discordapp.com/attachments/978285960414502982/1076551250700669019/-.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1077929814394150932/Youtube_logo.png")
            embed.add_field(name="▶️斜線指令：", value="", inline=False)
            embed.add_field(name="/youtube_inform_add\n🟥添加youtube通知", value="*1.在哪個頻道輸入此指令，就是在該頻道發送開台通知。\n2.有時會需要等待3分鐘後再輸入，因為需要先等yt開台檢查都跑完後才能添加新頻道。*", inline=False)
            embed.add_field(name="/youtube_inform_delete\n🟥刪除youtube通知", value="*開台通知在哪個頻道，就在該頻道輸入此指令來刪除開台通知。*", inline=False)
            embed.add_field(name="/youtube_change_name\n🟥更改youtube主播的名字", value="*開台通知在哪個頻道，就在該頻道輸入此指令來更改主播名字。*", inline=False)
            embed.add_field(name="/youtube_change_at\n🟥更改youtube通知的艾特", value="*1.開台通知在哪個頻道，就在該頻道輸入此指令來更改艾特。\n2.如果想換回@ everyone，艾特id輸入*「everyone」*即可，如不想被艾特了，艾特id輸入*「123」*即可。*", inline=False)
            embed.add_field(name="/youtube_id_search\n🟥查詢youtube的頻道ID", value="*不限輸入頻道。*", inline=False)
            embed.add_field(name="🔢參數說明：", value="", inline=False)
            embed.add_field(name="yt頻道id", value="*需要輸入指令*「/youtube_id_search」*獲取。*", inline=False)
            embed.add_field(name="yt編號", value="*當添加新的頻道時，機器人會自動給編號。輸入*「/all_inform」*也可以查詢。*", inline=False)
            embed.add_field(name="主播名字", value="*想填甚麼，就填甚麼。*", inline=False)
            embed.add_field(name="艾特id", value="*需要輸入指令*「/at_id」*獲取。*", inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/978285960414502982/1077969609149386762/722_20230222230606.png")
            embed.set_footer(text="⚠️特別注意，「艾特」和「艾特id」是不同的東西，艾特id為艾特的id\n例如要「@陽光」，需查詢@陽光的艾特id後，才可輸入。")
            await interaction.response.edit_message(embed=embed)

        elif selsct.values[0] == "Twitch":
            embed=discord.Embed(title="Twitch", color=0x6441a5)
            embed.set_author(name="陽光", icon_url="https://cdn.discordapp.com/attachments/978285960414502982/1076551250700669019/-.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1077930866455613532/721_20230222203059.png")
            embed.add_field(name="▶️斜線指令：", value="", inline=False)
            embed.add_field(name="/twitch_inform_add\n🟪添加twitch通知", value="*在哪個頻道輸入此指令，就是在該頻道發送開台通知。*", inline=False)
            embed.add_field(name="/twitch_inform_delete\n🟪刪除twitch通知", value="*開台通知在哪個頻道，就在該頻道輸入此指令來刪除開台通知。*", inline=False)
            embed.add_field(name="/twitch_change_name\n🟪更改twitch主播的名字", value="*開台通知在哪個頻道，就在該頻道輸入此指令來更改主播名字。*", inline=False)
            embed.add_field(name="/twitch_change_at\n🟪更改twitch通知的艾特", value="*1.開台通知在哪個頻道，就在該頻道輸入此指令來更改艾特。\n2.如果想換回@ everyone，艾特id輸入*「everyone」*即可，如不想被艾特了，艾特id輸入*「123」*即可。*", inline=False)
            embed.add_field(name="/twitch_id_search\n🟪查詢twitch的頻道ID", value="*不限輸入頻道。*", inline=False)
            embed.add_field(name="🔢參數說明：", value="", inline=False)
            embed.add_field(name="tw頻道id", value="*需要輸入指令*「/twitch_id_search」*獲取。*", inline=False)
            embed.add_field(name="tw編號", value="*當添加新的頻道時，機器人會自動給編號。輸入*「/all_inform」*也可以查詢。*", inline=False)
            embed.add_field(name="主播名字", value="*想填甚麼，就填甚麼。*", inline=False)
            embed.add_field(name="艾特id", value="*需要輸入指令*「/at_id」*獲取。*", inline=False)
            embed.set_image(url="https://cdn.discordapp.com/attachments/978285960414502982/1077969609149386762/722_20230222230606.png")
            embed.set_footer(text="⚠️特別注意，「艾特」和「艾特id」是不同的東西，艾特id為艾特的id\n例如要「@陽光」，需查詢@陽光的艾特id後，才可輸入。")
            await interaction.response.edit_message(embed=embed)

        elif selsct.values[0] == "功能":
            embed=discord.Embed(title="功能", color=0xFFD700)
            embed.set_author(name="陽光", icon_url="https://cdn.discordapp.com/attachments/978285960414502982/1076551250700669019/-.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1077931248963555348/653_20230222203346.png")
            embed.add_field(name="/at_id\n🟨查詢艾特的ID", value="*不限輸入頻道。*", inline=False)
            embed.add_field(name="/all_inform\n🟨查看此頻道裡的所有通知", value="*在哪個頻道輸入此指令，就是查看該頻道裡的所有通知。*", inline=False)
            embed.add_field(name="/talk\n🟨傳送提問/建議/bug回報", value="*1.不限輸入頻道。\n2.如需要傳送圖片或影片，直接貼網址連結就可以了。\n3.用此指令回報的回覆速度會比表單快。\n4.特別注意當此機器人發生意外下線後，此指令會無法使用，而我會盡快處理讓機器人上線。*", inline=False)
            embed.add_field(name="/question_channel_add\n🟨添加獲取更新資訊的頻道", value="*在哪個頻道輸入此指令，就是在該頻道發送更新資訊。*", inline=False)
            embed.add_field(name="/question_channel_delete\n🟨刪除獲取更新資訊的頻道", value="*更新資訊在哪個頻道，就在該頻道輸入此指令來刪除更新資訊。*", inline=False)
            embed.add_field(name="/about\n🟨關於此機器人的所有指令", value="*1.不限輸入頻道。\n2.輸入此指令後一個小時，下拉選單就會失效，如還需要使用，則再次輸入此指令即可。*", inline=False)
            await interaction.response.edit_message(embed=embed)

        elif selsct.values[0] == "娛樂":
            embed=discord.Embed(title="娛樂", color=0x32CD32)
            embed.set_author(name="陽光", icon_url="https://cdn.discordapp.com/attachments/978285960414502982/1076551250700669019/-.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1078692341688315995/10.png")
            embed.add_field(name="/ouo運勢\n🟩每日一抽，運勢在手", value="*1.不限輸入頻道。\n2.此籤為日本淺草觀音寺一百籤，求籤時，可以在心裡默念想詢問的方向(像是工作、戀愛、生病等等...)，求到籤後再去找自己對應的類別才是最準的唷。*", inline=False)
            embed.add_field(name="/陽光\n🟩多多認識我吧!", value="*不限輸入頻道。*", inline=False)
            await interaction.response.edit_message(embed=embed)

        elif selsct.values[0] == "待修bug":
            embed=discord.Embed(title="bug", color=0x1E90FF)
            embed.set_author(name="陽光", icon_url="https://cdn.discordapp.com/attachments/978285960414502982/1076551250700669019/-.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1077577427561218109/1676984811869.png")
            bbug = 1
            for b in bdata:
                if str(bdata[b]["TF"]) == "T":
                    tbug = str(bdata[b]["title"])
                    cbug = str(bdata[b]["content"])
                    embed.add_field(name=f"{tbug}", value=f"*{cbug}*", inline=False)
                    bbug = 0
                else:
                    pass

            if bbug == 1:
                embed.add_field(name="目前沒有bug", value="", inline=False)
            else:
                pass

            await interaction.response.edit_message(embed=embed)

        else:
            await interaction.response.edit_message('錯誤')

#---------------------------------------------------------------------------------------------------

@tasks.loop(seconds=600)
async def checkforvideos():
    async with aiohttp.ClientSession() as session:
        start = datetime.now()

        jdate['ya']="0"

        print("Now Checking!")
        #channelprint = bot.get_channel(1041725091228164216)

        for n in ndata:
            x = 0
            y = 0
            z = 0

            channel_id = str(ndata[n]["channel_id"])
            channel = f"https://www.youtube.com/channel/{channel_id}"

            #embed = discord.Embed(title={n}, description='🎬📺📸', color=discord.Color.red())

            try:
                async with session.get(channel+"/videos") as html:#8s
                    html = await html.text()#11s
                    latest_video_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()

                    #embed.add_field(
                    #name=f"🎬{latest_video_url}",
                    #value=f"[youtube]({latest_video_url})",
                    #inline=False
                    #)

                if latest_video_url not in str(udate[n]):
                    x = 1
                else:
                    pass
            except:
                pass
            try:
                await asyncio.sleep(0.1)
                async with session.get(channel+"/streams") as html1:#8s
                    html1 = await html1.text()#11s
                    latest_stream_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html1).group()

                    #embed.add_field(
                    #name=f"📺{latest_stream_url}",
                    #value=f"[youtube]({latest_stream_url})",
                    #inline=False
                    #)

                if latest_stream_url not in str(udate[n]):
                    y = 1
                else:
                    pass
            except:
                pass
            try:
                await asyncio.sleep(0.1)
                async with session.get(channel+"/shorts") as html2:#8s
                    html2 = await html2.text()#11s
                    latest_short_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html2).group()

                    #embed.add_field(
                    #name=f"📸{latest_short_url}",
                    #value=f"[youtube]({latest_short_url})",
                    #inline=False
                    #)

                if latest_short_url not in str(udate[n]):
                    z = 1
                else:
                    pass
            except:
                pass

            #await channelprint.send(embed=embed)

            if x != 1 and y != 1 and z != 1:#000
                print(f"{n}Now Checking!")

            elif x == 1 and y != 1 and z != 1:#100
                score = ndata[n]['id']
                for d in score:
                    if data[str(d)]['notifying_discord_channel'] != 'nop':
                        discord_channel_id = data[str(d)]['notifying_discord_channel']
                        discord_channel = bot.get_channel(int(discord_channel_id))
                        if (str(d)) in ['1','2','3','4','5','6']:
                            msg1 = f"{latest_video_url}"
                            try:
                                await discord_channel.send(msg1)
                            except:
                                pass
                        else:
                            try:
                                try:
                                    msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                    await discord_channel.send(msg)
                                except:
                                    msg = f"@everyone {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                    await discord_channel.send(msg)
                            except:
                                pass
                    else:
                        pass
                udate[str(n)].append(latest_video_url)
                print(f"{n}Now Checking!✅")

            elif x != 1 and y == 1 and z != 1:#010
                score = ndata[n]['id']
                for d in score:
                    if data[str(d)]['notifying_discord_channel'] != 'nop':
                        discord_channel_id = data[str(d)]['notifying_discord_channel']
                        discord_channel = bot.get_channel(int(discord_channel_id))
                        if (str(d)) in ['1','2','3','4','5','6']:
                            msg1 = f"{latest_stream_url}"
                            try:
                                await discord_channel.send(msg1)
                            except:
                                pass
                        else:
                            try:
                                try:
                                    msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                    await discord_channel.send(msg)
                                except:
                                    msg = f"@everyone {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                    await discord_channel.send(msg)
                            except:
                                pass
                    else:
                        pass
                udate[str(n)].append(latest_stream_url)
                print(f"{n}Now Checking!✅")

            elif x != 1 and y != 1 and z == 1:#001
                score = ndata[n]['id']
                for d in score:
                    if data[str(d)]['notifying_discord_channel'] != 'nop':
                        discord_channel_id = data[str(d)]['notifying_discord_channel']
                        discord_channel = bot.get_channel(int(discord_channel_id))
                        if (str(d)) in ['1','2','3','4','5','6']:
                            msg1 = f"{latest_short_url}"
                            try:
                                await discord_channel.send(msg1)
                            except:
                                pass
                        else:
                            try:
                                try:
                                    msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} shorts啦!!!\n{latest_short_url}"
                                    await discord_channel.send(msg)
                                except:
                                    msg = f"@everyone {data[str(d)]['channel_name']} shorts啦!!!\n{latest_short_url}"
                                    await discord_channel.send(msg)
                            except:
                                pass
                    else:
                        pass
                udate[str(n)].append(latest_short_url)
                print(f"{n}Now Checking!✅")

            elif x == 1 and y == 1 and z != 1:#110
                if latest_video_url != latest_stream_url:
                    score = ndata[n]['id']
                    for d in score:
                        if data[str(d)]['notifying_discord_channel'] != 'nop':
                            discord_channel_id = data[str(d)]['notifying_discord_channel']
                            discord_channel = bot.get_channel(int(discord_channel_id))
                            if (str(d)) in ['1','2','3','4','5','6']:
                                msg1 = f"{latest_video_url}"
                                msg2 = f"{latest_stream_url}"
                                try:
                                    await discord_channel.send(msg1)
                                    await discord_channel.send(msg2)
                                except:
                                    pass
                            else:
                                try:
                                    try:
                                        msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                        msg3 = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                        await discord_channel.send(msg3)
                                    except:
                                        msg = f"@everyone {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                        msg3 = f"@everyone {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                        await discord_channel.send(msg3)
                                except:
                                    pass
                        else:
                            pass
                    udate[str(n)].extend([latest_video_url, latest_stream_url])
                    print(f"{n}Now Checking!✅")

                else:#110-
                    score = ndata[n]['id']
                    for d in score:
                        if data[str(d)]['notifying_discord_channel'] != 'nop':
                            discord_channel_id = data[str(d)]['notifying_discord_channel']
                            discord_channel = bot.get_channel(int(discord_channel_id))
                            if (str(d)) in ['1','2','3','4','5','6']:
                                msg1 = f"{latest_video_url}"
                                try:
                                    await discord_channel.send(msg1)
                                except:
                                    pass
                            else:
                                try:
                                    try:
                                        msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                    except:
                                        msg = f"@everyone {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                except:
                                    pass
                        else:
                            pass
                    udate[str(n)].append(latest_video_url)
                    print(f"{n}Now Checking!✅")

            elif x != 1 and y == 1 and z == 1:#011
                if latest_stream_url != latest_short_url:
                    score = ndata[n]['id']
                    for d in score:
                        if data[str(d)]['notifying_discord_channel'] != 'nop':
                            discord_channel_id = data[str(d)]['notifying_discord_channel']
                            discord_channel = bot.get_channel(int(discord_channel_id))
                            if (str(d)) in ['1','2','3','4','5','6']:
                                msg1 = f"{latest_stream_url}"
                                msg2 = f"{latest_short_url}"
                                try:
                                    await discord_channel.send(msg1)
                                    await discord_channel.send(msg2)
                                except:
                                    pass
                            else:
                                try:
                                    try:
                                        msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                        await discord_channel.send(msg)
                                        msg3 = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} shorts啦!!!\n{latest_short_url}"
                                        await discord_channel.send(msg3)
                                    except:
                                        msg = f"@everyone {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                        await discord_channel.send(msg)
                                        msg3 = f"@everyone {data[str(d)]['channel_name']} shorts啦!!!\n{latest_short_url}"
                                        await discord_channel.send(msg3)
                                except:
                                    pass
                        else:
                            pass
                    udate[str(n)].extend([latest_stream_url, latest_short_url])
                    print(f"{n}Now Checking!✅")

                else:#011-
                    score = ndata[n]['id']
                    for d in score:
                        if data[str(d)]['notifying_discord_channel'] != 'nop':
                            discord_channel_id = data[str(d)]['notifying_discord_channel']
                            discord_channel = bot.get_channel(int(discord_channel_id))
                            if (str(d)) in ['1','2','3','4','5','6']:
                                msg1 = f"{latest_stream_url}"
                                try:
                                    await discord_channel.send(msg1)
                                except:
                                    pass
                            else:
                                try:
                                    try:
                                        msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                        await discord_channel.send(msg)
                                    except:
                                        msg = f"@everyone {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                        await discord_channel.send(msg)
                                except:
                                    pass
                        else:
                            pass
                    udate[str(n)].append(latest_stream_url)
                    print(f"{n}Now Checking!✅")

            elif x == 1 and y != 1 and z == 1:#101
                if latest_video_url != latest_short_url:
                    score = ndata[n]['id']
                    for d in score:
                        if data[str(d)]['notifying_discord_channel'] != 'nop':
                            discord_channel_id = data[str(d)]['notifying_discord_channel']
                            discord_channel = bot.get_channel(int(discord_channel_id))
                            if (str(d)) in ['1','2','3','4','5','6']:
                                msg1 = f"{latest_video_url}"
                                msg2 = f"{latest_short_url}"
                                try:
                                    await discord_channel.send(msg1)
                                    await discord_channel.send(msg2)
                                except:
                                    pass
                            else:
                                try:
                                    try:
                                        msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                        msg3 = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} shorts啦!!!\n{latest_short_url}"
                                        await discord_channel.send(msg3)
                                    except:
                                        msg = f"@everyone {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                        msg3 = f"@everyone {data[str(d)]['channel_name']} shorts啦!!!\n{latest_short_url}"
                                        await discord_channel.send(msg3)
                                except:
                                    pass
                        else:
                            pass
                    udate[str(n)].extend([latest_video_url, latest_short_url])
                    print(f"{n}Now Checking!✅")

                else:#101-
                    score = ndata[n]['id']
                    for d in score:
                        if data[str(d)]['notifying_discord_channel'] != 'nop':
                            discord_channel_id = data[str(d)]['notifying_discord_channel']
                            discord_channel = bot.get_channel(int(discord_channel_id))
                            if (str(d)) in ['1','2','3','4','5','6']:
                                msg1 = f"{latest_video_url}"
                                try:
                                    await discord_channel.send(msg1)
                                except:
                                    pass
                            else:
                                try:
                                    try:
                                        msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                    except:
                                        msg = f"@everyone {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                except:
                                    pass
                        else:
                            pass
                    udate[str(n)].append(latest_video_url)
                    print(f"{n}Now Checking!✅")

            elif x == 1 and y == 1 and z == 1:#111
                if latest_video_url != latest_stream_url and latest_stream_url != latest_short_url and latest_video_url != latest_short_url:
                    score = ndata[n]['id']
                    for d in score:
                        if data[str(d)]['notifying_discord_channel'] != 'nop':
                            discord_channel_id = data[str(d)]['notifying_discord_channel']
                            discord_channel = bot.get_channel(int(discord_channel_id))
                            if (str(d)) in ['1','2','3','4','5','6']:
                                msg1 = f"{latest_video_url}"
                                msg2 = f"{latest_stream_url}"
                                msg3 = f"{latest_short_url}"
                                try:
                                    await discord_channel.send(msg1)
                                    await discord_channel.send(msg2)
                                    await discord_channel.send(msg3)
                                except:
                                    pass
                            else:
                                try:
                                    try:
                                        msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                        msg4 = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                        await discord_channel.send(msg4)
                                        msg5 = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} shorts啦!!!\n{latest_short_url}"
                                        await discord_channel.send(msg5)
                                    except:
                                        msg = f"@everyone {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                        msg4 = f"@everyone {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                        await discord_channel.send(msg4)
                                        msg5 = f"@everyone {data[str(d)]['channel_name']} shorts啦!!!\n{latest_short_url}"
                                        await discord_channel.send(msg5)
                                except:
                                    pass
                        else:
                            pass
                    udate[str(n)].extend([latest_video_url, latest_stream_url, latest_short_url])
                    print(f"{n}Now Checking!✅")

                elif latest_video_url == latest_stream_url and latest_stream_url != latest_short_url and latest_video_url != latest_short_url:#111-1
                    score = ndata[n]['id']
                    for d in score:
                        if data[str(d)]['notifying_discord_channel'] != 'nop':
                            discord_channel_id = data[str(d)]['notifying_discord_channel']
                            discord_channel = bot.get_channel(int(discord_channel_id))
                            if (str(d)) in ['1','2','3','4','5','6']:
                                msg1 = f"{latest_video_url}"
                                msg2 = f"{latest_short_url}"
                                try:
                                    await discord_channel.send(msg1)
                                    await discord_channel.send(msg2)
                                except:
                                    pass
                            else:
                                try:
                                    try:
                                        msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                        msg3 = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} shorts啦!!!\n{latest_short_url}"
                                        await discord_channel.send(msg3)
                                    except:
                                        msg = f"@everyone {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                        msg3 = f"@everyone {data[str(d)]['channel_name']} shorts啦!!!\n{latest_short_url}"
                                        await discord_channel.send(msg3)
                                except:
                                    pass
                        else:
                            pass
                    udate[str(n)].extend([latest_video_url, latest_short_url])
                    print(f"{n}Now Checking!✅")

                elif latest_video_url != latest_stream_url and latest_stream_url == latest_short_url and latest_video_url != latest_short_url:#111-2
                    score = ndata[n]['id']
                    for d in score:
                        if data[str(d)]['notifying_discord_channel'] != 'nop':
                            discord_channel_id = data[str(d)]['notifying_discord_channel']
                            discord_channel = bot.get_channel(int(discord_channel_id))
                            if (str(d)) in ['1','2','3','4','5','6']:
                                msg1 = f"{latest_video_url}"
                                msg2 = f"{latest_stream_url}"
                                try:
                                    await discord_channel.send(msg1)
                                    await discord_channel.send(msg2)
                                except:
                                    pass
                            else:
                                try:
                                    try:
                                        msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                        msg3 = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                        await discord_channel.send(msg3)
                                    except:
                                        msg = f"@everyone {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                        msg3 = f"@everyone {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                        await discord_channel.send(msg3)
                                except:
                                    pass
                        else:
                            pass
                    udate[str(n)].extend([latest_video_url, latest_stream_url])
                    print(f"{n}Now Checking!✅")

                elif latest_video_url != latest_stream_url and latest_stream_url != latest_short_url and latest_video_url == latest_short_url:#111-3
                    score = ndata[n]['id']
                    for d in score:
                        if data[str(d)]['notifying_discord_channel'] != 'nop':
                            discord_channel_id = data[str(d)]['notifying_discord_channel']
                            discord_channel = bot.get_channel(int(discord_channel_id))
                            if (str(d)) in ['1','2','3','4','5','6']:
                                msg1 = f"{latest_video_url}"
                                msg2 = f"{latest_stream_url}"
                                try:
                                    await discord_channel.send(msg1)
                                    await discord_channel.send(msg2)
                                except:
                                    pass
                            else:
                                try:
                                    try:
                                        msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                        msg3 = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                        await discord_channel.send(msg3)
                                    except:
                                        msg = f"@everyone {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                        msg3 = f"@everyone {data[str(d)]['channel_name']} 開台啦!!!\n{latest_stream_url}"
                                        await discord_channel.send(msg3)
                                except:
                                    pass
                        else:
                            pass
                    udate[str(n)].extend([latest_video_url, latest_stream_url])
                    print(f"{n}Now Checking!✅")

                elif latest_video_url == latest_stream_url and latest_stream_url == latest_short_url and latest_video_url == latest_short_url:#111-4
                    score = ndata[n]['id']
                    for d in score:
                        if data[str(d)]['notifying_discord_channel'] != 'nop':
                            discord_channel_id = data[str(d)]['notifying_discord_channel']
                            discord_channel = bot.get_channel(int(discord_channel_id))
                            if (str(d)) in ['1','2','3','4','5','6']:
                                msg1 = f"{latest_video_url}"
                                try:
                                    await discord_channel.send(msg1)
                                except:
                                    pass
                            else:
                                try:
                                    try:
                                        msg = f"<@&{data[str(d)]['role']}> {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                    except:
                                        msg = f"@everyone {data[str(d)]['channel_name']} 發片啦!!!\n{latest_video_url}"
                                        await discord_channel.send(msg)
                                except:
                                    pass
                        else:
                            pass
                    udate[str(n)].append(latest_video_url)
                    print(f"{n}Now Checking!✅")

                else:
                    pass
            else:
                pass

        try:
            requests.put(url['udate'], json=udate)
        except:
            pass

        jdate['ya']="1"
        end = datetime.now()
        yttime = end - start
        channel = bot.get_channel(1039919671455006790)
        await channel.send(f'☀️YT ok\n執行時間：{yttime}')

        

@bot.slash_command(description = "🟥添加youtube通知")
@guild_only()
async def youtube_inform_add(ctx, yt頻道id: discord.Option(str), 主播名字: discord.Option(str)):

    await ctx.response.defer()

    if (jdate['ya']) == "1":
        t1 = 1

        for n in data:
            if yt頻道id in {data[n]['channel_id']} and str(ctx.channel.id) in {data[n]['notifying_discord_channel']}:
                an = n

                data[str(an)]["channel_name"]=主播名字
                requests.put(url['data'], json=data)

                t1 = 0
                await ctx.followup.send(f'編號「{n}」{主播名字} 更新成功!')
                break

            else:
                pass

        if t1 == 1:
            t2 = 1

            for o in ndata:
                if yt頻道id in {ndata[o]['channel_id']}:
                    n=(jdate['youtube'])
                    n=(int(n))
                    n=n+1
                    jdate['youtube']=(str(n))
                    requests.put(url['jdate'], json=jdate)

                    data[str(n)]={}
                    data[str(n)]["channel_id"]=yt頻道id
                    data[str(n)]["channel_name"]=主播名字
                    data[str(n)]["notifying_discord_channel"]=(str(ctx.channel.id))
                    requests.put(url['data'], json=data)

                    ndata[str(o)]['id'].append(str(n))
                    requests.put(url['ndata'], json=ndata)

                    t2 = 0
                    await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                    break
                    
                else:
                    pass

            if t2 == 1:
                t3 = 1

                x = 0
                y = 0
                z = 0

                channel = f"https://www.youtube.com/channel/{yt頻道id}"

                try:
                    html = requests.get(channel+"/videos").text
                    latest_video_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
                    x = 1
                except:
                    pass
                try:
                    html1 = requests.get(channel+"/streams").text
                    latest_stream_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html1).group()
                    y = 1
                except:
                    pass
                try:
                    html2 = requests.get(channel+"/shorts").text
                    latest_short_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html2).group()
                    z = 1
                except:
                    pass

                if x != 1 and y != 1 and z != 1:#000
                    await ctx.followup.send(f'`yt頻道id`輸入錯誤or該頻道尚未有任何`影片`或`直播`或`shorts`')
                    t3 = 0

                if t3 == 1:
                    n=(jdate['youtube'])
                    n=(int(n))
                    n=n+1
                    jdate['youtube']=(str(n))

                    data[str(n)]={}
                    data[str(n)]["channel_id"]=yt頻道id
                    data[str(n)]["channel_name"]=主播名字
                    data[str(n)]["notifying_discord_channel"]=(str(ctx.channel.id))

                    m=(jdate['ytchannel'])
                    m=(int(m))
                    m=m+1
                    jdate['ytchannel']=(str(m))

                    ndata[str(m)]={}
                    ndata[str(m)]["channel_id"]=yt頻道id
                    ndata[str(m)]["id"]=[str(n)]

                    

                    if x == 1 and y != 1 and z != 1:#100
                        requests.put(url['jdate'], json=jdate)
                        requests.put(url['data'], json=data)
                        requests.put(url['ndata'], json=ndata)
                        udate[str(m)]=[latest_video_url]
                        requests.put(url['udate'], json=udate)
                        await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                    elif x != 1 and y == 1 and z != 1:#010
                        requests.put(url['jdate'], json=jdate)
                        requests.put(url['data'], json=data)
                        requests.put(url['ndata'], json=ndata)
                        udate[str(m)]=[latest_stream_url]
                        requests.put(url['udate'], json=udate)
                        await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                    elif x != 1 and y != 1 and z == 1:#001
                        requests.put(url['jdate'], json=jdate)
                        requests.put(url['data'], json=data)
                        requests.put(url['ndata'], json=ndata)
                        udate[str(m)]=[latest_short_url]
                        requests.put(url['udate'], json=udate)
                        await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                    elif x == 1 and y == 1 and z != 1:#110
                        requests.put(url['jdate'], json=jdate)
                        requests.put(url['data'], json=data)
                        requests.put(url['ndata'], json=ndata)
                        if latest_video_url != latest_stream_url:
                            udate[str(m)]=[latest_video_url, latest_stream_url]
                            requests.put(url['udate'], json=udate)
                            await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                        else:#110-
                            udate[str(m)]=[latest_video_url]
                            requests.put(url['udate'], json=udate)
                            await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                    elif x != 1 and y == 1 and z == 1:#011
                        requests.put(url['jdate'], json=jdate)
                        requests.put(url['data'], json=data)
                        requests.put(url['ndata'], json=ndata)
                        if latest_stream_url != latest_short_url:
                            udate[str(m)]=[latest_stream_url, latest_short_url]
                            requests.put(url['udate'], json=udate)
                            await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                        else:#011-
                            udate[str(m)]=[latest_stream_url]
                            requests.put(url['udate'], json=udate)
                            await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                    elif x == 1 and y != 1 and z == 1:#101
                        requests.put(url['jdate'], json=jdate)
                        requests.put(url['data'], json=data)
                        requests.put(url['ndata'], json=ndata)
                        if latest_video_url != latest_short_url:
                            udate[str(m)]=[latest_video_url, latest_short_url]
                            requests.put(url['udate'], json=udate)
                            await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                        else:#101-
                            udate[str(m)]=[latest_video_url]
                            requests.put(url['udate'], json=udate)
                            await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                    elif x == 1 and y == 1 and z == 1:#111
                        requests.put(url['jdate'], json=jdate)
                        requests.put(url['data'], json=data)
                        requests.put(url['ndata'], json=ndata)
                        if latest_video_url != latest_stream_url and latest_stream_url != latest_short_url and latest_video_url != latest_short_url:
                            udate[str(m)]=[latest_video_url, latest_stream_url, latest_short_url]
                            requests.put(url['udate'], json=udate)
                            await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                        elif latest_video_url == latest_stream_url and latest_stream_url != latest_short_url and latest_video_url != latest_short_url:#111-1
                            udate[str(m)]=[latest_video_url, latest_short_url]
                            requests.put(url['udate'], json=udate)
                            await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                        elif latest_video_url != latest_stream_url and latest_stream_url == latest_short_url and latest_video_url != latest_short_url:#111-2
                            udate[str(m)]=[latest_video_url, latest_stream_url]
                            requests.put(url['udate'], json=udate)
                            await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                        elif latest_video_url != latest_stream_url and latest_stream_url != latest_short_url and latest_video_url == latest_short_url:#111-3
                            udate[str(m)]=[latest_video_url, latest_stream_url]
                            requests.put(url['udate'], json=udate)
                            await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                        elif latest_video_url == latest_stream_url and latest_stream_url == latest_short_url and latest_video_url == latest_short_url:#111-4
                            udate[str(m)]=[latest_video_url]
                            requests.put(url['udate'], json=udate)
                            await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

                        else:
                            await ctx.followup.send(f'`yt頻道id`輸入錯誤or該頻道尚未有任何`影片`或`直播`或`shorts`')
                    else:
                        await ctx.followup.send(f'`yt頻道id`輸入錯誤or該頻道尚未有任何`影片`或`直播`或`shorts`')
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        await ctx.followup.send(f'請稍等3分鐘後重試')



@bot.slash_command(description = "🟥刪除youtube通知")
@guild_only()
async def youtube_inform_delete(ctx, yt編號: discord.Option(str)):

    await ctx.response.defer()

    if str(ctx.channel.id) in {data[yt編號]['notifying_discord_channel']}:
        channel_name = data[yt編號]['channel_name']

        data[yt編號]["notifying_discord_channel"]='nop'
        requests.put(url['data'], json=data)

        await ctx.followup.send(f'編號「{yt編號}」{channel_name} 刪除成功!')
    else:
        await ctx.followup.send("對象不存在!")



@bot.slash_command(description = "🟥更改youtube主播的名字")
@guild_only()
async def youtube_change_name(ctx, yt編號: discord.Option(str), 主播名字: discord.Option(str)):

    await ctx.response.defer()

    if str(ctx.channel.id) in {data[yt編號]['notifying_discord_channel']}:
        data[yt編號]["channel_name"]=主播名字
        requests.put(url['data'], json=data)
        await ctx.followup.send(f'編號「{yt編號}」{主播名字} 更新成功!')
    else:
        await ctx.followup.send("對象不存在!")



@bot.slash_command(description = "🟥更改youtube通知的艾特")
@guild_only()
async def youtube_change_at(ctx, yt編號: discord.Option(str), 艾特id: discord.Option(str)):

    await ctx.response.defer()

    if str(ctx.channel.id) in {data[yt編號]['notifying_discord_channel']}:
        channel_name = data[yt編號]['channel_name']

        channel_id = data[yt編號]['channel_id']
        channel_name1 = data[yt編號]['channel_name']
        notifying_discord_channel = data[yt編號]['notifying_discord_channel']

        data[yt編號]={}
        data[yt編號]["channel_id"]=channel_id
        data[yt編號]["channel_name"]=channel_name1
        data[yt編號]["notifying_discord_channel"]=notifying_discord_channel
        data[yt編號]["role"]=艾特id
        requests.put(url['data'], json=data)
        await ctx.followup.send(f'編號「{yt編號}」{channel_name}_<@&{艾特id}>設定成功!')
    else:
        await ctx.followup.send("對象不存在!")



@bot.slash_command(description = "🟥查詢youtube的頻道ID")
@guild_only()
async def youtube_id_search(ctx):
    await ctx.response.defer()
    await ctx.followup.send('https://cdn.discordapp.com/attachments/978285960414502982/1077605387420839966/713_20230221225854.png', view=ytid())



#twitch
@tasks.loop(seconds=60)
async def check_twitch_online_streamers():
    async with aiohttp.ClientSession() as session:
        start = time.perf_counter()

        ct1=(jdate['ct1'])
        ct1=(int(ct1))
        ct1=ct1+1
        if ct1 > 10:
            ct1 = 1
            jdate['ct1']=(str(ct1))
        else:
            jdate['ct1']=(str(ct1))

        cid=[]

        for n in wdata:
            m = wdata[n]['channel_id']
            cid.append(m)

        users = await get_users(cid)
        streams = await get_streams(users)

        for n in wdata:
            print(f"TW {n}Now Checking For {wdata[n]['channel_name']}")
            tw_id = wdata[n]['channel_id']
            user_name = wdata[n]['channel_id']
            notifications = []
            if user_name not in online_users:
                online_users[user_name] = datetime.utcnow()

            if user_name not in streams:
                online_users[user_name] = None
            else:
                started_at = datetime.strptime(streams[user_name]["started_at"], "%Y-%m-%dT%H:%M:%SZ")
                if online_users[user_name] is None or started_at > online_users[user_name]:
                    notifications.append(streams[user_name])
                    online_users[user_name] = started_at

                    for i in wdata:
                        if wdata[i]['channel_id'] == tw_id:
                            
                            if wdata[str(i)]['notifying_discord_channel'] != 'nop':
                                discord_channel_id = wdata[str(i)]['notifying_discord_channel']
                                discord_channel = bot.get_channel(int(discord_channel_id))
                
                                for notification in notifications:
                                    characters = "{'}"
                                    title = notification["title"]
                                    title = ''.join( x for x in title if x not in characters)
                                    url = f"https://www.twitch.tv/{wdata[i]['channel_id']}"
                                    url = ''.join( x for x in url if x not in characters)
                                    name = notification["user_name"]
                                    name = ''.join( x for x in name if x not in characters)
                                    image = notification["thumbnail_url"]
                                    image = ''.join( x for x in image if x not in characters)
                                    image = image.replace("width", "1920")
                                    image = image.replace("height", "1080")

                                    embed=discord.Embed(title=f"{title}", url=f"{url}", color=0x6441A5)
                                    embed.set_author(name=f"{name}")

                                    embed2=discord.Embed(title=f"{title}", url=f"{url}", color=0x6441A5)
                                    embed2.set_author(name=f"{name}")
                                    embed2.set_image(url=f"{image}")
                                    if (str(i)) in ['1','2','3','4','5','6']:
                                        await discord_channel.send(f"https://www.twitch.tv/{wdata[i]['channel_id']}")
                                        discord_channel1 = bot.get_channel(905064079998193664)
                                        try:
                                            await discord_channel1.send(f"@everyone {wdata[i]['channel_name']}開台啦!還不趕快去看!➲\nhttps://www.twitch.tv/{wdata[i]['channel_id']}",embed=embed2)
                                        except:
                                            await discord_channel1.send(f"@everyone {wdata[i]['channel_name']}開台啦!還不趕快去看!➲\nhttps://www.twitch.tv/{wdata[i]['channel_id']}",embed=embed)

                                        if (str(i)) in ['2']:
                                            discord_channelo = bot.get_channel(878218144966115338)
                                            try:
                                                await discord_channelo.send(f"@everyone {wdata[i]['channel_name']}開台啦!還不趕快去看!➲\nhttps://www.twitch.tv/{wdata[i]['channel_id']}",embed=embed2)
                                            except:
                                                await discord_channelo.send(f"@everyone {wdata[i]['channel_name']}開台啦!還不趕快去看!➲\nhttps://www.twitch.tv/{wdata[i]['channel_id']}",embed=embed)
                                    else:
                                        try:
                                            try:
                                                try:
                                                    await discord_channel.send(f"<@&{wdata[str(i)]['role']}> {wdata[str(i)]['channel_name']} 開台啦!!!\nhttps://www.twitch.tv/{wdata[i]['channel_id']}",embed=embed2)
                                                except:
                                                    await discord_channel.send(f"<@&{wdata[str(i)]['role']}> {wdata[str(i)]['channel_name']} 開台啦!!!\nhttps://www.twitch.tv/{wdata[i]['channel_id']}",embed=embed)
                                            except:
                                                try:
                                                    await discord_channel.send(f"@everyone {wdata[i]['channel_name']} 開台啦!!\nhttps://www.twitch.tv/{wdata[i]['channel_id']}",embed=embed2)
                                                except:
                                                    await discord_channel.send(f"@everyone {wdata[i]['channel_name']} 開台啦!!\nhttps://www.twitch.tv/{wdata[i]['channel_id']}",embed=embed)
                                        except:
                                            pass
                            else:
                                pass
                        else:
                            pass
                else:
                    pass
        
        end = time.perf_counter()
        twtime = end - start
        if jdate['ct1'] == (str(1)):
            channel = bot.get_channel(1039919671455006790)
            await channel.send(f'TW ok測量時間：{twtime}')



@bot.command()
async def token(ctx):
    if ctx.guild.id == 868011979460190299:
        access_token = get_app_access_token()
        await ctx.send(access_token)


def get_app_access_token():
    params = {
        "client_id": tdate["client_id"],
        "client_secret": tdate["client_secret"],
        "grant_type": "client_credentials"
    }

    response = requests.post("https://id.twitch.tv/oauth2/token", params=params)
    access_token = response.json()["access_token"]
    return access_token



async def get_users(login_names):
    params = {
        "login": login_names
    }

    headers = {
        "Authorization": "Bearer {}".format(tdate["access_token"]),
        "Client-Id": tdate["client_id"]
    }

    response = requests.get("https://api.twitch.tv/helix/users", params=params, headers=headers)
    
    return {entry["login"]: entry["id"] for entry in response.json()["data"]}



async def get_streams(users):
    params = {
        "user_id": users.values()
    }

    headers = {
        "Authorization": "Bearer {}".format(tdate["access_token"]),
        "Client-Id": tdate["client_id"]
    }

    response = requests.get("https://api.twitch.tv/helix/streams", params=params, headers=headers)

    return {entry["user_login"]: entry for entry in response.json()["data"]}



online_users = {}



@bot.slash_command(description = "🟪添加twitch通知")
@guild_only()
async def twitch_inform_add(ctx, tw頻道id: discord.Option(str), 主播名字: discord.Option(str)):

    await ctx.response.defer()

    t1 = 1

    for n in wdata:
        if tw頻道id in {wdata[n]['channel_id']} and str(ctx.channel.id) in {wdata[n]['notifying_discord_channel']}:
            an = n

            wdata[str(an)]["channel_name"]=主播名字
            requests.put(url['wdata'], json=wdata)

            await ctx.followup.send(f'編號「{n}」{主播名字} 更新成功!')
            t1 = 0

        else:
            pass

    if t1 == 1:

        n=(jdate['twitch'])
        n=(int(n))
        n=n+1
        jdate['twitch']=(str(n))
        requests.put(url['jdate'], json=jdate)

        wdata[str(n)]={}
        wdata[str(n)]["channel_id"]=tw頻道id
        wdata[str(n)]["channel_name"]=主播名字
        wdata[str(n)]["notifying_discord_channel"]=(str(ctx.channel.id))
        requests.put(url['wdata'], json=wdata)

        await ctx.followup.send(f'編號「{n}」{主播名字} 加入成功!')

    else:
        pass



@bot.slash_command(description = "🟪刪除twitch通知")
@guild_only()
async def twitch_inform_delete(ctx, tw編號: discord.Option(str)):

    await ctx.response.defer()

    if str(ctx.channel.id) in {wdata[tw編號]['notifying_discord_channel']}:
        channel_name = wdata[tw編號]['channel_name']

        wdata[tw編號]["notifying_discord_channel"]='nop'
        requests.put(url['wdata'], json=wdata)

        await ctx.followup.send(f'編號「{tw編號}」{channel_name} 刪除成功!')
    else:
        await ctx.followup.send("對象不存在!")



@bot.slash_command(description = "🟪更改twitch主播的名字")
@guild_only()
async def twitch_change_name(ctx, tw編號: discord.Option(str), 主播名字: discord.Option(str)):

    await ctx.response.defer()

    if str(ctx.channel.id) in {wdata[tw編號]['notifying_discord_channel']}:
        wdata[tw編號]["channel_name"]=主播名字
        requests.put(url['wdata'], json=wdata)
        await ctx.followup.send(f'編號「{tw編號}」{主播名字} 更新成功!')
    else:
        await ctx.followup.send("對象不存在!")



@bot.slash_command(description = "🟪更改twitch通知的艾特")
@guild_only()
async def twitch_change_at(ctx, tw編號: discord.Option(str), 艾特id: discord.Option(str)):

    await ctx.response.defer()

    if str(ctx.channel.id) in {wdata[tw編號]['notifying_discord_channel']}:
        channel_name = wdata[tw編號]['channel_name']
        
        channel_id = wdata[tw編號]['channel_id']
        channel_name1 = wdata[tw編號]['channel_name']
        notifying_discord_channel = wdata[tw編號]['notifying_discord_channel']

        wdata[tw編號]={}
        wdata[tw編號]["channel_id"]=channel_id
        wdata[tw編號]["channel_name"]=channel_name1
        wdata[tw編號]["notifying_discord_channel"]=notifying_discord_channel
        wdata[tw編號]["role"]=艾特id
        requests.put(url['wdata'], json=wdata)
        await ctx.followup.send(f'編號「{tw編號}」{channel_name}_<@&{艾特id}>設定成功!')
    else:
        await ctx.followup.send("對象不存在!")



@bot.slash_command(description = "🟪查詢twitch的頻道ID")
@guild_only()
async def twitch_id_search(ctx):
    await ctx.response.defer()
    await ctx.followup.send(f'https://cdn.discordapp.com/attachments/978285960414502982/1077604515806724147/719_20230221225523.png')



#其他
@bot.slash_command(description = "🟨查詢艾特的ID")
@guild_only()
async def at_id(ctx):
    await ctx.response.defer()
    await ctx.followup.send(f'https://cdn.discordapp.com/attachments/978285960414502982/1077604268745429084/720_20230221225425.png')



@bot.slash_command(description = "🟨查看此頻道裡的所有通知")
@guild_only()
async def all_inform(ctx):

    await ctx.response.defer()

    yt = 1
    tw = 1
    embed = discord.Embed(title='Inform:', color=discord.Color.gold())
    embed.add_field(name="🟥youtube", value="yt編號/主播名字", inline=False)
    for n in data:
        if str(ctx.channel.id) in {data[n]['notifying_discord_channel']}:
            an = n
            
            embed.add_field(name=f"{an}. {data[an]['channel_name']}", value=f"[{data[an]['channel_name']}のyoutube](https://www.youtube.com/channel/{data[an]['channel_id']})", inline=False)
            yt = 0

    if yt == 1:
        embed.add_field(name="沒有通知在此頻道", value="", inline=False)

    embed.add_field(name="🟪twitch", value="tw編號/主播名字", inline=False)
    for n in wdata:
        if str(ctx.channel.id) in {wdata[n]['notifying_discord_channel']}:
            an = n
            
            embed.add_field(name=f"{an}. {wdata[an]['channel_name']}", value=f"[{wdata[an]['channel_name']}のtwitch](https://www.twitch.tv/{wdata[an]['channel_id']})", inline=False)
            tw = 0

    if tw == 1:
        embed.add_field(name="沒有通知在此頻道", value="", inline=False)

    await ctx.followup.send(embed=embed)



@bot.slash_command(description = "🟨傳送提問/建議/bug回報")
@guild_only()
async def talk(ctx):
    modal_bug = bug(title="回報")
    await ctx.send_modal(modal_bug)



@bot.slash_command(description = "🟨添加獲取更新資訊的頻道")
@guild_only()
async def question_channel_add(ctx):

    await ctx.response.defer()

    t1 = 1

    for n in cdata:
        if str(ctx.channel.id) in {cdata[n]['channel_id']} and "F" in {cdata[n]['OX']}:
            an = n

            cdata[str(an)]["OX"]='T'
            requests.put(url['cdata'], json=cdata)

            await ctx.followup.send(f'update channel加入成功!')
            t1 = 0

        elif str(ctx.channel.id) in {cdata[n]['channel_id']} and "T" in {cdata[n]['OX']}:
            await ctx.followup.send(f'update channel已存在!')
            t1 = 0

        else:
            pass

    if t1 == 1:

        n=(jdate['channel'])
        n=(int(n))
        n=n+1
        jdate['channel']=(str(n))
        requests.put(url['jdate'], json=jdate)

        cdata[str(n)]={}
        cdata[str(n)]["channel_id"]=(str(ctx.channel.id))
        cdata[str(n)]["OX"]='T'
        requests.put(url['cdata'], json=cdata)

        await ctx.followup.send(f'update channel加入成功!')

    else:
        pass



@bot.slash_command(description = "🟨刪除獲取更新資訊的頻道")
@guild_only()
async def question_channel_delete(ctx):

    await ctx.response.defer()

    t1 = 1

    for n in cdata:
        if str(ctx.channel.id) in {cdata[n]['channel_id']} and "T" in {cdata[n]['OX']}:
            an = n

            cdata[str(an)]["OX"]='F'
            requests.put(url['cdata'], json=cdata)

            await ctx.followup.send(f'update channel刪除成功!')
            t1 = 0

        elif str(ctx.channel.id) in {cdata[n]['channel_id']} and "F" in {cdata[n]['OX']}:
            await ctx.followup.send(f'update channel已刪除!')
            t1 = 0

        else:
            pass

    if t1 == 1:
        await ctx.followup.send(f'你好像沒有加入提問題和更新資訊的頻道!')



@bot.slash_command(description = "🟨關於此機器人的所有指令")
@guild_only()
async def about(ctx):

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
    view = Sabout(timeout=3600)
    await ctx.followup.send(embed=embed, view = view)



@bot.slash_command(description = "🚫發送更新公告(一般人沒權限)")
@guild_only()
async def update_notice(ctx):
    if (str(ctx.author.id)) == "833717980633628732":
        modal = update(title="公告")
        await ctx.send_modal(modal)
    else:
        await ctx.response('你沒有權限')



@bot.slash_command(description = "🚫發送回覆(一般人沒權限)")
@guild_only()
async def response(ctx):
    if (str(ctx.author.id)) == "833717980633628732":
        modal_reply = reply(title="回覆")
        await ctx.send_modal(modal_reply)
    else:
        await ctx.followup.send('你沒有權限')



@bot.slash_command(description = "🚫添加bug說明(一般人沒權限)")
@guild_only()
async def bug_description_add(ctx):
    if (str(ctx.author.id)) == "833717980633628732":
        modal_abug = abug(title="bug說明")
        await ctx.send_modal(modal_abug)
    else:
        await ctx.followup.send('你沒有權限')



@bot.slash_command(description = "🚫刪除bug說明(一般人沒權限)")
@guild_only()
async def bug_description_delete(ctx, bug編號: discord.Option(str)):

    await ctx.response.defer()

    if (str(ctx.author.id)) == "833717980633628732":
        if "T" in {bdata[bug編號]['TF']}:
            title = bdata[bug編號]['title']

            bdata[bug編號]['TF'] = "F"
            requests.put(url['bdata'], json=bdata)

            embed=discord.Embed(title="bug", color=0x1E90FF)
            embed.set_author(name="陽光", icon_url="https://cdn.discordapp.com/attachments/978285960414502982/1076551250700669019/-.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/978285960414502982/1077577427561218109/1676984811869.png")
            bbug = 1
            for b in bdata:
                if str(bdata[b]["TF"]) == "T":
                    tbug = str(bdata[b]["title"])
                    cbug = str(bdata[b]["content"])
                    embed.add_field(name=f"{b}.{tbug}", value=f"*{cbug}*", inline=False)
                    bbug = 0
                else:
                    pass

            if bbug == 1:
                embed.add_field(name="目前沒有bug", value="", inline=False)
            else:
                pass

            await ctx.followup.send(content=f"編號「{bug編號}」{title} 刪除成功!", embed=embed)

        else:
            await ctx.followup.send('對象不存在!')

    else:
        await ctx.followup.send('你沒有權限')



@bot.command()
async def form(ctx):
    await ctx.send(f'https://forms.gle/34cVxoiuNF31BB4Q6')



for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdate['TOKEN3'])
