// is_prime.js
// a demo js to test a given number is prime number or not


// return true if prime, false if not
function is_prime(nn)
{
	if (nn <= 1)
		return false;

	if (nn == 2 || nn == 3 || nn == 5 || nn == 7)
		return true;

	if (nn % 2 == 0 || nn % 3 == 0 || nn % 5 == 0 || nn % 7 == 0)
		return false;

	// first prime to test from 11
	for (pp = 11; pp*pp < nn; pp += 2)  {
		if (nn % pp == 0)
			return false;
	}

	return true;
}
