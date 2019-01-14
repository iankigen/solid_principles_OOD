# S.O.L.I.D: The First 5 Principles of OOD (object-oriented design)
S - single responsibility principle

O - open closed principle

L - Liskov substitution principle

I - Interface segregation  principle

D - dependency inversion principle


- Single Responsibility Principle (SRP):
	- A Class should be responsible for a single task or a class must have a specific purpose. The idea behind this principle is that each of your classes, modules, methods are responsible for one and only one thing.
	
- Open-Close Principle:
    - This principle states that Objects or entities should be open for extension, but closed for modification. This simply means that a class should be easily extendable without modifying the class itself.

- Liskov substitution principle:
    - Liskov substitution principle says every class that inherit from a parent class, must not replicate functionality already implemented in the parent class.
    
- Interface segregation principle:
    - Interface segregation principle states that many specialized interfaces are better than one universal. In other words we can say this also that client must not be forced to implement an interface that it doesn’t use. So the main purpose is to divide the interfaces so that they are more specific.
    
- Dependency Inversion Principle:
    - Dependency inversion principle states that :
        - High level modules should not depend on low-level modules, both should depend on abstractions.
        - Abstractions should not depend on details. Details should depend on abstractions.
        - Or it can be rephrases as “the dependencies should be based on abstractions, not details.”