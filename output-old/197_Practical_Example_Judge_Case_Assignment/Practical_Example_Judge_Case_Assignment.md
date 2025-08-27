# Practical Example: Judge Case Assignment



Consider Judge Alice and Judge Bob. They are both Judges, but their privileges are scoped to the cases they preside over.



Judge Alice is assigned with Judge role to Case #1001. She can review evidence, issue rulings, and set hearings for this case.

Judge Bob is assigned with Judge role to Case #1002. He has similar privileges but only within the context of his case.

Neither Judge Alice nor Judge Bob can interfere in each other's cases, even though both are Judges.

This fine-grained control is achieved by defining the court case as a Subject, ensuring that privileges are only valid within the assigned scope.



