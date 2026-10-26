
# Fuel Consumption and Route Comparison

distance = 300  # Journey distance in km
reserve_percent = 10

# Vehicle details: [name, mileage, fuel price per litre, available fuel]
vehicles = [
    ["Bike", 40, 105, 10],
    ["Car", 15, 105, 25],
    ["SUV", 10, 105, 40],
    ["Diesel Van", 18, 95, 20]
]

lowest_cost = 0
best_vehicle = ""
feasible_count = 0

print("FUEL CONSUMPTION AND ROUTE COMPARISON")
print("-" * 55)
print("Journey Distance:", distance, "km")
print("Fuel Reserve:", reserve_percent, "%")

for name, mileage, fuel_price, available_fuel in vehicles:

    fuel_needed = distance / mileage
    reserve = fuel_needed * reserve_percent / 100
    total_fuel = fuel_needed + reserve
    journey_cost = fuel_needed * fuel_price

    print("\nVehicle:", name)
    print("Fuel Needed:", round(fuel_needed, 2), "litres")
    print("Reserve Fuel:", round(reserve, 2), "litres")
    print("Total Fuel Required:", round(total_fuel, 2), "litres")
    print("Journey Cost: INR", round(journey_cost, 2))

    if available_fuel >= total_fuel:
        print("Status: Feasible")
        feasible_count = feasible_count + 1

        if lowest_cost == 0 or journey_cost < lowest_cost:
            lowest_cost = journey_cost
            best_vehicle = name
    else:
        print("Status: Not Feasible")

print("\n" + "-" * 55)

if feasible_count > 0:
    print("Lowest-Cost Feasible Vehicle:", best_vehicle)
    print("Lowest Journey Cost: INR", round(lowest_cost, 2))
else:
    print("No vehicle has enough fuel for the journey.")
