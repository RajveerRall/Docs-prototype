# Tutorial 12: Main and Micro Applications

This tutorial covers the following Learning Objectives:

● Understand how to set up and manage a main application and micro-application 	architecture.

● Learn the advantages of micro-application architecture for scalability and flexibility.

In this tutorial, you will learn how to set up a main application with micro-applications. Micro-application architecture allows you to split your application into smaller, more manageable components, which enhances scalability, flexibility, and performance—an ideal solution for rapidly evolving environments. This aligns with the micro-frontend framework.

● These two Main and Micro applications have been created for you. Your current Designer Training Application that you have been working on is a “Standalone” application type.







● Generally, the Main application will contain the menu and it will load child Micro 	application(s). Note that one Main application can be tied to multiple micro applications.

● Navigator should be done in the Main application. Refer back to Practical 9.2 for more 	details.

● Customization of global layout should be done in the Main application via ‘Save to 	Application’ function. Refer back to Practical 9.2for more details.







● Customization of individual layout should be done in the Micro application via ‘Save to 	Page’ function. Refer back to Practical 9.2for more details.

Practical 12.1 Export and Import Pages to Main/Micro Apps

(Optional)

This practical covers the following Learning Objectives:

● Understand how to export and import pages in the App Designer.

In this practical, you will learn how to export and import your pages for use. This will be required in development when you need to either duplicate your existing pages in your application for ease of development, or in the case of this tutorial, to import pages into other applications.

● In your Designer Training application, we will first export the login page and 	import it over to the Main application.

○ Export Login Page from your original Designer Training application





○ Import into the Designer Training - Main application

● Do the same for the rest of the pages and import it accordingly as follows. Ensure to 	save and publish your applications once all imports are done.

○ Designer Training - Main 
	■ Login Page 
○ Designer Training - Micro 
	■ Listing Page 
	■ Landing Page 
	■ Form Page 
	■ Course Table





● Create the navigator in your main app to point to all 4 pages in the micro app.

● Once you preview your main app, you will be able to navigate to the different pages via 	the menu bar.







