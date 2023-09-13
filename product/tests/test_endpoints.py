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

    def test_product_all_product(self, product_factory, api_client):
        # Arrange
        product_factory.create_batch(3)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_return_single_product_by_slug(self, product_factory, api_client):
        # Arrange
        obj = product_factory(slug="test_slug")
        # Act
        response = api_client().get(f"{self.endpoint}{obj.slug}/")
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_return_products_by_category_slug(self, product_factory, category_factory, api_client):
        # Arrange
        obj = category_factory(slug="test_slug")
        product_factory(category=obj)
        # Act
        response = api_client().get(f"{self.endpoint}category/{obj.slug}/")
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1
