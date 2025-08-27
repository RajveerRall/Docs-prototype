# Practical 21.1: Using default workflow (Claim-based routing)

The backend APIs have been integrated with some of the workflow APIs, enabling smooth communication and data exchange between the application's backend system and the workflow management platform.

Task Claiming: When a task becomes available within the workflow, it is open for claiming by any eligible participant or user.

Claim Ownership: The participant who claims the task takes ownership and responsibility for its completion.

Task Completion: Once claimed, the participant is expected to complete the task within a specified timeframe or according to predefined criteria.

● Navigate to the “Workflow Inbox” page 
	○ Task Claiming: When a task becomes available within the workflow, it is open 		for claiming by any eligible participant or user. Hence, all users can see the task 		for any user.

● Under “Actions” column, each user claim their own task by clicking on the “Claim” button 	○ Claim Ownership: The participant who claims the task takes ownership and 		responsibility for its completion.







● After claiming their own task, each user is now able to see only his/her own task. 	○ Task Completion: Once claimed, the participant is expected to complete the 		task within a specified timeframe or according to predefined criteria.

● Click on Approve/Reject button to complete the task



![Image Description](./images/image_68.png)





● According to the workflow, the task can either go through ‘Approval' or ‘Rejection’ flow. 	Click on either Approve or Reject

● In the workflow inbox, each user can see their own completed workflow by filtering status 	‘Finished’







Practical 21.2: Designing and Deploying customworkflow

This exercise involves designing and deploying a custom workflow by creating a sequence of automated steps to improve a business process. You'll start by analyzing the requirements, then design the workflow with tasks, conditions, and decision points. Next, implement the workflow by writing code or configuring a workflow tool.

● Click on the “Workflow” icon

● Import the workflow 
	○











Disclaimer: For this training , we will focus more on the BPMN workflow.

Import the downloaded workflow and press Create button.





Disclaimer: Above is the sample description of workflow element, not representing the imported workflow.

KAIZEN Workflow Task Elements

● In the imported workflow, rename it by changing the Process name to your username 	○ <username>





● Save the workflow

● Start designing the workflow





● We will be using the following two tasks for this training: 
	○ JDBC Task: involves connecting to a database using Java Database 
		Connectivity (JDBC) to execute SQL queries and manage database operations. 		This task allows for reading, updating, and manipulating database records within 		a workflow, ensuring data consistency and enabling dynamic data-driven 		processes.

○ Javascript Task: involves writing and executing JavaScript code within a workflow to perform custom operations. This task can include data manipulation, making API calls, handling conditional logic, and other dynamic behaviors, allowing for flexibility and control over workflow execution.







● Drag the JDBC task beside the HTTP Task



● Remove the original HTTP Task

● Update the JDBC task with the following values:





The JDBC task is trying to update the database directly by setting the status to ‘Approved’.

This database is the training central database that you have connected to via the Training Environment Profile earlier (the Profile feature will be explained in further details in Tutorial 23).

The workflow feature is running on the central db so all trainees can see Approved and Rejected tasks.







● Drag the Javascript Task to the workflow



● Update the Javascript task with the following javascript code:





This Javascript task ensures that the location must be ‘Singapore’ or ‘Malaysia’, else it will change the ‘isStatus’ to ‘Rejected’ and takes the Reject flow instead

try {
	 if ($processVariable.savedProduct.location=="Singapore"|| $processVariable.savedProduct.location=="Malaysia"){ 
				$processVariable.isStatus='Approved'; 
	} 
else { 
		$processVariable.isStatus='Rejected'; 
}

![Image Description](./images/image_69.png)

} catch (error){ 
console.log("Error has occurred: "+error.message); }



![Image Description](./images/image_70.png)





● Your complete workflow look like this

● Export your workflow

● Login to Training Environment ○ Username (Example: yongheng) 
○ Password (Password$1234)





● Navigate to Workflow Admin





● Deploy the workflow

● To use your workflow, frontend code logic needs to be modified.

Navigate to BE-Training App







![Image Description](./images/image_71.png)

Make Sure Training Profile is selected and configured as below

na 
Under the Source Code Panel of the FormSubmission page, edit and replace the value with your username





● Submit a form to trigger user task







![Image Description](./images/image_72.png)

● From the admin page, a new workflow instance was started.







![Image Description](./images/image_73.png)

● Open workflow inbox to claim and Reject the task that was submitted















● After rejecting the task , the workflow instance has been completed as shown below.





●  But why does it goes to “Approved” flow?

Previously we have added a javascript task to do location check in javascript in here.Thus if the location of product task was “Singapore” or “Malaysia”, the status will set to Approved”









![Image Description](./images/image_74.png)

Practical 21.3: Workflow observability 
In this practical 4.3, we will look into workflow observability features.

● Workflow Dashboard 
	● Workflow Instance Tracking 
	● Workflow Execution Timeline View 
Workflow Dashboard 
Dashboard allows users to gain overview of workflow running and status





Workflow Instance Tracking

Track and monitor the live execution of your workflows visually with color-coded indicators for easy identification, allowing you to spot workflow issues at a glance. Instance variable  and allows users to zoom in on specific tasks for quick diagnosis and resolution, by looking into the variables comparison passed between each workflow task. This will be useful in observing the variable transfer and changes in the workflow.

● Workflow Admin can also monitor the status of each workflow instances 	○ For example, the two instances were the one created earlier







● Click on “View Instance”

● By clicking on the page, we can view the instance variable values before and after the 	workflow task.

Workflow Execution Timeline View

The timeline feature allows users to look into the time execution of each workflow task. This is useful in observing any bottlenecks and deep dive into individual tasks for debugging in the event of error.

● We can also click on the ‘Timeline’ tab





● We can see the time execution of the task







