# 1. Railway Ticket Booking System

# Railway Ticket Booking System

trains = {
    1: ("Bengaluru Express", 250),
    2: ("Hubli Express", 180),
    3: ("Mysore Express", 200),
    4: ("Chennai Express", 350)
}

print("===== RAILWAY TICKET BOOKING SYSTEM =====")

print("\nAvailable Trains:")

for key, value in trains.items():
    print(key, value[0], "- Rs.", value[1])

name = input("\nEnter passenger name: ")
age = int(input("Enter passenger age: "))

choice = int(input("Select train number: "))

if choice in trains:

    tickets = int(input("Enter number of tickets: "))

    if tickets > 0:
        train_name, price = trains[choice]

        total = price * tickets

        print("\n===== BOOKING SUMMARY =====")
        print("Passenger Name:", name)
        print("Passenger Age:", age)
        print("Train Name:", train_name)
        print("Number of Tickets:", tickets)
        print("Total Amount: Rs.", total)
        print("Booking successful!")

    else:
        print("Please enter a valid ticket quantity.")

else:
    print("Invalid train selection.")


# 2. Electricity Bill Calculator


# Electricity Bill Calculator

print("===== ELECTRICITY BILL CALCULATOR =====")

name = input("Enter customer name: ")
customer_id = input("Enter customer ID: ")
units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units entered.")

else:
    if units <= 100:
        bill = units * 2

    elif units <= 200:
        bill = (100 * 2) + ((units - 100) * 3)

    else:
        bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    print("\n===== ELECTRICITY BILL =====")
    print("Customer Name:", name)
    print("Customer ID:", customer_id)
    print("Units Consumed:", units)
    print("Total Electricity Bill: Rs.", bill)

    print("Thank you!")
