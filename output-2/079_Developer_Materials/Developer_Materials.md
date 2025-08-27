# Developer Materials

In the upcoming tutorials, we will shift our focus to backend features that KAIZEN offers to support the development of backend services and APIs for your application. To explore these capabilities, we will use another application called “BETraining” which is designed to guide you through backend-centric functionalities.

Prerequisites (in folde

For Windows:

1. Node.js Version 18 (Preferably 18.20.4)
	○ Download and install 
2. Nginx
	○ Download  unzip and place it in your C:\ drive (C:/nginx).

3. Java
	○ Download and install 
		
4. Maven
	○ Download Maven Zip File and Extract 
	○ Install via this guide from Step 2 onwards -

For MacOS: 
	5. Node.js Version 18 (Preferably 18.20.4)
		○ Download this package 
			Or 
	6. Nginx
		○ brew install nginx 
	7. Java
		○ Download and install 
				
	8. Maven
		○ Download Maven: 
			Or download from URL
			
		○ Open the Terminal where your file being downloaded and Run this command on 			terminal 
			$ tar -xvf apache-maven-3.9.9-bin.tar.gz 
			$ sudo mv apache-maven-3.9.9 /opt/

$ export M2_HOME=/opt/apache-maven-3.9.9 	 export PATH=$M2_HOME/bin:$PATH





$ mvn -version (make sure it is v3.9.9 and its using JDK 17)





Architecture 
A simple network architecture of the training environment is provided below.

Full Diagram:





Creation of Profile

Add to create the “Training Environment Profile” in your App Designer. This will connect your application to the training environment which we have pre-created.

This is the runtime environment set up for this BETraining application, which we are connecting your application to via the App Designer profile feature directly. 
We will be going through more on the profile feature in Tutorial 23.



Ensure it is checked and refresh the page







