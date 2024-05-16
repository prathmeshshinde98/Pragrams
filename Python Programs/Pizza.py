if __name__ == "__main__":
    print("Thank you for choosing Python Pizza!")
    size = input("What size of Pizza do you want? S, M, or L ")
    add_pepperoni = input("Add pepporoni? Y/N ")
    extra_cheese = input("Add extra cheese? Y/N ")
    price = 0

    if size == 'S':
        price = price + 15
        if add_pepperoni == 'Y':
            price = price + 2
    elif size == 'M':
        price = price + 20
        if add_pepperoni == 'Y':
            price = price + 3
    elif size == 'L':
        price = price + 25
        if add_pepperoni == 'Y':
            price = price + 2

    if extra_cheese == 'Y':
        price = price + 1

    print("Your order price is $" + str(price))
    print("Your order is being prepared!")


