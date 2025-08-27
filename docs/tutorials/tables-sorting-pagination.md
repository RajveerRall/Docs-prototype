# Tutorial 5: Tables, Sorting and Pagination

This tutorial covers the following Learning Objectives:

- Understand how to create and structure tables in KAIZEN to display data effectively.
- Learn how to implement client-side sorting functionality to allow users to organize data by different columns.
- Explore how to add client-side pagination to tables to manage large data sets efficiently.
- Discover how KAIZEN simplifies the integration of sorting and pagination features to enhance user interaction.

In this tutorial, you will learn how to create and manage tables in KAIZEN to display data clearly and efficiently. We'll guide you through implementing sorting and pagination features, allowing users to interact with and organize large sets of data easily. By the end of this tutorial, you'll be able to enhance your application's data presentation with dynamic, user-friendly tables.

## Overview

For this example, we will be creating a registered course list table, containing the following columns:
- Course Name
- Course Code
- Subject
- Enrollment Type
- Duration
- Schedule
- Price
- Number of Students enrolled

## Practical 5.1: The Table Component

The Table Component is a template that you can use to create tables for your projects with relative ease. You can find it in the Component Library as a component called 'Table'. Simply drag it out into the design space as you would any other component.

### Setting up the Table Component

1. **Create a new Course Table Page**
2. **Add the Table Component**
   - From the Component Library, drag out the Table Component into the Cell in the Design space
3. **Configure the Table**
   - Under Props, remove the Add and Edit buttons by deleting them under the Action Bar
   - Delete the Edit and Preserve links under the Action Column as well
4. **Set Table Dimensions**
   - Under Styles, change the width of the Table to 100%
   - Go to the Props tab and go to Style and theme
   - Turn on the Fixed Header switch
   - Set the Max body height to 800px

### Setting the Table Headers

The configuration for changing the headers are located in the Props tab of the Table itself under Data Column. You can change these values and it will reflect on the Design space. Add and/or remove the headers accordingly with the buttons in the Data Column menu.

You should add headers for:
- Course Name
- Course Code
- Subject
- Enrollment Type
- Duration
- Schedule
- Price
- Students

## Practical 5.2: Sorting

### Understanding Sorting
Sorting allows users to organize table data by different columns in ascending or descending order. This enhances data exploration and user experience.

### Implementation Steps
1. **Enable Sorting**
   - Configure sorting options in the table properties
   - Set which columns are sortable
   - Define default sort order

2. **Sort Configuration**
   - Choose between single or multi-column sorting
   - Set initial sort column and direction
   - Configure sort indicators

## Practical 5.3: Pagination

### Understanding Pagination
Pagination breaks large datasets into manageable pages, improving performance and user experience when dealing with extensive data.

### Implementation Steps
1. **Configure Pagination**
   - Set items per page
   - Configure page navigation controls
   - Set initial page number

2. **Pagination Controls**
   - Previous/Next buttons
   - Page number indicators
   - Items per page selector

## Practical 5.4: Download Functionality (Optional)

### Adding Export Features
Enhance your table with data export capabilities:
- CSV export
- PDF generation
- Excel file download

### Implementation
1. **Add Export Button**
   - Configure export button in action bar
   - Set export format options
   - Handle export data processing

## Advanced Table Features

### Data Binding
- Connect table to data sources
- Implement real-time data updates
- Handle data refresh scenarios

### Custom Styling
- Apply consistent theming
- Customize row and cell appearance
- Implement conditional styling

### Responsive Design
- Ensure table works on mobile devices
- Implement horizontal scrolling for small screens
- Optimize column widths for different screen sizes

## Key Learning Points

- **Table Structure**: Understanding how to create and configure table components
- **Data Management**: Implementing effective data display and organization
- **User Interaction**: Adding sorting and pagination for better user experience
- **Performance**: Managing large datasets efficiently
- **Customization**: Styling and configuring tables to match your application design

## Expected Outcome

By the end of this tutorial, you will have created a professional data table that demonstrates:
- Clean, organized data presentation
- Interactive sorting functionality
- Efficient pagination for large datasets
- Professional styling and theming
- Responsive design principles

This foundation will prepare you for more complex data display requirements and advanced table customization scenarios.
