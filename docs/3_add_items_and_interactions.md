# Adding Items and User Interactions

## Overview
This guide explains how to add items to your recommender system and record user interactions using the `WeaviateRecommendClient`.

## Prerequisites
- Established connection to the Recommender Service (see `1_connection.md`)
- Created recommender schema (see `2_create_schema.md`)

## Adding Items

This ensures items stored in Weaviate are represented with the vector from the Recommender model.

### Adding a Single Item

To add a single item:

```python
item_id = "unique_item_id"
item_properties = {
    "property1": "value1",
    "property2": 42,
    "property3": ["array", "value"],
    # Include all properties defined in your schema
}

response = wrc.add_item(item_id, item_properties)
print(response)
```

### Adding Multiple Items

To add multiple items efficiently:

```python
from client.models import RecommenderItem

items = [
    RecommenderItem(uuid="id1", properties={"property1": "value1", ...}),
    RecommenderItem(uuid="id2", properties={"property1": "value2", ...}),
    # Add more items as needed
]

response = wrc.add_items(items)
print(response)
```

## Recording User Interactions

To record user interactions with items:

```python
user_id = "user123"
item_id = "item456"
interaction_type = "purchase"  # Or "like", "view", etc. as defined in your schema
weight = 1.0  # Interaction strength, typically between -1 and 1

response = wrc.add_user_interaction(
    user_id=user_id,
    item_id=item_id,
    interaction_property_name=interaction_type,
    weight=weight
)
print(response)
```

### Adding Multiple Interactions

For bulk addition of user interactions:

```python
interactions = [
    {"user_id": "user1", "item_id": "item1", "interaction_property_name": "purchase", "weight": 1.0},
    {"user_id": "user1", "item_id": "item2", "interaction_property_name": "like", "weight": 0.5},
    # Add more interactions as needed
]

for interaction in interactions:
    wrc.add_user_interaction(**interaction)
```

## Best Practices

1. Ensure all required properties are included when adding items.
2. Use batch operations (`add_items`) for adding multiple items efficiently.
3. Choose appropriate weights for user interactions to reflect their importance.
4. Regularly add user interactions to keep the recommender system up-to-date.

## Next Steps

After adding items and user interactions, you can train your recommender system to generate personalized recommendations. See `4_train.md` for information on training the system.
