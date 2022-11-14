class Manufacturer:
    def __init__(self, full_name, short_brand_name,
            trade_website=None, trade_telephone=None,
            customer_website=None, customer_telephone=None,
            id=None):
        self.full_name = full_name
        self.short_brand_name = short_brand_name
        self.trade_website = trade_website
        self.trade_telephone = trade_telephone
        self.customer_website = customer_website
        self.customer_telephone = customer_telephone
        self.id = id

    def has_trade_contacts(self):
        return self.trade_website or self.trade_telephone

    def has_customer_contacts(self):
        return self.customer_website or self.customer_telephone