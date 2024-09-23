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
recommendations = client.recommendation.item.from_item(item_id="1", limit=10, remove_reference=True)
print(recommendations)
```

### Multi-Item Recommendations

To get recommendations based on multiple items:

```python
recommendations = client.recommendation.item.from_items(item_ids["1", "2", "3"], limit=10, remove_references=True)
print(recommendations)
```

### User-Based Recommendations

To get recommendations for a specific user:

```python
recommendations = client.recommendations.item.from_user(user_id="user1", limit=10,
                                                        remove_reference=True, top_n_interactions=100)
print(recommendations)
```

### Multi-User Recommendations

To get recommendations based on multiple users' preferences:

```python
recommendations = client.recommendations.item.from_users(user_id=["user1","user2","user3"], limit=10,
                                                        remove_reference=True, top_n_interactions=100)
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
