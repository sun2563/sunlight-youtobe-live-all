import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
from discord import File
from PIL import Image, ImageDraw, ImageFont
import io, asyncio
import requests
from discord import guild_only

# with open('URL.json', mode='r', encoding='utf8') as jfile:
#     url = json.load(jfile)

# json6 = requests.get(url['odate'])
# odate = json6.json()

class ouo(Cog_Extension):

    @commands.command()
    @guild_only()
    async def 名片(self, ctx, text=None):
        if ctx.guild.id == 877943603845013524:
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

            text = f'{ctx.author.name}'
            font = ImageFont.truetype(r'FFC//中明體.ttc', 40)
            text_width, text_height = draw.textsize(text, font=font)
            x = (IMAGE_WIDTH - text_width)//2
            y = 350
            draw.text( (x, y), text, fill=(0,0,0), font=font)

            AVATAR_SIZE = 256
            ct = ctx.author
            avatar_asset = ct.avatar.with_size(AVATAR_SIZE).url
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

            await ctx.send(f'給~<@{ctx.author.id}>', file=File(buffer, 'SunLight_OuO.png'))
        else:
            pass

    @commands.command()
    @guild_only()
    async def 決鬥(self, ctx, user: discord.User):
        if ctx.guild.id == 877943603845013524:
            msg102 = [f'<@{ctx.author.id}>獲勝', f'<@{user.id}>獲勝']
            random_msg3 = random.choice(msg102)
            await ctx.send({random_msg3})
        else:
            pass

    @commands.command()
    @guild_only()
    async def ouo吃(self, ctx, *, msg):
        if ctx.guild.id == 877943603845013524:
            await ctx.send(f'謝謝<@{ctx.author.id}>給的 {msg} !!好吃~喵!!')
        else:
            pass

    @commands.command()
    @guild_only()
    async def ouo選(self, ctx, msg1, msg2):
        if ctx.guild.id == 877943603845013524:
            msg100 = [msg1, msg2]
            random_msg = random.choice(msg100)
            await ctx.send(f'<@{ctx.author.id}>~我選擇 {random_msg} !!喵~')
        else:
            pass

    @commands.command()
    @guild_only()
    async def ouo是不是(self, ctx, msg10, msg11):
        if ctx.guild.id == 877943603845013524:
            msg101 = ['是', '可能是', '可能不是', '不是']
            random_msg2 = random.choice(msg101)
            await ctx.send(f'<@{ctx.author.id}>~emmm... {msg10} {random_msg2} {msg11} !喵~')
        else:
            pass

    @commands.command()
    @guild_only()
    async def ouo誰是(self, ctx, *, msg):
        if ctx.guild.id == 877943603845013524:
            if msg != '最美麗的人':
                if msg != '世界上最美麗的人':
                    if msg != '最美的人':
                        if msg != '世界上最美的人':
                            if msg != '最美丽的人':
                                if msg != '世界上最美丽的人':
                                    if msg != '最美的人':
                                        if msg != '世界上最美的人':
                                            if msg != '最美麗的女人':
                                                if msg != '世界上最美麗的女人':
                                                    if msg != '最美的女人':
                                                        if msg != '世界上最美的女人':
                                                            if msg != '最美丽的女人':
                                                                if msg != '世界上最美丽的女人':
                                                                    if msg != '最美的女人':
                                                                        if msg != '世界上最美的女人':
                                                                            if msg != '最漂亮的人':
                                                                                if msg != '世界上最漂亮的人':
                                                                                    if msg != '最漂亮的女人':
                                                                                        if msg != '世界上最漂亮的女人':
                                                                                            if msg != '姐姐':
                                                                                                if msg != '姊姊':
                                                                                                    if msg != '陽光':
                                                                                                        if msg != '陽光姐姐':
                                                                                                            if msg != '陽光姊姊':
                                                                                                                if msg != '阳光':
                                                                                                                    if msg != '阳光姐姐':
                                                                                                                        if msg != '阳光姊姊':    
                                                                                                                            await ctx.send(f'<@{ctx.author.id}>是 {msg} !喵~!!')
                                                                                                                        else:
                                                                                                                            await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                                                                    else:
                                                                                                                        await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                                                                else:
                                                                                                                    await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                                                            else:
                                                                                                                await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                                                        else:
                                                                                                            await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                                                    else:
                                                                                                        await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                                                else:
                                                                                                    await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                                            else:
                                                                                                await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                                        else:
                                                                                            await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                                    else:
                                                                                        await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                                else:
                                                                                    await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                            else:
                                                                                await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                        else:
                                                                            await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                    else:
                                                                        await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                                else:
                                                                    await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                            else:
                                                                await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                        else:
                                                            await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                    else:
                                                        await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                                else:
                                                    await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                            else:
                                                await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                        else:
                                           await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                    else:
                                        await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                                else:
                                    await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                            else:
                                await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                        else:
                            await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                    else:
                        await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
                else:
                    await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
            else:
                await ctx.send(f'<@{ctx.author.id}>~當然是陽光姐姐是 {msg} 啦~喵~! ')
        else:
            pass

def setup(bot):
    bot.add_cog(ouo(bot))
