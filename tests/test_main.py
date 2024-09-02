import ast
import inspect
import io
from contextlib import redirect_stdout

import pytest

import app.main as main


@pytest.mark.parametrize("class_name", ["Animal", "Cat", "Dog"])
def test_classes_should_be_defined(class_name):
    assert hasattr(main, class_name)


@pytest.mark.parametrize(
    "class_name,methods",
    [
        ("Animal", ["print_name", "feed"]),
        ("Cat", ["print_name", "feed", "catch_mouse"]),
        ("Dog", ["print_name", "feed", "bring_slippers"]),
    ],
)
def test_classes_should_have_corresponding_methods(class_name, methods):
    class_to_test = getattr(main, class_name)
    for method in methods:
        assert (
            hasattr(class_to_test, method) is True
        ), f"Class '{class_to_test}' should have method {method}"


@pytest.mark.parametrize(
    "class_name,method",
    [
        ("Cat", "catch_mouse"),
        ("Dog", "bring_slippers"),
    ],
)
def test_only_one_method_should_be_declared_in_each_of_children_classes(
    class_name, method
):
    class_to_test = getattr(main, class_name)
    class_source = inspect.getsource(class_to_test)
    parsed_class = ast.parse(class_source)
    assert [name.id for name in parsed_class.body[0].bases] == [
        "Animal"
    ], f"'{class_name}' should be inherited from 'Animal'"
    assert (
        len(parsed_class.body[0].body) == 2
    ), f"Only one method '{method}' should be defined inside class '{class_name}' except '__init__'"
    assert method in (
        parsed_class.body[0].body[0].name,
        parsed_class.body[0].body[1].name,
    ), f"Only one method '{method}' should be defined inside class '{class_name}' except '__init__'"


@pytest.mark.parametrize(
    "name,appetite,output",
    [
        ("Puppy", 1, "Hello, I'm Puppy\n"),
        ("Kitten", 10, "Hello, I'm Kitten\n"),
    ],
)
def test_animal_print_name_method(name, appetite, output):
    animal = main.Animal(name, appetite)
    f = io.StringIO()
    with redirect_stdout(f):
        animal.print_name()
    assert f.getvalue() == output


@pytest.mark.parametrize(
    "name,appetite,output",
    [
        ("First", 3, "Eating 3 food points...\n"),
        ("Second", 7, "Eating 7 food points...\n"),
        ("Third", 102, "Eating 102 food points...\n"),
    ],
)
def test_animal_feed_method(name, appetite, output):
    animal = main.Animal(name, appetite)
    f = io.StringIO()
    with redirect_stdout(f):
        assert animal.feed() == appetite
    assert f.getvalue() == output


def test_animal_feed_not_hungry_animal():
    lion = main.Animal(name="Alex", appetite=25, is_hungry=False)

    f = io.StringIO()
    with redirect_stdout(f):
        feed_points = lion.feed()

    assert f.getvalue() == "", (
        "Method 'feed' should not print anything for non-hungry animal."
    )
    assert feed_points == 0, (
        "Method 'feed' should return 0 for non-hungry animal."
    )


@pytest.mark.parametrize(
    "name,output",
    [
        ("Cat1", "Hello, I'm Cat1\n"),
        ("Cat2", "Hello, I'm Cat2\n"),
        ("Cute Cat", "Hello, I'm Cute Cat\n"),
        ("Lady Stark", "Hello, I'm Lady Stark\n"),
    ],
)
def test_cat_print_name_method(name, output):
    cat = main.Cat(name)
    f = io.StringIO()
    with redirect_stdout(f):
        cat.print_name()
    assert f.getvalue() == output


@pytest.mark.parametrize(
    "name,output",
    [
        ("Cat1", "Eating 3 food points...\n"),
        ("Cat2", "Eating 3 food points...\n"),
        ("Cat3", "Eating 3 food points...\n"),
    ],
)
def test_cat_feed_method(name, output):
    cat = main.Cat(name)
    f = io.StringIO()
    with redirect_stdout(f):
        assert cat.feed() == 3
    assert f.getvalue() == output


@pytest.mark.parametrize(
    "name,output",
    [
        ("Dog1", "Hello, I'm Dog1\n"),
        ("Dog2", "Hello, I'm Dog2\n"),
        ("Cute Dog", "Hello, I'm Cute Dog\n"),
    ],
)
def test_dog_print_name_method(name, output):
    dog = main.Dog(name)
    f = io.StringIO()
    with redirect_stdout(f):
        dog.print_name()
    assert f.getvalue() == output


@pytest.mark.parametrize(
    "name,output",
    [
        ("Dog1", "Eating 7 food points...\n"),
        ("Dog2", "Eating 7 food points...\n"),
        ("Dog3", "Eating 7 food points...\n"),
    ],
)
def test_dog_feed_method(name, output):
    dog = main.Dog(name)
    f = io.StringIO()
    with redirect_stdout(f):
        assert dog.feed() == 7
    assert f.getvalue() == output


def test_cat_catch_method():
    cat = main.Cat("My cat")
    f = io.StringIO()
    with redirect_stdout(f):
        cat.catch_mouse()
    assert f.getvalue() == "The hunt began!\n"


def test_dog_bring_slippers_method():
    dog = main.Dog("My dog")
    f = io.StringIO()
    with redirect_stdout(f):
        dog.bring_slippers()
    assert f.getvalue() == "The slippers delivered!\n"


@pytest.mark.parametrize(
    "animals,total_food_points",
    [
        ([main.Cat("")], 3),
        ([main.Cat("", False)], 0),
        ([main.Dog("")], 7),
        ([main.Animal("", 10, False), main.Animal("", 10, False)], 0),
        ([main.Cat(""), main.Dog(""), main.Animal("", 10)], 20),
        ([main.Cat(""), main.Cat(""), main.Cat("")], 9),
        ([main.Dog(""), main.Dog(""), main.Dog(""), main.Animal("", 100, False)], 21),
    ],
)
def test_feed_animals_function(animals, total_food_points):
    assert main.feed_animals(animals) == total_food_points


def test_feed_animals_should_feed_animal():
    cat = main.Cat("Tom", is_hungry=True)
    lion = main.Animal("Lion", appetite=25, is_hungry=True)
    dog = main.Dog("Dog", is_hungry=True)
    main.feed_animals([cat, lion, dog])

    assert all([not animal.is_hungry for animal in [cat, lion, dog]]), (
        "Function `feed_animals` should feed all hungry animals."
    )


def test_animal_feed_is_used(mocker):
    mocked_method = mocker.patch("app.main.Animal.feed")
    cat = main.Cat("Tom", is_hungry=True)
    lion = main.Animal("Lion", appetite=25, is_hungry=True)
    dog = main.Dog("Dog", is_hungry=True)
    main.feed_animals([cat, lion, dog])
    assert mocked_method.call_count > 0, ("You have to use 'animal.feed' "
                                            "method in feed_animals function")
