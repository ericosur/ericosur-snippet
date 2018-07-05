# Readme on 24C12

c24.py is a python script to list combinations about a game that user selects 12 numbers from 1 to 24.
Total combinations are
$ C^{12}_{24} = 2704156 $

* All hit case is 1.
* All miss case is 1.

* Only one hit, 11 misses case is 144.
$ C^{1}_{12} * C^{11}_{12} = 144 $
and its ratio is
$ \frac{144}{2704156} = 5.325*10^{-5} = 0.005325\% $

* Two hits, 10 misses
$ C^{2}_{12} * C^{10}_{12} = 4356 $
and its ratio is
$ \frac{4356}{2704156} = 1.611*10^{-3} = 0.1611\% $
