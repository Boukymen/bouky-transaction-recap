

def generate_transaction_recap():
    print("Select conversion direction:")
    print("1. 🅵🅲🅵🅰 to 🅳🅷")
    print("2. 🅳🅷y to 🅵🅲🅵🅰")
    choice = input("Enter your choice (1 or 2): ")

    # while loop to ensure valid input
    while choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        choice = input("Enter your choice (1 or 2): ")

    border = "=" * 48 #  60
    empty_line = "||" # + " " * 56 + "||"

    if choice == '1':

        # ask if the amount is in 🅵🅲🅵🅰 or 🅳🅷
        print("\nYou have selected 🅵🅲🅵🅰 to 🅳🅷 conversion.")
        print("|"
              "\nthe amount is in 🅵🅲🅵🅰 or 🅳🅷 ?")
        choice2 = input("Enter 1 for 🅵🅲🅵🅰 or 2 for 🅳🅷: ")
        while choice2 not in ['1', '2']:
            choice2 = input("Enter 1 for 🅵🅲🅵🅰 or 2 for 🅳🅷: ")


        # message = choice2 == 1 ? "You have selected 🅵🅲🅵🅰 to 🅳🅷 conversion." : "You have selected 🅳🅷 to 🅵🅲🅵🅰 conversion."
        message = "\nEnter your amount in 🅵🅲🅵🅰 : " if choice2 == '1' else "\nEnter your amount in 🅳🅷 : "
        amount = float(input(message))

        #  if the amount is not a valid number, prompt again
        while amount <= 0:
            print("Please enter a valid amount greater than 0.")
            amount = float(input(message))



        # ****************   Calculate fees and totals ****************
        if choice2 == '1':
            transfer_fee = amount * 0.025
            orange_fee = amount * 0.02
            total_inclusive_fees = (amount - transfer_fee - orange_fee) / 63
            transfer_inclusive_fees = (amount - transfer_fee) / 63
            total_exclusive_fess = amount / 63
        else:
            transfer_fee = amount * 0.025 * 63
            orange_fee = amount * 0.02 * 63
            total_exclusive_fess_temp = amount * 63
            total_inclusive_fees = amount - (amount * 0.025) - (amount * 0.02)
            transfer_inclusive_fees = amount - (amount * 0.025)
            total_exclusive_fess = amount
            amount = total_exclusive_fess_temp

        after_amount_space = 13 - len(str(int(amount)))
        transfer_fee_space = 14 - len(str(int(transfer_fee))) # 🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉


        print(f"\n{border}")
        print(empty_line)
        print("||" + " " * 17 + "\033[1m\033[4mTRANSFERT D'ARGENT\033[0m\033[0m") # + " " * 18 + "||")
        print("||" + " " * 18 + "\033[1m🅵🅲🅵🅰 ==> 🅳🅷\033[0m") # + " " * 21 + "||")
        print(empty_line)
        print(empty_line)
        print(f"|| \033[1mMONTANT\033[0m            =====> \033[93m\033[1m{amount:>10.2f} 🅵🅲🅵🅰\033[0m\033[0m") # + " " * after_amount_space + "||")
        print(empty_line)
        print(f"|| FRAIS DE TRANSFERT =====> \033[94m\033[1m{transfer_fee:>10.2f} 🅵🅲🅵🅰\033[0m\033[0m") # + " " * after_amount_space + "||")
        print(f"|| FRAIS ORANGE M.    =====> \033[94m\033[1m{orange_fee:>10.2f} 🅵🅲🅵🅰\033[0m\033[0m") # + " " * after_amount_space + "||")
        print(empty_line)
        print(empty_line)
        print("|| \033[1mTOTAL EN 🅳🅷\033[0m") # + " " * 44 + "||")
        print(f"||   FRAIS T. INCLUS   =====> \033[92m\033[1m{transfer_inclusive_fees:>10.2f} 🅳🅷\033[0m\033[0m") # + " " * transfer_fee_space + "||")
        print(f"||   TOUT FRAIS INCLUS =====> \033[92m\033[1m{total_inclusive_fees:>10.2f} 🅳🅷\033[0m\033[0m") # + " " * transfer_fee_space + "||")
        print(f"||   FRAIS EXCLUS    =====> \033[92m\033[1m{total_exclusive_fess:>10.2f} 🅳🅷\033[0m\033[0m") # + " " * transfer_fee_space + "||")
        # print(empty_line)
        print(empty_line)
        print(empty_line)
        print(border)

    elif choice == '2':

        # ask if the amount is in 🅵🅲🅵🅰 or 🅳🅷
        print("\nYou have selected 🅳🅷 to 🅵🅲🅵🅰 conversion.")
        print("|"
              "\nthe amount is in 🅳🅷 or 🅵🅲🅵🅰 ?")
        choice2 = input("Enter 1 for 🅳🅷 or 2 for 🅵🅲🅵🅰: ")
        while choice2 not in ['1', '2']:
            choice2 = input("Enter 1 for 🅳🅷 or 2 for 🅵🅲🅵🅰: ")


        message = "\nEnter your amount in 🅳🅷 : " if choice2 == '1' else "\nEnter your amount in 🅵🅲🅵🅰 : "
        amount = float(input(message))
        #  if the amount is not a valid number, prompt again
        while amount <= 0:
            print("Please enter a valid amount greater than 0.")
            amount = float(input(message))


        # ****************   Calculate fees and totals ****************
        if choice2 == '1':
            transfer_fee = amount * 0.025
            orange_fee = amount * 0.02
            total_inclusive_fees = (amount - transfer_fee - orange_fee) * 60
            transfer_inclusive_fees = (amount - transfer_fee) * 60
            total_exclusive_fess = amount * 60
        else:
            transfer_fee = amount * 0.025 / 60
            orange_fee = amount * 0.02 / 60
            total_exclusive_fess_temp = amount / 60
            total_inclusive_fees = amount - (amount * 0.025) - (amount * 0.02)
            transfer_inclusive_fees = amount - (amount * 0.025)
            total_exclusive_fess = amount
            amount = total_exclusive_fess_temp

        after_amount_space = 13 - len(str(int(amount)))
        transfer_fee_space = 9 - len(str(int(transfer_fee)))

        print(f"\n{border}")
        print(empty_line)
        print("||" + " " * 17 + "\033[1m\033[4mTRANSFERT D'ARGENT\033[0m\033[0m") # + " " * 18 + "||")
        print("||" + " " * 18 + "\033[1m🅳🅷 ==> 🅵🅲🅵🅰\033[0m") # + " " * 21 + "||")
        print(empty_line)
        print(empty_line)
        print(f"|| \033[1mMONTANT\033[0m            =====> \033[93m\033[1m{amount:>10.2f} 🅳🅷\033[0m\033[0m") # + " " * after_amount_space + "||")
        print(empty_line)
        print(f"|| FRAIS DE TRANSFERT =====> \033[94m\033[1m{transfer_fee:>10.2f} 🅳🅷\033[0m\033[0m") #+ " " * after_amount_space + "||")
        print(f"|| FRAIS ORANGE M.    =====> \033[94m\033[1m{orange_fee:>10.2f} 🅳🅷\033[0m\033[0m") #+ " " * after_amount_space + "||")
        print(empty_line)
        print(empty_line)
        print("|| \033[1mTOTAL EN 🅵🅲🅵🅰\033[0m") # + " " * 42 + "||")
        print(f"||   FRAIS T. INCLUS   =====> \033[92m\033[1m{transfer_inclusive_fees:>10.2f} 🅵🅲🅵🅰\033[0m\033[0m") # + " " * transfer_fee_space + "||")
        print(f"||   TOUT FRAIS INCLUS =====> \033[92m\033[1m{total_inclusive_fees:>10.2f} 🅵🅲🅵🅰\033[0m\033[0m") # + " " * transfer_fee_space + "||")
        print(f"||   FRAIS EXCLUS    =====> \033[92m\033[1m{total_exclusive_fess:>10.2f} 🅵🅲🅵🅰\033[0m\033[0m") # + " " * transfer_fee_space + "||")
        # print(empty_line)
        print(empty_line)
        print(empty_line)
        print(border)

    else:
        print("Invalid choice. Please select 1 or 2.")


# Run the function
generate_transaction_recap()
