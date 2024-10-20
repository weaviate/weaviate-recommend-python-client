from datetime import datetime
from typing import Dict, List, Literal

from pydantic import BaseModel, Field

from weaviate_recommend.models.filter import FilterConfig
from weaviate_recommend.models.train import TRAINING_STATE


class CreateConfiguredEndpointResponse(BaseModel):
    endpoint_name: str
    from_: Literal["item", "items", "user", "users"] = Field(alias="from")
    to: Literal[
        "item",
        "items",
        "user",
        "users",
    ]
    message: str


class ListConfiguredEndpointsResponse(BaseModel):
    items_from_item_configured: Dict[str, List[FilterConfig]]
    items_from_items_configured: Dict[str, List[FilterConfig]]
    items_from_user_configured: Dict[str, List[FilterConfig]]
    items_from_users_configured: Dict[str, List[FilterConfig]]
    users_from_item_configured: Dict[str, List[FilterConfig]]
    users_from_items_configured: Dict[str, List[FilterConfig]]
    users_from_user_configured: Dict[str, List[FilterConfig]]
    users_from_users_configured: Dict[str, List[FilterConfig]]


class DeleteConfiguredEndpointResponse(BaseModel):
    message: str


class AddItemResponse(BaseModel):
    message: str


class AddItemsResponse(BaseModel):
    message: str
    num_items_added: int


class DeleteItemResponse(BaseModel):
    message: str


class RecommendationResponse(BaseModel):
    uuid: str
    distance: float
    properties: dict


class RecommendationResponseWithScore(BaseModel):
    uuid: str
    score: float
    properties: dict


class RecommendationsResponse(BaseModel):
    recommendations: List[RecommendationResponse]


class CreateRecommenderResponse(BaseModel):
    message: str


class DeleteRecommenderResponse(BaseModel):
    message: str


class RecommenderDetailsResponse(BaseModel):
    item_collection_name: str | None
    user_collection_name: str | None
    interaction_property_names: List[str] | None
    text_search_property_name: str | List[str] | None
    created_at: datetime
    training_state: TRAINING_STATE
    trainable_properties: List[str] | None


class PersonalisedSearchResponse(BaseModel):
    results: List[RecommendationResponseWithScore]


class TrainRecommenderResponse(BaseModel):
    message: str


class TrainingStatusResponse(BaseModel):
    status: TRAINING_STATE


class AddUserInteractionResponse(BaseModel):
    message: str


class AddUserInteractionsResponse(BaseModel):
    message: str
    num_interactions_added: int


class CreateUserResponse(BaseModel):
    message: str


class DeleteUserResponse(BaseModel):
    message: str


class UpdateUserResponse(BaseModel):
    message: str
