# Adding a Static Dataset to the Table

Now that the table is set up, it is time to add the content to each row for testing.



The Table Component parses JSON and uses it to generate the data it displays on the rows. Each Key in a JSON object will correspond to the header in the table and each Value in a JSON object will be the row value.





We can add the row values through 3 different ways under the Props tab > Data Column of the Table Component:

Click on the ‘Edit Data’ button. Modify the JSON accordingly.

Add the JSON data into the Source Code Panel in the Designer, then variable bind it.

Retrieve the data from an external datasource, like a backend server, then apply

variable binding to it.



For today, we will only be covering (b) in detail:



Open the Source Code Panel. Copy the entire file from below: Tutorial5-code.txt

Click Save on the top-right of the Source Code Panel.





Select the Table Component and under Props tab > Data Column, click on the Variable Binding (the {/}) for Data Source.





Under the Variable List, select State Attribute > table. Click on Confirm





Notice the data in the table has changed.





You can see that the headers are there, but the data it is displaying doesn’t look right. Let’s figure out what’s wrong:

Select the Table Component and under Props tab > Data Column, Click on the Edit

button on the ‘Course Name’ header.





Look at the Data Key field. This field takes the values of the key in a JSON object to put in the Table. So, this field must have exactly the same name as whatever the key is in our dataset.

Let’s examine one of the entries in the data we put in the Source Code Panel earlier:





We can see that the key, ‘name’, in this JSON, corresponds with ‘name’ in our own ‘Course Name Header. So that explains why the Table has those rows under ‘Course Name’ populated even though we have not done anything yet.

Now that we have figured it out, all that’s left to do is to change the rest of the headers.



On Props tab > Data Column, edit each header’s Data Key:







![Image Description](./images/image_44.jpeg)



Once done, you should have a table like this:





