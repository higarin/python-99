# P46 Truth tables for logical expressions.

Define predicates and/2, or/2, nand/2, nor/2, xor/2, impl/2 and equ/2 (for logical equivalence) which succeed or fail according to the result of their respective operations; e.g. and(A,B) will succeed, if and only if both A and B succeed. Note that A and B can be Prolog goals (not only the constants true and fail).

### Example
```
>>> from main import *
>>> AND(True, True)
True
>>> OR(True, True)
True
>>> NAND(True, True)
False
>>> NOR(True, True)
False
>>> XOR(True, True)
False
>>> IMP(True, True)
True
>>> EQ(True, True)
True
```

A logical expression in two variables can then be written in prefix notation, as in the following example: and(or(A,B),nand(A,B)).

Now, write a predicate table/3 which prints the truth table of a given logical expression in two variables.

### Example
```
>>> from main import *
>>> def sample1(a, b):
...     return AND(a, OR(a, b))
...
>>> table(sample1)
[[True, True, True], [True, False, True], [False, True, False], [False, False, False]]
>>> # Or
...
>>> sample2 = lambda a, b: AND(a, OR(a, b))
>>> table(sample2)
[[True, True, True], [True, False, True], [False, True, False], [False, False, False]]
```
