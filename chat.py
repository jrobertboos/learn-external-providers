import os

import fire
from llama_stack_client import LlamaStackClient
from llama_stack_client.lib.agents.agent import Agent
from llama_stack_client.lib.agents.event_logger import EventLogger
from llama_stack_client.types.agent_create_params import AgentConfig
from termcolor import colored


def main(host: str, port: int):

    client = LlamaStackClient(
        base_url=f"http://{host}:{port}",
    )

    available_models = [
        model.identifier for model in client.models.list() if model.model_type == "llm"
    ]

    if not available_models:
        print(colored("No available models. Exiting.", "red"))
        return
    else:
        selected_model = available_models[0]
        print(f"Using model: {selected_model}")

    client.shields.register(shield_id="grumpy-guard-shield", provider_shield_id="grumpy-guard")

    agent = Agent(
        client=client,
        model=selected_model,
        instructions="You are a helpful assistant.",
        sampling_params={
            "strategy": {"type": "top_p", "temperature": 1.0, "top_p": 0.9},
        },
        tools=[],
        input_shields=["grumpy-guard-shield"],
        output_shields=[],
        enable_session_persistence=False,
    )
    session_id = agent.create_session("test-session")

    while True:
        prompt = input("Enter a prompt: ")
        if not prompt:
            break
        response = agent.create_turn(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            session_id=session_id,
        )

        for log in EventLogger().log(response):
            log.print()


if __name__ == "__main__":
    fire.Fire(main)
