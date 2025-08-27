# Data Display (Tables & Charts)

Effectively displaying data is crucial for creating a user-friendly application. KAIZEN provides powerful components for organizing and visualizing data, including tables and charts.

## Tables

The **Table** component is a versatile tool for displaying structured data in a tabular format. It is highly customizable and supports features like sorting, pagination, and custom cell rendering.

### Practical Example: Creating a Table with Sorting and Pagination

In this tutorial, we will create a table to display a list of registered courses.

#### 1. Setting Up the Table

-   **Create a New Page:** Start with a new page for your table.
-   **Add a Table Component:** From the **Component Library**, drag a **Table** component onto the canvas.
-   **Configure Headers:** In the **Props** tab of the Table component, go to the **Data Column** section. Here, you can define the headers for your table. For our example, we will add headers for `Course Name`, `Course Code`, `Subject`, `Price`, etc.

#### 2. Adding Data to the Table

You can populate the table with data in several ways, but a common method is to use a state variable.

-   **Prepare Your Data:** In the **Source Code Panel**, create a state variable (e.g., `tableData`) and populate it with an array of JSON objects. Each object represents a row in the table, and the keys in the object should correspond to the **Data Key** you define for each column.
-   **Bind the Data:** Select the Table component, and in the **Props** tab, find the **Data Source** field. Use the **Variable Binding** option to link it to your `tableData` state variable.

#### 3. Implementing Sorting

-   **Enable Sorting:** For each column that you want to be sortable, edit the column in the **Data Column** section and enable the **Allow Sorting** option.
-   **Bind the Sort Event:** In the **Events** tab of the Table component, bind the `onSort` event to a function in your source code that will handle the sorting logic. This function should update the order of the data in your `tableData` state variable.

#### 4. Implementing Pagination

-   **Enable Pagination:** In the **Props** tab of the Table component, you will find the **Pagination Configuration** section.
-   **Bind Pagination Properties:**
    -   Bind the **Current Page** property to a state variable (e.g., `currentPage`).
    -   Bind the **Total Records** property to a state variable that holds the total number of items in your dataset.
    -   Bind the `onChange` event to a function that updates the `currentPage` state variable and fetches the data for the new page.

---

## Charts

Charts are an excellent way to visualize data and make it easier to understand. KAIZEN provides several chart components, including bar charts and pie charts.

### Practical Example: Adding a Bar Chart

Let's create a bar chart to compare the prices of different courses.

-   **Add a Chart Component:** From the **Component Library**, drag a **Bar Chart** component onto your page.
-   **Bind the Data:** In the **Props** tab, use the **Variable Binding** option to link the chart's data source to the same `tableData` state variable we used for the table.
-   **Configure Axes:**
    -   Set the **x-axis label** to the key in your data that represents the price (e.g., `price`).
    -   Set the **y-axis label** to the key that represents the course name (e.g., `name`).

By following these steps, you can create rich, interactive data displays that enhance the user experience of your application.
