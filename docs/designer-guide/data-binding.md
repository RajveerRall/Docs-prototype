# Data Binding & Dynamic Content

Data binding is the process that connects your application's user interface (UI) to its data source. This connection is crucial for creating **dynamic content**—content that changes based on the data it receives, rather than being hard-coded into the page.

In KAIZEN, data binding allows you to build complex, data-driven applications with ease. When your data updates, the UI elements bound to it will automatically reflect those changes.

## How Data Binding Works in KAIZEN

The core of data binding in KAIZEN revolves around two key concepts:

1.  **State Variables:** You can store data in the page's state. This data can be a simple value (like a string or a number) or a complex object or array.
2.  **Variable Binding:** You can then "bind" the properties of your UI components to these state variables.

This is typically done in the **Setter Plugin** using the **Variable Input** option, which is indicated by a `{/}` icon.

---

## Practical Example: Creating a Dynamic Card Grid

Let's walk through a common use case for data binding: creating a grid of cards that is dynamically populated from a list of data.

### 1. Prepare Your Data

First, you need a data source. For this example, we will create an array of objects in the **Source Code Panel**. Each object in the array will represent a card and will have properties for an image, a title, and a description.

```javascript
this.state = {
  cards: [
    {
      imageUrl: 'path/to/image1.png',
      title: 'First Card',
      description: 'This is the first card.'
    },
    {
      imageUrl: 'path/to/image2.png',
      title: 'Second Card',
      description: 'This is the second card.'
    }
  ]
};
```

### 2. Create a Reusable Card Template

Next, design a single **Card** component that will serve as the template for all the cards in your grid.

-   Drag a **Card** component onto the canvas.
-   Inside the Card, add a **Picture** component and two **Text** components (one for the title and one for the description).

### 3. Bind the Data to the Card

Now, we will use data binding to create a card for each item in our `cards` array.

-   Select the **Card** component.
-   In the **Advanced** tab of the Setter Plugin, click on **Bind Data**.
-   In the pop-up, bind the component to the `this.state.cards` array.

This tells KAIZEN to loop through the `cards` array and render one Card component for each object it finds.

### 4. Bind the Component Properties

The final step is to bind the properties of the components inside the card to the corresponding fields in the data.

-   Select the **Picture** component inside the card.
-   In the **Props** tab, click the **{/}** icon next to the `Image` property.
-   In the pop-up, bind the property to `this.item.imageUrl`. The `this.item` object represents the current item in the loop.

    ![Binding a Component Property](../assets/components/general/bd365229-dda1-44d6-9c24-8f88ea433687.png)

-   Repeat this process for the **Text** components, binding them to `this.item.title` and `this.item.description`.

Your card grid will now be dynamically rendered based on your data. If you add or remove items from the `cards` array, the UI will update automatically to reflect the changes.
