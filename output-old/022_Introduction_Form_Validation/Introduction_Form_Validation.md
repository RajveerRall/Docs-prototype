# Introduction: Form Validation

Validation (or Form Control) is a set of formatting rules defined for the browser to check. These validation rules usually act as an input format sanity check or as the first layer of defense against user-submitted dirty data, by allowing the browser to know when to warn and restrict the user before submission. The users are usually then allowed to change their inputs based on the warnings given by the browser.

You can see this in action, if you ever played around with the Login Form above, and tried to submit without any values typed into the form:





This is because the Form Template that is in App Designer’s Component Library has Mandatory Validation enabled by default for both its form fields. Mandatory Validation on means that the field in question has to have a value in it for the form to treat it as a valid submission.

Of course, Mandatory Validation is the simplest validation. There are other more complex validation types that might find more use in more complex form fields. In Kaizen’s App Designer, the Validations can be found in the Props tab for a Form.Item component.





