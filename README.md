# Design Pattern

Before learning desing pattern we should take deep knowledge about **Object Oriented Programming**.

## Major aspects of OOP

#### Encapsulation:
The key features of encapsulation:

<ul>
<li>An objects behavior is kept hidden from the outside world.</li>
<li>Client not directly change internal state acting on them rather client can send request to object. According to this request object change state such as set and get .</li>
<li>In python doesn't have public, private and protected keywords but accessibility can be made using __(double underscore) in the variable or function name.
</ul>

#### Polymorphism:
The key features of polymorphism:

<ul>
<li>Two types of polymorphism:<ul>
<li>An object provides different implementation of the method based on input parameters.</li>
<li>The same interface can be used by objects different types.</li>
</ul></li>
<li>In python polymorphism build in feature.For example: + operator can add two or more integers and also concate string</li>
</ul>


#### Inheritance
The key features of inheritance:

<ul>
<li>Inheritance indicates that one class derives functionality from the parent class.</li>
<li>Inheritance is described as an option to reuses functionality of parent class.</li>
<li>Inheritance creates hierarchy via the relationships among objects of different classes.</li>
</ul>

#### Abstract
The key features of Abstruct:

<ul>
<li>It provides you simpe interface to the client , where the clients can interact with class objects and call methods defined in the interface.</li>
<li>Abstruct can create abstruct method as well as can implement method inside class but interface can't do that.</li>
</ul>


#### Composition
The key features of Composition:

<ul>
<li>It is way to combine objects or classes into more complex data structure or software implementation.</li>
<li>In composition, an object is used to call member functions in other modules thereby making base functionality available across modules without inheritance.</li>
</ul>

```python
class A:
    def a1(self):
        print("a1")

class B:
    def b(self):
        print("b")
        A().a1()
obj = B()
obj.b()
```

## Object Oriented Design Principles:


#### The Single responsibility principle:

>  Single responsibility principle states that a class should have only one reason to change.

If a class taking care of two functionality, it is better to split them.

#### The Open/Close principle:
> The open/close principle state that classes or objects and methods are open for extension but close from modifications.

That means when we develop our software make sure that our writing classes or modules in a generic way. That's you can do extend behavior of class but not change to class itself.

For example: In Django user has to create a class implementation by extending the base abstract class to implement the required behavior insteat of changing the abstract class.

#### The inversion of control principle:

> The inversion of control principle states that hight level modules shouldn't be depend on low level modules; they should both dependent on abstractions. Details should depend on abstractions and not the other way round.

This principle suggested that any two modules shouldn't be dependent on each other(loose coupling or decouple).

This priciciples also suggested that the details of your class should represent the abstractions.

#### The interface segregation principle:
> This principle states that clients shouldn't be forced to depend on interface they don't use.

This principle suggestes that Develop mothods relevant to functionality. If there any method that is not related to the interface, the class dependent on the interface has to implement it unnecessary. 

#### The substitute principle:
> This principle states that derived classes must be able to completely substitute the base classes.

# The concept of design pattern:

#### Advantage of design pattern:

<ul>
<li>They are reusable across multiple projects.</li>
<li>The architectural level problems can be solved.
<li> They are time-tested and well-proven, which is the experience of developers and architects.
<li> They have reability and dependence.
</ul>


## Classification of Patterns:

 <ul>
 <li>Creational Patterns
 <li>Structural Patterns
 <li>Behavioral Patterns
 </ul>

#### Creational Patterns:
<ul>
<li>They work on basis of how objects can be created.
<li> They isolate the details of objects creations.
<li> Code is independent of the type of object
</ul>

#### Structural Patterns:
<ul>
<li>They design the structure of objects and classes so that they can compose to achieve larger results.
<li> The focus is on simplifiying the structure and identifying the relationship between classes and objects.
<li> They focus on class inheritance and composition.
</ul>