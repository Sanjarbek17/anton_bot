# src/main.py
import asyncio
from pydantic import ValidationError

from telethon_bot.bot import TelethonBot
from adk_agent.agent import GoogleADKAgent
from config.settings import settings

async def main():
    try:
        # --- Configuration is loaded automatically by Pydantic ---
        print("Configuration loaded successfully.")
    except ValidationError as e:
        print("Error: Configuration validation failed. Make sure your .env file is correctly set up.")
        print(e)
        return

    # --- Initialize Components ---
    adk_agent = GoogleADKAgent()
    telethon_bot = TelethonBot(settings.TELEGRAM_API_ID, settings.TELEGRAM_API_HASH)

    # Connect bot to agent
    telethon_bot.set_agent(adk_agent)
    telethon_bot.register_message_handler()

    # --- Start Bot ---
    print("Starting bot...")
    try:
        await telethon_bot.start()
    except Exception as e:
        print(f"Error starting bot: {e}")
    finally:
        await telethon_bot.stop()

if __name__ == '__main__':
    asyncio.run(main())
