from primes_and_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print(odds.intersection(squares))  # odd perfect squares less than 100
print(evens & squares)  # even perfect squares less than 50

# pass an iterable to the method (won't work with operators '&', etc)
even_squares = evens.intersection(squares_generator(100))
print(even_squares)
