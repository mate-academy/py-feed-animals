# Сheck Your Code Against the Following Points

## Make Code Easier

1. Don't use an extra `else` statement.

Good example:

```python
if self.is_hungry:
    return "Is hungry!"
return "Is not hungry!"
```

Bad example:

```python
if self.is_hungry:
    return "Is hungry!"
else:
    return "Is not hungry!"
```

2. Don't use a `for` loop if you can use generator expression.

Good example:

```python
return sum(item.process() for item in collection)
```

Bad example:

```python
total = 0
for item in collection:
    total += item.process()
return total
```

## Code Style

1. Use descriptive and correct variable names.

Good example:

```python
my_dict = {"one": "a", "two": "b"}
[(number + " " + letter) for (number, letter) in my_dict.items()]
```

Bad example:

```python
my_dict = {"one": "a", "two": "b"}
[(k + "  " + v) for (k, v) in my_dict.items()]
```

2. While creating a dictionary/list — write key-value pairs/values in a single row. The curly braces must be located in one of two options: open and start with the text or have a line break between the text. 

Good example:

```python
my_dict = {
    "greeting": "Good morning, have a nice day!", 
    "answer": "Good morning, thanks!"
}

```

Also a good example:

```python
my_dict = {"greeting": "Good morning, have a nice day!", 
	   "answer": "Good morning, thanks!"}
```

Bad example:

```python
my_dict = {"greeting": "Good morning, have a nice day!", 
	   "answer": "Good morning, thanks!"
}
```

