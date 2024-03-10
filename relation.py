class Relations:
    def __init__(self, person1m, person2):
        self.__person1 = person1m
        self.__person2 = person2
        self.__amountowed = 0
        self.__payments = []

    def addpayment(self, person1, person2, amount, reason):
        if self.__person1 == person1:
            self.__amountowed += amount
            self.__payments.append(self.__person1 + " paid for " + self.__person2 + " by amount of $" + str(amount) + " for the " + reason)
        elif self.__person1 == person2:
            self.__amountowed -= amount
            self.__payments.append(self.__person2 + " paid for " + self.__person1 + " by amount of $" + str(amount) + " for the " + reason)
        else:
            raise "not the correct relation"

    def getPerson1(self):
        return self.__person1

    def getPerson2(self):
        return self.__person2

    def getAmountOwed(self):
        return self.__amountowed

    def settle(self):
        self.__amountowed = 0

    def printPayments(self, number):
        if number == -1:
            for i in self.__payments:
                print(i)
        elif number > len(self.__payments) :
            raise "You have entered a number greater than the number of payments"
        else:
            for i in range(number):
                print(self.__payments[len(self.__payments)-1-i])

    def __str__(self) -> str:
        if self.__amountowed > 0:
            return str(self.__person1) + " owes " + str(self.__person2) + " $" + str(self.__amountowed)
        elif self.__amountowed < 0:
            return str(self.__person2) + " owes " + str(self.__person1) + " $" + str(abs(self.__amountowed))
        else:
            return str(self.__person1) + " does not owe " + str(self.__person2) + " anything"

# class main:
#     x = Relations("John", "Amy")
#     x.addpayment("John", "Amy", 65, "food")
#     x.addpayment("Amy", "John", 65, "food")
#     x.addpayment("Amy", "John", 65, "food")
#     x.addpayment("Amy", "John", 65, "food")
#     x.addpayment("Amy", "John", 65, "food")
#     x.addpayment("John", "Amy", 15, "food")
#     print(x)
#     x.printPayments(-1)