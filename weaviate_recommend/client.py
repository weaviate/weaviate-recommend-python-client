from typing import Dict, List, Union

import requests
from weaviate.classes.config import DataType

from weaviate_recommend.exceptions import RecommendApiException
from weaviate_recommend.services import (
    _ConfiguredEndpoints,
    _Item,
    _Recommendation,
    _RecommenderManagement,
    _User,
)


class WeaviateRecommendClient:
    def __init__(self, url: str):
        self._url = url
        self.base_url = f"{url}/v1"

        self._recommender_management = _RecommenderManagement(self)
        self.recommendation = _Recommendation(self)
        self.endpoint = _ConfiguredEndpoints(self)
        self.item = _Item(self)
        self.user = _User(self)

    def _perform_health_check(self) -> None:
        response = requests.get(self._url + "/health")
        if response.status_code != 200:
            raise RecommendApiException(response.text)

    def _training_state(self) -> str:
        return self._recommender_management.details()["training_state"]

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
    ):
        self._recommender_management.create(
            name,
            properties,
            user_properties,
            user_interaction_property_names,
            text_search_property_name,
            trainable_properties,
        )

    def delete(self):
        self._recommender_management.delete()

    def details(self):
        return self._recommender_management.details()
