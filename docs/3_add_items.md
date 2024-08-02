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
