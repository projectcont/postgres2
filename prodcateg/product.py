class Product(object):

    def set_pr (self, ean, title, price):

        self.title = title
        self.ean = ean
        self.price = price

    def __str__(self):
        return f' ean={self.ean} title={self.title} price={self.price}'











