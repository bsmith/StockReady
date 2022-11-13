from decimal import Decimal
import unittest

from models.manufacturer import Manufacturer
from models.product import Product
from models.product_type import ProductType


class TestProduct(unittest.TestCase):
    def setUp(self):
        # Associated objects
        self.manufacturer = Manufacturer("Full Name of Manufactuer",
            "Brand", None, None, None, None)
        self.product_type = ProductType("Soundbar")

        # Test all fields filled
        self.product_filled = Product(
            "MPN123",
            self.manufacturer,
            "Short Description",
            "Very long description about this product",
            self.product_type,
            19.5,
            100,
            Decimal(50.00),
            Decimal(100.00),
            id=123
        )
        # Test some fields may be none
        self.product_none = Product(
            "MPN123",
            self.manufacturer,
            "Short Description",
            None,
            self.product_type,
            None,
            100,
            Decimal(50.00),
            Decimal(100.00)
        )
        # Discontinued product
        self.product_discontinued = Product(
            "MPN456",
            self.manufacturer,
            "Discont. Prod",
            "Discontinued Product 456",
            self.product_type,
            24.1,
            0,
            Decimal(50.00),
            Decimal(25.00),
            discontinued=True
        )

    def test_product_has_mpn(self):
        self.assertEqual("MPN123", self.product_filled.mpn)

    def test_product_has_manufacturer(self):
        self.assertEqual(self.manufacturer, self.product_filled.manufacturer)

    def test_product_has_short_description(self):
        self.assertEqual("Short Description", self.product_filled.short_description)

    def test_product_has_long_description(self):
        self.assertEqual("Very long description about this product", self.product_filled.long_description)

    def test_product_has_product_type(self):
        self.assertEqual(self.product_type, self.product_filled.product_type)

    def test_product_has_screen_size(self):
        self.assertEqual(19.5, self.product_filled.screen_size)

    def test_product_has_stock_on_hand(self):
        self.assertEqual(100, self.product_filled.stock_on_hand)

    def test_product_has_cost_price(self):
        self.assertEqual(Decimal(50.00), self.product_filled.cost_price)

    def test_product_has_retail_price(self):
        self.assertEqual(Decimal(100.00), self.product_filled.retail_price)

    def test_product_has_id(self):
        self.assertEqual(123, self.product_filled.id)

    def test_product_without_long_description(self):
        self.assertIsNone(self.product_none.long_description)

    def test_product_without_screen_size(self):
        self.assertIsNone(self.product_none.screen_size)

    def test_product_without_id(self):
        self.assertIsNone(self.product_none.id)

    def test_get_longer_description__long_description_used(self):
        self.assertEqual(self.product_filled.long_description,
            self.product_filled.get_longer_description())

    def test_get_longer_description__short_description_used(self):
        self.assertEqual(self.product_none.short_description,
            self.product_none.get_longer_description())

    def test_is_out_of_stock__in_stock(self):
        self.assertFalse(self.product_filled.is_out_of_stock())

    def test_is_out_of_stock__out_of_stock(self):
        self.product_filled.stock_on_hand = 0
        self.assertTrue(self.product_filled.is_out_of_stock())

    def test_is_stock_low__high_price_high_stock(self):
        self.product_filled.retail_price = 100
        self.product_filled.stock_on_hand = 10
        self.assertFalse(self.product_filled.is_stock_low())

    def test_is_stock_low__high_price_low_stock(self):
        self.product_filled.retail_price = 100
        self.product_filled.stock_on_hand = 1
        self.assertTrue(self.product_filled.is_stock_low())

    def test_is_stock_low__low_price_high_stock(self):
        self.product_filled.retail_price = 20
        self.product_filled.stock_on_hand = 10
        self.assertFalse(self.product_filled.is_stock_low())

    def test_is_stock_low__low_price_low_stock(self):
        self.product_filled.retail_price = 20
        self.product_filled.stock_on_hand = 4
        self.assertTrue(self.product_filled.is_stock_low())

    # Tests added for discontinued products
    def test_has_discontinued__false_by_default(self):
        self.assertFalse(self.product_filled.discontinued)

    def test_has_discontinued__true(self):
        self.assertTrue(self.product_discontinued.discontinued)

    def test_should_hide_discontinued_product__not_discontinued(self):
        self.assertFalse(self.product_filled.should_hide_discontinued_product())

    def test_should_hide_discontinued_product__no_stock(self):
        self.product_discontinued.stock_on_hand = 0
        self.assertTrue(self.product_discontinued.should_hide_discontinued_product())

    def test_should_hide_discontinued_product__has_stock(self):
        self.product_discontinued.stock_on_hand = 2
        self.assertFalse(self.product_discontinued.should_hide_discontinued_product())

    # Regression test to make sure discontinued=None is translated to False
    def test_discontinued_is_none_translated_to_false(self):
        test_product = Product(
            "MPN456",
            self.manufacturer,
            "Discont. Prod",
            "Discontinued Product 456",
            self.product_type,
            24.1,
            0,
            Decimal(50.00),
            Decimal(25.00),
            discontinued=None
        )
        self.assertFalse(test_product.discontinued)