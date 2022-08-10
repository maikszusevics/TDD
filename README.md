# Test Driven Development
## Definition
Test driven development is a method of development revolving around having predetermined test cases before deveopment begins.
It relies on an iterative approach which includes creation of tests first, development after, and finally refratoring.

![image](https://user-images.githubusercontent.com/110176257/183910933-804826ee-e782-4de2-9de0-09e6af137a24.png)


#### Steps of TDD
- Create tests
- Test tests to check if they are testing what we are looking to test
- Code what you need to be able to pass the test, and pass the test.
- Refractor what is necessary
- Repeat

### Benefits of TDD
- Efficient
- Cohesive
- Results in error-free code
- Results in readable code


## Create new python project for TDD 
### Created file with calculator class
``` python
class SimpleCals:

    def add(self, value1, value2):
        return value1+value2

    def subtract(self, value1, value2 ):
        return value1-value2
    def multiply(self, value1, value2 ):
        return value1*value2
    def divide(self, value1, value2 ):
        return value1/value2
        
```

### Created file called tdd for testing calculator class
```python 
import pytest
import unittest
from calc import SimpleCals

class Caltests(unittest.TestCase):
    calc_obj = SimpleCals()

    def test_add(self):
        self.assertEqual(self.calc_obj.add(4,2),6)

    def test_sub(self):
        self.assertEqual(self.calc_obj.subtract(4,2),2)

    def test_mult(self):
        self.assertEqual(self.calc_obj.multiply(4,2),8)

    def test_div(self):
        self.assertEqual(self.calc_obj.divide(4,2),2)
```
