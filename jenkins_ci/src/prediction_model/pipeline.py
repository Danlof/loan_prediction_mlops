from sklearn.pipeline import Pipeline
from prediction_model.config import config
import prediction_model.processing.preprocessing as pp 
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import numpy as np


classification_pipeline = Pipeline([
    ("DomainProcessing",pp.DomainProcessing(variable_to_modify=config.FEATURE_TO_MODIFY,
                                            variable_to_add=config.FEATURE_TO_ADD)),
    ("MeanImputer",pp.MeanImputer(variables=config.NUM_FEATURES)),
    ("ModeImputer",pp.ModeImputer(variables=config.CAT_FEATURES)),
    ("DropColumns",pp.DropColumns(variables_to_drop=config.DROP_FEATURES)),
    ("LabelEncoder",pp.CustomLabelEncoder(variables=config.FEATURES_TO_ENCODE)),
    ("LogTransforamtion",pp.LogTransforms(variables=config.LOG_FEATURES)),
    ("MinMaxscaler",MinMaxScaler()),
    ("LogisticClassifier",LogisticRegression(random_state=42))
])