-- comment go here
print("hello world")

-- defines a factorial function
function fact (n)
	if n == 0 then
		return 1
	else
		return n * fact(n-1)
	end
end

num = 10
print("fact(10):")
print(fact(10))

a = 1; b = a * 2
print(a)
print(b)
