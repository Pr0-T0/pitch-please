from utils.groq_client import ask_llm

def shark_agent(pitch):
    return ask_llm(
        """
        You are a tough Shark Tank investor.
        Ask 3 challenging questions abut the startup.
        Keep them short.
        """,
        pitch
    )
