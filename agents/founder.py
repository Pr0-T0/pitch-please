from utils.groq_client import ask_llm

def founder_agent(idea):
    return ask_llm(
        """
        You are a startup founder on Shark Tank.
        Create a concise startup pitch.
        Mention:
        - Problem
        - Solution
        - Revenue model
        - Funding requested
        """,
        idea
    )
def founder_reply_agent(pitch, questions):
    return ask_llm(
    """
    You are the founder of this startup.
    Answer the investor's questions confidently.
    Keep answers realistic and concise.
    """,
    f"""
    Startup Pitch:{pitch}
    Investor Questions:{questions}
    """
    )
