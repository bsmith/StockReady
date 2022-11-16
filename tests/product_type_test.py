import unittest
from models.product_type import ProductType

class TestProductType(unittest.TestCase):
    def setUp(self):
        # Test with optional fields filled
        self.product_type_filled = ProductType("Television", id=5)
        # Test without optional fields filled
        self.product_type_none = ProductType("Soundbar")

    def test_product_type_has_name(self):
        self.assertEqual("Television", self.product_type_filled.name)

    def test_product_type_has_id(self):
        self.assertEqual(5, self.product_type_filled.id)

    def test_product_type_without_id(self):
        self.assertIsNone(self.product_type_none.id)