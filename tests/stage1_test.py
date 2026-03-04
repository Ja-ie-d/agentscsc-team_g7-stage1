"""
Basic Stage 1 test to verify the agent app imports and can be constructed.

This is a placeholder for the course-provided tests. Replace with the official
version from your starter materials if required.
"""

from src.agent import Agent  # type: ignore[import]
from src.logger import build_logger  # type: ignore[import]
from src.utils import load_yaml, load_text  # type: ignore[import]


def test_agent_can_respond():
    cfg = load_yaml("config/agent.yaml")
    policies = load_yaml("config/policies.yaml")
    logger = build_logger(cfg["logging"]["path"], cfg["logging"]["level"])

    prompts = {
        "system": load_text("prompts/system.md"),
        "style": load_text("prompts/style.md"),
        "refusal": load_text("prompts/refusal.md"),
    }

    agent = Agent(cfg=cfg, policies=policies, prompts=prompts, logger=logger)
    reply = agent.respond("Hello, who are you?")

    assert isinstance(reply, str)
    assert reply.strip() != ""
