### 1. IMPORT PICOCV ###
"""WARNING
Make sure to upgrade picocv to latest version via following shell command

> pip install picocv --upgrade

"""
import picocv
from picocv import Settings

### 2. IMPORT CUSTOM  MODEL / DATASET
from model import MyClassifier
from dataset import MyDataset

import os

def model_func():
    """
    Initialize Custom Model
    :return: Initialized Custom Model
    """
    return MyClassifier()

def dataset_func():
    """
    Initialize Custom Dataset
    :return: Initialized Custom Dataset
    """
    # Dataset Should Return tuple(image(tensor(width,height,3)), label(tensor)))
    return MyDataset()

if __name__ == '__main__':
    ### 3. CONFIGURE SETTINGS
    # Reference pico._settings documentation for more info

    ## Settings Params
    # result_dir : Where relabeled results are stored
    root = os.path.dirname(os.path.realpath(__file__))
    result_dir = os.path.join(root, "./relabeled_result")

    settings = Settings(result_dir=result_dir)

    ### 4. RUN AUTO_CORRECT
    picocv.autoCorrect(model_func=model_func, dataset_func=dataset_func, settings=settings)
