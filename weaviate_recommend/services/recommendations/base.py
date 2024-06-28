from weaviate_recommend.services import _ItemRecommendation


class _Recommendation:
    def __init__(self, client):
        super().__init__(client)
        self.endpoint_url = f"{self.client.base_url}/recommendation/"
        self.item = _ItemRecommendation(client)
        self.user = None
