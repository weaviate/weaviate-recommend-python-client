# Generating Recommendations

## Overview
This guide explains how to generate recommendations using the trained recommender system via the `WeaviateRecommendClient`.

## Prerequisites
- Established connection to the Recommender Service (see `1_connection.md`)
- Trained recommender system (see `4_train.md`)

## Types of Recommendations

### Item-to-Item Recommendations

To get recommendations based on a single item:

```python
item_id = "unique_item_id"
recommendations = wrc.get_item_recommendations(uuid=item_id, limit=10)
print(recommendations)
```

### Multi-Item Recommendations

To get recommendations based on multiple items:

```python
item_ids = ["item1", "item2", "item3"]
recommendations = wrc.get_items_recommendations(uuids=item_ids, limit=10)
print(recommendations)
```

### User-Based Recommendations

To get recommendations for a specific user:

```python
user_id = "user123"
recommendations = wrc.items_from_user(user_id=user_id, limit=10)
print(recommendations)
```

### Multi-User Recommendations

To get recommendations based on multiple users' preferences:

```python
user_ids = ["user1", "user2"]
recommendations = wrc.items_from_users(user_ids=user_ids, limit=15)
print(recommendations)
```

## Interpreting Results

Recommendation results include:
- Item UUID
- Relevance score or distance
- Item properties

You can process these results to display or use in your application as needed.

## Next Steps

Explore more advanced features like personalized search (`personalized_search.md`) and configured endpoints (`configured_endpoints.md`) to further enhance your recommendation system.
