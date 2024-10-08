from typing import TYPE_CHECKING, List, Union
from uuid import UUID

import requests

from weaviate_recommend.exceptions import RecommendApiException
from weaviate_recommend.models.data import User, UserInteraction
from weaviate_recommend.models.responses import (
    AddUserInteractionResponse,
    AddUserInteractionsResponse,
    CreateUserResponse,
    DeleteUserResponse,
    UpdateUserResponse,
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
        self, interactions: List[UserInteraction]
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

    def get_user_interactions(self, user_id: Union[str, UUID]) -> List[UserInteraction]:
        """
        Get all interactions for a user.
        """
        if isinstance(user_id, UUID):
            user_id = str(user_id)

        response = requests.get(
            f"{self.endpoint_url}interactions/{user_id}",
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return [
            UserInteraction(
                user_id=interaction["id"],
                item_id=interaction["item_id"],
                interaction_property_name=interaction["interaction_property_name"],
                weight=interaction["weight"],
                created_at=interaction["created_at"],
            )
            for interaction in response.json()
        ]

    def create_user(self, user: User) -> CreateUserResponse:
        """
        Create a new user in the recommender with the given properties, not including interactions.
        """
        response = requests.post(
            f"{self.endpoint_url}create",
            json=user.model_dump(),
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return CreateUserResponse.model_validate(response.json())

    def get_user(self, user_id: Union[str, UUID]) -> User:
        """
        Get all properties for a user by ID.
        """
        if isinstance(user_id, UUID):
            user_id = str(user_id)

        response = requests.get(
            f"{self.endpoint_url}{user_id}",
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return User.model_validate(response.json())

    def update_user(self, user: User) -> UpdateUserResponse:
        """
        Update a user by ID.
        """
        response = requests.post(
            f"{self.endpoint_url}update",
            json=user.model_dump(),
            headers=get_auth_header(self.client._api_key),
        )

        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return UpdateUserResponse.model_validate(response.json())

    def delete_user(self, user_id: Union[str, UUID]) -> DeleteUserResponse:
        """
        Delete a user by ID.
        """
        if isinstance(user_id, UUID):
            user_id = str(user_id)

        response = requests.delete(
            f"{self.endpoint_url}{user_id}",
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return DeleteUserResponse.model_validate(response.json())

    def exists(self, user_id: Union[str, UUID]) -> bool:
        """
        Check if a user exists by ID.
        """
        if isinstance(user_id, UUID):
            user_id = str(user_id)

        response = requests.get(
            f"{self.endpoint_url}exists/{user_id}",
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return response.json()

    def delete_all_interactions(
        self,
        user_id: Union[str, UUID],
    ) -> DeleteUserResponse:
        """
        Delete all interactions for a user.
        """
        if isinstance(user_id, UUID):
            user_id = str(user_id)

        response = requests.delete(
            f"{self.endpoint_url}{user_id}/interactions",
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return DeleteUserResponse.model_validate(response.json())

    def delete_interactions_by_property(
        self,
        user_id: Union[str, UUID],
        interaction_property_name: str,
    ) -> DeleteUserResponse:
        """
        Delete all interactions for a user and a specific property.
        """
        if isinstance(user_id, UUID):
            user_id = str(user_id)

        response = requests.delete(
            f"{self.endpoint_url}{user_id}/interactions/{interaction_property_name}",
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return DeleteUserResponse.model_validate(response.json())

    def delete_interactions_by_property_and_item(
        self,
        user_id: Union[str, UUID],
        interaction_property_name: str,
        item_id: Union[str, UUID],
    ) -> DeleteUserResponse:
        """
        Delete specific interactions for a user, property, and item.
        """
        if isinstance(user_id, UUID):
            user_id = str(user_id)
        if isinstance(item_id, UUID):
            item_id = str(item_id)

        response = requests.delete(
            f"{self.endpoint_url}{user_id}/interactions/{interaction_property_name}/{item_id}",
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return DeleteUserResponse.model_validate(response.json())
