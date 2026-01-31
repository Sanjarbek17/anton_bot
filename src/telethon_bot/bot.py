# src/telethon_bot/bot.py
from telethon import TelegramClient, events
import asyncio


from src.adk_agent.agent import process_answer
from config.settings import settings

class TelethonBot:
    def __init__(self, api_id, api_hash, session_name='telethon_session'):
        self.client = TelegramClient(session_name, api_id, api_hash)
        self.agent = None # To be set by main.py
        print("Telethon Bot initialized.")

    async def start(self):
        print("Starting Telethon Bot...")
        await self.client.start()
        print("Telethon Bot started.")
        await self.client.run_until_disconnected()

    async def send_message(self, entity, message):
        await self.client.send_message(entity, message)

    def register_message_handler(self):
        @self.client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
        async def handler(event):
            sender = await event.get_sender()
            print(f"[{sender.username or sender.id}] {event.text}")

            adk_response = process_answer(event.text)
            if adk_response:
                await self.client.send_message(event.chat_id, adk_response)
            else:
                await self.client.send_message(event.chat_id, "Idk")

    async def stop(self):
        await self.client.disconnect()
        print("Telethon Bot stopped.")

if __name__ == '__main__':
    # Placeholder for running bot directly (requires API_ID and API_HASH)
    # You would typically get these from environment variables or a config file
    # from dotenv import load_dotenv
    # load_dotenv()
    API_ID = settings.TELEGRAM_API_ID
    API_HASH = settings.TELEGRAM_API_HASH


    if not API_ID or not API_HASH:
        print("Please set TELEGRAM_API_ID and TELEGRAM_API_HASH environment variables.")
    else:
        bot = TelethonBot(int(API_ID), API_HASH)
        bot.register_message_handler()
        asyncio.run(bot.start())
    print("Telethon Bot placeholder. Run via main.py")
