import pytest

@pytest.mark.integartion
def test_service_interaction():
    service_a_output = {"value": 10}
    service_b_output = service_a_output["value"] * 2
    assert service_b_output == 20
