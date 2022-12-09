![logo](readmeImages/AWILOGO.png)

## Project Overview

Currently, astronauts use antiquated and inefficient methods to display typical (extra-vehicular activity) EVA procedures, emergency protocols, and various pieces of information such as critical EMU suit metrics.  This would allow astronauts to easily access and interact with these protocols and metrics, as well as provide additional functionality for EVA missions and location services. 

This information could consist of important information such as suit diagnostics, consumption rates, location monitoring, emergency checklists, and potential vehicle drone control. There are multiple ways that this system could be interacted with and expanded upon once implemented. 

The AWI will use an electronic screen that shall display relevant information to the astronaut. The display will show the astronaut the necessary checklists, location data, pictures, and videos that they will need for a given mission, and should be controllable even during an EVA. Additional features such as navigation will also require a number of sensors to collect the data required to show up on the visual interface. A navigational connection with the “home base” is the main priority.

Design considerations must be made for the unique conditions of the planned area this device will be used, including radiation, thermal, and vacuum related variables that don’t normally come up during typical projects. The AWI must also conform to all NASA safety requirements, most relevant regulations can be located in the Human Integration Design Handbook (NASA-STD-3001.)

---
### Flight Model

![Flight Concept](readmeImages/Curved_Prototype2.JPG)

Flight Model Concept CAD

From heritage we know:
- There was a lot of glare
- The font and contrast made it difficult to read
- The unit needed an internal heating source to maintain operational temperatures of electronics and battery.
- The unit interfered with some astronaut movements.
- The seal broke and the screen lost functionality while on mission

In all likelihood, the flight model AWI will be slightly bigger than an ipad in thickness when using custom electronics and integrating heating units. However, additional volume will come from the enclosure. We focused on how to use the enclosure to help retain heat emitted from the battery, CPU, and heater to ensure operational temperatures. One way was to use a double walled, vacuumed sealed enclosure. Like the coffee cups you get from the store. The vacuum between the walled prevents heat transfer from one wall to the other and then outside the system. The gap between the walls does not need to be manufactured as a vacuumed space. A vent port can be incorporated in the house to vent atmosphere and create vacuumed space. 

It is important to note, the double walled and vacuumed seal housing would require the chamber containing the components to be fully pressurized. If not, a vacuum environment around the heater and components will ONLY allow heat transfer through direct contact. The constant change of depressurization within the chamber could also have a negative effect on the lifespan of the components. 

The flight model prototype design can be advanced by developing thermal simulations of various aluminum and stainless steel materials. The sims can be run as double walled, vacuum sealed containers to establish a baseline for the heat retention of the materials. Aluminum is lighter but weaker than steel and may require more material to be structurally sound. Steel should be considered if using the doubled walled design for its heat retention properties. The steel can absorb heat and retain it longer than Al. The double-wall will help reduce the dissipation from the steel to the environment. The chamber housing the components should only be as large as needed. Larger volumes allow the heat to “spread” throughout the pressurized atmosphere and leads to lower internal temperatures.

Insulation covering is also a means to retain heat. The research was based on the EMU suit layers which used mylar and ripstop for both insulation and debris protection. These layers will encompass the entire AWI system and also be the contact/ connection points to the EMU. Velcro can be used to secure the covering to the EMU and should also be curved to fit the suit arm.

![Insulated Suit](readmeImages/Cross-section-of-material-layup-used-for-fabric-for-the-arms-and-legs-of-the-spacesuit.png)

Suit insulation layers

For lunar models, particular care should be taken to minimize the volumetric “footprint” when adding buttons. For this reason, I research using  piezoelectric disc to use as switch. They are much smaller than standard mechanical switches and will be easier to protect from dust and debris by fully enclosing the switched with a flexible membrane or metal. These discs create a potential difference when in tension or compression and could be used to initiate a command on the user interface. However, the change is voltage is very small , 10e-6 V or less, and would need an amplifier or highly sensitive pickup. Voltage output can be calculated using V = P*G*t, where P is the applied force, G is the material sensitivity, and t is the disc thickness. Many of the commercially available discs are 0.1mm or less in thickness. https://www.americanpiezo.com/product-service/custom-piezoelectric-elements/shapes-sizes.html

![Piezo Disc Size](readmeImages/piezo.JPG)

piezo disc sizing

![Piezo Disc Placement](readmeImages/piezo2.JPG)

Concept CAD for button replacement

