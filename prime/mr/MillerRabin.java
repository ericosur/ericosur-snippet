/* Copyright (c) 2009 the authors listed at	the	following URL, and/or
the	authors	of referenced articles or incorporated external	code:
http://en.literateprograms.org/Miller-Rabin_primality_test_(Java)?action=history&offset=20080201093914

Permission is hereby granted, free of charge, to any person	obtaining
a copy of this software	and	associated documentation files (the
"Software"), to	deal in	the	Software without restriction, including
without	limitation the rights to use, copy,	modify,	merge, publish,
distribute,	sublicense,	and/or sell	copies of the Software,	and	to
permit persons to whom the Software	is furnished to	do so, subject to
the	following conditions:

The	above copyright	notice and this	permission notice shall	be
included in	all	copies or substantial portions of the Software.

THE	SOFTWARE IS	PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS	OR IMPLIED,	INCLUDING BUT NOT LIMITED TO THE WARRANTIES	OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT	SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER	LIABILITY, WHETHER IN AN ACTION	OF CONTRACT,
TORT OR	OTHERWISE, ARISING FROM, OUT OF	OR IN CONNECTION WITH THE
SOFTWARE OR	THE	USE	OR OTHER DEALINGS IN THE SOFTWARE.

Retrieved from:	http://en.literateprograms.org/Miller-Rabin_primality_test_(Java)?oldid=12469
*/

import java.math.BigInteger
import java.util.Random

public class MillerRabin
{
	private	static final Random	rnd	= new Random();

	private	static boolean miller_rabin_pass(BigInteger	a, BigInteger n) {
		BigInteger n_minus_one = n.subtract(BigInteger.ONE);
		BigInteger d = n_minus_one;
	int	s =	d.getLowestSetBit();
	d =	d.shiftRight(s);

		BigInteger a_to_power =	a.modPow(d,	n);
		if (a_to_power.equals(BigInteger.ONE)) return true;
		for	(int i = 0;	i <	s-1; i++) {
			if (a_to_power.equals(n_minus_one))	return true;
			a_to_power = a_to_power.multiply(a_to_power).mod(n);
		}
		if (a_to_power.equals(n_minus_one))	return true;
		return false;
	}


	public static boolean miller_rabin(BigInteger n) {
		for	(int repeat	= 0; repeat	< 20; repeat++)	{
			BigInteger a;
			do {
				a =	new	BigInteger(n.bitLength(), rnd);
			} while	(a.equals(BigInteger.ZERO));
			if (!miller_rabin_pass(a, n)) {
				return false;
			}
		}
		return true;
	}

    private static void try_nbits(int nbits) {
		BigInteger p;
		do {
			p =	new	BigInteger(nbits, rnd);
			if (p.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO)) continue;
    		if (p.mod(BigInteger.valueOf(3)).equals(BigInteger.ZERO)) continue;
	        if (p.mod(BigInteger.valueOf(5)).equals(BigInteger.ZERO)) continue;
	        if (p.mod(BigInteger.valueOf(7)).equals(BigInteger.ZERO)) continue;
		} while	(!miller_rabin(p));
		System.out.println(p);
    }

	public static void main(String[] args) {
	    if (args.length == 0) {
		    int nb = 1024;
            System.out.println("try " + nb + " bits...");
            try_nbits(nb);
        } else if (args.length == 2) {
    		if (args[0].equals("test"))	{
    			BigInteger n = new BigInteger(args[1]);
    			System.out.println(miller_rabin(n) ? "PRIME" : "COMPOSITE");
    		} else if (args[0].equals("genprime")) {
    			int	nbits =	Integer.parseInt(args[1]);
    			try_nbits(nbits);
		    }
		} else {
		    System.out.println("mr test 1234\nmr genprime 1024");
		}
	}
}

