import math, unittest

def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result

class StatmentTest(unittest.TestCase):

    def test_statment_empty(self):
        self.assertEqual("Statement for Wojciech\nAmount owed is $0.00\nYou earned 0 credits\n", statement({"customer": "Wojciech", "performances": []}, {}))

    def test_statment_tragedy_audience_less_than_30(self):
        self.assertEqual("Statement for Wojcieszko\n Hamlet: $400.00 (25 seats)\nAmount owed is $400.00\nYou earned 0 credits\n", statement({"customer": "Wojcieszko", "performances": [{"playID": "hamlet", "audience": 25}]}, {"hamlet": {"name": "Hamlet", "type": "tragedy"}}))

    def test_statment_tragedy_audience_30(self):
        self.assertEqual("Statement for Wojcieszko\n Hamlet: $400.00 (30 seats)\nAmount owed is $400.00\nYou earned 0 credits\n", statement({"customer": "Wojcieszko", "performances": [{"playID": "hamlet", "audience": 30}]}, {"hamlet": {"name": "Hamlet", "type": "tragedy"}}))

    def test_statment_tragedy_audience_more_than_30(self):
        self.assertEqual("Statement for Wojcieszko\n Hamlet: $600.00 (50 seats)\nAmount owed is $600.00\nYou earned 20 credits\n", statement({"customer": "Wojcieszko", "performances": [{"playID": "hamlet", "audience": 50}]}, {"hamlet": {"name": "Hamlet", "type": "tragedy"}}))

    def test_statment_comedy_tragedy_audience_less_than_20(self):
        self.assertEqual("Statement for Wojcieszko\n As You Like It: $345.00 (15 seats)\nAmount owed is $345.00\nYou earned 3 credits\n", statement({"customer": "Wojcieszko", "performances": [{"playID": "as-like", "audience": 15}]}, {"as-like": {"name": "As You Like It", "type": "comedy"}}))

    def test_statment_comedy_audience_20(self):
        self.assertEqual("Statement for Wojcieszko\n As You Like It: $360.00 (20 seats)\nAmount owed is $360.00\nYou earned 4 credits\n", statement({"customer": "Wojcieszko", "performances": [{"playID": "as-like", "audience": 20}]}, {"as-like": {"name": "As You Like It", "type": "comedy"}}))

    def test_statment_comedy_audience_more_than_20(self):
        self.assertEqual("Statement for Wojcieszko\n As You Like It: $500.00 (25 seats)\nAmount owed is $500.00\nYou earned 5 credits\n", statement({"customer": "Wojcieszko", "performances": [{"playID": "as-like", "audience": 25}]}, {"as-like": {"name": "As You Like It", "type": "comedy"}}))

    def test_statment_plays_error(self):
        self.assertRaises(KeyError, statement, {"customer": "Wojcieszko"}, None)

    def test_statment_invoice_plays_error(self):
        self.assertRaises(KeyError, statement, {}, {})

    def test_statment_play_type_error(self):
        self.assertRaises(KeyError, statement, {"customer": "Wojcieszko", "performances": [{"playID": "as-like","audience":"dwa"}]}, {"hamlet": {"brak":"kurde"}})


if __name__ == "__main__":
    unittest.main()