![Piezo Disc Layout](readmeImages/piezo3.JPG)

Concept CAD for piezo disc button build

# Prototype Build
During the semesters starting from spring 2022 and fall 2022. The AWI team has been working on a prototype that is supposed to emulate the functions of the flight unit version of the AWI project. Below are some of the materials that were utilized in the building of the prototype. These materials are all commercially available components that are relatively inexpensive. 

## Materials
These are some of the main components I utilized to develop the first prototype (*Mark I*)
- Raspberry Pi 4 (RP4)
- Arduino Nano
- Kuman 7 in touchscreen display
- HiLetgo 433 MHz transmitter and receiver  
- DS18B20 Temperature sensor module
- Adafruit 9-DOF IMU Fusion-Breakout BNO055
- PiSugar Plus 2 Battery Pack
- 7 Push buttons


## Material Overview
- **Raspberry Pi 4:** We decided to go with the Raspberry Pi 4 due to the wealth of available projects and information on the internet. This mean that if we ran into a problem, it was pretty much certain that someone else at some point had run into the same problem before. With the vision of making the AWI a platform, not just a checklist replacement, we needed a microcontroller capable of withstanding the possible implementations of the AWI. 
- **Arduino Nano:** The Arduino Nano board is nothing else but what simulates the "Base" on a celestial body like the Moon or Mars. Its whole purpose is to emit a small RF signal used to demonstrate part of the navigation system. 
- **Kuman Display:** This is nothing more than a cheap display made for the RP4. The original plan was to lead with a flexible OLED display, unfortunately, those are were not available to us as companies we reached out did not answer back to our request to purchase one. 
- **HiLetgo 433 MHz transmitter and receiver:** This is pretty self-explanatory. Simple RF receiver and transmitter  
- **BNO055:** This is Adafruit accelerometer and gyroscope. It is the main sensor that is implemented in the inertial navigation system. 
- **PiSugar Plus 2 Battery Pack:** As the name implies, this is a battery pack for the RP4. The great thing about this specific battery pack is that it has its own integrated board that is connected to a website. In this website, we can modulate the power sent to the RP4 board and even include power modes. 
- **The rest:** The rest include wires, simple push buttons, 3D prints, breadboards, empty PCBs 


As of right now, the physical integration of the components is still in development. The image below displays a potential arrangement of some of the components. 

![old Version](readmeImages/old4.png)

Original testing prototype

![New ISS Version](readmeImages/ISS.JPG)

Current ISS testing prototype

![New Lunar Version](readmeImages/lunar1.JPG)

Current Lunar testing prototype

## AWI Physical Assembly Guide 
Given the current state of the development of AWI this specific section is still pending. The only physical assembly instructions available at the moment is the connection of the screen to the RP4 via the HDMI connection port, as well as a connection of the screen and Pi to a power source. As the coming weeks pass and the physical development of the Pi evolves, there will be a more detailed guide on how our version of the AWI can be assembled together.

### CAD file explanation and assembly
CAD files can be accessed via GrabCAD and Professor Nokes has the ability to give access. If there is an issue with accessing the file contact Ryan Scott at 2059032411 (cell). The GrabCAD desktop app Workbench is going to go away as of June 1, 2023 but files will still be accessible via web browser and other software. https://blog.grabcad.com/blog/2022/08/09/a-fond-farewell-to-grabcad-workbench/

The folder are organized as follows:
- Assembly: Contains solidworks assemblies for the enclosures that include relevant parts or sub-assemblies. Sub-assemblies are most likely to be found in parts since they are parts made up of sub-parts. The most recent versions are called V3.
- Parts: All other CAD files used to create assemblies. Some were pulled from GrabCAD libraries and are non-english. All OLD versions are contained here
- Images: Images taken from CAD for reviews.
- Old Drawings_Images

I have found the dimensions to be fairly accurate for the screen.
The Solidworks part for the PiSugar battery has screw holes that are not entirely accurate. They should align perfectly with the Raspberry Pi but do not.

### Raspberry Pi set up

### Battery set up

### BNO055 (Inertial Measurement Unit, IMU) set up
- include physical diagrams
- open I2C ports 
- Run from terminal

### Radio Module set up
- include diagrams


---
# Programming

## File Overview
Currently there is one main folder called checklists. In this specific folder, there are subfolders that correspond to specific types of checklists. The path to these checklists is important. If you change the file structure, when you run the code there will be issues finding the checklists unless you update the path inside the code. 

