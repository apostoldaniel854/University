distance((X1, Y1), (X2, Y2), ANS) :- ANS is sqrt((X1 - X2)**2 + (Y1 - Y2)**2).
fibg(0, 1, 0).
fibg(1, 1, 1).
fibg(N, X, Y) :- N > 1, A is N - 1, fibg(A, Y, Z), X is Y + Z.

line(0, C) :- nl.
line(N, C) :- N > 0, write(C), M is N - 1, line(M, C).
rectangle(0, M, C) :- nl.
rectangle(N, M, C) :- N > 0, line(M, C), K is N - 1, rectangle(K, M, C).
square(N, C):- rectangle(N, N, C).
