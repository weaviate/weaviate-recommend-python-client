# Personalized Search

## Overview
This guide explains how to use the personalized search feature of the recommender system, which combines text-based search with user preferences.

## Prerequisites
- Established connection to the Recommender Service (see `1_connection.md`)
- Trained recommender system (see `4_train.md`)
- User interactions recorded (see `3_add_items_and_interactions.md`)

## Performing a Personalized Search

To perform a personalized search:

```python
user_id = "user123"
search_query = "red wine"
results = wrc.search(
    text=search_query,
    user_id=user_id,
    limit=10,
    influence_factor=0.2
)
print(results)
```

### Parameters:

- `text`: The search query string
- `user_id`: ID of the user for whom to personalize results
- `limit`: Maximum number of results to return
- `influence_factor`: How much user preferences should influence results (0 to 1)

## Understanding the Influence Factor

- `influence_factor = 0`: Pure text-based search, no personalization
- `influence_factor = 1`: Heavily personalized, may diverge from text query
- Values between 0 and 1 balance text relevance and user preferences

## Interpreting Results

Results will include:
- Item UUID
- Relevance score (combining text match and user preference)
- Item properties

Example of processing results:

```python
for item in results.results:
    print(f"Item: {item.uuid}, Score: {item.score}")
    print(f"Properties: {item.properties}")
    print("---")
```

## Adding Filters

You can further customize the search by adding filters:

```python
from client.models import FilterConfig

filters = [
    FilterConfig(property_name="country", operator="Equal", value="France")
]

results = wrc.search(
    text="red wine",
    user_id="user123",
    limit=10,
    influence_factor=0.2,
    filters=filters
)
```

## Next Steps

Explore configuring custom endpoints (`configured_endpoints.md`) to create reusable, business-logic driven search and recommendation queries.
