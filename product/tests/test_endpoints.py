import pytest
import json

pytestmark = pytest.mark.django_db


class TestCategoryEndpoint:
    endpoint = "/api/category/"

    def test_category_get(self, category_factory, api_client):
        # Arrange
        # generate 4 sample
        category_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        # print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4


class TestBrandEndpoint:
    endpoint = "/api/brand/"

    def test_category_get(self, brand_factory, api_client):
        # Arrange
        brand_factory.create_batch(3)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3


class TestProductEndpoint:
    endpoint = "/api/product/"

    def test_product_get(self, product_factory, api_client):
        # Arrange
        product_factory.create_batch(3)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 3
