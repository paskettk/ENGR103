import math # ALLOWS PI VALUE

# INPUT AND VALIDATE LOOP FUNCTIONS
def get_tank_height():
    while True:
        try:
            tank_height = int(input("Enter the height of the cylindrical tank in meters (between 1 and 80): "))
            if (1 <= tank_height <= 80):
                return tank_height
            else:
                print("Enter a value inside the bounds")
        except:
            print("Invalid input")
            continue
    
def get_tank_radius():
    while True:
            try:
                tank_radius = int(input("Enter the radius of the cylindrical tank in meters (between 1 and 20): "))
                if (1 <= tank_radius <= 20):
                    return tank_radius
                else:
                    print("Enter a value inside the bounds")
            except:
                print("Invalid input")
                continue

def get_time_steps():
    while True:
        try:
            time_steps = int(input("Enter the number of time steps in seconds (between 1 and 3000): "))
            if (1 <= time_steps <= 3000):                    
                return time_steps
            else:
                print("Enter a value inside the bounds")
        except:
            print("Invalid input")
            continue

# RUN INPUT FUNCTIONS: 
initial_height = get_tank_height()
tank_radius = get_tank_radius()
time_steps = get_time_steps()

# STATE CONSTANTS:
outlet_radius = 0.05 # METERS
outlet_area = (math.pi * outlet_radius ** 2) # CALCULATE OUTLET AREA
current_volume = (math.pi * initial_height * tank_radius ** 2) # CALCULATE CURRENT VOLUME
initial_volume = current_volume # ASSIGN INITIAL VOLUME TO CURRENT
total_volume_lost = 0 # ASSIGN TOTAL VOLUME LOST TO 0

# DISPLAY INPUT
print("Tank Height: ", initial_height, " meters")
print("Tank Radius: ", tank_radius, " meters")
print("Initial volume: ", initial_volume, " liters")
print("Number of Time Steps: ", time_steps, " seconds\n")

# LOOP
for i in range(time_steps): 

    # UPDATE HEIGHT OF WATER
    current_height = (current_volume / (math.pi * tank_radius ** 2))

    # CALCULATE VELOCITY OF FLOW
    velocity = (4.429 * math.sqrt(current_height))

    # UPDATE VOLUME LOST
    volume_lost = (outlet_area * velocity * (1)) 

    # UPDATE CURRENT VOLUME
    current_volume -= volume_lost

    # UPDATE TOTAL VOLUME LOST
    total_volume_lost += volume_lost

    print("The time is ", i + 1, "seconds")
    print("The volume lost during this step is ", volume_lost, "liters")
    print("The height is now ", current_height, "meters\n")

    # CHECK IF VOLUME IS 0
    if current_volume <= 0:
        break	

# CHECK IF VOLUME RAN OUT BEFORE TIME STEPS COMPLETE
if current_volume <= 0:
    print(f"Tank has run out of water")
elif i + 1 >= 0:
    print(f"Time steps complete.")

# FINAL PRINT STATEMENTS
print("Number of time steps taken: ", i + 1, " seconds")
print(f"Initial Volume: {initial_volume} liters")
print("Volume lost: ", total_volume_lost, " liters")
print("Height of water: ", current_height, " meters")
