if __name__ == "__main__":
    print("Welcome to the tip Calculator.")
    total = float(input("What was the total bill? "))
    people = int(input("How many people split the bill? "))
    tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

    total_amount = total + ((total/100)*tip)
    total_amount_pp = total_amount/people
    print("Each person should pay: $" + str(total_amount_pp))