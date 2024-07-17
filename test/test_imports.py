import pytest


def test_import_weaviate_recommend():
    try:
        pass
    except ImportError:
        pytest.fail("Failed to import weaviate_recommend")


def test_import_weaviate_recommend_client():
    try:
        pass
    except ImportError:
        pytest.fail("Failed to import WeaviateRecommendClient from weaviate_recommend")


def test_weaviate_recommend_client_is_class():
    from weaviate_recommend import WeaviateRecommendClient

    assert isinstance(WeaviateRecommendClient, type)
