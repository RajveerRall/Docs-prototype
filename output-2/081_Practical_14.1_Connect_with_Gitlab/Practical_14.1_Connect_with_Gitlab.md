# Practical 14.1: Connect with Gitlab

In thisenvironment, a group “KAIZEN-Training” has already been created for the purpose of this training. In addition, a sub-group has also been created for each trainee prefixed with your username ‘kaizen-training-<username>’ (E.g. kaizen-training-amandalam).

Similarly, in your project’s context, you may create subgroups for different applications required in your project (E.g. FE internet portal, BE intranet portal), and each subgroup will then be initialized with your application repositories. After which, you may then connect to Git in KAIZEN by configuring the respective group.

Navigate back to your KAIZEN studio console, you will notice that the current branch for your application is on ‘main’. We will go through a later tutorial on Git Branch Management to allow you to push your changes onto your repositories.





14.1.1 Generate Gitlab Personal Access Token

● Login to your gitlab account as follows and reset your password 	○ URL: 		
	○ Username: <username> 
	○ Password: ahdoh6shaechaip0seidu1ahnailoogaeF8Ainie● Navigate to your gitlab account profile, click Edit Profile

● Click on Access Tokens







● Create your personal access token 
○ Token name:access_token 
○ Expiration date: leave as default 
○ scope:api, read_api, read_repository, write_repository

●  Copy the generated token to store it for later use

14.1.2 Connect to Git

● On the KAIZEN studio console, click on the Git button of your BE Training project and 	click Connect.





● Select Gitlab as the service provider and click Next

● Enter the following details to connect to Gitlab 
	○ URL: 	○ Personal Access Token: <token-string> 
	○ Group: kaizen-training/kaizen-training-<username> ● Click on Test Connect to test your connection







● The group to specify is the url path of your group and subsequent subgroups where you 	will be initializing your project.

● Note that if the “Separate BE Group” checkbox is selected, then “Group” will specify the 	group for your Frontend Repository and “BE Group” will be for your Backend Repository.

If it is not selected, then both FE and BE will be connected to the same Git group. This is to help aid in development such that you will not need to always re-connect to another group path in the event you want to push your code in your BE repository.

● Once successful, click on Save to connect.

