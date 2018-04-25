# P48 Truth tables for logical expressions (3).

Generalize problem P47 in such a way that the logical expression may contain any number of logical variables. Define table/2 in a way that table(List,Expr) prints the truth table for the expression Expr, which contains the logical variables enumerated in List.

### Example
```
>>> import sys
>>> sys.path.append('../')
>>> from P46.main import AND, OR, EQ
>>> from main import table
>>>
>>> def sample1(a, b):
...     return AND(a, OR(a, b))
...
>>> table(sample1)
[[True, True, True], [True, False, True], [False, True, False], [False, False, False]]
>>>
>>> # Or
...
>>> sample2 = lambda a, b, c: EQ(AND(a, OR(b, c)), OR(AND(a, b), AND(a, c)))
>>> table(sample2)
[[True, True, True, True], [True, True, False, True], [True, False, True, True], [True, False, False, True], [False, True, True, True], [False, True, False, True], [False, False, True, True], [False, False, False, True]]
```
