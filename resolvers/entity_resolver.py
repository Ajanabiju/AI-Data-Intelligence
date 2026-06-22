KNOWN_ENTITIES = {
    "open ai": "OpenAI",
    "openai": "OpenAI",
    "openai inc": "OpenAI",
    "openai, inc.": "OpenAI",

    "anthropic": "Anthropic",
    "anthropic ai": "Anthropic",

    "google deepmind": "Google DeepMind",
    "deepmind": "Google DeepMind",

    "meta ai": "Meta AI",
    "meta": "Meta AI",

    "x ai": "xAI",
    "xai": "xAI",

    "mistral ai": "Mistral AI",
    "mistral": "Mistral AI"
}

def normalize(text):
    return (
        text.lower()
        .replace(",", "")
        .replace(".", "")
        .strip()
    )

def resolve_entity(name):

    key = normalize(name)

    return KNOWN_ENTITIES.get(
        key,
        name
    )