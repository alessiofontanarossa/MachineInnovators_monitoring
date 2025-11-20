import pytest
import numpy as np
from src.model import get_pipeline, get_label_predictions

############### PREPARATION PART ###############

@pytest.fixture(scope = "module") # needed to execute my_pipeline a single 
                                  # time for the whole test session
def my_pipeline(): 
    return get_pipeline()

@pytest.fixture
def conversion_func():
    label_to_int = {'negative': 0, 'neutral': 1, 'positive': 2}
    return np.vectorize(label_to_int.get)

############### TEST PART ###############

def test_get_pipeline(my_pipeline):
    assert my_pipeline is not None
    assert my_pipeline.task == "text-classification"
    # assert my_pipeline.model: leave freedom of changing model

def test_get_label_predictions(my_pipeline, conversion_func):
  # now define three sentences with a very clear sentiment
  test_sentences = ["I hate this", "I am neutral.", "I love this."]
  expected_output = [0, 1, 2]
  predictions = get_label_predictions(my_pipeline, conversion_func, test_sentences).tolist()
  assert predictions == expected_output