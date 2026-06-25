import pytest
from osef.core.container import Container
from osef.contracts.exceptions import ConfigurationError

class DummyInterface:
    pass

class DummyImplementation(DummyInterface):
    pass

def test_container_singleton():
    container = Container()
    impl = DummyImplementation()
    container.register_singleton(DummyInterface, impl)
    
    resolved = container.resolve(DummyInterface)
    assert resolved is impl

def test_container_factory():
    container = Container()
    container.register_factory(DummyInterface, lambda: DummyImplementation())
    
    resolved1 = container.resolve(DummyInterface)
    resolved2 = container.resolve(DummyInterface)
    
    # Assert factory lazy resolves to singleton
    assert isinstance(resolved1, DummyImplementation)
    assert resolved1 is resolved2

def test_container_unregistered():
    container = Container()
    with pytest.raises(ConfigurationError):
        container.resolve(DummyInterface)
