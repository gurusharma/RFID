# RFID
RFID Reader Project
# Build Instructions for RFID Reader Project

## Table of Contents
1. [Introduction](#introduction)
2. [Bill of Materials](#bill-of-materials)
3. [Time Commitment](#time-commitment)
4. [Mechanical Assembly](#mechanical-assembly)
5. [PCB or Soldering](#pcb-or-soldering)
6. [Power Up](#power-up)
7. [Unit Testing](#unit-testing)
8. [Production Testing](#production-testing)
9. [Reproducible](#reproducible)

### Introduction
On this page, you will find the instructions for building your own project on Raspberry Pi 2 utilizing RFID Serial tag reader. This project can be used to identify different RFID tags. RFID tag readers are already used in many applications, such as automatic user identification, robotics, inventory tracking and payment systems. This project is part of a bigger project where we plan to utilize the functionality of RFID reader to authenticate users of a shopping mall to conveniently login and browse helpline service.

##### Note: 
Please note that I will be referring to Raspberry Pi 2 as Pi occasionally. 

### Bill of Materials
You would need a budget of approximately $200.00 if you do not own or have access to any of the parts listed below. It is possible to obtain better deals, so feel free to do a little research before making a purchase. 

|                      Item                      	|        Quantity       	|                                                             Cost                                                             	|                                                                                     Supplier                                                                                     	|
|:----------------------------------------------:	|:---------------------:	|:----------------------------------------------------------------------------------------------------------------------------:	|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:	|
| Raspberry Pi 2 (Includes USB cable connectors) 	|           1           	| Only Pi: $ 45.95; Ultimate Starter Kit: $119.95; Complete Starter Kit: $99.95; Basic Starter Kit With Power Adaptor: $59.95 	|                                                        [Cana Kit](https://www.canakit.com/raspberry-pi/raspberry-pi-kits)                                                        	|
|            RFID Card Reader and Tags           	| 1(reader) + 3(tags) 	|                                                            $ 59.99                                                           	|                                                             [Parallax Inc](https://www.parallax.com/product/32390)                                                              	|
|           Female-Female Jumper Wires           	|           6           	|                                                           $ 3.95 *                                                           	|                            [adafruit](https://www.adafruit.com/product/266)                           	|
|                    Resistors                   	|           2           	|                                                           $ 6.86 **                                                          	|              [Amazon](https://www.amazon.com/dp/B01ERPXFZK/ref=sspa_dk_detail_3?psc=1&pd_rd_i=B01ERPXFZK&pd_rd_wg=MK4GM&pd_rd_r=60TKJ3G1SDZ08G6YW486&pd_rd_w=REy7O)             	|
|       Soldering Kit (with Soldering Iron)      	|           1           	|                                                          $ 31.00 ***                                                         	| [Amazon](https://www.amazon.ca/Primacc-Adjustable-Temperature-Controlled-Interchangeable/dp/B06XCZC4PF/ref=sr_1_3?ie=UTF8&qid=1516578338&sr=8-3&keywords=soldering+kit)   Humber Prototype Lab 	|
|            3-D Case for RFID reader            	|           1           	|                                                            $ 1.80                                                            	|                      [Toronto Public Library](https://www.torontopubliclibrary.ca/using-the-library/computer-services/innovation-spaces/3D-design-print.jsp)                     	|

\* Premium Female/Female Jumper Wires - 40 x 6" (you can strip wires to make individual ones)

\** Elegoo Electronics component pack with resistors, LEDs, Switch, Potentiometer for Arduino UNO, MEGA2560, Raspberry Pi

\*** Primacc Soldering Iron Kit

##### Note:
Prices may change over time and some of the prices are in USD, so, please verify before making a purchase.

### Time Commitment
This was part of a project course, divided over a period of 12 weeks, but the actual work hours spent on it were 3 to 5 hours every week. If the project is the only thing you have to do, then it should take less than a week, depending on how you divide tasks and deal with delays associated with finding and purchasing items. The table below gives an approximate time breakdown per task: 

|    Tasks                                           	|    Time   Required to Finish Successfully    	|
|----------------------------------------------------	|----------------------------------------------	|
|    Look for parts and make a purchase *             	|    2 Hours                                   	|
|    Wait for delivery                               	|    1 day to 1 week                           	|
|    Soldering and Testing Voltage Divider           	|    < 1 hours                                 	|
|    Create .stl file for custom case 3D printing    	|    < 1 hour                                  	|
|    Print the 3D case                               	|    ~ 2 hours                                 	|
|    Configure the Pi and download libraries            |    ~ 2 hours                                  |
|    Project setup                                   	|    < 10 minutes                              	|
|    Demo and Testing                                	|    < 30 minutes                              	|

\* Less than 30 Minutes if you follow the links provided in previous section

From the breakdown above, it is clear that the project does not take very long to complete. If you follow the instructions correctly and are dedicated, you can build your own prototype in less than a week.  

### Mechanical Assembly
The Parallax Serial RFID (Radio Frequency Identification) Card Reader (#28140) can be connected to any host microcontroller easily using only four connections. For the purpose of this project, I am using Raspberry Pi 2. There are 4 pins on the RFID reader and following table (from official documentation) lists their type and functionality: 
![RFIDPins](https://github.com/gurusharma/RFID/blob/master/RFID%20Pins.PNG)

    Figure 1: RFID Serial Card Reader pin type and functionality

![Connections](https://github.com/gurusharma/RFID/blob/master/Connections.png)

    Figure 2: Schematic for connecting RFID Serial Card Reader to Raspberry Pi 2 

Use the schematic in Figure 2 above, to establish connections. The SOUT pin of the RFID reader is connected to a voltage divider. Use a 2200 Ω (R1) resistor and a 3300 Ω (R2) resistor to reduce 5 volts coming out of the RFID reader's SOUT to about 3 volts. This is done to avoid the risk of damaging Pi with higher voltages. You can solder these resistors along with a jumper wire to create the voltage divider as shown in the picture below (also put a heat shrink on the soldered part). Make sure you check the output of voltage divider using a multimeter before incorporating it in the assembly.

![VoltageDivider](https://github.com/gurusharma/RFID/blob/master/Voltage%20Divider.PNG)

     Figure 3: Voltage Divider

Now create the circuit in Figure 2; this should not take more than 10 minutes if done carefully. 

#### Linux configuration: 
Use raspi-config to ensure that the shell is configured to run on serial port. From the main menu, select “Advanced Options” followed by “Serial”. Select “No” for the prompt to login shell over serial port. “Finish” and save configuration. Before you reboot also check that the “enable_uart” filed in “/boot/config.txt” is set equal to “1” and not “0”. Now reboot.

#### Install Python Packages: 
You may choose to program in any other language compatible with Pi. For the purpose of these build instructions, I will explain steps of programming Pi using Python. You will need to have “Python GPIO” and “Serial” packages installed. Raspberry Pi Linux distribution usually have some python packages installed. In case they are missing you can use the following commands to install it: 
```
sudo apt-get install python
sudo apt-get install python-dev
sudo apt-get install libjpeg-dev
sudo apt-get install libfreetype6-dev
sudo apt-get install python-setuptools
sudo apt-get install python-pip
```
After installing Python, you may now install above mentioned packages using: 

```
sudo pip install RPi.GPIO
sudo pip install pySerial
```
If you run into any issues with installation, follow this [link](https://jeffskinnerbox.wordpress.com/linux-python-packages-for-my-raspberry-pi/). 

#### Write a Python script: 
You can download the script [here](https://github.com/gurusharma/RFID/blob/master/rfid.py)
and modify as needed. This script simply sets up Pi’s serial port and GPIO header. It identifies the tags being read by the reader inside a while loop. The reader reads the input tag when it is enabled low. When you run the code, it makes reader enabled low and goes into the while loop and waits for the tag to be read. It is worth knowing that the RFID tag has 12 bytes of data, the validate_rfid function ensures that the tag being read has 12 characters.      

#### Print a case for the sensor: 
I utilized [TINKERCAD](https://www.tinkercad.com/) to create .stl file needed for 3D printing. You may utilize the [file](https://github.com/gurusharma/RFID/blob/master/RFID%203D%20case/RFID%203D%20case.stl) I created and edit it as needed or use any other freely available online tool of your choice to do it from scratch. Once you are satisfied with .stl file, you may get it printed from any facility of your choice. If you choose to do it with Toronto Public Library, make sure to read the detailed instructions on their [website](https://www.torontopubliclibrary.ca/using-the-library/computer-services/innovation-spaces/3D-design-print.jsp). 

![3DPrintOutput](https://github.com/gurusharma/RFID/blob/master/RFID%203D%20case/rfid1.jpg)
    
    Figure 4: 3D Printed Sensor Case

##### TIP: 
The software they use for reading .stl file and printing is “CURA”, which by default tends to select the thickness of printing thread to be 0.4 mm, which usually takes more than 2 hours to finish. Make sure to change this thickness to 0.6 mm (recommended) or 0.8 mm in order to get the print done in 2 hours. In case you still have any issues, ask the staff; they are very helpful. 

### PCB or Soldering
Only soldering needed for this project is the one needed to create a voltage divider circuit. Here are the steps:
1.	Get the following parts: 
    1. two resistors R1 (2200 Ω) and R2 (3300 Ω)
    2. one jumper wire and heat shrink
    3. soldering iron
2.	Strip both ends of the wire
3.	When soldering iron is ready to use: 
    1. solder two resistors at one end and one end of the jumper wire between them 
    2. now put the heat shrink on the soldered part
    
Following these steps, you will get your voltage divider ready. Make sure to check the output voltage using a multimeter. 

### Assembly 
Now assemble all the parts as shown in the image below and put the RFID tag inside its case. Also, you may utilize any 'ground pin' for assembly.

![Circuit](https://github.com/gurusharma/RFID/blob/master/Circuit.png)

    Figure 5: Circuit Assembly with ports

![Assembly1](https://github.com/gurusharma/RFID/blob/master/Assembly1.jpg)
![Assembly2](https://github.com/gurusharma/RFID/blob/master/Assembly2.jpg)

    Figure 6: Complete Assembly

### Power Up
After successfully completing the tasks above, you are ready to power up. Make sure your circuit connections are correctly established; fix errors in the setup if you encounter any. Now plug the USB into Pi and connect to a computer device. In order to get the output displayed on computer, plug in the HDMI cable. Turn on the Pi. Make sure you have all the packages listed above installed in order to run the python script.

### Unit Testing
After proper setup and power up, we can now test the RFID sensor. Run the Python script using the following command: 
```
    sudo python rfid.py
```    
Now check for LED color change on RFID reader; it should turn red from green. Now you can bring one of the “world tags” closer to the reader to read. You will see the message displayed on the screen as “Welcome User #” if it was the tag belonging to a pre-registered user. If instead it was a new tag, then the message displayed would be: “Please contact admin to register first”.

### Production Testing 
If you successfully passed the unit testing, you can now go ahead with production testing. Run the python script multiple times and test different RFID tags. Check if you get the expected results. The tags are read when the LED on the reader is red (i.e. enabled low). Now your prototype is functional, you may modify the script to add more functionality.

### Reproducible
If you have the required budget and are able to follow the instructions listed above, you can easily reproduce the project and hopefully add more features to it. Happy coding and prototyping!!! All the Best!

### References
[Helpful Link](https://medium.com/@coryaspencer/using-the-parallax-serial-rfid-reader-with-the-raspberry-pi-8c948090e687)

[RFID Documentation](https://www.parallax.com/sites/default/files/downloads/28140-28340-RFID-Reader-Documentation-v2.4.pdf)

[Toronto Public Library Printing](https://www.torontopubliclibrary.ca/using-the-library/computer-services/innovation-spaces/3D-design-print.jsp)
