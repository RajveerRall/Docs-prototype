# Tutorial 6: Charts and Graphs

This tutorial covers the following Learning Objectives:

- Understand how to integrate and display various types of charts and graphs in KAIZEN.
- Learn how to visualize data effectively using different chart types like bar and pie charts.
- Explore how to bind data dynamically to charts for real-time updates.

In this tutorial, you will learn how to create and display charts and graphs in KAIZEN to visualize data effectively. We'll guide you through selecting the right chart types and binding them to dynamic data, enabling real-time updates. By the end of this tutorial, you'll be able to enhance your application with informative and interactive visualizations that help users interpret data quickly and easily.

## Practical 6.1: Adding Graph Components

### Setup Steps

1. **Add Cell Component**
   - From the Component Library, drag a Cell Component to the top of the Table in the Course Table Page that you have created from Tutorial 5.

2. **Add Tab Component**
   - Drag a Tab Component into the Cell Component.

3. **Configure Tabs**
   - Rename the tabs (and remove any extra) so that there are only these 2 tabs: 'Price Comparison' and 'Enrollment'.

Once you are done, you should have a structured layout with tabs for different chart types.

## Practical 6.2: Adding a Bar Graph

### Bar Chart Implementation
1. **Select Tab**
   - Select the 'Price Comparison' tab in the Tab Component.

2. **Add Bar Chart**
   - From the Component Library, search for 'chart' and drag a Bar Chart Component (aka Column Component) into the Price Comparison Tab.

3. **Configure Chart**
   - Set appropriate dimensions and styling for the bar chart
   - Configure axis labels and chart properties

## Practical 6.3: Adding a Pie Chart

### Pie Chart Implementation
1. **Select Tab**
   - Select the 'Enrollment' tab in the Tab Component.

2. **Add Pie Chart**
   - From the Component Library, search for 'chart' and drag a Pie Chart Component into the Enrollment Tab.

3. **Configure Chart**
   - Set appropriate dimensions and styling for the pie chart
   - Configure chart properties and legend settings

## Practical 6.4: Sending Data to the Graph

### Data Binding Process
1. **Select Chart Component**
   - Select the Column Component and under the Props Tab, click on Variable Binding.

2. **Configure Data Source**
   - Under 'Variable List', Select 'State attribute', then select 'data'.

3. **Confirm Binding**
   - Click the 'Confirm' button.

**Note**: The graph may disappear initially during the binding process.

4. **Configure Axis Labels**
   - Change the 'x-axis label' to 'price' and the 'y-axis label' to 'name'.

5. **Set Chart Dimensions**
   - With the Bar Chart Component still selected, go to the Styles tab and change the Height to 600px.

6. **Test Functionality**
   - If you click on Preview, you can hover over each column to see their specific x-axis labels.

## Chart Types and Use Cases

### Bar Charts
- **Best for**: Comparing quantities across categories
- **Use cases**: Price comparisons, enrollment numbers, performance metrics
- **Configuration**: X-axis (categories), Y-axis (values)

### Pie Charts
- **Best for**: Showing proportions of a whole
- **Use cases**: Enrollment distribution, course popularity, demographic breakdowns
- **Configuration**: Data labels, legend positioning, color schemes

### Line Charts
- **Best for**: Showing trends over time
- **Use cases**: Enrollment trends, performance tracking, time-series data
- **Configuration**: Time axis, value axis, trend lines

## Advanced Chart Features

### Interactive Elements
- **Tooltips**: Display detailed information on hover
- **Click Events**: Handle user interactions with chart elements
- **Zoom and Pan**: Allow users to explore data in detail

### Data Updates
- **Real-time Updates**: Bind charts to live data sources
- **Dynamic Filtering**: Update charts based on user selections
- **Data Refresh**: Implement automatic data refresh mechanisms

### Customization
- **Color Schemes**: Apply consistent branding and theming
- **Fonts and Typography**: Ensure readability and professional appearance
- **Responsive Design**: Optimize charts for different screen sizes

## Key Learning Points

- **Chart Selection**: Understanding which chart type best represents your data
- **Data Binding**: Connecting charts to dynamic data sources
- **Visual Design**: Creating clear and informative visualizations
- **User Experience**: Making charts interactive and user-friendly
- **Performance**: Optimizing chart rendering and data handling

## Expected Outcome

By the end of this tutorial, you will have created interactive charts that demonstrate:
- Effective data visualization techniques
- Dynamic data binding capabilities
- Professional chart styling and theming
- User-friendly interactive features
- Responsive design principles

This foundation will prepare you for more complex data visualization requirements and advanced chart customization scenarios.