There will be another folder called *"venv"*. This file corresponds to the virtual environment in which the code should run when you run the code in your computer. There is a section below just about the virtual environment, this section explains in detail how it works and why it is needed. 

Finally there is a folder called *"readmeImages"*, this folder houses all the images utilized for this ReadMe document.

Aside from the folders previously mentioned, there are also some important files:
- **MainInterface.py:** This file is the main file that you run in order to boot up the AWI. This file interacts with other files and the folders needed. The main structure of the GUI is delineated in this file. This file receives the inputs from the subsystems and is in charge of displaying them.
- **requirements.txt:** This file is a simple text file that has the libraries and install requirements needed in order to run the AWI code. This file interacts with the virtual environment.
- **.gitignore:** This file is very important. This file in essence tells GitHub which files or folders to not push into the repo. The specific folder and set of files that we are not interested in pushing to GitHub are the virtual environment related files. This means the "venv" folder. This is because each computer system has a different way of setting up the virtual environment, and using the one pushed to the code will most likely not run.
- **telemetry.py:** This specific file is the program that will determine the values that are displayed by the telemetry dashboard. Some of the values will be pressure, power, or temperature. More over, this specific file will also be in charge of raising any telemetry based alerts. 
- **navigation.py:** This file, as the name states, is for the navigation. The current state of this file simply outputs data from the BNO055 module once the module is wired and ports are turned on. Eventually, this should be the file that runs all the navigation in the background and sends the data to the MainInterface.py
- **nav.py:** This file is one of the several files that were used for navigation development purposes. The file is used to explore the accelerometer and gyroscope capabilities from the IMU sensor. This file also has the logic for distance calculation which should be implemented in the navigation algorithm explained below.
- **fullNavigation.py:** This file, same as the nav.py file, is a file utilized during development of the navigation system. This file implements the distance calculation method developed in the nav.py but adds functionalities liked "motion/resting" detection which is used to create the navigation network. The section detailing the navigation algorithm will make this file easier to understand. 

Eventually there will be files for each of the functionalities that the AWI system provides, like communications or video.

---

## GUI Architecture
The outline below describes the overall architecture of the AWI GUI. The diagram details how some buttons are connected with the submenus and the path of each submenu. An important addition to this diagram will be the interaction of alert systems and their impact on the view that is present in the screen. These specific alerts would mainly stem from the telemetry code. 

![GUI flowchart](readmeImages/diagram.png)

---


## Inertial Navigation Algorithm


---

