from django.core.exceptions import ValidationError
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


class TestProductLine:
    def test_str_method(self, product_line_factory, attribute_value_factory):
        # Arrange
        # Act
        attr = attribute_value_factory(attribute_value="test")
        obj = product_line_factory(attribute_value=(attr,))
        # Assert
        assert obj.__str__() == "12345"

    def test_duplicate_order_values(self, product_line_factory, product_factory):
        obj = product_factory()
        product_line_factory(order=1, product=obj)
        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=obj).clean()


class TestProductImage:
    def test_str_method(self, product_image_factory):
        # Arrange
        # Act
        obj = product_image_factory(order=1)
        # Assert
        assert obj.__str__() == "1"

    def test_duplicate_order_values(self, product_image_factory, product_line_factory, product_factory):
        obj_product = product_factory()
        obj_product_line = product_line_factory(order=1, product=obj_product)
        product_image_factory(order=1, product_line=obj_product_line)
        with pytest.raises(ValidationError):
            product_image_factory(order=1, product_line=obj_product_line)


class TestProductType:
    def test_str_method(self, product_type_factory, attribute_factory):
        test = attribute_factory()
        obj = product_type_factory(name="test_type", attribute=(test,))
        assert obj.__str__() == "test_type"


class TestAttribute:
    def test_str_method(self, attribute_factory):
        obj = attribute_factory(name="test_attribute")
        assert obj.__str__() == "test_attribute"


class TestAttributeValue:
    def test_str_method(self, attribute_value_factory, attribute_factory):
        attr = attribute_factory(name="test_attribute")
        obj = attribute_value_factory(attribute_value="test_value", attribute=attr)
        assert obj.__str__() == "test_attribute-test_value"
