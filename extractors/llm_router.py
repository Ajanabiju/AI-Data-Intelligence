import time
import random

MODEL_CHAIN = [
    "gemini",
    "groq",
    "deepseek"
]

def get_next_provider(current):

    try:
        idx = MODEL_CHAIN.index(current)
        return MODEL_CHAIN[idx + 1]

    except:
        return None


def call_provider(provider, text):

    if provider == "gemini":
        return {"provider": "gemini"}

    if provider == "groq":
        return {"provider": "groq"}

    if provider == "deepseek":
        return {"provider": "deepseek"}

    raise Exception("No provider")


def route_request(text):

    provider = MODEL_CHAIN[0]

    while provider:

        try:

            print(f"Trying {provider}")

            result = call_provider(
                provider,
                text
            )

            return result

        except Exception as e:

            print(f"Error: {e}")

            wait = random.uniform(1, 3)

            time.sleep(wait)

            provider = get_next_provider(provider)

    return None