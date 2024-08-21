from typing import TYPE_CHECKING

import requests

from weaviate_recommend.exceptions import RecommendApiException
from weaviate_recommend.models.responses import (
    TrainingStatusResponse,
    TrainRecommenderResponse,
)
from weaviate_recommend.utils import get_auth_header

if TYPE_CHECKING:
    from weaviate_recommend import WeaviateRecommendClient


class _Trainer:
    def __init__(self, client: "WeaviateRecommendClient"):
        self.client = client
        self.endpoint_url = f"{self.client.base_url}/train/"

    def train(self, overwrite: bool = False) -> TrainRecommenderResponse:
        """
        Triggers the recommender training.
        """
        params = {"overwrite_existing": overwrite}
        response = requests.post(
            self.endpoint_url,
            json=params,
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)

        return TrainRecommenderResponse.model_validate(response.json())

    def status(self) -> TrainingStatusResponse:
        """
        Get the training status.
        """
        response = requests.get(
            self.endpoint_url + "status", headers=get_auth_header(self.client._api_key)
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)

        return TrainingStatusResponse.model_validate(response.json())
