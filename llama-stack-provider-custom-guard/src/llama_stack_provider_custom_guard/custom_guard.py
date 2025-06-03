import logging
from typing import Any

from llama_stack.apis.inference import Message
from llama_stack.apis.safety import (
    RunShieldResponse,
    Safety,
    SafetyViolation,
    ViolationLevel,
)
from llama_stack.apis.shields import Shield
from llama_stack.providers.utils.inference.prompt_adapter import (
    interleaved_content_as_str,
)

from .config import CustomGuardConfig

log = logging.getLogger(__name__)

class CustomGuardSafetyImpl(Safety):
    def __init__(self, config: CustomGuardConfig, deps) -> None:
        self.config = config

    async def initialize(self) -> None:
        pass

    async def shutdown(self) -> None:
        pass

    async def register_shield(self, shield: Shield) -> None:
        pass

    async def run_shield(
        self,
        shield_id: str,
        messages: list[Message],
        params: dict[str, Any] = None,
    ) -> RunShieldResponse:
        violation = SafetyViolation(
            violation_level=(ViolationLevel.ERROR),
            user_message="Sorry, what you are doing is dumb :)",
            metadata={},
        )
        return RunShieldResponse(violation=violation)
