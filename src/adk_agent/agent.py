from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

root_agent = Agent(
    model='gemini-3-flash-preview',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)

app_name = "Weather bot"
user_id = 'sanjarbek'
session_id = 'v1'

session_service = InMemorySessionService()

runner = Runner(
    app_name=app_name,
    agent=root_agent,
    session_service=session_service,
)

session = session_service.create_session_sync(
    app_name=app_name,
    user_id=user_id,
)

while True:
    user_message = input("enter message: ")
    msg_content = types.Content(
        role="user",
        parts=[types.Part(text=user_message)]
    )

    response = runner.run(
        user_id=user_id,
        session_id=session.id,
        new_message=msg_content,
    )

    for event in response:
        print(event.content.parts[0].text)
