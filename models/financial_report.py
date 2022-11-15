class FinancialReport:
    def __init__(self):
        self.total_cost = 0
        self.total_retail = 0
        self.potential_profit = 0

    def calc_report(self, products):
        self.total_cost = sum(p.cost_price * p.stock_on_hand for p in products)
        self.total_retail = sum(p.retail_price * p.stock_on_hand for p in products)
        self.potential_profit = self.total_retail - self.total_cost