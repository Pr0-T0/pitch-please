from agents.founder import founder_agent, founder_reply_agent
from agents.shark import shark_agent
from agents.judge import judge_agent

idea = input("Startup Idea: ")

print("\n🧑 FOUNDER PITCH\n")

pitch = founder_agent(idea)
print(pitch)

print("\n🦈 SHARK QUESTIONS\n")

questions = shark_agent(pitch)
print(questions)

print("\n🧑 FOUNDER RESPONSES\n")

answers = founder_reply_agent(
    pitch,
    questions
)
print(answers)

print("\n⚖️ FINAL VERDICT\n")

decision = judge_agent(
    pitch,
    questions,
    answers
)
print(decision)
