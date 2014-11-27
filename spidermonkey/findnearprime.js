// findnearprime.js

// return a nearest prime from given number
// print() need to be connected or redirected

function print(x) { console.log(x); }

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

function find_near_prime(nn)
{
	if (is_prime(nn))
		return nn;

	var forward;
	var backward;

	// forward
	for (tt = nn+1; tt < nn*10; tt ++)
	{
		if (is_prime(tt))
		{
			forward = tt;
			break;
		}
	}

	// backward
	for (tt = nn-1; tt > 1; tt --)
	{
		if (is_prime(tt))
		{
			backward = tt;
			break;
		}
	}

	var ff_dis = Math.abs(nn-forward);
	var bb_dis = Math.abs(nn-backward);

	if (ff_dis <= bb_dis)  {
		return forward;
	}
	else  {
		return backward;
	}
}

var test_num = 3141592653;
print("find nearest prime for " + test_num);
var res = find_near_prime(test_num);
print("res: " + res);
