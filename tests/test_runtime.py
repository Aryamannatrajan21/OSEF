import pytest
from osef.core.bootstrapper import bootstrap


@pytest.mark.asyncio
async def test_runtime_lifecycle():
    runtime = bootstrap()
    assert not runtime.is_running

    await runtime.start()
    assert runtime.is_running

    await runtime.shutdown()
    assert not runtime.is_running
