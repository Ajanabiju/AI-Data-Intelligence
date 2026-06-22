KNOWN_ENTITIES = {
    "open ai": "OpenAI",
    "openai": "OpenAI",
    "openai inc": "OpenAI",
    "anthropic ai": "Anthropic",
    "anthropic": "Anthropic"
}

def resolve_entity(name):

    key = name.lower().strip()

    return KNOWN_ENTITIES.get(
        key,
        name
    )