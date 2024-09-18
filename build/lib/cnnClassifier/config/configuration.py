from src.cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,  # is path pe yaml file padi h
        params_filepath=PARAMS_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)  # returing a ConfigBox type
        self.params = read_yaml(params_filepath)

        create_directories(
            [self.config.artifacts_root]
        )  # creating directories takes list so we packed it in list

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion  # data ingestion part of config.yaml
        # unpacking the config
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )
        return data_ingestion_config
