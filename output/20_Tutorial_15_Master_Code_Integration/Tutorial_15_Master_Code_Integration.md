# Tutorial 15: Master Code Integration

This tutorial covers the following Learning Objectives:



Understand how to integrate Master Code functionality within a low-code application.

Learn to bind specific master codes, such as location codes, dynamically to different entities.

Enhance application flexibility by allowing the dynamic assignment of master codes.



In this tutorial, you will learn how to integrate Master Code functionality into your application. Master Codes allow users to assign predefined codes to different entities, such as location or category codes. This integration improves the flexibility of your application, enabling dynamic assignment of codes that enhance data management and workflow precision.

## Practical 15.1: Integrating Master Code



(Note) Two Master Codes “Category” and “Location” were already created





In App Designer, click on Page1 Table page





![Image Description](./images/image_84.png)



Click on Category search field





(Note) Notice that the current values for this dropdown are static and hardcoded under

Datasource section





Click on the switch icon to switch to MasterCodeSetter in order to dynamically populate this field

![Image Description](./images/image_85.png)





![Image Description](./images/image_86.jpeg)



Select MasterCodeSetter





Note: MasterCodeSetter supports multiple components such as Select, Cascader, CascaderSelect, PhoneInput.

In the dropdown, select Category





Similarly,select Location form search field. Under Datasource, click on switch icon

and change to MasterCodeSetter





![Image Description](./images/image_87.jpeg)



In the dropdown, select Location





Preview the page





Perform the Searching function. Note that it still works as intended using Master Code values fetched dynamically, instead of hardcoded values





![Image Description](./images/image_88.jpeg)





## Practical 15.2: Multi language support (Optional)



Master code feature has a multi-language support. This enhancement will allow users to view and select master codes, such as location codes, in their preferred language, improving the accessibility and usability of your application for a global audience.

Master code translation to Chinese have already been created



Click on “Edit Application”. Note that multi-language support “Chinese” is enabled.



Preview the page and select “Chinese” as the language





In the dropdown select, noted that master code is using chinese translation







![Image Description](./images/image_89.png)



