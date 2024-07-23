from typing import TYPE_CHECKING
from uuid import UUID

import requests

from weaviate_recommend.exceptions import RecommendApiException
from weaviate_recommend.models.filter import FilterConfig
from weaviate_recommend.models.responses import PersonalisedSearchResponse

if TYPE_CHECKING:
    from weaviate_recommend import WeaviateRecommendClient


class _PersonalisedSearch:
    def __init__(self, client: "WeaviateRecommendClient"):
        self.client = client
        self.endpoint_url = f"{self.client.base_url}/search/"

    def search(
        self,
        text: str,
        user_id: str | UUID,
        limit: int = 10,
        influence_factor: float = 0.2,
        filters: list[FilterConfig] | None = None,
    ) -> PersonalisedSearchResponse:
        """
        Search for text in the Weaviate database and return the results personalised for the user.
        """
        if not isinstance(user_id, UUID):
            user_id = UUID(user_id)

        _filters = (
            [filter_config.model_dump() for filter_config in filters] if filters else []
        )

        params = {
            "text": text,
            "user_id": str(user_id),
            "limit": limit,
            "influence_factor": influence_factor,
            "filters": _filters,
        }

        response = requests.post(self.endpoint_url, json=params)
        if response.status_code != 200:
            raise RecommendApiException(response.text)
        return PersonalisedSearchResponse.model_validate(response.json())
