class Customer:
    orders = [10, 20, 30, 40, 50]

    def getTotalAmount(self):
        x = 0
        for amount in self.orders:
            x += amount
        return x


def main():
    customer = Customer()
    amount = customer.getTotalAmount()
    print("Total amount:", amount)


if __name__ == '__main__':
    main()
