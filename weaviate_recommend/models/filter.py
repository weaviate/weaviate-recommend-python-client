from typing import List, Literal, Union

from pydantic import BaseModel, field_validator


class ItemPropertyReference(BaseModel):
    type: Literal["ItemPropertyReference"]


class UserPropertyReference(BaseModel):
    type: Literal["UserPropertyReference"]


FILTER_OPERATOR = Literal[
    "Equal",
    "NotEqual",
    "LessThan",
    "LessThanEqual",
    "GreaterThan",
    "GreaterThanEqual",
    "Like",
    "IsNull",
    "ContainsAny",
    "ContainsAll",
]


FilterValueType = Union[
    str,
    int,
    float,
    List[str],
    List[int],
    List[float],
    ItemPropertyReference,
    UserPropertyReference,
]


class FilterConfig(BaseModel):
    property_name: str
    operator: FILTER_OPERATOR
    value: FilterValueType

    @field_validator("value")
    def deserialize_value(cls, v):
        if isinstance(v, dict) and "type" in v:
            if v["type"] == "ItemPropertyReference":
                return ItemPropertyReference(**v)
            elif v["type"] == "UserPropertyReference":
                return UserPropertyReference(**v)
        return v
