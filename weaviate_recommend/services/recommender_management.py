from typing import TYPE_CHECKING, Dict, List, Union

import requests
from weaviate.classes.config import DataType

from weaviate_recommend.exceptions import RecommendApiException

if TYPE_CHECKING:
    from weaviate_recommend import WeaviateRecommendClient


class _RecommenderManagement:

    def __init__(self, client: "WeaviateRecommendClient"):
        self.client = client
        self.endpoint_url = f"{self.client.base_url}/recommender/"

    def create(
        self,
        name: str,
        properties: Dict[str, DataType],
        user_properties: Dict[str, DataType],
        user_interaction_property_names: List[str],
        text_search_property_name: Union[str, None] = None,
        trainable_properties: Union[List[str], None] = None,
    ):
        """
        Creates a new recommender.
        """
        params = {
            "collection_name": name,
            "properties": properties,
            "user_properties": user_properties,
            "user_interaction_property_names": user_interaction_property_names,
            "text_search_property_name": text_search_property_name,
            "trainable_properties": trainable_properties,
        }

        response = requests.post(self.endpoint_url, json=params)
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return response.json()

    def delete(self):
        """
        Deletes the recommender.
        """
        response = requests.delete(self.endpoint_url)
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return response.json()

    def details(self):
        """
        Get details about the recommender.
        """
        response = requests.get(self.endpoint_url + "details")
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return response.json()
