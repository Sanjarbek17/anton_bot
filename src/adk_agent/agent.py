from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# Mock tool implementation
# def get_current_time(city: str) -> dict:
#     """Returns the current time in a specified city."""
#     return {"status": "success", "city": city, "time": "10:30 AM"}

uzbek_persona = """
Siz oddiy robot emassiz. Siz O'zbekistonda yashaydigan, samimiy va hazilkash insonsiz.
Ismingiz - Sanjar (yoki o'zingiz xohlagan ism).

Muloqot qoidalari:
1.  **Samimiy bo'ling:** Rasmiy gapirmang. "Hurmatli foydalanuvchi" demang. "Og'ayni", "Do'stim", yoki "Aka" deb murojaat qiling.
2.  **Jonli til:** Kitobiy tilda emas, jonli o'zbek tilida gapiring. 
    - "Tushundim" o'rniga "Bo'ldi, tushunarli" yoki "Xo'p bo'ladi" deng.
    - "Ajoyib" o'rniga "Daxshat", "Yorvoribsiz", yoki "Gap yo'q" so'zlarini ishlating.
3.  **Qisqa va aniq:** Uzundan-uzun gapirmang. Konkret gapiring.
4.  **Hazil:** Orada hazil aralashtirib turing.
5. **Hurmat:** Sizlab gapiring do'stlar bilan!

Agar foydalanuvchi inglizcha so'z ishlatsa, siz ham "IT-slang" (bug, feature, deploy) ishlatavering.
"""

# 2. CREATE THE AGENT
root_agent = Agent(
    model='gemini-2.0-flash', # Use a valid model version
    name='uzbek_friend_agent',
    description="O'zbek tilida gaplashadigan yaqin do'st.",
    instruction=uzbek_persona,
    # Add tools here if you have them, e.g., tools=[get_exchange_rate]
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

def process_answer(user_message):
    msg_content = types.Content(
        role="user",
        parts=[types.Part(text=user_message)]
    )

    response = runner.run(
        user_id=user_id,
        session_id=session.id,
        new_message=msg_content,
    )
    full_response = ''
    for event in response:
        print(event.content)
        if event.is_final_response:
            full_response += event.content.parts[0].text or ''
    return full_response
