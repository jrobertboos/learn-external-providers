from typing import Any

from .config import GrumpyGuardConfig

async def get_provider_impl(config: GrumpyGuardConfig, deps: dict[str, Any]):
    from .grumpy_guard import GrumpyGuardSafetyImpl

    impl = GrumpyGuardSafetyImpl(config, deps)
    await impl.initialize()
    return impl
