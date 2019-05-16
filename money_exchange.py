
class Money:

    exchange = {'EUR_USD': 1.2, 'EUR_EUR': 1,
                'USD_EUR': 0.8, 'EUR_CHF': 0.9, 'CHF_EUR': 1.1}

    def __init__(self, budget=0):
        self.budget = budget

    def set_budget(self, budget):
        self.budget = budget

    def get_budget(self):
        return self.budget

    def get_amount_by_currency(self, currency):
        return self.budget[currency]

    def get_total_by_currency(self, currency):
        total = 0
        for key, value in sorted(self.budget.items()):
            key_exchange = self.create_key_value(currency)
            for i in range(0, len(key_exchange)):
                exchange_value = self.exchange[key_exchange[i]]
                total += (value * exchange_value)
        return total

    def get_exchange(self, from_to):
        return self.exchange[from_to]

    def create_key_value(self, to):
        key_value = []
        for key in self.budget.keys():
            key_value.append('_'.join([key, to]))
        return key_value
