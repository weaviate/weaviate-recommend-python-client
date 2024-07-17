from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from weaviate_recommend import WeaviateRecommendClient
    from weaviate_recommend.services.recommendations.item import _ItemRecommendation


class _Recommendation:
    def __init__(self, client: "WeaviateRecommendClient"):
        self.client = client
        self.endpoint_url = f"{self.client.base_url}/recommendation/"
        self.item = _ItemRecommendation(client)
        self.user = None
