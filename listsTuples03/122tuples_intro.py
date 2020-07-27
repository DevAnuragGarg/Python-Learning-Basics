t = "a", "b", "c"
print(t)

# try to use parenthesis around tuples
s = ("a", "b", "c")
print(s)

imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the lightning", "Metallica", 1984

print(imelda[0])
print(metallica[2])

# tuples are immutable, if you try to change
# something at any index you will get error. They don't have overhead
# methods so they use less memory than list. Protect the integrity of tulip

metallica2 = list(metallica)
print(metallica2)
