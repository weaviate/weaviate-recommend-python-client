# Creating the Recommender Schema

## Overview

This guide explains how to create and configure the schema for your recommender system using the `WeaviateRecommendClient`.

## Why do I need a Schema for the Recommender Service?

The Recommender Service Schema is crucial for two main reasons:

1. Data Structure and Training:
   - The schema defines what your data looks like and specifies the data types.
   - This information is essential for the recommender system to perform its training step effectively.

2. Interaction Tracking:
   - The schema allows you to define the types of interactions that will occur in your system.
   - For example, you can specify interactions like "view", "like", or "purchase".

Additionally, the schema enables two key features:

3. Weighted Interactions:
   - You can assign different weights to various interactions.
   - For instance, you might want "Add_To_Cart" to have more influence than "Viewed_Item".
   - You can even set negative weights for interactions like "Dislike".

4. Text Search Capability:
   - Alongside the trained recommendation vector, you can enable text-based search.
   - This search can be based on one or multiple properties, which will be combined.
   - Text search provides a natural entry point for many recommendation systems, allowing users to find items through traditional search before receiving personalized recommendations.

By setting up a proper schema, you ensure that your recommender system has all the necessary information to provide accurate and relevant recommendations while also supporting flexible search options.

## Prerequisites

- Established connection to the Recommender Service (see `1_connection.md`)
- Understanding of your data model and recommendation requirements

## Creating the Schema

To create the recommender schema, use the `create` method of your `WeaviateRecommendClient` instance:

```python
import weaviate.classes.config as wvcc

client.create(
    name="MyCollection",
    properties={
        "property1": wvcc.DataType.TEXT,
        "property2": wvcc.DataType.NUMBER,
        "property3": wvcc.DataType.TEXT_ARRAY,
        # Add more properties as needed
    },
    trainable_properties=[
        "property1",
        "property2"
    ],
    user_properties={
        "user_property1": wvcc.DataType.NUMBER,
        # Add more user properties as needed
    },
    user_interaction_property_names=["purchase", "like", "view"],
    text_search_property_name="property1"  # Can be a single property
    # Or use multiple properties:
    # text_search_property_name=["property1", "property3"]
)
```

### Parameters:

- `collection_name`: Name of your item collection.
- `properties`: Dictionary of item properties and their data types.
- `trainable_properties`: Properties used to compute the item vector representation.
- `user_properties`: Dictionary of user properties and their data types.
- `user_interaction_property_names`: List of interaction types you want to track.
- `text_search_property_name`: Property or list of properties to be used for text-based searches. If a list is provided, the text search will be performed on a combination of these properties.

> **Note: Trainable Properties**
>
> The `trainable_properties` parameter allows you to specify which properties will be used to compute the item vector representation.
>
> - Include properties that add predictive power to the recommendations. This typically includes most of your properties.
> - You may want to exclude:
>   - Properties that are just noise (e.g., UUIDs or other non-predictive identifiers)
>   - Properties that you don't want to influence the recommendations.
> - If you leave `trainable_properties` empty, the system will train on all properties

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
```

## Best Practices

1. Plan your schema carefully before creation, as changing it requires recreating the recommender.
2. Include all relevant properties that might influence recommendations.
3. Choose appropriate data types for each property to ensure efficient processing.
4. Consider future needs when defining user interaction types.

## Next Steps

Once your schema is set up, you can proceed to add items and user interactions to your recommender system. See `3_add_items_and_interactions.md` for more information.
