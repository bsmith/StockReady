import unittest
from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):
    def setUp(self):
        # Test all fields filled
        self.manufacturer1 = Manufacturer(
            "Full Name of Manufacturer",
            "Brand",
            "https://web.site/corp",
            "+447700900123",
            "https://web.site/uk/buybuybuy",
            "08081570123",
            id=123
        )
        # Test some fields may be None
        self.manufacturer2 = Manufacturer(
            "Full Name of Manufactuer",
            "Brand",
            None,
            None,
            None,
            None,
        )

    def test_manufacturer_has_full_name(self):
        self.assertEqual("Full Name of Manufacturer", self.manufacturer1.full_name)

    def test_manufacturer_has_short_brand_name(self):
        self.assertEqual("Brand", self.manufacturer1.short_brand_name)

    def test_manufacturer_has_trade_website(self):
        self.assertEqual("https://web.site/corp", self.manufacturer1.trade_website)

    def test_manufacturer_has_trade_telephone(self):
        self.assertEqual("+447700900123", self.manufacturer1.trade_telephone)

    def test_manufacturer_has_customer_website(self):
        self.assertEqual("https://web.site/uk/buybuybuy", self.manufacturer1.customer_website)

    def test_manufacturer_has_customer_telephone(self):
        self.assertEqual("08081570123", self.manufacturer1.customer_telephone)

    def test_manufacturer_has_id(self):
        self.assertEqual(123, self.manufacturer1.id)

    def test_manufacturer_without_trade_website(self):
        self.assertIsNone(self.manufacturer2.trade_website)

    def test_manufacturer_without_trade_telephone(self):
        self.assertIsNone(self.manufacturer2.trade_telephone)

    def test_manufacturer_without_customer_website(self):
        self.assertIsNone(self.manufacturer2.customer_website)

    def test_manufacturer_without_customer_telephone(self):
        self.assertIsNone(self.manufacturer2.customer_telephone)

    def test_manufacturer_without_id(self):
        self.assertIsNone(self.manufacturer2.id)

    def test_has_trade_contacts(self):
        self.assertTrue(self.manufacturer1.has_trade_contacts())
        self.assertFalse(self.manufacturer2.has_trade_contacts())

    def test_has_customer_contacts(self):
        self.assertTrue(self.manufacturer1.has_customer_contacts())
        self.assertFalse(self.manufacturer2.has_customer_contacts())