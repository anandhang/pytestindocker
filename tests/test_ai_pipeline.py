import pytest
import numpy as np

@pytest.fixture
def sample_data():
    return np.array([1,2,3])

def preprocess(data):
    return data * 2

def test_preprocessing(sample_data):
    processed = preprocess(sample_data)
    assert all(processed == np.array([2,4,6]))