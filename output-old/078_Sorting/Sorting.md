# Sorting

In order to sort a table, we will first need to determine which data columns will be sortable and then set them as such in the Designer.

The 4 columns that will be sortable are:

Course Name

Duration

Price

Students

Under Data Column, Click on the Edit button beside the Course Name header.





Enable Allow Sorting.

Repeat the same steps for Duration, Price and Students



Note in the Table in the Designer’s display area has changed the column to have an up/down arrow beside the headers you have changed. Clicking on it does nothing for now. We will need to do some event binding.

Under the Events tab, click on the Component native event button.





In the dropdown, select the onSort event.





In the popup, select Event, click on onSort. Then click on the Confirm button.





We should now be able to sort by clicking on the headers in each column.



