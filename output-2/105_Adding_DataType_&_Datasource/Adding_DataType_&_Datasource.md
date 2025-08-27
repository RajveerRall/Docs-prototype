# Adding DataType & Datasource

In the API Designer, defining data types and individual query parameters serves distinct but complementary purposes in the development of a robust API. When you define a data type, you create a reusable structure that represents an object in your application, such as a product or user. This data type encapsulates multiple attributes (fields) and their types, forming a Value Object (VO) in Java. VOs help maintain a clear and consistent representation of complex data throughout the application. By leveraging data types, developers can:

1. Promote Reusability: Once defined, a data type can be utilized across multiple 	endpoints, reducing redundancy and enhancing maintainability.

2. Simplify Code: Using VOs simplifies method signatures and enhances code readability by allowing developers to work with well-defined objects rather than primitive types.

● Firstly, in Service API designer, click on Add Data Type

● Define the Data Type with the following details: ○ Name: ProductVO 
○ Params:























● Click Apply to create the Data Type

● Next, select Add Datasource (+) under controller

● Create a postProduct datasource with the following details:









