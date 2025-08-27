# Information Input (Forms)

Forms are essential for collecting user input. KAIZEN's App Designer provides a powerful set of tools to create everything from simple contact forms to complex, multi-step wizards with validation.

## Introduction to Form Fields

Forms are built using a variety of **Form Item** components that accept user input. These can be found in the **Component Library**.

Common form fields include:
-   **Text Input:** For single-line text entries.
-   **Text Area:** For multi-line text.
-   **Select (Dropdown):** For selecting from a list of options.
-   **Checkbox:** For binary choices.
-   **Radio Button:** For selecting one option from a group.
-   **Date Picker:** For selecting dates.

## Form Validation

Validation rules ensure that the data submitted by users is in the correct format. This is the first line of defense against invalid data.

You can add validation rules to any **Form Item** from the **Props** tab. Common validation types include:
-   **Mandatory:** Ensures the field is not left empty.
-   **Length:** Restricts the minimum and/or maximum number of characters.
-   **Format:** Enforces specific formats, such as numbers, email addresses, or custom patterns using Regular Expressions (Regex).

---

## Practical Example: Creating a Multi-Step Form

In this tutorial, we will build a multi-step course creation form. This is a common pattern for breaking down long forms into manageable steps, improving the user experience.

Our form will have four steps:
1.  Course Info
2.  Instructor Particulars
3.  Class Location
4.  Class Schedule

### 1. Setting Up the Form Skeleton

Before adding the form fields, we need to create the basic structure.

-   **Create a New Page:** Start by creating a new page for your form.
-   **Add a Steps Component:** From the **Component Library**, drag a **Steps** component to the top of your page. This will serve as the visual indicator for the form's progress.
-   **Add a Form Template:** Drag a **Form Template** component below the Steps component. This will be the container for all our form fields.
-   **Create Navigation Buttons:** Inside the Form Template, add "Next" and "Previous" buttons to allow users to navigate between the steps.

### 2. Building the "Course Info" Form

The first step is to collect basic information about the course.

-   **Add Form Items:** Drag the necessary **Form Item** components into the form. For this step, we'll need:
    -   `Course Title` (Text Input)
    -   `Course Code` (Text Input with number validation)
    -   `Enrollment Type` (Select)
    -   `Subject Type` (Select)
    -   `Course Fee` (Text Input with number validation)
    -   `Description` (Text Area)
-   **Configure Validation:** Add validation rules to each field as needed. For example, make the `Course Title` and `Course Code` mandatory.

### 3. Creating Subsequent Steps

Follow a similar process to create the remaining forms for "Instructor Particulars," "Class Location," and "Class Schedule." You can use a variety of form fields to meet the requirements of each step.

### 4. Implementing Step Navigation

To make the multi-step form functional, you need to control the visibility of each form based on the current step.

-   **Use a State Variable:** In the **Source Code Panel**, create a state variable (e.g., `currentStep`) to keep track of the active step.
-   **Control Visibility:** For each form, use the **Advanced** tab to set the **Visible** property to an expression that checks the value of `currentStep`. For example, the "Course Info" form should be visible only when `this.state.currentStep === 0`.
-   **Add Logic to Buttons:** In the **Events** tab for the "Next" and "Previous" buttons, bind `onClick` events to functions that increment or decrement the `currentStep` variable.

By following these steps, you can create a user-friendly, multi-step form that guides users through the data entry process in a clear and organized manner.
