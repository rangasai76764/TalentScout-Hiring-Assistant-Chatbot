# Prompt Engineering Strategy

## Goals
- Collect candidate details reliably.
- Generate focused technical questions by tech stack.
- Keep conversation on-task and gracefully end.

## Prompts & Behavior
- **Greeting**: friendly intro and immediate prompt for Full Name.
- **Collection**: sequential prompts for fields (Full Name → Email → Phone → Years → Position → Location → Tech Stack).
- **Tech stack**: request comma-separated list of techs.
- **Question generation**: deterministic mapping from tech → candidate questions.
- **Fallback**: short reply prompting rephrase or next step.

## Notes
- Keep prompts concise and specific.
- Validate emails and phone numbers at point of entry.
- Optional: integrate LLM (OpenAI GPT) for more dynamic question generation.
