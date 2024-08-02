# Connect to Weaviate Recommender

To get an API key for the Weaviate Recommender service, please sign up for our [Beta testing program here](https://weaviate.io/workbench/recommender)!

```python
import os
from client import WeaviateRecommendClient

wrc = WeaviateRecommendClient(api_key=os.get_env("WCS_API_KEY"))
```
