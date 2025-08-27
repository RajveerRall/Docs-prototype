# Adding the logic for the Modal Dialog

Open the Source Code Panel and uncomment lines 118 - 123 and 127 - 129. And click

Save.





Select the Dialog Component (Under Component Tree)





Under the Events tab and click on the Component native event button.





Select the onOk event from the dropdown that appears.





Under Event and then click ‘OnClick_ConfirmSubmit’.





Go to the Props tab for this Dialog Component. For the ‘Visible’ field, click on the

Variable Binding {/}.





Under Bind Variables, enter the following: this.state.confirmVisible. Once done, click Confirm.





Select the Submit button on the ‘Class Schedule’ Form, and go to the Events tab. Click on the ‘Component native event’ button.

Temporary changes the showAll flag to true







Select ‘onClick’ in the dropdown that appears.





Under ‘Select event’, click on ‘Event’, and then click on ‘onClick_Submit’.





Now go back to your Source Code Panel, change back the flag to false





Change your OnClick_ConfirmSubmit function to navigate back to your course listing page, by changing the navigateTo in utils1 function to use the correct App ID and Page ID.

If you have not completed tutorial 3 in creating your course listing page, you may navigate to your landing page instead for now.











Having trouble finding the App ID and Page ID?



You can find the App ID under resources. Click on the App, then click on Edit Application.

































Similarly, you can find the Page ID under resources as well. All you have to do is to hover over your page created in Day 2 and you will get the Page ID. You may also click on edit page to view the Page ID.



And Finally…



Let’s go through the form together. Click Preview.



Step 1: Course Info



Step 2: Instructor Particulars



Step 3: Class Schedule



Step 4: Class Location



Form Submission: Redirect back to Course Listing





