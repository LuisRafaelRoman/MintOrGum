print("=== Freshener Buddy ===")

def Mint_Gum_system():
    # Choose your brand
    print("Please choose your brand below:")
    print("1. Mentos")
    print("2. Doublemint")
    Brand_choice = input("Enter 1 or 2: ")

    if Brand_choice == "1":
        brand = "Mentos"
    elif Brand_choice == "2":
        brand = "Doublemint"
    else:
        print("Choice is invalid. Defaulting to Mentos.")
        brand = "Mentos"

    # Choose your product type
    print("\nChoose your product type:")
    print("1. Sugarfree Mint")
    print("2. Sugarfree Gum")
    Product_choice = input("Enter 1 or 2: ")

    if Product_choice == "1":
        product = "Sugarfree Mints"
    elif Product_choice == "2":
        product = "Sugarfree Gum"
    else:
        print("Choice is invalid. Defaulting to Sugarfree Mints.")
        product = "Sugarfree Mints"

    # Choose your flavor
    print("\nChoose your flavor:")
    print("1. Peppermint")
    print("2. Spearmint")
    print("3. Winterfrost")
    print("4. Fruity Mint")
    print("5. Others")
    Flavor_choice = input("Please Enter 1-5: ")
    
    if Flavor_choice == "1":
        flavor = "Peppermint"
    elif Flavor_choice == "2":
        flavor = "Spearmint"
    elif Flavor_choice == "3":
        flavor = "Winterfrost"
    elif Flavor_choice == "4":
        fruity_flavor = input("Enter fruity flavor (e.g., Strawberry, Grape, Mango): ")
        flavor = f"Fruity Mint ({fruity_flavor})"
    elif Flavor_choice == "5":
        flavor = input("Enter other flavor: ")
    else:
        print("Choice is invalid. Defaulting to Peppermint.")
        flavor = "Peppermint"

    # If Doublemint Sugarfree Mints -> Choose container size
    container_size = None
    if brand == "Doublemint" and product == "Sugarfree Mints":
        print("\nChoose your container size:")
        print("1. Small Pocket Container")
        print("2. Regular Pocket Container")
        size_choice = input("Enter 1 or 2: ")

        if size_choice == "1":
            container_size = "Small Pocket Container"
        elif size_choice == "2":
            container_size = "Regular Pocket Container"
        else:
            print("Invalid choice. Defaulting to Regular Pocket Container.")
            container_size = "Regular Pocket Container"

    # If you choose gum -> ask gum type
    gum_type = None
    if product == "Sugarfree Gum":
        while True:
            print("\nChoose your gum type:")
            print("1. Pellets")
            print("2. Sticks")
            print("3. Pod")
            Gum_choice = input("Enter 1-3: ")

            if Gum_choice == "1":
                gum_type = "Pellets"
                break
            elif Gum_choice == "2":
                gum_type = "Sticks"
                break
            elif Gum_choice == "3":
                gum_type = "Pod"
                break
            else:
                print("Choice is invalid. Try again.")

    # Final details
    print("\n========== Purchase Summary ==========")
    print(f"Brand: {brand}")
    print(f"Product: {product}")
    print(f"Flavor: {flavor}")
    if container_size:
        print(f"Container Size: {container_size}")
    if gum_type:
        print(f"Gum Type: {gum_type}")
    print("====================================")
    print("Enjoy!!!\n")


# Main vending machine loop
while True:
    Mint_Gum_system()
    again = input("Would you like to buy again? (yes/no): ").strip().lower()
    if again not in ["yes", "y"]:
        print("Thank you for using Freshener Buddy! Come again")
        break
