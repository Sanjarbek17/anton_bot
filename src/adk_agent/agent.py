# src/adk_agent/agent.py
import google.generativeai as genai
from config.settings import settings

class GoogleADKAgent:
    def __init__(self):
        print("Google ADK Agent initialized.")
        if not settings.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set in environment variables or config/settings.py")

        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        print("Gemini model configured.")

    def process_message(self, message):
        """
        Processes a message using the Google Gemini API.
        """
        try:
            print(f"Sending to Gemini: {message}")
            response = self.model.generate_content(message)
            response_text = response.text
            print(f"Received from Gemini: {response_text}")
            return response_text
        except Exception as e:
            print(f"Error processing message with Gemini: {e}")
            return "Sorry, I'm having trouble connecting to the AI at the moment."

if __name__ == '__main__':
    # This block will now require a valid GEMINI_API_KEY in .env or config/settings.py
    # for testing purposes.
    try:
        agent = GoogleADKAgent()
        agent.process_message("Hello from test agent!")
    except ValueError as e:
        print(f"Test agent initialization failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during test agent execution: {e}")
