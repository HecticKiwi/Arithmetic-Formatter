# Arithmetic-Formatter
This function takes in a list of strings that are arithmetic problems and formats them vertically and side-by-side.

For example, arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]) becomes:

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

arithmetic_arranger() optionally takes a second argument *show_answer*, which when `True` will add the answer to the display.

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True) will return:

```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Input Constraints
This function will return an error if given an invalid input in the following cases:
* There are more than five problems
* An operator other than '+' or '-' is used
* Operands are not positive integers
* Operands are more than four digits
