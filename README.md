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

### refractor calculator class in calc file
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

### Added 3 more tests to the TDD file:

![image](https://user-images.githubusercontent.com/110176257/183935671-9d482622-a5aa-472c-b479-52bc33fbb4f7.png)


#### When run, they fail:

![image](https://user-images.githubusercontent.com/110176257/183935887-77af5dba-8cc1-47b8-9325-150dcc678fcd.png)


- added functionality for DOB:

![image](https://user-images.githubusercontent.com/110176257/183937325-dfae9760-c3ad-4002-ae35-3a566a9f57e5.png)

- now only 2 tests fail, so DOB passes test

![image](https://user-images.githubusercontent.com/110176257/183937454-316ff7ec-9641-46ba-aa8b-9bee056abc38.png)


- added the rest of the fucntions

![image](https://user-images.githubusercontent.com/110176257/183937965-706bd48a-8820-4b52-83fd-3f9ea4ff65b7.png)

#### All tests passed:

![image](https://user-images.githubusercontent.com/110176257/183938027-320360da-cb8b-49c6-9ad6-916e108b4751.png)




