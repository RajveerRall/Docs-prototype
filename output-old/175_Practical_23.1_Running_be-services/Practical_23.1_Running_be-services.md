# Practical 23.1: Running be-services



For local development, the application requires running multiple services to simulate the production environment effectively. Developers need to run four jar files locally, each representing a critical component of the application. These jar files work together to provide the necessary backend functionality for testing, debugging, and developing features.

Download the following based on your Operating System:

If you are using Windows:

BETraining_JAR(CloudDaaSenv)-Windows.zip







Unzip the zip file. There should be a script file included (either a .sh for MacOS or Linux or .bat for Windows)





Open command prompt in the unzipped folder





Run the jar files through the script provided:

For Windows:

Run the script using ./start.bat









The script should open 5 terminal windows with the following KAIZEN microservices: IAM, Common, Console, Gateway, IAM Proxy:





Ensure that the applications run with no exceptions/stack traces. Alternatively, you can look out for the default Spring Boot Application started message (ie. Started Application in xx.xxx seconds (process running for xx.xxx))



