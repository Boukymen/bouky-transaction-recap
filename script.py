def generate_transaction_recap():
    print("Select conversion direction:")
    print("1. FCFA to DH")
    print("2. DH to FCFA")
    choice = input("Enter your choice (1 or 2): ")

    # while loop to ensure valid input
    while choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        amount = float(input("Enter amount in FCFA: "))
        transfer_fee = amount * 0.025
        orange_fee = amount * 0.02
        total_in_dh_inclusive = (amount - transfer_fee - orange_fee) / 63
        total_in_dh_exclusive = amount / 63

        print("\n" + "="*60)
        print("||" + " " * 56 + "||")
        print("||" + " " * 20 + "TRANSFERT D'ARGENT" + " " * 19 + "||")
        print("||" + " " * 24 + "FCFA ==> DH" + " " * 21 + "||")
        print("||" + " " * 56 + "||")
        print("||" + " " * 56 + "||")
        print(f"|| MONTANT                 =====>   {amount:>10.2f} FCFA       ||")
        print("||" + " " * 56 + "||")
        print(f"|| FRAIS DE TRANSFERT      =====>   {transfer_fee:>10.2f} FCFA          ||")
        print(f"|| FRAIS ORANGE M.         =====>   {orange_fee:>10.2f} FCFA        ||")
        print("||" + " " * 56 + "||")
        print("||" + " " * 56 + "||")
        print("|| TOTAL EN DH" + " " * 43 + "||")
        print(f"||   FRAIS INCLUS          =====>   {total_in_dh_inclusive:>10.2f} DH   ||")
        print(f"||   FRAIS EXCLUS          =====>   {total_in_dh_exclusive:>10.2f} DH   ||")
        print("||" + " " * 56 + "||")
        print("||" + " " * 56 + "||")
        print("||" + " " * 56 + "||")
        print("=" * 60)

    elif choice == '2':
        amount = float(input("Enter amount in DH: "))
        transfer_fee = amount * 0.025
        orange_fee = amount * 0.02
        total_in_fcfa_inclusive = (amount - transfer_fee - orange_fee) * 60
        total_in_fcfa_exclusive = amount * 60

        print("\n" + "="*60)
        print("||" + " " * 56 + "||")
        print("||" + " " * 20 + "TRANSFERT D'ARGENT" + " " * 19 + "||")
        print("||" + " " * 24 + "DH ==> FCFA" + " " * 21 + "||")
        print("||" + " " * 56 + "||")
        print("||" + " " * 56 + "||")
        print(f"|| MONTANT                 =====>   {amount:>10.2f} DH     ||")
        print("||" + " " * 56 + "||")
        print(f"|| FRAIS DE TRANSFERT      =====>   {transfer_fee:>10.2f} DH     ||")
        print(f"|| FRAIS ORANGE M.         =====>   {orange_fee:>10.2f} DH     ||")
        print("||" + " " * 56 + "||")
        print("||" + " " * 56 + "||")
        print("|| TOTAL EN FCFA" + " " * 41 + "||")
        print(f"||   FRAIS INCLUS          =====>   {total_in_fcfa_inclusive:>10.2f} FCFA ||")
        print(f"||   FRAIS EXCLUS          =====>   {total_in_fcfa_exclusive:>10.2f} FCFA ||")
        print("||" + " " * 56 + "||")
        print("||" + " " * 56 + "||")
        print("||" + " " * 56 + "||")
        print("=" * 60)

    else:
        print("Invalid choice. Please select 1 or 2.")

# Run the function
generate_transaction_recap()
