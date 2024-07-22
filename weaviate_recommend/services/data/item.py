from typing import TYPE_CHECKING, Any, Dict, List, Union
from uuid import UUID

import requests

from weaviate_recommend.exceptions import RecommendApiException
from weaviate_recommend.models.data import RecommenderItem
from weaviate_recommend.models.responses import (
    AddItemResponse,
    AddItemsResponse,
    DeleteItemResponse,
)

if TYPE_CHECKING:
    from weaviate_recommend import WeaviateRecommendClient


class _Item:
    def __init__(self, client: "WeaviateRecommendClient"):
        self.client = client
        self.endpoint_url = f"{self.client.base_url}/item/"

    def add(
        self, item_id: Union[str, UUID], properties: Dict[str, Any]
    ) -> AddItemResponse:
        """
        Add a new item to the recommender.
        """
        if isinstance(item_id, str):
            item_id = UUID(item_id)

        params = {
            "id": str(item_id),
            "properties": properties,
        }

        response = requests.post(self.endpoint_url, json=params)
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return AddItemResponse.model_validate(response.json())

    def add_batch(self, items: List[RecommenderItem]) -> AddItemsResponse:
        """
        Add multiple items to the recommender.
        """
        params = [
            {
                "id": str(item.id),
                "properties": item.properties,
            }
            for item in items
        ]

        response = requests.post(self.endpoint_url + "batch", json=params)
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return AddItemsResponse.model_validate(response.json())

    def delete(self, uuid: UUID | str) -> DeleteItemResponse:
        """
        Delete an item from the recommender.
        """
        if isinstance(uuid, str):
            uuid = UUID(uuid)

        response = requests.delete(self.endpoint_url + str(uuid))
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return DeleteItemResponse.model_validate(response.json())
