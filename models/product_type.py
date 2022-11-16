class ProductType:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        if self.id:
            return f"ProductType({self.name!r}, id={self.id!r})"
        else:
            return f"ProductType({self.name!r})"