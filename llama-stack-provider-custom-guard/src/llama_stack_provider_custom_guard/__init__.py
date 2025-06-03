from typing import Any

from .config import CustomGuardConfig

async def get_provider_impl(config: CustomGuardConfig, deps: dict[str, Any]):
    from .custom_guard import CustomGuardSafetyImpl

    impl = CustomGuardSafetyImpl(config, deps)
    await impl.initialize()
    return impl
