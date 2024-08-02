# Create Recommender Schema

```python
wrc.create(
    collection_name= "xWines",
    properties= {
        "wineName": wvcc.DataType.TEXT,
        "type": wvcc.DataType.TEXT,
        "elaborate": wvcc.DataType.TEXT,
        "grapes": wvcc.DataType.TEXT_ARRAY,
        "harmonize": wvcc.DataType.TEXT_ARRAY,
        "abv": wvcc.DataType.NUMBER,
        "body": wvcc.DataType.TEXT,
        "acidity": wvcc.DataType.TEXT,
        "country": wvcc.DataType.TEXT,
        "regionName": wvcc.DataType.TEXT,
        "wineryName": wvcc.DataType.TEXT,
        "vintages": wvcc.DataType.NUMBER_ARRAY,
    },
    user_properties= {
        "age": wvcc.DataType.NUMBER,
    },
    user_interaction_property_names = ["purchase", "like", "dislike"],
    text_search_property_name = "wineName"
)
```
