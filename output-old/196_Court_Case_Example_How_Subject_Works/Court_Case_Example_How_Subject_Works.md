# Court Case Example: How "Subject" Works



We can use Subject to add RBAC control to the data level. In a Court Case Management system, we can use Subject to control the access rights for each court case.

Imagine a judicial system where different individuals take on roles such as Judges, Lawyers, and Clerks. Each role comes with specific privileges, but access to court cases should be restricted based on assignment.

Admin users may oversee case management but should not influence case outcomes.

Lawyers should only access the cases they are representing and file documents, but they cannot assign judges.

Judges should have full decision-making privileges over cases they are assigned to, but they cannot access or modify cases they are not involved in.

In this scenario, the court case itself acts as the Subject. A judge is not simply assigned a role, they are assigned a role in relation to a specific case.

