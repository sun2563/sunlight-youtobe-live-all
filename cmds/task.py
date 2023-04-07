from core.classes import Cog_Extension
import json,asyncio,datetime
import requests

with open('URL.json', mode='r', encoding='utf8') as jfile:
    url = json.load(jfile)

json6 = requests.get(url['odate'])
odate = json6.json()

class task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = 0

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(880390431932825712)
            while not self.bot.is_closed():
                now = datetime.datetime.now().strftime("%H:%M")
                if now == '16:00' and self.counter == 0:
                    odate['people'] = ["1"]
                    requests.put(url['odate'], json=odate)
                    self.bot.reload_extension(f'cmds.slash')
                    await self.channel.send(f'好了~')
                    self.counter = 1
                    await asyncio.sleep(90)
                    self.counter = 0
                else:
                    await asyncio.sleep(1)
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())



def setup(bot):
    bot.add_cog(task(bot))
