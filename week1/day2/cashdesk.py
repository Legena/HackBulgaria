from itertools import combinations


class CashDesk():
    def __init__(self, money={100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}):
        self.money = money

    def take_money(self, money_taken):
        for note in money_taken:
            self.money[note] += money_taken[note]

    def total(self):
        sum = 0
        for note in self.money:
            sum += note * self.money[note]
        return sum

    def can_withdraw_money(self, amount_of_money):
        lis = []
        for note in self.money:
            for count in range(0, self.money[note]):
                lis.append(note)
        for i in range(1, len(lis)+1):
            for comb in combinations(lis, i):
                if (sum(comb) == amount_of_money):
                    return True
        return False


def main():
    my_cash_desk = CashDesk()
    my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
    print(my_cash_desk.total())
    print(my_cash_desk.can_withdraw_money(70))

if __name__ == "__main__":
    main()