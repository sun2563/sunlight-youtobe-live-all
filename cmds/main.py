import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random,datetime
import json,asyncio
from discord import File
from PIL import Image, ImageDraw, ImageFont
import io
import requests
from discord.ui import View

with open('URL.json', mode='r', encoding='utf8') as jfile:
    url = json.load(jfile)

json6 = requests.get(url['odate'])
odate = json6.json()

#---------------------------------------------------------------------------------------------------

class sun(View):
    @discord.ui.button(label="涵", style=discord.ButtonStyle.green)
    async def button_callback(self, button, interaction):
        button.disabled = True
        yu = 761967543698980866
        await interaction.response.edit_message(content=f'At完畢，稍後將自動刪除此訊息', view=no())
        await interaction.channel.send(f'<@{yu}>')

    @discord.ui.button(label="妮", style=discord.ButtonStyle.blurple)
    async def button_callback2(self, button, interaction):
        button.disabled = True
        ni = 843145173407760435
        await interaction.response.edit_message(content=f'At完畢，稍後將自動刪除此訊息', view=no())
        await interaction.channel.send(content=f'<@{ni}>')

    @discord.ui.button(label="大家", style=discord.ButtonStyle.secondary)
    async def button_callback3(self, button, interaction):
        button.disabled = True
        await interaction.response.edit_message(content=f'At完畢，稍後將自動刪除此訊息', view=no())
        await interaction.channel.send('@everyone')

class yu(View):
    @discord.ui.button(label="江", style=discord.ButtonStyle.green)
    async def button_callback(self, button, interaction):
        button.disabled = True
        sun = 833717980633628732
        await interaction.response.edit_message(content=f'At完畢，稍後將自動刪除此訊息', view=no())
        await interaction.channel.send(f'<@{sun}>')

    @discord.ui.button(label="妮", style=discord.ButtonStyle.blurple)
    async def button_callback2(self, button, interaction):
        button.disabled = True
        ni = 843145173407760435
        await interaction.response.edit_message(content=f'At完畢，稍後將自動刪除此訊息', view=no())
        await interaction.channel.send(f'<@{ni}>')

    @discord.ui.button(label="大家", style=discord.ButtonStyle.secondary)
    async def button_callback3(self, button, interaction):
        button.disabled = True
        await interaction.response.edit_message(content=f'At完畢，稍後將自動刪除此訊息', view=no())
        await interaction.channel.send('@everyone')

class ni(View):
    @discord.ui.button(label="涵", style=discord.ButtonStyle.green)
    async def button_callback(self, button, interaction):
        button.disabled = True
        yu = 761967543698980866
        await interaction.response.edit_message(content=f'At完畢，稍後將自動刪除此訊息', view=no())
        await interaction.channel.send(f'<@{yu}>')

    @discord.ui.button(label="江", style=discord.ButtonStyle.blurple)
    async def button_callback2(self, button, interaction):
        button.disabled = True
        sun = 833717980633628732
        await interaction.response.edit_message(content=f'At完畢，稍後將自動刪除此訊息', view=no())
        await interaction.channel.send(f'<@{sun}>')

    @discord.ui.button(label="大家", style=discord.ButtonStyle.secondary)
    async def button_callback3(self, button, interaction):
        button.disabled = True
        await interaction.response.edit_message(content=f'At完畢，稍後將自動刪除此訊息', view=no())
        await interaction.channel.send('@everyone')

class no(View):
    pass

#---------------------------------------------------------------------------------------------------

