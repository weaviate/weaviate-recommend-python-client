from typing import Dict, List, Union

import requests
from weaviate.classes.config import DataType

from weaviate_recommend.exceptions import RecommendApiException
from weaviate_recommend.models.responses import (
    TRAINING_STATE,
    CreateRecommenderResponse,
    DeleteRecommenderResponse,
    RecommenderDetailsResponse,
    TrainingStatusResponse,
    TrainRecommenderResponse,
)
from weaviate_recommend.services import (
    _ConfiguredEndpoints,
    _Item,
    _Recommendation,
    _RecommenderManagement,
    _Trainer,
    _User,
)


class WeaviateRecommendClient:
    def __init__(self, url: str):
        self._url = url
        self.base_url = f"{url}/v1"

        self._recommender_management = _RecommenderManagement(self)
        self._trainer = _Trainer(self)
        self.recommendation = _Recommendation(self)
        self.endpoint = _ConfiguredEndpoints(self)
        self.item = _Item(self)
        self.user = _User(self)

    def _perform_health_check(self) -> None:
        response = requests.get(self._url + "/health")
        if response.status_code != 200:
            raise RecommendApiException(response.text)

    def _training_state(self) -> TRAINING_STATE:
        return self._recommender_management.details().training_state

    def is_trained(self) -> bool:
        return self._training_state() == "trained"

    def is_training(self) -> bool:
        return self._training_state() == "training"

    def create(
        self,
        name: str,
        properties: Dict[str, DataType],
        user_properties: Dict[str, DataType],
        user_interaction_property_names: List[str],
        text_search_property_name: Union[str, None] = None,
        trainable_properties: Union[List[str], None] = None,
    ) -> CreateRecommenderResponse:
        """
        Create a new recommender.

        Args:
            name (str): _description_
            properties (Dict[str, DataType]): _description_
            user_properties (Dict[str, DataType]): _description_
            user_interaction_property_names (List[str]): _description_
            text_search_property_name (Union[str, None], optional): _description_. Defaults to None.
            trainable_properties (Union[List[str], None], optional): _description_. Defaults to None.
        """
        return self._recommender_management.create(
            name,
            properties,
            user_properties,
            user_interaction_property_names,
            text_search_property_name,
            trainable_properties,
        )

    def delete(self) -> DeleteRecommenderResponse:
        """
        Delete the recommender.
        """
        return self._recommender_management.delete()

    def details(self) -> RecommenderDetailsResponse:
        """
        Get details about the recommender.
        """
        return self._recommender_management.details()

    def train(self, overwrite: bool = False) -> TrainRecommenderResponse:
        """
        Triggers the recommender training.

        Args:
            overwrite (bool, optional): _description_. Defaults to False.
        """
        return self._trainer.train(overwrite)

    def train_status(self) -> TrainingStatusResponse:
        """
        Get the training status of the recommender.
        """
        return self._trainer.status()
