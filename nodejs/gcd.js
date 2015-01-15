// module gcd.js

exports.version = "1.0.0";

// calculate gcd number by rescursive
exports.gcd = function _gcd(m, n) {
	if (n == 0)
		return m;
	else
		return _gcd(n, m % n);
}

// 3rd arg is callback function to recv result
exports.hello = function(m, n, callback) {
    callback(m+n);
}
