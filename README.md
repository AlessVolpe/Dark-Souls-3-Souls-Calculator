# Dark Souls 3: Souls Calculator

A really simple python script used to calculate the amount of souls needed
to reach a certain level in Dark Souls 3.
Takes two levels as inputs from stdin, then uses the sequent formulas to 
calculate the minimum souls needed to reach that level:
- for levels in between 2 and 12
    ```
    ⌊673 * ((1 + 2.5 / 100)^x)⌋ where x is the level - 2
    ```
- for levels from 13 and onwards
    ```
    ⌊0.02 * x^3 + 3.06 * x^2 + 105.6 * x + 895⌋ where x is the level
    ```

The following function calculates the minimum amount of souls to reach a 
certain level
```python
def min_souls_needed(level):
    souls_2_12 = sum(levels_2_12(lvl) for lvl in range(2, min(level + 1, 13)))
    souls_13_onwards = sum(levels_13_onwards(lvl) for lvl in range(13, level + 1))
    return souls_2_12 + souls_13_onwards
```

To get the souls required to level up from your current level to the desired
one we have to subtract like following
```python
min_souls_needed(desired_level) - min_souls_needed(current_level)
```

## Soon, maybe

A website