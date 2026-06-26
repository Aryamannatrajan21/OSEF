
from osef.contracts.models import OSEFModel


def test_osef_model_instantiation():
    model = OSEFModel()
    assert model is not None
    assert model.model_dump() == {}
