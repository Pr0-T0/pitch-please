import time
import gradio as gr

from agents.founder import founder_agent, founder_reply_agent
from agents.shark import shark_agent
from agents.judge import judge_agent


def run_pitch(idea):

    messages = []

    # Founder Thinking
    messages.append({
        "role": "assistant",
        "content": "Founder is preparing the pitch..."
    })
    yield messages

    pitch = founder_agent(idea)

    time.sleep(1)

    messages[-1] = {
        "role": "assistant",
        "content": f"""
## Founder

{pitch}

---
"""
    }
    yield messages

    # Shark Thinking
    messages.append({
        "role": "assistant",
        "content": "Shark is analyzing the pitch..."
    })
    yield messages

    questions = shark_agent(pitch)

    time.sleep(1)

    messages[-1] = {
        "role": "assistant",
        "content": f"""
## Shark

{questions}

---
"""
    }
    yield messages

    # Founder Reply Thinking
    messages.append({
        "role": "assistant",
        "content": "Founder is answering the questions..."
    })
    yield messages

    answers = founder_reply_agent(
        pitch,
        questions
    )

    time.sleep(1)

    messages[-1] = {
        "role": "assistant",
        "content": f"""
## Founder Response

{answers}

---
"""
    }
    yield messages

    # Judge Thinking
    messages.append({
        "role": "assistant",
        "content": "⚖️ Judge is evaluating the startup..."
    })
    yield messages

    decision = judge_agent(
        pitch,
        questions,
        answers
    )

    time.sleep(1)

    messages[-1] = {
        "role": "assistant",
        "content": f"""
# Final Verdict

{decision}
"""
    }
    yield messages


with gr.Blocks(
    title="Pitch Please",
) as demo:

    gr.Markdown(
        """
        # Pitch Please

        Pitch your startup idea to an AI Shark Tank.
        Watch the Founder, Shark, and Judge debate your idea.
        """
    )

    with gr.Row():
        idea = gr.Textbox(
            label="Startup Idea",
            placeholder="Edible headphones",
            scale=4
        )

        start_btn = gr.Button(
            "Start Pitch",
            variant="primary",
            scale=1
        )

    chat = gr.Chatbot(
        height=700,
    )

    start_btn.click(
        fn=run_pitch,
        inputs=idea,
        outputs=chat
    )

demo.launch()
