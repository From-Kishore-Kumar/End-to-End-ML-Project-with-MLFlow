import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd

from mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config = DataTransformationConfig):
        # Only train test split has been done since the data 
        # is cleaned and not much categorical variables
        self.config = config
    
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logger.info("Data splitted into train and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)