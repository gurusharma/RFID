# RFID
RFID Reader Project
# Build Instructions for RFID Reader Project

## Table of Contents
1. [Introduction](#introduction)
2. [Bill of Materials](#bill-of-materials)
3. [Time Commitment](#time-commitment)
4. [Mechanical Assembly](#mechanical-assembly)
5. [PCB/Soldering](#pcb-soldering)
6. [Power Up](#power-up)
7. [Unit Testing](#unit-testing)
8. [Production Testing](#production-testing)
9. [Reproducible](#reproducible)

### Introduction
Here you will find the instructions for building your own project on Raspberry Pi 2 utilizing RFID Serial tag reader. This project can be used to identify different RFID tags. RFID tag readers are used already in many applications such as allowing users to enter in buildings. This project is part of a bigger project where we plan to utilize functionality of RFID reader to authenticate users of a shopping mall to conveniently login and browse helpline service. 
Note: Please note that I will be referring to Raspberry Pi 2 as Pi occasionally. 

### Bill of Materials
|    Item                                              	|    Quantity                 	|    Cost                                                                                                                                       	|    Supplier                                                 	|
|------------------------------------------------------	|-----------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------	|-------------------------------------------------------------	|
|    Raspberry Pi 2 (Includes USB cable connectors)    	|    1                        	|    Only Pi: $ 45.95      ULTIMATE STARTER   KIT: $119.95   COMPLETE   STARTER KIT: $99.95   BASIC STARTER   KIT WITH POWER ADAPTOR: $59.95    	|    Cana Kit                                                 	|
|    RFID Card Reader and Tags                         	|    1 (reader) + 3 (tags)    	|    $ 59.99                                                                                                                                    	|    Parallax Inc   https://www.parallax.com/product/32390    	|
|    Female-Female Jumper Wires                        	|    1                        	|    $ 4.00 *                                                                                                                                   	|    Seed   Studio                                            	|
|    Resistors                                         	|    2                        	|    $ 6.86 **                                                                                                                                  	|    Amazon                                                   	|
|    Soldering Kit (with Soldering Iron)               	|    1                        	|    $ 31.00 ***                                                                                                                                	|    Amazon   Humber                                          	|
|    3-D Case for RFID reader                          	|    1                        	|    $ 1.80                                                                                                                                     	|    Toronto   Public Library                                 	|
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg .tg-gwa0{font-weight:bold;background-color:#646809;color:#ffffff;text-align:center;vertical-align:top}
.tg .tg-zktd{font-weight:bold;background-color:#646809;color:#ffffff;text-align:center}
.tg .tg-yw4l{vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-zktd"><br>  Item<br>  </th>
    <th class="tg-zktd"><br>  Quantity<br>  </th>
    <th class="tg-gwa0"><br>  Cost<br>  </th>
    <th class="tg-gwa0"><br>  Supplier<br>  </th>
  </tr>
  <tr>
    <td class="tg-031e"><br>  Raspberry Pi 2 (Includes USB cable connectors)<br>  </td>
    <td class="tg-031e"><br>  1<br>  </td>
    <td class="tg-yw4l"><br>  Only Pi: $ 45.95<br>  <br>  ULTIMATE STARTER<br>  KIT: $119.95<br>  COMPLETE<br>  STARTER KIT: $99.95<br>  BASIC STARTER<br>  KIT WITH POWER ADAPTOR: $59.95<br>  </td>
    <td class="tg-yw4l"><br>  Cana Kit<br>  </td>
  </tr>
  <tr>
    <td class="tg-031e"><br>  RFID Card Reader and Tags<br>  </td>
    <td class="tg-031e"><br>  1 (reader) + 3 (tags)<br>  </td>
    <td class="tg-yw4l"><br>  $ 59.99<br>  </td>
    <td class="tg-yw4l"><br>  Parallax Inc<br>  https://www.parallax.com/product/32390<br>  </td>
  </tr>
  <tr>
    <td class="tg-031e"><br>  Female-Female Jumper Wires<br>  </td>
    <td class="tg-031e"><br>  1<br>  </td>
    <td class="tg-yw4l"><br>  $ 4.00 *<br>  </td>
    <td class="tg-yw4l"><br>  Seed<br>  Studio<br>  </td>
  </tr>
  <tr>
    <td class="tg-031e"><br>  Resistors<br>  </td>
    <td class="tg-031e"><br>  2<br>  </td>
    <td class="tg-yw4l"><br>  $ 6.86 **<br>  </td>
    <td class="tg-yw4l"><br>  Amazon<br>  </td>
  </tr>
  <tr>
    <td class="tg-031e"><br>  Soldering Kit (with Soldering Iron)<br>  </td>
    <td class="tg-031e"><br>  1<br>  </td>
    <td class="tg-yw4l"><br>  $ 31.00 ***<br>  </td>
    <td class="tg-yw4l"><br>  Amazon<br>  Humber<br>  </td>
  </tr>
  <tr>
    <td class="tg-031e"><br>  3-D Case for RFID reader<br>  </td>
    <td class="tg-031e"><br>  1<br>  </td>
    <td class="tg-yw4l"><br>  $ 1.80<br>  </td>
    <td class="tg-yw4l"><br>  Toronto<br>  Public Library<br>  </td>
  </tr>
</table>