## Coding Resources
These are some links that can help with the development.
- [You can download latest version of pyqt5](https://pypi.org/project/PyQt5/) 
- [pyqt5 documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/) 
- [Raspberry Pi GPIO python documentation](https://pythonhosted.org/RPIO/) 
- [GitHub commands](https://education.github.com/git-cheat-sheet-education.pdf)
- [Virtual Environment Windows](https://code.visualstudio.com/docs/python/environments)
- [Accelerometer Documentation](https://docs.circuitpython.org/projects/bno055/en/latest/)
- [Accelerometer Python Tutorial](https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor/python-circuitpython)
- [PyQT Plotting Library](https://www.pythonguis.com/tutorials/plotting-pyqtgraph/)
- [Distance Calculation From Accelerometer](http://web.cs.wpi.edu/~emmanuel/courses/cs528/F20/slides/papers/deepak_ganesan_pedometer.pdf)
- [IOS PyTo Motion Library Documentation](https://pyto.readthedocs.io/en/latest/library/motion.html)

## Raspberry Pi and AWI running instructions
In order to get the AWI application that is on the GitHub to run, there are several steps that are needed to be done on the Raspberry Pi first. 

Before you can set up the software of the Raspberry Pi, you need to hook up the Pi to a power source, a visual source (monitor), and ideally a mouse and keyboard. Once that is done, you can set up the software with the following steps.

1. Set up the RP4 operating system. When Raspberry Pis first arrive, they do not currently run any visual operating systems. For our purposes, we installed "Raspbian OS" on an SD card, which is what hold the data of the Pi.  [This](https://www.raspberrypi.com/software/) is a link that has a guide about the Raspbian OS and how to get it on the Raspberry Pi. 
2. Get an IDE that can edit and run python scripts on the Pi itself. This is important whenever you get to the button testing and sensor implementation. 
3. Get the codebase from the GitHub repo on a flash drive and connect it directly to the Pi. You can transfer the whole project folder on to the Pi.
4. Inside the console/terminal of the Pi, make sure to install the appropriate versions of the Python and the PyQT5 libraries, as well as any other GPIO (General Pins Input Output) or sensor libraries needed for the code to run properly. Specific instructions on how to install those libraries and versions will be added in the next iteration of this document. 
5. Connect all the sensors and buttons per the **AWI Physical Assembly Guide** above.
6. Run MainInterface.py script on the terminal utilizing the command:  ``` python3 MainInterface.py ```


Once you have familiarized yourself with the AWI system and how the current iteration operates, feel free to grow it and make it your own! 

---

---
## Virtual Environment
What is a virtual environment? A virtual environment is a virtual space within your project folder where you run the code you are looking to run. This is very important in the case of AWI if you have several team members coding. You can set the specific library and code versions that are installed and can be run on the virtual environment. This ensures that whenever the computer you are programming in updates and the python version changes, the code for AWI still runs as expected. This also accounts for different team members having different versions of Python, which means that the code would not run on their system. This way, everyone that wants to run the AWI code on their computer, will be able to and without problems. 


### **Instructions for macOS**
In order to run the code efficiently, and avoid version issues, you will need to set up a virtual environment. As of right now, the environment should work with python version 3.9.12 and pyqt5 5.15.7

Make a folder called ```venv```

Then run the following command on your IDE terminal/console

```
$ python3 -m venv venv
```

When you want to run the code, you will need to activate the environment by typing the following command:

```
$ source venv/bin/activate
```

This will let you enter your environment, and you can then install the right python version and the right pyqt5 version

```
pip3 install python
```

```
pip3 install pyqt5
```


### **Instructions for Windows**
We used Visual Studio Code as our IDE to do this project. This is how to install the virtual environment to run the code.

Once you are in VS Code, write the following command in the terminal. 
```
$ python -m venv .venv
```

Then write the following command to get to the correct folder
```
$ cd .\venv\venv\bin\
```
Then write the following command to activate the virtual environment.
```
$ ./activate
```
---

## Trouble shooting

Screen display issues
1. If the Pi is not showing any ouput to the screen, this could be due the HDMI input plugged into prior to the Pi being turned on. Make sure the HDMI input is plugged in first before turning on the Pi.
2. If the screen is still not turning on, check the backside of the screen board to see if the ON switch is flipped on.

Wifi Issues
1. The raspberry pi has a wifi adapter plugged into it, this should cover all the wireless needs. It is an older adapter (2014) so if the internet stops working be sure to check if it is functioning or get a new unit. 

Power Issues
1. Make sure that the battery is fully charged before using the AWI.
2. If the AWI is not turning on through the battery, use a USB-C cable to power it instead.
3. The screen can be powered either from the raspberry pi or any USB-A input.

Coding Issues
1. If you code from your personal computer to import new code for the AWI, make sure that you are coding with Python version 3.9.12 to ensure optimal compatibilty.
2. If PyQt5 is not working, do the following.
3. Check to see if the PyQt5 widgets are spelled correctly in the code.
4. Check if they are compatibilty issues with other loaded in modules.
5. Try creating functions to seperate the code so the problem can be isolated.
6. If this doesnt work, create a virtual environment and download Python and PyQt5 on there instead.
7. Be sure to use the command 'git pull' to update the code if you are working through GitHub. 
8. If a module is going to be installed, update pip.

Button Issues
1. Make sure each button wire has one wire connected to the correct GPIO pins (reference a Pi GPIO chart) and one wire connected to a ground pin as well.

CAD and 3d Printing issues
1. Most models were printed on Raise3d and required special permission to print overnight. A Prusa printer was used (personal printer) and the quality was better and required less time. This may be due to the recommended settings by TIW.
2. Allow for increased tolerances. The hinge pin connecting the flap and casing is a 3mm rod. The holes were CAD initially at 2.8 to allow a tight fit. This ended up requiring alot of sanding on the rod. I did this by inserting it into a power drill and wrapping sandpaper around it. From this, I increased the CAD hole to 3mm but this stilled required the rod to be sanded. In the end, a 3.2mm hole let the rod insert with little resistance and did not back out. 
3. Wiring was not a large initial consideration and caused some fit problems when we began to integrate more components. Afterwards more consideration was given to the added space required to install components. With the RF, the antenna needs to extend outside the AWI to prevent signal interferance
