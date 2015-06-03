use JavaScript;

#print JavaScript::get_engine_version(),"\n";

my $rt = JavaScript::Runtime->new();
my $cx = $rt->create_context();
$cx->bind_function(write => sub { print @_; });
$cx->eval(q[

function is_prime(nn)
{
	if (nn <= 1)
		return false;

	if (nn == 2 || nn == 3)
		return true;

	if (nn % 2 == 0 || nn % 3 == 0)
		return false;

	for (pp = 5; pp*pp < nn; pp += 2)  {
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

	var res = find_near_prime(31415);
	write("res: " + res);


]);	# end of javascript section
