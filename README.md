# Astronaut Wrist Interface (AWI)

## Project Overview
The AWI is an electronic interface that astronauts will wear in space enviroments that provides them with relevant information.



## File Overview
There are three folders in the files. These folders are what store the checklists.txt files. The main fail that right now runs all the interface is the file named MainInterface.py. This file runs the entire GUI and implements the pyqt5 library. As the project moves on, specific functions like the direction finding system and the telemetry communication can be handled by other python files that will be called from the MainInterface.py file.  



## Resources
- You can download latest version of pyqt5: https://pypi.org/project/PyQt5/ 
- pyqt5 documentation: https://www.riverbankcomputing.com/static/Docs/PyQt5/ 
- Raspberry Pi GPIO python documentation: https://pythonhosted.org/RPIO/

## Virtual Environment

**Instructions for mac**

In order to run the code efficiently, and avoid version issues, you will need to set up a virtual environment. As of right now, the environment should work with python version 3.9.12 and pyqt5 5.15.7

Make a folder called ```venv```

Then run the following command on your IDE terminal/console

```
$ python3 -m venv venv
```

When you want to run the code you will need to activate the environment by typing the following command:

```
$ source venv/bin/activate
```

This will let you enter your environment and you can then install the right python version and the right pyqt5 version

```
pip3 install python
```

```
pip3 install pyqt5
```


## GUI Architecture

*insert diagram*

