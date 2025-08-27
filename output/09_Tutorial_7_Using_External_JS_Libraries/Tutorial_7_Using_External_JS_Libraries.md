# Tutorial 7: Using External JS Libraries

This tutorial covers the following Learning Objectives:



Understand how to integrate external JavaScript libraries into your KAIZEN application.

Learn how to enhance application functionality by leveraging popular libraries like uuid.js, and others.

Explore the process of importing and utilizing external libraries to extend the capabilities of your application.

In this tutorial, you will learn how to integrate external JavaScript libraries into your KAIZEN application to enhance its functionality. We’ll guide you through the process of importing and using libraries like uuid.js to add features such as advanced data transformation and interactivity. By the end of this tutorial, you’ll be equipped to extend your application’s capabilities by seamlessly integrating third-party JavaScript libraries.



## Practical 7.1: Importing a UUID JS Library (Demonstration)



We will be returning to the Step Form page we created before to demonstrate how to use this feature.

Let’s say, now, the Instructor has to submit a special Registration code that was provided to them before to confirm their identity. This Registration code will be in a UUIDv4 format. When working on the form, we would like to generate the UUID to make it more convenient for ourselves.

However, by default, the Kaizen App Designer does not have a library to generate UUIDs. Fortunately, Kaizen is capable of supporting external JS libraries to help with this.

Setup Steps

Go to the 2nd Step (Open the Source Code Panel and change the “currentStep” to 1,

then save the Source Code).

Duplicate the Cell of the Contact No Form Item.





Select the duplicated form item and change the Label to ‘Registration No’ and Property Name to ‘registrationNo’.





Select the Registration No Form Item and select Default for the Format Validation.





Adding the Library

Select the Libraries option from the left sidebar. Click on the ‘Install’ button.





Fill in the info for the ‘Add Library’ form:







Click on the ‘Save’ button.

Reload the Page.



With the uuid library installed, we can now use it in our Source Code. You can look at the possible functions here: https://www.npmjs.com/package/uuid/v/8.3.1.



Using the library

Before using the library, make sure that Tutorial 4.7.3 Adding the ‘MyInfo’ Button is done so there is the button to trigger the below method. If not, do proceed to create a button in the Instructor Particulars form component under the FormPage.

In the Source Code Panel, add the following line in the retrieveSingPassMyInfo() function:











Preview and click on the MyInfo button to check if the UUID is generated correctly.





