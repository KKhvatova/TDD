from unittest import TestCase
import money_exchange


class MoneyTest(TestCase):

    def test_set_budget(self):
        new_money = money_exchange.Money({'EUR': 10})
        # new_money.set_budget({'EUR': 10})
        self.assertEqual(new_money.get_budget(), {'EUR': 10})

    def test_get_amount_by_currency(self):
        new_money = money_exchange.Money()
        new_money.set_budget({'EUR': 10})
        currency = 'EUR'
        self.assertEqual(new_money.get_amount_by_currency(currency), 10)

    def test_get_total_by_currency(self):
        new_money = money_exchange.Money()
        new_money.set_budget({'USD': 20})
        currency = 'EUR'
        self.assertEqual(new_money.get_total_by_currency(
            currency), (20*0.8))

    def test_get_exchange(self):
        new_money = money_exchange.Money()
        from_to = 'EUR_USD'
        self.assertEqual(new_money.get_exchange(from_to), 1.2)

    def test_create_key_value(self):
        new_money = money_exchange.Money()
        new_money.set_budget({'USD': 20})
        to = 'CHF'
        self.assertEqual(new_money.create_key_value(to), ['USD_CHF'])
