from utils.groq_client import ask_llm

def judge_agent(pitch, questions, answers):
    return ask_llm(
        """
        You are a Shark Tank judge.

        Review:
        1. The startup pitch
        2. The investor's questions
        3. The founder's answers

        Decide whether the startup deserves funding.

        Return exactly in this format:

        Decision: INVEST or PASS
        Amount: <amount>
        Equity: <percentage>
        Reason: <2-3 sentence explanation>

        Be critical and realistic. Do not always invest.
        """,
        f"""
        Startup Pitch:
        {pitch}

        Investor Questions:
        {questions}

        Founder Answers:
        {answers}
        """
    )
