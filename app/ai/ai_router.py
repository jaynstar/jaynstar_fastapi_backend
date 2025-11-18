from app.ai.providers import (
    groq_provider,
    hf_provider,
    gemini_provider,
    openai_provider,
)

# Provider priority order
PROVIDERS = [
    groq_provider,      # free + fast
    hf_provider,        # free
    gemini_provider,    # free
    openai_provider,    # paid / quota limited
]


def generate_resume_smart(details: str) -> str:
    """
    Try each provider in order.
    Skip providers with no API key.
    Collect errors and raise if all fail.
    """
    errors = []

    for provider in PROVIDERS:
        name = provider.PROVIDER_NAME

        try:
            # Skip if no API key
            if not provider.is_available():
                print(f"Skipping provider (no key): {name}")
                continue

            print(f"Trying provider: {name}")

            result = provider.generate_resume(details)

            print(f"Provider succeeded: {name}")
            return result

        except Exception as e:
            print(f"AI Provider failed: {name} -> {e}")
            errors.append(f"{name}: {e}")

    # If we reach here, all failed
    raise Exception("All AI providers failed: " + " | ".join(errors))
