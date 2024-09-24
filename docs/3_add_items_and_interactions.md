# Adding Items and User Interactions

## Overview

This guide explains how to add items to your recommender system, record user interactions, and manage user data using the `WeaviateRecommendClient`.

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

response = client.item.add(item_id, item_properties)
print(response)
```

### Adding Multiple Items

To add multiple items efficiently:

```python
from weaviate_recommend.models.data import RecommenderItem

items = [
    RecommenderItem(uuid="id1", properties={"property1": "value1", ...}),
    RecommenderItem(uuid="id2", properties={"property1": "value2", ...}),
    # Add more items as needed
]

response = client.item.add_batch(items)
print(response)
```

## Managing User Data

### Creating a New User

To create a new user in the recommender system:

```python
from weaviate_recommend.models.data import User

new_user = User(id="user123", properties={"name": "John Doe", "age": 30})
response = client.user.create_user(new_user)
print(response)
```

### Retrieving User Information

To get all properties for a user by ID:

```python
user_id = "user123"
user = client.user.get_user(user_id)
print(user)
```

## Recording User Interactions

### Adding a Single User Interaction

To record a single user interaction with an item:

```python
user_id = "user123"
item_id = "item456"
interaction_type = "purchase"  # Or "like", "view", etc. as defined in your schema
weight = 1.0  # Interaction strength, typically between -1 and 1

response = client.user.add_interaction(
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
from weaviate_recommend.models.data import UserInteraction

interactions = [
    UserInteraction(user_id="user1", item_id="1", interaction_property_name="purchase", weight=1.0),
    UserInteraction(user_id="user1", item_id="4", interaction_property_name="purchase", weight=0.5),
    # add more interactions as needed
]

response = client.user.add_interactions(interactions)
print(response)
```

### Retrieving User Interactions

To get all interactions for a specific user:

```python
user_id = "user123"
interactions = client.user.get_user_interactions(user_id)
for interaction in interactions:
    print(f"Item: {interaction.item_id}, Type: {interaction.interaction_property_name}, Weight: {interaction.weight}")
```

## Best Practices

1. Ensure all required properties are included when adding items or creating users.
2. Use batch operations for adding multiple items or user interactions efficiently.
3. Choose appropriate weights for user interactions to reflect their importance.
4. Regularly add user interactions to keep the recommender system up-to-date.
5. Use the `get_user` and `get_user_interactions` methods to retrieve and analyze user data as needed.

## Next Steps

After adding items, managing user data, and recording user interactions, you can train your recommender system to generate personalized recommendations. See `4_train.md` for information on training the system.
