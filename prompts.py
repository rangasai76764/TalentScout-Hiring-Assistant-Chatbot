# prompts.py

# Greeting and flow control
GREETING_PROMPT = (
    "👋 Hello! I’m the Hiring Assistant. "
    "I’ll collect a few details and then generate tailored technical questions based on your tech stack. Let's start!"
)

EXIT_KEYWORDS = ["exit", "bye", "quit", "goodbye"]

THANK_YOU_PROMPT = (
    "✅ Thank you for your time. We'll review your submission and contact you with next steps."
)

FALLBACK_PROMPT = "⚠️ Sorry, I didn't quite understand that. Could you rephrase?"

# Candidate detail prompts (keys aligned with chatbot.py)
DETAIL_PROMPTS = {
    "full_name": "Please provide your Full Name.",
    "email": "Please provide your Email.",
    "phone": "Please provide your Phone Number (with country code, e.g. +91 9876543210).",
    "years_experience": "Please provide your Years of Experience.",
    "desired_position": "Please provide your Desired Position(s).",
    "current_location": "Please provide your Current Location.",
    "tech_stack": (
        "✅ All set. Please now provide your Tech Stack (comma-separated): "
        "languages, frameworks, databases, tools."
    ),
}
