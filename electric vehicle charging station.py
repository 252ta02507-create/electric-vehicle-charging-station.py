def calculate_charging_cost(battery_capacity, current_charge,
                            target_charge, price_per_kwh):
    energy_needed = battery_capacity * (target_charge - current_charge) / 100
    cost = energy_needed * price_per_kwh
    return energy_needed, cost


print("===================================")
print("     EV CHARGING STATION")
print("===================================")

vehicle = input("Enter vehicle name: ")

battery_capacity = float(input("Enter battery capacity (kWh): "))
current_charge = float(input("Enter current battery charge (%): "))
target_charge = float(input("Enter target battery charge (%): "))
price_per_kwh = float(input("Enter charging price (Rs/kWh): "))

if current_charge < 0 or current_charge > 100:
    print("Invalid current charge percentage.")
elif target_charge < 0 or target_charge > 100:
    print("Invalid target charge percentage.")
elif target_charge <= current_charge:
    print("Target charge must be greater than current charge.")
else:
    energy, cost = calculate_charging_cost(
        battery_capacity,
        current_charge,
        target_charge,
        price_per_kwh
    )

    print("\n---------- Charging Details ----------")
    print("Vehicle           :", vehicle)
    print("Battery Capacity  :", battery_capacity, "kWh")
    print("Current Charge    :", current_charge, "%")
    print("Target Charge     :", target_charge, "%")
    print("Energy Required   :", round(energy, 2), "kWh")
    print("Charging Cost     : Rs.", round(cost, 2))
    print("--------------------------------------")
