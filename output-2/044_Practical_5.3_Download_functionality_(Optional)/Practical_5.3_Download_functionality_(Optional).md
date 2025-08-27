# Practical 5.3: Download functionality (Optional)

Sometimes there is a need for the user to download files or data from your end. It is possible to do this with the Designer’s Source Code Panel. In this Practical, we will add a button that allows users to download the JSON data of the table we did in the previous Practical.





5.3.1 Add a download button 
	● Add a block to the bottom of the table.

● Drag a Button Component to Cell.







● Do some styling for the button and rename it to ‘Download Data as JSON’.

5.3.2 Add the download code 
	● Open the Source Code Panel. Uncomment the lines 297 - 301.

5.3.3 Event bind the download button 
	● Click on the Button Component and go to the Events tab and click on the ‘Component 		native event’ button. In the dropdown, click on ‘OnClick’.







● Under ‘Select event’, Click on ‘Event’, then click on ‘OnClick_Download’.

● Click on the ‘Ok’ button.

Now, whenever you click on the Download button, you will start downloading a JSON file with the table’s data.