class Main(Cog_Extension):

    @commands.command()
    async def s(self, ctx, *,msg):
        if (str(ctx.author.id)) == '833717980633628732':
            await ctx.message.delete()
            await ctx.send(msg)
        else:
            pass

    @commands.command()
    async def d(self, ctx, num:int):
        if (str(ctx.author.id)) in ['833717980633628732', '539461996869845003', '897089011749892168', '856540895880020040', '822745446274433035','872499575397691452', '664336750998716426', '487278026779000832']:
            await ctx.channel.purge(limit=num+1)
        else:
            pass

    @commands.command()
    async def NOW(self, ctx):
        if (str(ctx.author.id)) == "833717980633628732":
            now = datetime.datetime.now().strftime("%H:%M")
            await ctx.send(now)

    @commands.command()
    async def ping(self, ctx):
        if (str(ctx.author.id)) == "833717980633628732":
            await ctx.send(f'{round(self.bot.latency*1000)} ms') 

    @commands.Cog.listener()
    async def on_member_join(self, member, text=None):
        if member.guild.id == 877943603845013524:
            IMAGE_WIDTH = 1100
            IMAGE_HEIGHT = 500

            image = Image.open('pic/ouo.png')
            draw = ImageDraw.Draw(image)
        
            text = f'welcome to 陽光姐姐の閨房(≧▽≦)'
            font = ImageFont.truetype(r'FFC//中明體.ttc', 20)
            text_width, text_height = draw.textsize(text, font=font)
            x = (IMAGE_WIDTH - text_width)//2
            y = 325
            draw.text( (x, y), text, fill=(0,0,0), font=font)

            text = f'{member}'
            font = ImageFont.truetype(r'FFC//中明體.ttc', 40)
            text_width, text_height = draw.textsize(text, font=font)
            x = (IMAGE_WIDTH - text_width)//2
            y = 350
            draw.text( (x, y), text, fill=(0,0,0), font=font)

            AVATAR_SIZE = 256
            avatar_asset = member.avatar.with_size(AVATAR_SIZE).url
            buffer_avatar = requests.get(str(avatar_asset)).content
            with open('pic/zimage_name.jpg', 'wb') as handler:
                handler.write(buffer_avatar)
            avatar_image = Image.open('pic/zimage_name.jpg')
            avatar_image = avatar_image.resize((AVATAR_SIZE, AVATAR_SIZE))
            circle_image = Image.new('L', (AVATAR_SIZE, AVATAR_SIZE))
            circle_draw = ImageDraw.Draw(circle_image)
            circle_draw.ellipse((0, 0, AVATAR_SIZE, AVATAR_SIZE), fill=255)
            px = 422
            py = 50
            image.paste(avatar_image, (px, py), circle_image)
            buffer = io.BytesIO()
            image.save(buffer, format='PNG')
            buffer.seek(0)

            channel = self.bot.get_channel(878102405202460722)
            await channel.send(f'嗨~<@{member.id}>歡迎來到🌞陽光姐姐の閨房(≧▽≦)!\n請先至<#{877947213513388103}>查看規則&點選身分組!\n再至<#{880883496476897352}>詳閱看V禮儀!謝謝~祝玩得愉快~', file=File(buffer, 'SunLight_OuO.png'))
        
            channel = self.bot.get_channel(int(odate['WEC']))
            await channel.send(f'歡迎<**{member.name}**>!(YA!!我是第一個歡迎的!沒人比我快的~喵~~')
        else:
            pass
            if member.guild.id == 905057576411078706:
                IMAGE_WIDTH = 1100
                IMAGE_HEIGHT = 500

                image = Image.open('pic/czb.png')
                draw = ImageDraw.Draw(image)
        
                text = f'welcome to COZY BOX'
                font = ImageFont.truetype(r'FFC//中明體.ttc', 20)
                text_width, text_height = draw.textsize(text, font=font)
                x = (IMAGE_WIDTH - text_width)//2
                y = 325
                draw.text( (x, y), text, fill=(255,255,255), font=font)

                text = f'{member}'
                font = ImageFont.truetype(r'FFC//中明體.ttc', 40)
                text_width, text_height = draw.textsize(text, font=font)
                x = (IMAGE_WIDTH - text_width)//2
                y = 350
                draw.text( (x, y), text, fill=(255,255,255), font=font)

                AVATAR_SIZE = 256
                avatar_asset = member.avatar.with_size(AVATAR_SIZE).url
                buffer_avatar = requests.get(str(avatar_asset)).content
                with open('pic/zimage_name.jpg', 'wb') as handler:
                    handler.write(buffer_avatar)
                avatar_image = Image.open('pic/zimage_name.jpg')
                avatar_image = avatar_image.resize((AVATAR_SIZE, AVATAR_SIZE))
                circle_image = Image.new('L', (AVATAR_SIZE, AVATAR_SIZE))
                circle_draw = ImageDraw.Draw(circle_image)
                circle_draw.ellipse((0, 0, AVATAR_SIZE, AVATAR_SIZE), fill=255)
                px = 422
                py = 50
                image.paste(avatar_image, (px, py), circle_image)
                buffer = io.BytesIO()
                image.save(buffer, format='PNG')
                buffer.seek(0)

                channel = self.bot.get_channel(905098419264180246)
                await channel.send(f'嗨~<@{member.id}>歡迎來到COZY BOX!\n請先至<#{905060043051901049}>查閱「規則」&點選「身分組」謝謝~', file=File(buffer, 'COZY BOX.png'))
            else:
                pass
                if member.guild.id == 1026156622176849931:
                    IMAGE_WIDTH = 1100
                    IMAGE_HEIGHT = 500

                    image = Image.open('pic/Iiroace.png')
                    draw = ImageDraw.Draw(image)
        
                    text = f'welcome to 伊洛絲的舒適貓窩'
                    font = ImageFont.truetype(r'FFC//HanyiSentyBubbleTea.ttf', 20)
                    text_width, text_height = draw.textsize(text, font=font)
                    x = (IMAGE_WIDTH - text_width)//2
                    y = 350
                    draw.text( (x, y), text, fill=(128,192,192), font=font)

                    text = f'{member}'
                    font = ImageFont.truetype(r'FFC//HanyiSentyBubbleTea.ttf', 40)
                    text_width, text_height = draw.textsize(text, font=font)
                    x = (IMAGE_WIDTH - text_width)//2
                    y = 375
                    draw.text( (x, y), text, fill=(128,192,192), font=font)

                    AVATAR_SIZE = 256
                    avatar_asset = member.avatar.with_size(AVATAR_SIZE).url
                    buffer_avatar = requests.get(str(avatar_asset)).content
                    with open('pic/zimage_name.jpg', 'wb') as handler:
                        handler.write(buffer_avatar)
                    avatar_image = Image.open('pic/zimage_name.jpg')
                    avatar_image = avatar_image.resize((AVATAR_SIZE, AVATAR_SIZE))
                    circle_image = Image.new('L', (AVATAR_SIZE, AVATAR_SIZE))
                    circle_draw = ImageDraw.Draw(circle_image)
                    circle_draw.ellipse((0, 0, AVATAR_SIZE, AVATAR_SIZE), fill=255)
                    px = 422
                    py = 50
                    image.paste(avatar_image, (px, py), circle_image)
                    buffer = io.BytesIO()
                    image.save(buffer, format='PNG')
                    buffer.seek(0)

                    channel = self.bot.get_channel(1026465927082025011)
                    await channel.send(f'🍭 <@{member.id}> 🍭歡迎來到伊洛絲的貓窩💕\n請小魚乾先去 <#{1026466074981576797}> 閱覽守則跟領取身分組喔‼️', file=File(buffer, 'Iiroace.png'))
                else:
                    pass

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 877943603845013524:
            channel = self.bot.get_channel(int(odate['LEC']))
            await channel.send(f'{member} 掰掰~喵~!')
        else:
            pass

    @commands.Cog.listener()
    async def on_message(self, msg):
        if (str(msg.channel.id)) == '905086063595356210':#光-TW
            dele = self.bot.get_channel(895712603886735381)
            await dele.send(f"{msg.content}")
        else:
            pass
            if msg.guild.id == 877943603845013524:
                keyword = ['QQ', 'Qq', 'qQ', 'qq', 'QAQ', '早', 'OHaYoU', '午安', '晚安', '晚上好', '|･ω･｀)', '生日快樂', '可以瑟瑟', '可以色色']
                for key in keyword:
                    if key in msg.content and key in ['QQ', 'Qq', 'qQ', 'qq', 'QAQ'] and msg.author != self.bot.user:
                        msg1000 = ['不哭不哭，ouo給你抱抱!', '再哭就不好看了~所以不要哭哭了~~好嗎?'] 
                        random_msg1 = random.choice(msg1000)
                        await msg.channel.send(f'{random_msg1}')
                        emoji = self.bot.get_emoji(916922650033549375)
                        await msg.add_reaction(emoji)
                    else:
                        pass
                        if key in msg.content and key in ['早', 'OHaYoU'] and msg.author != self.bot.user:
                            emoji = self.bot.get_emoji(916725269652439091)
                            await msg.add_reaction(emoji)
                        else:
                            pass
                            if key in msg.content and key in ['午安'] and msg.author != self.bot.user:
                                emoji = self.bot.get_emoji(916725269652439091)
                                await msg.add_reaction(emoji)
                            else:
                                pass
                                if key in msg.content and key in ['晚安'] and msg.author != self.bot.user:
                                    emoji = self.bot.get_emoji(916725269652439091)
                                    await msg.add_reaction(emoji)
                                else:
                                    pass
                                    if key in msg.content and key in ['晚上好'] and msg.author != self.bot.user:
                                        emoji = self.bot.get_emoji(916725269652439091)
                                        await msg.add_reaction(emoji)
                                    else:
                                        pass
                                        if key in msg.content and key in ['|･ω･｀)'] and msg.author != self.bot.user:
                                            emoji = self.bot.get_emoji(891609550258597918)
                                            await msg.add_reaction(emoji)
                                        else:
                                            pass
                                            if key in msg.content and key in ['生日快樂'] and msg.author != self.bot.user:
                                                await msg.channel.send(f'生日快樂喵!!!🎂')
                                                emoji = self.bot.get_emoji(879747304687538236)
                                                await msg.add_reaction(emoji)
                                            else:
                                                pass
                                                if key in msg.content and key in ['可以瑟瑟', '可以色色'] and '不可以' not in msg.content and msg.author != self.bot.user:
                                                    emoji = self.bot.get_emoji(917006288540553236)
                                                    await msg.add_reaction(emoji)
                                                else:
                                                    pass
                                                    if (str(msg.author.id)) == '761967543698980866':
                                                        emoji = self.bot.get_emoji(906203695191040030)
                                                        await msg.add_reaction(emoji)
                                                    else:
                                                        pass
            else:
                pass
                if 'https' in msg.content or 'http' in msg.content:
                    if (str(msg.channel.id)) == '905086555885035561':#光-YT
                        if msg.author == self.bot.user and 'twitch' in msg.content:
                            pass
                        else:
                            dele1 = self.bot.get_channel(905064079998193664)
                            dele2 = self.bot.get_channel(878218144966115338)
                            await dele1.send(f"@everyone 陽光-Nikko Sun開台啦!! 還不趕快去看!! 順便按個喜歡啦QWQ 拜託拜託➲\n{msg.content}")
                            await dele2.send(f"@everyone 陽光-Nikko Sun開台啦!! 還不趕快去看!! 順便按個喜歡啦QWQ 拜託拜託➲\n{msg.content}")
                    else:
                        pass
                        if (str(msg.channel.id)) == '905086603486167080' and (str(msg.author.id)) != '832731781231804447':#weedy
                            if msg.author == self.bot.user and 'twitch' in msg.content:
                                pass
                            else:
                                dele1 = self.bot.get_channel(905064079998193664)
                                await dele1.send(f"@everyone Weedy開台啦!! 還不趕快去看!! 順便按個喜歡啦QWQ 拜託拜託➲\n{msg.content}")
                        else:
                            pass
                            if (str(msg.channel.id)) == '905086581440933899':#千
                                if msg.author == self.bot.user and 'twitch' in msg.content:
                                    pass
                                else:
                                    dele1 = self.bot.get_channel(905064079998193664)
                                    await dele1.send(f"@everyone 千祈NOROI開台啦!! 還不趕快去看!! 順便按個喜歡啦QWQ 拜託拜託➲\n{msg.content}")
                            else:
                                pass
                                if (str(msg.channel.id)) == '905086711229464646':#修
                                    if msg.author == self.bot.user and 'twitch' in msg.content:
                                        pass
                                    else:
                                        dele1 = self.bot.get_channel(905064079998193664)
                                        await dele1.send(f"@everyone 修白開台啦!! 還不趕快去看!! 順便按個喜歡啦QWQ 拜託拜託➲\n{msg.content}")
                                else:
                                    pass
                                    if (str(msg.channel.id)) == '905086655357136946':#蕾
                                        if msg.author == self.bot.user and 'twitch' in msg.content:
                                            pass
                                        else:
                                            dele1 = self.bot.get_channel(905064079998193664)
                                            await dele1.send(f"@everyone 糜蕾MayLay開台啦!! 還不趕快去看!! 順便按個喜歡啦QWQ 拜託拜託➲\n{msg.content}")
                                    else:
                                        pass
                                        if (str(msg.channel.id)) == '905086675624013854':#布
                                            if msg.author == self.bot.user and 'twitch' in msg.content:
                                                pass
                                            else:
                                                dele1 = self.bot.get_channel(905064079998193664)
                                                await dele1.send(f"@everyone 布波BUBO開台啦!! 還不趕快去看!! 順便按個喜歡啦QWQ 拜託拜託➲\n{msg.content}")
                                        else:
                                            pass
                                            if (str(msg.channel.id)) == '868012004198187039':#聊
                                                if (str(msg.author.id)) == '833717980633628732' or (str(msg.author.id)) == '817536614020546590':#sun
                                                    mid = await msg.reply("你要@誰?", view=sun())
                                                    await asyncio.sleep(15)
                                                    await mid.delete()
                                                elif (str(msg.author.id)) == '761967543698980866' or (str(msg.author.id)) == '775227252685144074':#yu
                                                    mid = await msg.reply("你要@誰?", view=yu())
                                                    await asyncio.sleep(15)
                                                    await mid.delete()
                                                elif (str(msg.author.id)) == '843145173407760435':#ni
                                                    mid = await msg.reply("你要@誰?", view=ni())
                                                    await asyncio.sleep(15)
                                                    await mid.delete()
                                                else:
                                                    pass
                                            else:
                                                pass

                else:
                    pass

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        if data.message_id == 906184455398502450:
            if str(data.emoji) == '<:MilkTea:880913435821473802>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(877945582344355850)
                await data.member.add_roles(role)
            else:
                pass
                if str(data.emoji) == '<:Danger:884457729312309309>':
                    guild = self.bot.get_guild(data.guild_id)
                    role = guild.get_role(880329480659427340)
                    await data.member.add_roles(role)
                else:
                    pass
        else:
            pass
            if data.message_id == 905077422368641044:
                if str(data.emoji) == '<:VtuberBox:905083426695180288>':
                    guild = self.bot.get_guild(data.guild_id)
                    role = guild.get_role(905078388518174760)
                    await data.member.add_roles(role)
                else:
                    pass
                    if str(data.emoji) == '<:OnlyBox:905083426741301289>':
                        guild = self.bot.get_guild(data.guild_id)
                        role = guild.get_role(905078581707825244)
                        await data.member.add_roles(role)
                    else:
                        pass
                        if str(data.emoji) == '<:BabyBox:905083426581909575>':
                            guild = self.bot.get_guild(data.guild_id)
                            role = guild.get_role(905078468981710918)
                            await data.member.add_roles(role)
                        else:
                            pass
            else:
                pass
                if data.message_id == 1026550147615830047:
                    if str(data.emoji) == '<:big1:1030498913628733541>':
                        guild = self.bot.get_guild(data.guild_id)
                        role = guild.get_role(1028342888674889918)
                        await data.member.add_roles(role)
                    else:
                        pass
                        if str(data.emoji) == '<:small1:1030499311420723310>':
                            guild = self.bot.get_guild(data.guild_id)
                            role = guild.get_role(1028343071592677517)
                            await data.member.add_roles(role)
                        else:
                            pass
                            if str(data.emoji) == '<:vt1:1030499313824043060>':
                                guild = self.bot.get_guild(data.guild_id)
                                role = guild.get_role(1028342888674889918)
                                await data.member.add_roles(role)
                                channel = self.bot.get_channel(1030514307361947678)
                                await channel.send(f"{data.member.name} 按下了VT身分組!")
                            else:
                                pass
                else:
                    pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        if data.message_id == 906184455398502450:
            if str(data.emoji) == '<:MilkTea:880913435821473802>':
                guild = self.bot.get_guild(data.guild_id)
                user = await guild.fetch_member(data.user_id)
                role = guild.get_role(877945582344355850)
                await user.remove_roles(role)
            else:
                pass
                if str(data.emoji) == '<:Danger:884457729312309309>':
                    guild = self.bot.get_guild(data.guild_id)
                    user = await guild.fetch_member(data.user_id)
                    role = guild.get_role(880329480659427340)
                    await user.remove_roles(role)
                else:
                    pass
        else:
            pass
            if data.message_id == 905077422368641044:
                if str(data.emoji) == '<:VtuberBox:905083426695180288>':
                    guild = self.bot.get_guild(data.guild_id)
                    user = await guild.fetch_member(data.user_id)
                    role = guild.get_role(905078388518174760)
                    await user.remove_roles(role)
                else:
                    pass
                    if str(data.emoji) == '<:OnlyBox:905083426741301289>':
                        guild = self.bot.get_guild(data.guild_id)
                        user = await guild.fetch_member(data.user_id)
                        role = guild.get_role(905078581707825244)
                        await user.remove_roles(role)
                    else:
                        pass
                        if str(data.emoji) == '<:BabyBox:905083426581909575>':
                            guild = self.bot.get_guild(data.guild_id)
                            user = await guild.fetch_member(data.user_id)
                            role = guild.get_role(905078468981710918)
                            await user.remove_roles(role)
                        else:
                            pass
            else:
                pass
                if data.message_id == 1026550147615830047:
                    if str(data.emoji) == '<:big1:1030498913628733541>':
                        guild = self.bot.get_guild(data.guild_id)
                        user = await guild.fetch_member(data.user_id)
                        role = guild.get_role(1028342888674889918)
                        await user.remove_roles(role)
                    else:
                        pass
                        if str(data.emoji) == '<:small1:1030499311420723310>':
                            guild = self.bot.get_guild(data.guild_id)
                            user = await guild.fetch_member(data.user_id)
                            role = guild.get_role(1028343071592677517)
                            await user.remove_roles(role)
                        else:
                            pass
                            if str(data.emoji) == '<:vt1:1030499313824043060>':
                                guild = self.bot.get_guild(data.guild_id)
                                user = await guild.fetch_member(data.user_id)
                                role = guild.get_role(1028343189087715339)
                                await user.remove_roles(role)
                            else:
                                pass
                else:
                    pass

    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        if msg.guild.id == 877943603845013524:
            dele = self.bot.get_channel(915871311883018250)
            try:
                attachment = msg.attachments[0]
                await dele.send(f"```fix\n{msg.author}/{msg.channel}\n```\n{msg.content}\n{attachment.url}")
            except:
                await dele.send(f"```fix\n{msg.author}/{msg.channel}\n```\n{msg.content}")
        else:
            pass
            if msg.guild.id == 905057576411078706:
                if msg.author != self.bot.user and (str(msg.channel.id)) != '987785654685532190':
                    dele = self.bot.get_channel(915871364450242560)
                    try:
                        attachment = msg.attachments[0]
                        await dele.send(f"```fix\n{msg.author}/{msg.channel}\n```\n{msg.content}\n{attachment.url}")
                    except:
                        await dele.send(f"```fix\n{msg.author}/{msg.channel}\n```\n{msg.content}")
                else:
                    pass
            else:
                pass

def setup(bot):
    bot.add_cog(Main(bot))
