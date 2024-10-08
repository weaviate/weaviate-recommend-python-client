# Connect to Weaviate Recommender

This guide explains how to establish a connection to the Weaviate Recommender Service using the `WeaviateRecommendClient`.

## Prerequisites
- Python 3.7 or higher
- `weaviate-recommend` package installed

## Connecting to the Service

To connect to the Recommender Service, use the `WeaviateRecommendClient` class:

```python
from weaviate_recommend import WeaviateRecommendClient

# Replace with your service URL
service_url = "YOUR_SERVICE_URL"
api_key = "YOUR_API_KEY"

# Create a client instance
client = WeaviateRecommendClient(service_url, api_key)
```

To get an API key for the Weaviate Recommender service, please sign up for our [Beta testing program here](https://weaviate.io/workbench/recommender)!

## Verifying the Connection

After creating the client instance, you can verify the connection by checking the service details:

```python
details = client.details()
print(details)
```

This will return information about the current state of the recommender, including the collection names, interaction properties, and training state.

## Next Steps

Once connected, you can proceed to create your recommender schema, add items, and start generating recommendations.

## Troubleshooting

If you encounter connection issues:
1. Verify that the service URL is correct.
2. Ensure that the service is running and accessible from your network.

For persistent issues, please open an issue on the `weaviate-recommend-python-client` repository!
