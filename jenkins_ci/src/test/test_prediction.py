import pytest
import pathlib
import sys
PACKAGE_ROOT = sys.path.append('/media/danlof/dan_files/data_science_codes/udemy_course/jenkins_ci/src/prediction_model')

from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_predictions

# 3 tests that we will be writting to test this script
# output from predict script is not null
# output from predict script is of string type
# the output is Y for an example data 

@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[:1]
    result = generate_predictions(single_row)
    return result

# we start checking that predict script is not null
def test_single_pred_not_none(single_prediction):
    assert single_prediction is not None

# test 2: predict script is of type string

def test_single_str_type(single_prediction):
    assert isinstance(single_prediction.get('prediction')[0],str)

# test 3 : check the output is y
def test_single_pred_validate(single_prediction):
    assert single_prediction.get('prediction')[0] == 'Y'
