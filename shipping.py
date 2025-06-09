# Author: Vernell Mangum
#
# Description: Basic python program that calculates your cost of shipping
# based on shipping prices and weight of parcel.

weight = 41.5

# Ground Shipping

ground_ship_cost = 0

if weight <= 2:
    ground_ship_cost += (weight * 1.50) + 20
elif weight <= 6:
    ground_ship_cost += (weight * 3.00) + 20
elif weight <= 10:
    ground_ship_cost += (weight * 4.00) + 20
else:
    ground_ship_cost += (weight * 4.75) + 20
    
print("Ground Shipping cost: " + str(ground_ship_cost))

# Premium Ground Shipping

premium_ground_cost = 125

print("Premium Ground Shipping cost: " + str(premium_ground_cost))

# Drone Shipping

drone_ship_cost = 0

if weight <= 2:
    drone_ship_cost += (weight * 4.50)
elif weight <= 6:
    drone_ship_cost += (weight * 9.00)
elif weight <= 10:
    drone_ship_cost += (weight * 12.00)
else:
    drone_ship_cost += (weight * 14.25)

print("Drone Shipping cost: " + str(drone_ship_cost))