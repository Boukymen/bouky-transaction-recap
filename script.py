

def generate_transaction_recap():
    print("Select conversion direction:")
    print("1. FCFA to DH")
    print("2. DH to FCFA")
    choice = input("Enter your choice (1 or 2): ")

    # while loop to ensure valid input
    while choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        choice = input("Enter your choice (1 or 2): ")

    border = "=" * 47 #  60
    empty_line = "||" # + " " * 56 + "||"

    if choice == '1':

        # ask if the amount is in FCFA or DH
        print("\nYou have selected FCFA to DH conversion.")
        print("|"
              "\nthe amount is in FCFA or DH ?")
        choice2 = input("Enter 1 for FCFA or 2 for DH: ")
        while choice2 not in ['1', '2']:
            choice2 = input("Enter 1 for FCFA or 2 for DH: ")


        # message = choice2 == 1 ? "You have selected FCFA to DH conversion." : "You have selected DH to FCFA conversion."
        message = "\nEnter your amount in FCFA : " if choice2 == '1' else "\nEnter your amount in DH : "
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
            total_exclusive_fess = amount / 63
        else:
            transfer_fee = amount * 0.025 * 63
            orange_fee = amount * 0.02 * 63
            total_exclusive_fess_temp = amount * 63
            total_inclusive_fees = amount - (amount * 0.025) - (amount * 0.02)
            total_exclusive_fess = amount
            amount = total_exclusive_fess_temp

        after_amount_space = 13 - len(str(int(amount)))
        transfer_fee_space = 14 - len(str(int(transfer_fee)))


        print(f"\n{border}")
        print(empty_line)
        print("||" + " " * 20 + "TRANSFERT D'ARGENT") # + " " * 18 + "||")
        print("||" + " " * 24 + "FCFA ==> DH") # + " " * 21 + "||")
        print(empty_line)
        print(empty_line)
        print(f"|| MONTANT            =====>   {amount:>10.2f} FCFA") # + " " * after_amount_space + "||")
        print(empty_line)
        print(f"|| FRAIS DE TRANSFERT  =====>   {transfer_fee:>10.2f} FCFA") # + " " * after_amount_space + "||")
        print(f"|| FRAIS ORANGE M.     =====>   {orange_fee:>10.2f} FCFA") # + " " * after_amount_space + "||")
        print(empty_line)
        print(empty_line)
        print("|| TOTAL EN DH") # + " " * 44 + "||")
        print(f"||   FRAIS INCLUS    =====>   {total_inclusive_fees:>10.2f} DH") # + " " * transfer_fee_space + "||")
        print(f"||   FRAIS EXCLUS    =====>   {total_exclusive_fess:>10.2f} DH") # + " " * transfer_fee_space + "||")
        print(empty_line)
        print(empty_line)
        print(empty_line)
        print(border)

    elif choice == '2':

        # ask if the amount is in FCFA or DH
        print("\nYou have selected DH to FCFA conversion.")
        print("|"
              "\nthe amount is in DH or FCFA ?")
        choice2 = input("Enter 1 for DH or 2 for FCFA: ")
        while choice2 not in ['1', '2']:
            choice2 = input("Enter 1 for DH or 2 for FCFA: ")


        message = "\nEnter your amount in DH : " if choice2 == '1' else "\nEnter your amount in FCFA : "
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
            total_exclusive_fess = amount * 60
        else:
            transfer_fee = amount * 0.025 / 60
            orange_fee = amount * 0.02 / 60
            total_exclusive_fess_temp = amount / 60
            total_inclusive_fees = amount - (amount * 0.025) - (amount * 0.02)
            total_exclusive_fess = amount
            amount = total_exclusive_fess_temp

        after_amount_space = 13 - len(str(int(amount)))
        transfer_fee_space = 9 - len(str(int(transfer_fee)))

        print(f"\n{border}")
        print(empty_line)
        print("||" + " " * 20 + "TRANSFERT D'ARGENT") # + " " * 18 + "||")
        print("||" + " " * 24 + "DH ==> FCFA") # + " " * 21 + "||")
        print(empty_line)
        print(empty_line)
        print(f"|| MONTANT            =====>   {amount:>10.2f} DH") # + " " * after_amount_space + "||")
        print(empty_line)
        print(f"|| FRAIS DE TRANSFERT =====>   {transfer_fee:>10.2f} DH") #+ " " * after_amount_space + "||")
        print(f"|| FRAIS ORANGE M.    =====>   {orange_fee:>10.2f} DH") #+ " " * after_amount_space + "||")
        print(empty_line)
        print(empty_line)
        print("|| TOTAL EN FCFA") # + " " * 42 + "||")
        print(f"||   FRAIS INCLUS     =====>   {total_inclusive_fees:>10.2f} FCFA") # + " " * transfer_fee_space + "||")
        print(f"||   FRAIS EXCLUS     =====>   {total_exclusive_fess:>10.2f} FCFA") # + " " * transfer_fee_space + "||")
        print(empty_line)
        print(empty_line)
        print(empty_line)
        print(border)

    else:
        print("Invalid choice. Please select 1 or 2.")


# Run the function
generate_transaction_recap()
