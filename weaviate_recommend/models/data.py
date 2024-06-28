from typing import Any, Dict, Union
from uuid import UUID

from pydantic import BaseModel, field_validator


class RecommenderItem(BaseModel):
    uuid: Union[str, UUID]
    properties: Dict[str, Any]

    @field_validator("uuid")
    def validate_uuid(cls, value):
        # if the values is a string, try to convert it to a UUID object
        if isinstance(value, str):
            try:
                return UUID(value)
            except ValueError:
                raise ValueError("uuid must be a valid UUID")


class UserInteraction(BaseModel):
    user_id: Union[str, UUID]
    item_id: Union[str, UUID]
    interaction_property_name: str
    weight: float = 1.0
    created_at: Union[str, None] = None
