from typing import TYPE_CHECKING

import requests

from weaviate_recommend.exceptions import RecommendApiException

if TYPE_CHECKING:
    from weaviate_recommend import WeaviateRecommendClient


class _Trainer:
    def __init__(self, client: "WeaviateRecommendClient"):
        self.client = client
        self.endpoint_url = f"{self.client.base_url}/train/"

    def train(self, overwrite: bool = False):
        """
        Triggers the recommender training.
        """
        params = {"overwrite_existing": overwrite}
        response = requests.post(self.endpoint_url, json=params)
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return response.json()

    def status(self):
        """
        Get the training status.
        """
        response = requests.get(self.endpoint_url + "status")
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return response.json()
