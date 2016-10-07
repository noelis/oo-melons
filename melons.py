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

    def get_total(self):

        # base_price = 7.5 if self.species.lower() == 'christmas' else 5
        if self.species.lower() == "christmas":
            base_price = 7.5
        else:
            base_price = 5
        if self.order_type == "international" and self.qty < 10:
            total = ((1 + self.tax) * self.qty * base_price) + 3
        else:
            total = (1 + self.tax) * self.qty * base_price
        return total

class DomesticMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, "USA", "domestic", 0.08)

class InternationalMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, country_code, 
            "international", 0.17)

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty, "USA", "domestic", 0.08)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed