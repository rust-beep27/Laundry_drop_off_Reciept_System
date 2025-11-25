print("=== Laundry Shop System ===")

while True:
    name = input("Enter customer name: ")
    weight = float(input("Enter laundry weight (kg): "))

    price_per_kg = 25

    total = weight * price_per_kg

    print("Payment Method:")
    print("1 - Cash")
    print("2 - Gcash")
    mode = input("Enter choice (1/2): ")

    while mode not in ["1","2"]:
        mode=input("Invalid choice please Enter Again:")
    if mode == "1":
        payment = "Cash"
    elif mode == "2":
        payment = "GCash"
    else:
        break

    print("\n===== LAUNDRY RECEIPT =====")
    print(f"Customer Name: {name}")
    print(f"Laundry Weight: {weight} kg")
    print(f"Price per kg: {price_per_kg}")
    print(f"Total Amount: {total}")
    print(f"Payment Method: {payment}")
    print("===========================\n")

    again = input("Do another transaction? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using the Laundry System!")
        break
