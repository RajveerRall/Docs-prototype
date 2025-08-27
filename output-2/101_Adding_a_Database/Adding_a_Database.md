# Adding a Database

Configuring a database is a crucial step to enable data storage and retrieval within the 
application. Integrating a new database configuration allows you to specify connection details, select tables, and set up data sources that your app can interact with directly. By configuring the database, your application can seamlessly manage and access data as part of its automated workflows and user interactions.

● Click Add Database to add database configuration

● Enter the following configuration details and click Save: 
	○ Connection: @172.20.0.141 
	○ Database: trg_single 
	○ Schema: <username>_schema (e.g. amandalam_schema) 
	○ Dao Package Path: <BLANK> (Default) 
	○ Tables: product 
		■ Each of the tables in 'Assigned' will generate the DAO in the code. 		■ Usually in a project setting, you might not want to generate the DAO for 			all the tables in your project database for this particular microservice. In 			this case, you will select the relevant ‘product’ database table created.





● Click Apply to create the service







