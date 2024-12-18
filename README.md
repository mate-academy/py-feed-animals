# Feed animals

**Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
before starting.

All animals love delicious food. Let's create a new class to feed them.
Create class `Animal` which `__init__` method takes three arguments:
* `name` - the animal name
* `appetite` - an integer that shows how much *food points* this animal need to eat to be full.
* `is_hungry` - boolean that shows if animal is ready to eat with `True` default value.

`Animal` should have two methods:
* `print_name` - should print name in the following format: `Hello, I'm {name}`
* `feed` - should print `Eating {appetite} food points...`, 
set `is_hungry` to `False` and return number of eaten food points if animal is hungry.
Otherwise, it should return 0 and print nothing.

Example:
```python
lion = Animal("Lion", 25)
lion.print_name()  # "Hello, I'm Lion"
food_points = lion.feed()  # "Eating 25 food points..."
print(food_points)  # 25
print(lion.is_hungry)  # False
print(lion.feed())  # 0
```

There is a well-known fact that all cats eat 3 food points at a time.
Also, they can catch a mouse.
Write `Cat` class which is a child of `Animal`. 
It should have the `__init__` method with two arguments:
* `name` - the name of a cat
* `is_hungry` - with `True` default value

Note: you need call the super class `__init__` method with `appetite` equal to 3.

`Cat` should have only one additional method `catch_mouse` which should print 
`The hunt began!`

Example:
```python
cat = Cat("Cat")
cat.print_name()  # "Hello, I'm Cat"
cat.feed()  # "Eating 3 food points"

cat2 = Cat("Cat", False)
print(cat2.feed())  # 0
cat2.catch_mouse()  # "The hunt began!"
```

The last class you should implement is a `Dog` class.
Its `__init__` method should have two arguments:
* `name` - the name of a dog
* `is_hungry` - with `True` default value

All dogs should have `appetite` equal to 7.

`Dog` should have one additional method `bring_slippers` that should print
`The slippers delivered!`

Example:
```python
dog = Dog("Dog")
dog.print_name()  # "Hello, I'm Dog"
dog.feed()  # "Eating 7 food points"

dog2 = Dog("Dog", False)
print(dog2.feed())  # 0
dog2.bring_slippers()  # "The slippers delivered!"
```

Now, it's time to feed many animals at a time.
Implement `feed_animals` function which takes a list of animals. 
It should feed passed animals and return a sum of food points that are needed to feed all hungry
animals from this list.

Example:
```python
cat = Cat("Cat", False)
lion = Animal("Lion", 25, True)
dog = Dog("Dog")
feed_animals([cat, lion, dog]) == 32
```

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
