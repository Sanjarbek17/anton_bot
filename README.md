# Anton Bot: Google ADK and Telethon Integration

This project aims to integrate a Google ADK (Agent Development Kit) agent with a Telethon-based Telegram bot. The goal is to allow the Telegram bot to forward messages to the ADK agent for processing and respond with the agent's output.

## Project Structure

- `src/adk_agent/`: Contains the logic for the Google ADK agent integration.
  - `agent.py`: Placeholder for the ADK agent class.
- `src/telethon_bot/`: Contains the logic for the Telethon Telegram bot.
  - `bot.py`: Placeholder for the Telethon bot class.
- `src/main.py`: The entry point of the application, responsible for initializing and connecting the bot and agent.
- `config/`: Stores configuration files.
  - `settings.py`: Contains placeholder for API keys and other settings (can be overridden by environment variables).
- `data/`: For any data the bot might need to store.
- `scripts/`: For utility scripts.
- `tests/`: For unit and integration tests.
- `.env`: Used to store environment variables (e.g., API keys). This file is ignored by Git.
- `requirements.txt`: Lists Python dependencies.
- `README.md`: Project documentation.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd anton_bot
    ```

2.  **Create a Python Virtual Environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Credentials:**

    You need to set up credentials for both Telegram (Telethon) and Google ADK (Dialogflow).

    *   **Telegram (Telethon):**
        1.  Go to [my.telegram.org/apps](https://my.telegram.org/apps) and log in with your Telegram account.
        2.  Click on "API development tools" and create a new application.
        3.  Note down your `App api_id` and `App api_hash`.

    *   **Google ADK (Dialogflow):**
        1.  Create a Google Cloud Project and enable the Dialogflow API.
        2.  Create a service account key and download it as a JSON file. This file will be your `credentials.json`.
        3.  Note down your Google Cloud `Project ID`.

    **Update `.env` file:**
    Rename `.env.example` to `.env` (if it existed, in this case, it was created) and fill in your credentials:

    ```ini
    # .env
    TELEGRAM_API_ID=YOUR_TELEGRAM_API_ID
    TELEGRAM_API_HASH=YOUR_TELEGRAM_API_HASH
    GOOGLE_PROJECT_ID=YOUR_GOOGLE_PROJECT_ID
    GOOGLE_APPLICATION_CREDENTIALS_PATH=path/to/your/google_credentials.json
    ```

    Alternatively, you can update `config/settings.py` directly, but using `.env` is recommended for security and flexibility.

## Running the Bot

To start the integrated bot:

```bash
python src/main.py
```

The first time you run the Telethon bot, it will ask for your phone number and a verification code to authorize the session.

## Next Steps

- Implement the actual Google ADK (Dialogflow) integration in `src/adk_agent/agent.py`.
- Enhance the Telethon bot's functionality in `src/telethon_bot/bot.py`.
- Add proper logging and error handling.
- Write unit and integration tests in the `tests/` directory.
