# Tutorial 4: Creating a Form with Steps

This tutorial covers the following Learning Objectives:

- Understand how to design a multi-step form using KAIZEN.
- Learn how to break down complex forms into manageable steps for a smoother user experience.
- Explore how KAIZEN simplifies form creation by providing step-by-step navigation and validation between steps.

In this tutorial, you will learn how to design and build a multi-step form using KAIZEN. By breaking down a complex form into smaller, more manageable steps, you'll create a smoother and more engaging user experience. KAIZEN's tools will guide you through adding step-by-step navigation, validation, and data handling, ensuring that users can easily complete the form without confusion.

## Overview

There will be 4 Forms in total:

1. **Course Info** - Basic course information
2. **Instructor Particulars** - Instructor details and qualifications
3. **Class Location** - Location and venue information
4. **Class Schedule** - Timing and scheduling details

## Introduction: Form Fields

Forms are components that accept inputs from various Form fields and then, through user interaction (usually a button press), submit the field information from the form to the backend for processing.

### Form Field Types

Previously, we encountered forms in Tutorial 1. A refresher on what the form looked like:

- **Email Field**: An Input Field that accepts open-ended text values
- **Password Field**: A special Input Field that masks input for security
- **Login Button**: Submits the form values to the backend

While this is sufficient for a Login Form, modern web languages also support a multitude of other form fields, like:
- Radio buttons
- Dropdown selects
- Date pickers
- Checkboxes
- And more

Fortunately, KAIZEN supports a good number of these. You can access them in the Component Library and search for them.

## Introduction: Form Validation

Validation (or Form Control) is a set of formatting rules defined for the browser to check. These validation rules usually act as an input format sanity check or as the first layer of defense against user-submitted dirty data, by allowing the browser to know when to warn and restrict the user before submission.

### Validation Types

- **Mandatory Validation**: The simplest validation type - fields must have values
- **Format Validation**: Ensures data matches expected patterns (email, phone, etc.)
- **Custom Validation**: Advanced validation rules for complex business logic

In KAIZEN's App Designer, Validations can be found in the Props tab for a Form.Item component.

## Practical 4.1: Setting up the Form

### Creating the Form Skeleton

Before the Tutorial begins, please do the following steps. This is to set up the form for the rest of the Practicals:

1. Create a new Form Page
2. Set up the basic form structure
3. Configure the form template
4. Add initial form fields

## Practical 4.2: Course Info Form

1. **Form Setup Complete**
   - Configure the form template
   - Add necessary form fields
   - Set up validation rules

2. **Form Fields Configuration**
   - Course name (text input)
   - Course description (text area)
   - Course category (select dropdown)
   - Course duration (number input)

## Practical 4.3: Instructor Particulars Form

### Context
This form captures detailed information about course instructors.

### Objective
Create a comprehensive form for instructor information including personal details, qualifications, and experience.

### Requirements
- Personal information fields
- Qualification details
- Experience information
- Contact details

### Expected Result
A well-structured form that collects all necessary instructor information with proper validation.

## Practical 4.4: Class Location Form

### Context
This form handles location and venue information for classes.

### Objective
Design a form that captures location details, venue information, and accessibility features.

### Requirements
- Address fields
- Venue details
- Accessibility options
- Map integration (optional)

### Creating a Field with 2 Inputs
Some location fields may require multiple inputs (e.g., street address and building number).

### Styling for the Inputs
Apply consistent styling to maintain visual hierarchy and user experience.

## Practical 4.5: Class Schedule Form

### Context
This form manages class timing and scheduling information.

### Objective
Create a form for scheduling classes with time slots, recurrence, and availability.

### Requirements
- Date and time selection
- Recurrence options
- Duration settings
- Availability indicators

## Practical 4.7: Setting Field Values Using Form Variables (Optional)

### Context
Advanced form functionality using dynamic field population.

### Requirements
- Understanding of form variables
- Dynamic field binding
- Conditional field display

### Adding the 'MyInfo' Button
Implement a button that automatically populates form fields with user information.

## Practical 4.8: Binding It All Together

### Adding the Code
Integrate all form components and ensure proper data flow between steps.

## Practical 4.9: Modal Dialog Box

### Steps for Creating a Modal Dialog
1. Add a Dialog component
2. Configure the dialog content
3. Set up trigger mechanisms
4. Style the modal appearance

## Key Learning Points

- **Multi-step Navigation**: Understanding how to create and manage step-by-step forms
- **Form Validation**: Implementing various types of validation rules
- **Component Integration**: Working with different form field types
- **Data Binding**: Connecting form fields to data sources
- **User Experience**: Creating intuitive and accessible forms

## Expected Outcome

By the end of this tutorial, you will have created a comprehensive multi-step form system that demonstrates:
- Professional form design principles
- Effective validation implementation
- Smooth user navigation between steps
- Proper data handling and binding
- Responsive and accessible form design

This foundation will prepare you for more complex form applications and advanced validation scenarios.
