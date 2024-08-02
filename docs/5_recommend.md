
# Recommend

The part you've been waiting for, now that you are all setup you can use the Recommender Service to make recommendations! 🔥

- User(s) --> Item(s)
- User(s) --> User(s)
- Item(s) --> Item(s)

Item --> Item

```python
recs = wrc.get_item_recommendations(
    uuid=rand_wine["wineID"]
)
```
