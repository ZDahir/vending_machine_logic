    # (1) Print welcome message and set current amount to 0.
    soda_dollar = 0.0
    print("Soda Vending Machine")
    # (2) Print out the current amount (see below).
    print(f"Current amount ${soda_dollar:.2f} out of $1.00")
    # (3) Ask the user to input a selection between 1-5, where each selection corresponds to a Canadian coin as follows: 1 – Toonie ($2); 2 – Loonie ($1); 3 – Quarter ($0.25); 4 – Dime ($0.10); 5 – Nickel ($0.05)1
    soda_dollar_input = input(
        """Insert Coin
1. Toonie ($2.00)
2. Loonie ($1.00)
3. Quarter ($0.25)
4. Dime ($0.10)
5. Nickel ($0.05)
Selection [1-5]? """
    )
    if soda_dollar_input.isnumeric():
        soda_dollar_input = int(soda_dollar_input)
    # (5) Check the user's input to see what amount they entered. If they select a number that is not 1-5, print out "Invalid Selection." If a valid number is entered, add the corresponding amount to the current amount.

    while soda_dollar_input not in [1, 2, 3, 4, 5]:
        print("Invalid selection!")
        soda_dollar_input = input(
            """Insert Coin
1. Toonie ($2.00)
2. Loonie ($1.00)
3. Quarter ($0.25)
4. Dime ($0.10)
5. Nickel ($0.05)
Selection [1-5]? """
        )
        if soda_dollar_input.isnumeric():
            soda_dollar_input = int(soda_dollar_input)

    if soda_dollar_input == 1:
        soda_dollar = 2
    elif soda_dollar_input == 2:
        soda_dollar = 1
    elif soda_dollar_input == 3:
        soda_dollar = 0.25
    elif soda_dollar_input == 4:
        soda_dollar = 0.1
    elif soda_dollar_input == 5:
        soda_dollar = 0.05
    # (6) If the current amount is less than $1.00, go back to (2)
    while soda_dollar < 1:
        print(f"Current amount ${soda_dollar:.2f} out of $1.00")
        soda_dollar_input = input(
        """Insert Coin
1. Toonie ($2.00)
2. Loonie ($1.00)
3. Quarter ($0.25)
4. Dime ($0.10)
5. Nickel ($0.05)
Selection [1-5]? """
        )
        if soda_dollar_input.isnumeric():
            soda_dollar_input = int(soda_dollar_input)
        # (5) Check the user's input to see what amount they entered. If they select a number that is not 1-5, print out "Invalid Selection." If a valid number is entered, add the corresponding amount to the current amount.

        while soda_dollar_input not in [1, 2, 3, 4, 5]:
            print(f"Current amount ${soda_dollar:.2f} out of $1.00")
            soda_dollar_input = input(
            """Insert Coin
1. Toonie ($2.00)
2. Loonie ($1.00)
3. Quarter ($0.25)
4. Dime ($0.10)
5. Nickel ($0.05)
Selection [1-5]? """
            )
            if soda_dollar_input.isnumeric():
                soda_dollar_input = int(soda_dollar_input)

        if soda_dollar_input == 1:
            soda_dollar = soda_dollar + 2
        elif soda_dollar_input == 2:
            soda_dollar = soda_dollar +  1
        elif soda_dollar_input == 3:
            soda_dollar = soda_dollar +  0.25
        elif soda_dollar_input == 4:
            soda_dollar = soda_dollar +  0.1
        elif soda_dollar_input == 5:
            soda_dollar = soda_dollar +  0.05


    if soda_dollar  > 1:
        print(f"Current amount ${soda_dollar:.2f} out of $1.00")
        print(f"Total amount provided: ${soda_dollar:.2f}")
        print("Thank you for your purchase.")
        change = soda_dollar - 1
        print(f"Please take your change ${change:.2f}")
    elif soda_dollar == 1:
        print(f"Current amount ${soda_dollar:.2f} out of $1.00")
        print(f"Total amount provided: ${soda_dollar:.2f}")
        print("Thank you for your purchase.")

