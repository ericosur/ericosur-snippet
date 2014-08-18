function FindProxyForURL(url, host)
{
	if (
		isPlainHostName(host)
		/* || isInNet(host, "10.193.0.0", "255.255.0.0") */
	)
	{
		return "DIRECT";
	}
	else
	{
		if (
			(myIpAddress() == "10.193.82.66")
		|| (myIpAddress() == "10.193.82.64")
		|| (myIpAddress() == "10.193.82.66")
		)
		{
			return "PROXY proxy.local:80";
		}
	}

	return "DIRECT";
}
