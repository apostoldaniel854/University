fibg(0, 1, 0).
fibg(1, 1, 1).
fibg(N, X, Y) :- N > 1, A is N - 1, fibg(A, Y, Z), X is Y + Z.

line(0, _) :- nl.
line(N, C) :- N > 0, write(C), M is N - 1, line(M, C).
rectangle(0, _, _) :- nl.
rectangle(N, M, C) :- N > 0, line(M, C), K is N - 1, rectangle(K, M, C).
square(N, C):- rectangle(N, N, C).

all_a([]).

all_a([a|Tail]) :- all_a(Tail).

trans_a_b([], []).
trans_a_b([a|Taila], [b|Tailb]) :- trans_a_b(Taila, Tailb).
