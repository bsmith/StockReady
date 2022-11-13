class Product:
    def __init__(self, mpn, manufacturer, short_description,
            long_description, product_type, screen_size, stock_on_hand, cost_price, retail_price, id=None):
        self.mpn = mpn
        self.manufacturer = manufacturer
        self.short_description = short_description
        self.long_description = long_description
        self.product_type = product_type
        self.screen_size = screen_size
        self.stock_on_hand = stock_on_hand
        self.cost_price = cost_price
        self.retail_price = retail_price
        self.id = id

    def get_longer_description(self):
        if self.long_description is None:
            return self.short_description
        else:
            return self.long_description