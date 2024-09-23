# Creating the Recommender Schema

## Overview
This guide explains how to create and configure the schema for your recommender system using the `WeaviateRecommendClient`.

## Why do I need a Schema for the Recommender Service?

The Recommender Service Schema lets you achieve two key features:

1. Set Interaction Weights: The Recommender Schema enables weighting interactions such as "Add_To_Cart" more so than "Viewed_Item". This further lets you set negative weights for interactions such as "Dislike".
2. Table Representation Learning (Advanced): Weaviate's Recommender Service leverages `BOOLEAN`, `INT`, `FLOAT`, and `TEXT`-encoded categories to compute vector representations.

## Prerequisites
- Established connection to the Recommender Service (see `1_connection.md`)
- Understanding of your data model and recommendation requirements

## Creating the Schema

To create the recommender schema, use the `create` method of your `WeaviateRecommendClient` instance:

```python
import weaviate.classes.config as wvcc

client.create(
    collection_name="MyCollection",
    properties={
        "property1": wvcc.DataType.TEXT,
        "property2": wvcc.DataType.NUMBER,
        "property3": wvcc.DataType.TEXT_ARRAY,
        # Add more properties as needed
    },
    trainable_properties=[
        "property1",
        "property2"
    ]
    user_properties={
        "user_property1": wvcc.DataType.NUMBER,
        # Add more user properties as needed
    },
    user_interaction_property_names=["purchase", "like", "view"],
    text_search_property_name="property1"
)
```

### Parameters:

- `collection_name`: Name of your item collection.
- `properties`: Dictionary of item properties and their data types.
- `trainable_properties`: Properties used to compute the item vector representation.
- `user_properties`: Dictionary of user properties and their data types.
- `user_interaction_property_names`: List of interaction types you want to track.
- `text_search_property_name`: Property to be used for text-based searches.

## Verifying the Schema

After creating the schema, you can verify it using the `details` method:

```python
details = client.details()
print(details)
```

This will show you the current configuration of your recommender.

## Modifying the Schema

To modify an existing schema, you need to delete the current recommender and create a new one:

```python
client.delete()
# Then create a new schema as shown above
```

## Best Practices

1. Plan your schema carefully before creation, as changing it requires recreating the recommender.
2. Include all relevant properties that might influence recommendations.
3. Choose appropriate data types for each property to ensure efficient processing.
4. Consider future needs when defining user interaction types.

## Next Steps

Once your schema is set up, you can proceed to add items and user interactions to your recommender system. See `3_add_items_and_interactions.md` for more information.
