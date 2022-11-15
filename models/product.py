class Product:
    def __init__(self, mpn, manufacturer, short_description,
            long_description, product_type, screen_size,
            stock_on_hand, cost_price, retail_price,
            discontinued=False, id=None):
        self.mpn = mpn
        self.manufacturer = manufacturer
        self.short_description = short_description
        self.long_description = long_description
        self.product_type = product_type
        self.screen_size = screen_size
        self.stock_on_hand = stock_on_hand
        self.cost_price = cost_price
        self.retail_price = retail_price
        self.discontinued = False if discontinued is None else discontinued
        self.id = id

    def get_longer_description(self):
        if self.long_description is None:
            return self.short_description
        else:
            return self.long_description

    def is_out_of_stock(self):
        return self.stock_on_hand == 0

    def is_stock_low(self):
        if self.retail_price >= 100:
            return self.stock_on_hand == 1
        else:
            return 1 <= self.stock_on_hand < 6

    def calculate_markup(self):
        return (self.retail_price - self.cost_price) / self.cost_price

    def calculate_profit_margin(self):
        return (self.retail_price - self.cost_price) / self.retail_price

    def should_hide_discontinued_product(self):
        if not self.discontinued:
            return False
        return not (self.stock_on_hand > 0)
