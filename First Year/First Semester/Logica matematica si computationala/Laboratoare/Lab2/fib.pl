fib(0, X) :- X is 1.
fib(1, X) :- X is 1.
fib(N, X) :- N >= 2, F1 is N - 1, F2 is N - 2, fib(F1, Y), fib(F2, Z), X is Y + Z.
