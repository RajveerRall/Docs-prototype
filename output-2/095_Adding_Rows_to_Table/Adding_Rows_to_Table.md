# Adding Rows to Table

In a development environment, it is often necessary to quickly add data to a PostgreSQL table

for testing purposes. There are two main ways to add data to a PostgreSQL table: manually

through the user interface or by running SQL scripts. Below are the steps for both approaches.

● Right-click on the table and select Open Table.





● In the right panel, select Add Row (+)

● Enter the following details to the new row for the first record ○ id: 1 
○ name: Product A 
○ price: 499.99 
○ category: Electronics 
○ status: Approved 
○ brand: Brand X 
○ color: Black 
○ location: Singapore 
○ pdf_data: <null>

● Click Submit to save the new row





● Alternatively, we can select the Query console to run SQL scripts. Right click on table 	and select Query console

● Paste the SQL script below in the console and click Run







VALUES 
(2, 'Product B', 'Clothing', 'Brand Y', 'Blue', 'Approved', '29.99', 'Singapore'), (3, 'Product C', 'Electronics', 'Brand Z', 'Silver', 'Approved', '899.99', 
'Singapore'), 
(4, 'Product D', 'Clothing', 'Brand X', 'Blue', 'Approved', '49.99', 'Singapore'), (5, 'Product E', 'Electronics', 'Brand Y', 'Black', 'Approved', '99.99', 'Singapore'), (6, 'Product F', 'Home', 'Brand Z', 'Brown', 'Approved', '599.99', 'Singapore'), (7, 'Product G', 'Clothing', 'Brand Y', 'Red', 'Approved', '39.99', 'Singapore'), (8, 'Product H', 'Electronics', 'Brand X', 'White', 'Approved', '399.99', 
'Singapore'), 
(9, 'Product I', 'Clothing', 'Brand Z', 'Gray', 'Approved', '59.99', 'Singapore'), (10, 'Product J', 'Electronics', 'Brand Y', 'Silver', 'Approved', '149.99', 
'Singapore'), 
(11, 'Product 404', 'Electronics', 'Brand Y', 'Silver', 'Approved', '149.99', 
'Singapore'), 
(12, 'Product 400', 'Electronics', 'Brand Y', 'Silver', 'Approved', '149.99', 
'Singapore'), 
(13, 'Product 500', 'Electronics', 'Brand Y', 'Silver', 'Approved', '149.99', 
'Singapore');







![Image Description](./images/image_59.png)

● Back to the Table tab, we click Refresh and see the updated list of rows in the table

