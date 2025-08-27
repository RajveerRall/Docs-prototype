# Practical 12.2 Add Action Page Type to Main App (Optional)

This practical covers the following Learning Objectives:

● Learn how to utilise the ‘Action’ type page in your applications.

In this practical, you will learn how to create a ‘logout’ button which will persist across all your application pages. In order to avoid having to duplicate global components that you want to persist on all pages (e.g. profile, logout, language toggle), you can create an ‘Action’ type page in your main application. In addition to action components, you can also create ‘Menu Header’ and ‘Footer’ type pages to persist the design of headers and footers across your application respectively.







● There are a few types of pages you can create for different purposes. In previous 	tutorials, you have only been using the standard ‘Page’ type.

○ Menu Header: A navigation element used to group related pages under a common section in the application’s menu. It helps organize and structure the navigation for better usability.

○ Footer: A section that appears at the bottom of the application’s interface, typically used for displaying copyright information, quick links, or additional navigation options.

○ Action: A page type designed for action components that persist across all 	pages in the application, such as profile settings, logout, and language toggle.

These components remain accessible regardless of the user's navigation.

○ Page: The standard content page where users can design and display UI components, input forms, data tables, and other interactive elements. This is the primary type used for building application interfaces.







● For this tutorial, create a new ‘Action’ page in your main app.

● Drag a Button component into the page.







● Set the button with the following styles and code. Save and publish your page changes.



● In the Resource panel, click on the ‘edit’ icon of your main app.

● Under Action, select the ‘Action’ page that you have just created and click ‘Save’.





● In preview mode of your main app, notice that the ‘Logout’ button added now forms part 	of the page header.







● Click on the Setting icon to customize your navigator menu. Select ‘Top Menu Layout’ 	for the Navigation Mode and click ‘Save To Application’.

● Now, the ‘Logout’ action button will appear at the top right across all pages.







● However, you may not want your action buttons to appear on all pages. In this case, it would not make sense to have this button (or access to the other pages via the menu bar) on the first Login page. Hence, you can choose to customize your navigator menu further by disabling the layout for the login page and clicking on ‘Save To Page’.







● Once you have logged in, you will be able to see the navigator menu and ‘Logout’ action 	button across all other pages.







