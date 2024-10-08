# Training the Recommender System

## Overview
This guide explains how to train your recommender system using the `WeaviateRecommendClient`.

## Prerequisites
- Established connection to the Recommender Service (see `1_connection.md`)
- Created recommender schema (see `2_create_schema.md`)
- Added items and user interactions (see `3_add_items_and_interactions.md`)

## Training Process

Training the recommender system is an asynchronous process. Here's how to initiate and monitor the training:

### Initiating Training

To start the training process:

```python
response = client.train()
print(response)
```

This will return a message indicating that training has started.

### Overwrite Trained Model

Pass in an extra `overwrite=True` flag to overwrite the currently trained model and create a new one.

```python
response = client.train(overwrite=True)
print(response)
```

### Checking Training Status

To check if the training is complete:

```python
is_trained = client.is_trained()
print(is_trained)  # Returns True if trained, False otherwise
```

If there is an error, it can be seen with:

```python
status = client.train_status()
print(status)
```

You can use this in a loop to wait for training completion:

```python
import time

while not client.is_trained():
    print("Training in progress...")
    time.sleep(10)  # Wait for 10 seconds before checking again

print("Training completed!")
```

## When to Train

- After initial setup and adding a substantial number of items
- Periodically to incorporate new items and user interactions
- After significant changes in your data or user behavior patterns

## Next Steps

Once your recommender system is trained, you can start generating recommendations. See `recommend.md` for information on how to request and use recommendations.
