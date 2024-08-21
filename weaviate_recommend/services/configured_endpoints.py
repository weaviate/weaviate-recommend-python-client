from typing import TYPE_CHECKING, List

import requests

from weaviate_recommend.exceptions import RecommendApiException
from weaviate_recommend.models.configured import FROM_TO_OPTIONS
from weaviate_recommend.models.filter import FilterConfig
from weaviate_recommend.models.responses import (
    CreateConfiguredEndpointResponse,
    DeleteConfiguredEndpointResponse,
    ListConfiguredEndpointsResponse,
)
from weaviate_recommend.utils import get_auth_header

if TYPE_CHECKING:
    from weaviate_recommend import WeaviateRecommendClient


class _ConfiguredEndpoints:
    def __init__(self, client: "WeaviateRecommendClient"):
        self.client = client
        self.endpoint_url = f"{client.base_url}/configured/"

    def create(
        self,
        endpoint_name: str,
        from_type: FROM_TO_OPTIONS,
        to_type: FROM_TO_OPTIONS,
        filters: List[FilterConfig],
    ) -> CreateConfiguredEndpointResponse:
        """
        Create a new configured endpoint.
        """
        params = {
            "endpoint_name": endpoint_name,
            "from": from_type,
            "to": to_type,
            "filters": [filter.model_dump() for filter in filters],
        }
        response = requests.post(
            self.endpoint_url,
            json=params,
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return CreateConfiguredEndpointResponse.model_validate(response.json())

    def list(self) -> ListConfiguredEndpointsResponse:
        """
        List all configured endpoints, and details about their configuration.
        """
        response = requests.get(
            self.endpoint_url + "details", headers=get_auth_header(self.client._api_key)
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return ListConfiguredEndpointsResponse.model_validate(response.json())

    def delete(self, endpoint_name: str) -> DeleteConfiguredEndpointResponse:
        """
        Delete a configured endpoint.
        """
        response = requests.delete(
            self.endpoint_url + endpoint_name,
            headers=get_auth_header(self.client._api_key),
        )
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return DeleteConfiguredEndpointResponse.model_validate(response.json())
