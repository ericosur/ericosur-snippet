// a simple js to perform recusively call
console.log( (function fact(n)  {
    if (n <= 1) return 1;
    return n * fact(n-1);
})(5) );
