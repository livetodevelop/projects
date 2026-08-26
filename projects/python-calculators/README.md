# Python Calculators

bunch of calculators i made for math class and personal projects. some are pretty basic but others actually useful

## calculators included

- `basic.py` - simple arithmetic (bored in math class)
- `quadratic.py` - solves quadratic equations
- `matrix.py` - matrix operations (for when you forget how to do it by hand)
- `unit_converter.py` - convert between units
- `fibonacci.py` - fibonacci sequence generator
- `prime_checker.py` - check if number is prime

## usage

```bash
python basic.py          # interactive calculator
python quadratic.py      # solve ax² + bx + c = 0
python matrix.py         # matrix math
python unit_converter.py # unit conversions
python fibonacci.py 10   # first 10 fibonacci numbers
python prime_checker.py 17  # check if 17 is prime
```

## examples

### quadratic solver
```bash
$ python quadratic.py
enter a: 1
enter b: -5
enter c: 6

roots: x = 2.0, x = 3.0
```

### fibonacci
```bash
$ python fibonacci.py 8
[0, 1, 1, 2, 3, 5, 8, 13]
```

### prime checker
```bash
$ python prime_checker.py 97
97 is prime!

$ python prime_checker.py 100
100 is not prime (divisible by 2)
```

## notes

- matrix calculator only works for 2x2 and 3x3 rn
- quadratic solver shows complex roots if needed
- unit converter supports: length, weight, temperature, time

might add more calculators when i learn new stuff in class
