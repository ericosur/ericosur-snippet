# Readme on 24C12

## description

c24.py is a python script to list combinations about a game that user selects 12 numbers from 1 to 24.
Total combinations are
$ C^{12}_{24} = 2,704,156 $


* All hit case is 1.
```math
1 \cdot 1 \cdot ... \cdot 1 = 1
```

* All miss case is 1.

* Only one hit, 11 misses case is 144.
```math
C^{1}_{12} \cdot C^{11}_{12} = 144
```
and its ratio is
```math
\frac{144}{2704156} = 5.325*10^{-5} = 0.005325\%
```

* Two hits, 10 misses
```math
C^{2}_{12} \cdot C^{10}_{12} = 4356
```

and its ratio is
```math
\frac{4356}{2704156} = 1.611*10^{-3} = 0.1611\%
```

## appendix

Use my own Casio fx-3650P, to calculate $ C^{12}_{24} $
24 SHIFT ÷ (nCr) 12 EXE

* ÷ (U+00F7)

###### tags: ```math``` ```combination``` ```lottery```
