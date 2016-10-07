"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Covers all orders, domestic and international"""
    
    def __init__(self, species, qty, country_code, order_type, tax):
        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def mark_shipped(self):
        """Set shipped to True"""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, "USA", "domestic", 0.08)

    def get_total(self):
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

class InternationalMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, country_code, 
            "international", 0.17)

    def get_total(self):
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total
       