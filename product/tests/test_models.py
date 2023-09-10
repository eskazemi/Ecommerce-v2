import pytest

pytestmark = pytest.mark.django_db


class TestCategory:
    def test_str_method(self, category_factory):
        category = category_factory(name="test_category")
        # Assert
        assert category.__str__() == "test_category"


class TestBrand:
    def test_str_method(self, brand_factory):
        brand = brand_factory(name="test_brand")
        # Assert
        assert brand.__str__() == "test_brand"


class TestProduct:
    def test_str_method(self, product_factory):
        product = product_factory()
        # Assert
        assert product.__str__() == "test_product"
