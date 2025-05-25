import os
import pickle

def test_model_file_exists():
    assert os.path.exists("models/model_v1.pkl"), "Model file not found"

def test_model_is_pickled():
    with open("models/model_v1.pkl", "rb") as f:
        model = pickle.load(f)
    assert hasattr(model, "predict"), "Loaded object is not a valid model"
