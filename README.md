# Medical Android App Data Leakage Analysis Scripts



These scripts allow the researcher to decompile an android application and scan it for potential malicious injection points that could jeopardize the consumer's private information. It returns the decompiled code and two reports for the researcher to analyze.





Threat Model: 

The attacker aims to obtain sensitive health data from mobile applications.

Potential adversaries include:

* third-party analytics libraries
* advertising SDKs
* external network services receiving app data

Attackers may exploit insecure data handling practices or excessive data collection.

The defender analyzes application behavior to detect potential privacy leakage.





Requirements:

* Python 3.13
* JADX 1.5.5





Setup:

Windows

* Set JADX as a global installation by creating a new folder on the root of you C drive called tools
* Copy the contents of the "jadx-1.5.5.zip - cross-platform cli and gui bundle (system JRE must be installed)" download into a JADX folder within that tools folder

  * If it has a .bin file you copied the right thing
* Open Environment Variables
* Click edit the system environment variables
* Find the Path variable in User Variables
* Click New and paste the directory to the jadx .bin file
* Save changes
* Install Python 3.13





How to Run:

* In the root folder of this project you'll find/create APKS and DECOMPILED\_APKS folders
* Place your APKS in the APKS folder

  * If using XAPK files, rename them to .zip
  * the largest .APK in the folder is the base app, copy that back to the APKS folder and rename it to the app name
* Open a new terminal by right clicking the root folder
* Run $env:JAVA\_OPTS="-Xmx8G" to give Java 8GBs of RAM as a precaution
* Run python batch\_decompile\_jadx.py

  * you may get warnings but the decompile will still finish
* Run python analyze\_manifest\_jadx > manifest\_results.txt
* Run python scan\_java\_for\_sdks.py > sdk\_results.txt





Results:

* A populated DECOMPILED\_APKS folder
* A manifest\_results.txt file

  * results are in the order the files are in your folder
* A sdk\_results.txt file





Contributors:

* Eddie Soto-Ramirez
* Thinh Nguyen
* William Garcia

