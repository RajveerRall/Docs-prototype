# General Components

General components are the basic building blocks of your user interface. They include fundamental elements like text, buttons, images, and containers. In this section, we will explore how to use one of the most versatile general components: the **Card**.

![Dragging a Component from the Library](../celldrag_and_drop.gif)

## Practical Example: Creating a Responsive Card

A responsive card is a container that adapts to different screen sizes, providing a clean and readable layout for your content on mobile, tablet, and desktop devices.

### 1. Add a Card Component

-   From the **Component Library**, search for "Card" and drag it into a **Cell** on your canvas.

### 2. Add a Picture Component

-   Next, search for the **Picture** component in the Component Library.
-   Drag the Picture component *inside* the Card component. This will serve as the header image for your card.
-   In the **Props** tab of the Picture component, you can set the image source and other properties.

### 3. Add a Container for Text

-   To organize the text content of your card, drag a **Box** component from the Component Library and place it below the Picture component.

### 4. Add Text Components

-   Drag two **Text** components into the Box.
-   Use the first Text component for the card's heading and the second for the subheading or body text.
-   You can customize the text and styling of each Text component using the **Setter Plugin**.

### 5. Binding Data to Create a Dynamic Card Grid

In many cases, you will want to create a grid of cards that are populated with data from a dynamic source, such as an API.

-   **Select the Card Component:** In the **Advanced** tab of the Setter Plugin, click on **Bind Data**.
-   **Provide the Data:** In the pop-up, you can provide a JSON array of data. Each object in the array will represent a card.
-   **Bind the Fields:**
    -   Select the **Picture** component and, in the **Props** tab, use the **Variable Input** option to bind the `Image` property to the corresponding field in your data (e.g., `this.item.imageUrl`).
    -   Do the same for the **Text** components, binding them to the heading and subheading fields in your data.

By following these steps, you can create a dynamic and responsive grid of cards that is populated with data from any source.