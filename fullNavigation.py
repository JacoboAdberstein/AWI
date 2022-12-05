
import numpy as np
#import matplotlib.pyplot as plt
import time
import scipy.signal
import itertools
import board
import adafruit_bno055




# Records acceleration in given time
seconds = 60
start = time.time()
time.process_time()   
samples = 400

def Moving(accelData):
    if (np.max(accelData) < 1.1) & (np.min(accelData) > .96):
        return False
    return True

def AngleChange(avgAngle,originalAngle):
    
    if (avgAngle >(originalAngle+2)) | (avgAngle<(originalAngle-2)):
        print("Sirection Change")
        return True, avgAngle

    return False, originalAngle

def DistanceCalc(steps):
    strideLength = 0.70104 # meters
    distanceTraveled = steps * strideLength
    return distanceTraveled

def stepCalc(combined_data):
    if len(combined_data) > 50:
        b, a = scipy.signal.butter(3, 0.1)
        filtered_comb = scipy.signal.filtfilt(b, a, combined_data)
        derivative = np.gradient(filtered_comb)
        steps = len(list(itertools.groupby(derivative, lambda Input: Input > 0))) 
        steps = (steps-1)/2
    else:
        steps = 0
    return steps

dist = 10
steps = 0
z = 0
i = 0
loopBool = True

x_data = []
y_data = []
z_data = []
combined_data = []
yaw_data = []

while loopBool:
    (x,y,z) = sensor.linear_acceleration
    (roll,pitch,yaw) = sensor.euler
    yaw_data.append(yaw)
    combined_data.append(np.sqrt((x**2)+(y**2)+(z**2)))
    restTest = [] # 5 samples that are used to test if you are moving
    deltaSteps = [] 
    newCombinedData = [] # array that will have the acceleration data during distance M

    if i>20:  
        restTest.append(combined_data[-5:])
        avgAngle = np.mean(yaw_data[-19:])

        movingBool = Moving(restTest) # test if we are moving. True if we are moving
        angleBool,departureAngle = AngleChange(avgAngle,z) # test if we changed angle while at rest, True if it changed, returns new angle

        
        counter = 0
        while movingBool: # Runs while moving

            restTest2 = [] # 13 samples that we will use to figure out if we are moving or stopping
            (x,y,z) = sensor.linear_acceleration 
            (roll,pitch,yaw) = sensor.euler
            yaw_data.append(yaw)
            newCombinedData.append(np.sqrt((x**2)+(y**2)+(z**2))) # populate acceleration array during distance M
            angleBool,departureAngle = AngleChange(avgAngle,z)
            avgAngle = np.mean(yaw_data[-19:])
            angleBool,departureAngle = AngleChange(avgAngle,z)
            
            if (counter>12):
                restTest2.append(newCombinedData[-13:]) # populate the stopping samples 
                movingBool = Moving(restTest2)
                if movingBool == False:
                    break
                
            time.sleep(.01)
            counter = counter + 1
        #dist = DistanceCalc(newCombinedData)
    stepsTaken = stepCalc(newCombinedData)
    
    print("Steps: {}".format(stepsTaken))
    
    time.sleep(.1)
    i = i+1




    
