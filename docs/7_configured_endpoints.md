# Configured Endpoints

## Overview
This guide explains how to create and use configured endpoints, which allow you to save and reuse custom recommendation logic.

## Prerequisites
- Established connection to the Recommender Service (see `connection.md`)
- Understanding of your recommendation requirements and business logic

## Creating a Configured Endpoint

To create a configured endpoint:

```python
from client.models import FilterConfig

response = wrc.create_configured_endpoint(
    endpoint_name="my-custom-endpoint",
    from_type="item",
    to_type="items",
    filters=[
        FilterConfig(
            property_name="category",
            operator="Equal",
            value="Electronics"
        ),
        FilterConfig(
            property_name="price",
            operator="LessThan",
            value=1000
        )
    ]
)
print(response)
```

### Parameters:

- `endpoint_name`: A unique name for your configured endpoint
- `from_type`: The type of the input ("item", "items", "user", or "users")
- `to_type`: The type of the output ("items" or "users")
- `filters`: A list of `FilterConfig` objects defining your custom logic
