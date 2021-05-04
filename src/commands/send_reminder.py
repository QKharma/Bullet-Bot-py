import discord
import schedule
import time
import threading

class SendReminder:

    alias = ['send-reminder']

    def __init__(self, bot_client):
        self.bot_client = bot_client
        self.schedstop = None
        self.schedthread = None

    def create_schedule_tread(self):
        self.schedstop = threading.Event()

        def timer():
            while not self.schedstop.is_set():
                schedule.run_pending()
                time.sleep(3)

        self.schedthread = threading.Thread(target=timer)
        self.schedthread.start()

    def close_schedule_thread(self):
        self.schedstop.set()

    async def reminder(self, user):

        if not user.dm_channel:
            await user.create_dm()

        await user.dm_channel.send("blablabla")

    async def execute(self, message, args):

        schedule.every(10).seconds.do(self.call_async, user=message.author)

        while True:
            schedule.run_pending()
            time.sleep(1)
