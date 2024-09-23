from typing import TYPE_CHECKING, List, Union
from uuid import UUID

import requests

from weaviate_recommend.exceptions import RecommendApiException
from weaviate_recommend.models.filter import FilterConfig
from weaviate_recommend.models.responses import RecommendationsResponse
from weaviate_recommend.utils import get_auth_header

if TYPE_CHECKING:
    from weaviate_recommend import WeaviateRecommendClient


class _ItemRecommendation:

    def __init__(self, client: "WeaviateRecommendClient"):
        self.client = client
        self.endpoint_url = f"{self.client.base_url}/item-recommendations/"

    def from_item(
        self,
        item_id: Union[str, UUID],
        limit: int = 10,
        remove_reference: bool = False,
        filters: List[FilterConfig] | None = None,
    ) -> RecommendationsResponse:
        """
        Get recommendations for a single item.
        """
        # if uuid is a string, convert it to a UUID object
        if isinstance(item_id, str):
            item_id = UUID(item_id)

        if filters:
            _filters = [filter_config.model_dump() for filter_config in filters]
        else:
            _filters = None

        params = {
            "id": str(item_id),
            "limit": limit,
            "remove_reference": remove_reference,
            "filters": _filters,
        }
        response = requests.post(
            self.endpoint_url + "item",
            json=params,
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return RecommendationsResponse.model_validate(response.json())

    def from_items(
        self,
        item_ids: list[UUID | str],
        limit: int = 10,
        remove_reference: bool = True,
        filters: list[FilterConfig] | None = None,
    ) -> RecommendationsResponse:
        """
        Get recommendations for multiple items.
        """

        item_ids = [
            str(UUID(item_id)) if isinstance(item_id, str) else str(item_id)
            for item_id in item_ids
        ]

        if filters:
            _filters = [filter_config.model_dump() for filter_config in filters]
        else:
            _filters = None

        params = {
            "ids": item_ids,
            "limit": limit,
            "remove_reference": remove_reference,
            "filters": _filters,
        }
        response = requests.post(
            self.endpoint_url + "items",
            json=params,
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return RecommendationsResponse.model_validate(response.json())

    def from_item_configured(
        self,
        endpoint_name: str,
        item_id: Union[str, UUID],
        limit: int = 10,
        remove_reference: bool = True,
    ) -> RecommendationsResponse:
        """
        Get recommendations for a given item based on a configured endpoint.
        """
        if isinstance(item_id, str):
            item_id = UUID(item_id)

        params = {
            "configured_endpoint_name": endpoint_name,
            "id": str(item_id),
            "limit": limit,
            "remove_reference": remove_reference,
        }

        response = requests.post(
            self.endpoint_url + "item/configured",
            json=params,
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return RecommendationsResponse.model_validate(response.json())

    def from_items_configured(
        self,
        endpoint_name: str,
        item_ids: List[Union[str, UUID]],
        limit: int = 10,
        remove_reference: bool = True,
    ) -> RecommendationsResponse:
        """
        Get recommendations for multiple items based on a configured endpoint.
        """
        item_ids = [
            str(UUID(item_id)) if isinstance(item_id, str) else str(item_id)
            for item_id in item_ids
        ]

        params = {
            "configured_endpoint_name": endpoint_name,
            "ids": item_ids,
            "limit": limit,
            "remove_reference": remove_reference,
        }

        response = requests.post(
            self.endpoint_url + "items/configured",
            json=params,
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return RecommendationsResponse.model_validate(response.json())

    def from_user(
        self,
        user_id: Union[str, UUID],
        limit: int = 10,
        remove_reference: bool = True,
        shuffle: bool = True,
        top_n_interactions: int = 100,
    ) -> RecommendationsResponse:
        """
        Get recommendations for a given user.
        """
        if isinstance(user_id, str):
            user_id = UUID(user_id)
        params = {
            "user_id": str(user_id),
            "limit": limit,
            "remove_reference": remove_reference,
            "shuffle": shuffle,
            "top_n_interactions": top_n_interactions,
        }
        response = requests.post(
            self.endpoint_url + "user",
            json=params,
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return RecommendationsResponse.model_validate(response.json())

    def from_users(
        self,
        user_ids: list[UUID | str],
        limit: int = 10,
        remove_reference: bool = True,
    ) -> RecommendationsResponse:
        """
        Get recommendations for multiple users.
        """
        user_ids = [
            str(UUID(user_id)) if isinstance(user_id, str) else str(user_id)
            for user_id in user_ids
        ]
        params = {
            "user_ids": user_ids,
            "limit": limit,
            "remove_reference": remove_reference,
        }
        response = requests.post(
            self.endpoint_url + "users",
            json=params,
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return RecommendationsResponse.model_validate(response.json())
