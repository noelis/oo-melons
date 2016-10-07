from random import randint
"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Covers all orders, domestic and international"""
    
    def __init__(self, species, qty, country_code=None, order_type=None, tax=None):
        self.species = species
        self.qty = qty
        # self.country_code = country_code
        # self.order_type = order_type
        # self.tax = tax
        self.shipped = False

    def mark_shipped(self):
        """Set shipped to True"""

        self.shipped = True

    def get_base_price(self):
        base_price = randint(5, 10)
        return base_price

    def get_total(self):
        base_price = self.get_base_price()
        if self.species.lower() == "christmas":
            base_price = base_price * 1.5
        if self.order_type == "international" and self.qty < 10:
            total = ((1 + self.tax) * self.qty * base_price) + 3
        else:
            total = (1 + self.tax) * self.qty * base_price
        return total

class DomesticMelonOrder(AbstractMelonOrder):
    country_code = "USA"
    order_type = "domestic"
    tax = 0.08
    # def __init__(self, species, qty):
    #     super(DomesticMelonOrder, self).__init__(species, qty, "USA", "domestic", 0.08)

class InternationalMelonOrder(AbstractMelonOrder):
    order_type = "international"
    tax = 0.17
    # def __init__(self, species, qty, country_code):
    #     super(InternationalMelonOrder, self).__init__(species, qty, country_code, 
    #         "international", 0.17)

class GovernmentMelonOrder(DomesticMelonOrder):
    passed_inspection = False
    # def __init__(self, species, qty):
    #     super(GovernmentMelonOrder, self).__init__(species, qty, "USA", "domestic", 0.08)
    
    def mark_inspection(self, passed):
        self.passed_inspection = passed