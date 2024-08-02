# Add Items to the Recommender Service

## Single Import

```python
wrc.add_item(single_request["id"],single_request["properties"])
```

## Batch Import

```python
wrc.add_items(
    [
        RecommenderItem(
            uuid=item["id"],
            properties= item["properties"]
        )
        for item in bulk_requests
    ]
)
```
## Add Interaction

```python
wrc.add_user_interaction(
    user_id = user_id,
    item_id = wine_id,
    interaction_property_name = interaction_type,
    weight = weight
)
```
