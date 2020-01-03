README
======

To calculate a proper fraction into egyptian fraction form. That is a sum of unit fractions. For example,
```math
\frac{6}{17} = \frac{1}{3} + \frac{1}{51}
\\
\frac{8}{19} = \frac{1}{3} + \frac{1}{12} + \frac{1}{228}
```

required module: sympy

## reference

- [mathworld](http://mathworld.wolfram.com/EgyptianFraction.html)
- [wikipedia](https://en.wikipedia.org/wiki/Egyptian_fraction)
- [wolfram alpha](https://www.wolframalpha.com/input/?i=Egyptian+fraction&a=*C.Egyptian+fraction-_*MathWorld-&f2=4%2F5&f=EgyptianFractionCalculator.fraction%5Cu005f4%2F5)
- [geeksforgeeks](https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/)


## files

- [gcd_lcm.py](./gcd_lcm.py) my own handmade version to calculate gcd, lcm
- [rat.py](./rat.py) With sympy and greedy algorithm, to get egyptian fractions
- [egypt.py](./egypt.py) downloaded from geeksforgeeks, will overflow if some denominator is very large.

## note

```math
\frac{5}{121} =
\frac{1}{25} + \frac{1}{757} + \frac{1}{763309} + \\
\frac{1}{873960180913} +  \\
\frac{1}{1527612795642093418846225}
```

A puzzle relates with egyptian fraction, is [Shepherd and Sheep Problems](https://gdaymath.com/lessons/fractions/4-2-egyptian-fractions/)


An elderly shepherd, died and left his entire flock of 17 sheep to his three sons. To his first son, whom he admired dearly, he bequeathed half his flock of sheep. To his second son, with whom he was in some favor, one third his flock and to his third son, whom he considered a rogue, one-ninth of his flock. The sons realized that the proportions are strange and that the number 17 is resistant to convenient divisibility, yet they found a clever way to successfully honor their father’s wishes. What was their solution?

> lcm(2, 3, 9) = 18

```math
\frac{17}{18} =
\frac{1}{2} + \frac{1}{3} + \frac{1}{9}
```

lcm of multiple numbers: https://www.calculatorsoup.com/calculators/math/lcm.php
