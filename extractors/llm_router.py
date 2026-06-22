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


def route_request():

    provider = "gemini"

    print(f"Trying {provider}")

    print("429 received")

    provider = get_next_provider(provider)

    print(f"Switching to {provider}")

    print("413 received")

    provider = get_next_provider(provider)

    print(f"Switching to {provider}")

    print("Success")