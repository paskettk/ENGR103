import math # ALLOWS PI VALUE
import matplotlib.pyplot as plt
# INPUT AND VALIDATE LOOP FUNCTIONS
#######################################################################
# Function: get_tank_height()
# Description: gets and validates the height of the cylindrical tank
# Parameters: None
# Return values: tank height (int)
# Pre-Conditions: height input must be an integer between 1 and 80
# Post-Conditions: returns a valid tank height
#######################################################################
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
#######################################################################
# Function: get_tank_radius()
# Description: gets and validates the radius of the cylindrical tank
# Parameters: None
# Return values: tank radius (int)
# Pre-Conditions: radius input must be an integer between 1 and 20
# Post-Conditions: returns a valid tank radius
#######################################################################
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
#######################################################################
# Function: get_time_steps()
# Description: gets and validates the number of time steps
# Parameters: None
# Return values: time steps (int)
# Pre-Conditions: time steps input must be an integer between 1 and 3000
# Post-Conditions: returns a valid number of time steps
#######################################################################
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

    time_total = i
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


# MATPLOTLIB 
#create lists to hold time and activity data during activation
# height, radius, and time are defined above
height = current_height
radius = tank_radius

volume = height*math.pi*radius**2
volume_int = volume # intial volume
print(f"The Intiial Volume is {round(volume_int*1000,2)} liters")
time = 0
time_step = 1
out_rad = 0.05
total_time = [] #list for time
total_height = [] # list for height
total_volume_lost_list = []
volume = initial_volume
# while loop to determine height and volume lost with time
while time < time_steps and height > 0:
    total_time.append(time) # saves the time for each step
    total_height.append(height) # saves the height for each step
    total_volume_lost_list.append(volume)
    vel = 4.429*height**0.5
    vol_lost = vel*out_rad**2*math.pi*time_step
    volume = volume - vol_lost
    height = volume/(math.pi*radius**2)
    time = time+time_step
print("the end height is:", round(height,6),"meters")
print("We lost",round(volume_lost*1000,4),"liters during the last second")
print("the time is:", round(time,2),"seconds")

# plotting section
# feel free to play around with it
plt.plot(total_time, total_height)
plt.xlabel('Time(seconds)')
plt.ylabel('Height (m)')
plt.show()
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(total_time, total_height)
ax.set_xlabel('Time(seconds)')
ax.set_ylabel('Height (m)')
plt.show()



plt.plot(total_time, total_volume_lost_list)
plt.xlabel('Time(seconds)')
plt.ylabel('Total Volume Lost (liters)')
plt.show()
print(total_volume_lost_list)
print(total_height)