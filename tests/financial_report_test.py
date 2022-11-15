from decimal import Decimal
import unittest

from models.financial_report import FinancialReport
from models.manufacturer import Manufacturer
from models.product import Product
from models.product_type import ProductType

class TestFinancialReport(unittest.TestCase):
    def setUp(self):
        # Associated objects
        self.manufacturer = Manufacturer("Full Name of Manufactuer",
            "Brand", None, None, None, None)
        self.product_type = ProductType("Soundbar")

        self.product1 = Product(
            "MPN123",
            self.manufacturer,
            "Short Description",
            None,
            self.product_type,
            None,
            100,
            Decimal(50.00),
            Decimal(100.00),
            id=123
        )

    def test_calc_report(self):
        financial_report = FinancialReport()
        financial_report.calc_report([self.product1])
        self.assertEqual(5000, financial_report.total_cost)
        self.assertEqual(10000, financial_report.total_retail)
        self.assertEqual(5000, financial_report.potential_profit)