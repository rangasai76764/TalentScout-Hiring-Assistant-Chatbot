import json
from chatbot import HiringAssistantChatbot
from utils.context_manager import ContextManager
from data_handler import DataHandler


def test_greeting_and_flow(tmp_path):
    data_file = tmp_path / "test_data.json"
    dh = DataHandler(str(data_file))
    bot = HiringAssistantChatbot()
    ctx = ContextManager()

    # Greeting
    r1 = bot.process_message("hi", ctx, dh)
    assert "hello" in r1.lower() or "hiring assistant" in r1.lower()

    # Provide name
    r2 = bot.process_message("John Doe", ctx, dh)
    assert "recorded" in r2.lower() or "please provide" in r2.lower()

    # Provide invalid email -> expect validation message
    r_invalid = bot.process_message("not-an-email", ctx, dh)
    assert "valid email" in r_invalid.lower()

    r3 = bot.process_message("john@example.com", ctx, dh)
    assert "recorded" in r3.lower()

    # Provide phone
    r4 = bot.process_message("+1234567890", ctx, dh)
    assert "recorded" in r4.lower()

    # Fill remaining fields quickly
    bot.process_message("3", ctx, dh)  # years
    bot.process_message("Software Engineer", ctx, dh)
    r_tech = bot.process_message("Singapore", ctx, dh)
    assert "tech stack" in r_tech.lower()

    # Provide tech stack
    r_q = bot.process_message("Python, Django", ctx, dh)
    assert "technical questions" in r_q.lower()

    # Data file should exist with at least one entry
    with open(str(data_file), "r") as f:
        data = json.load(f)
    assert len(data) >= 1
