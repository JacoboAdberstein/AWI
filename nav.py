import numpy as np
import time
import scipy.signal
import itertools
import board
import adafruit_bno055

#-------------------------------------- Variable setup ----------------------------------------
time_axis = []
roll_data = []
pitch_data = []
yaw_data = []

combined_data = []
steps = []

# Records acceleration in given time
seconds = 60
start = time.time()
time.process_time()   
samples = 400
#samples = 50

#-------------------------------------- Data Collection ----------------------------------------
for i in range(0,samples):
    motion.start_updating()
    (x,y,z) = sensor.linear_acceleration
    (roll,pitch,yaw) = sensor.euler
    time_axis.append(i)
    roll_data.append(roll)
    pitch_data.append(pitch)
    yaw_data.append(yaw)
    combined_data.append(np.sqrt((x**2)+(y**2)+(z**2)))
    time.sleep(.01)

elapsed = time.time() - start

#-------------------------------------- Data Processing ----------------------------------------
b, a = scipy.signal.butter(3, 0.1)
filtered_comb = scipy.signal.filtfilt(b, a, combined_data)
derivative = np.gradient(filtered_comb)

#-------------------------------------- Step Counting ----------------------------------------
steps = len(list(itertools.groupby(derivative, lambda Input: Input > 0))) 
steps = (steps -1)/2

#-------------------------------------- Distance Calulation ----------------------------------------
strideLength = 0.67 # meters
distanceTraveled = steps * strideLength

print("Steps: {}".format(steps))
print("Distance traveled: {} meters".format(distanceTraveled))



    
