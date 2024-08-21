from typing import TYPE_CHECKING, Union
from uuid import UUID

import requests

from weaviate_recommend.exceptions import RecommendApiException
from weaviate_recommend.models.data import UserInteraction
from weaviate_recommend.models.responses import (
    AddUserInteractionResponse,
    AddUserInteractionsResponse,
)
from weaviate_recommend.utils import get_auth_header, get_datetime

if TYPE_CHECKING:
    from weaviate_recommend import WeaviateRecommendClient


class _User:

    def __init__(self, client: "WeaviateRecommendClient"):
        self.client = client
        self.endpoint_url = f"{self.client.base_url}/user/"

    def add_interaction(
        self,
        user_id: Union[str, UUID],
        item_id: Union[str, UUID],
        interaction_property_name: str,
        weight: float = 1.0,
        created_at: Union[str, None] = None,
    ) -> AddUserInteractionResponse:
        """
        Add a user interaction.
        """
        if isinstance(user_id, str):
            user_id = UUID(user_id)
        if isinstance(item_id, str):
            item_id = UUID(item_id)
        if not created_at:
            created_at = get_datetime()
        data = {
            "id": str(user_id),
            "item_id": str(item_id),
            "interaction_property_name": interaction_property_name,
            "weight": weight,
            "created_at": created_at,
        }

        response = requests.post(
            self.endpoint_url, json=data, headers=get_auth_header(self.client._api_key)
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return AddUserInteractionResponse.model_validate(response.json())

    def add_interactions(
        self, interactions: list[UserInteraction]
    ) -> AddUserInteractionsResponse:
        """
        Add multiple user interactions.
        """
        data = [interaction.model_dump() for interaction in interactions]
        for interaction in data:
            if not interaction["created_at"]:
                interaction["created_at"] = get_datetime()
        response = requests.post(
            self.endpoint_url + "batch",
            json=data,
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return AddUserInteractionsResponse.model_validate(response.json())
