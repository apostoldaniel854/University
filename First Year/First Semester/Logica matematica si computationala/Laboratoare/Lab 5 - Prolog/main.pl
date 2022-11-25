%si(1, 1).
%sau(1, 0).
%sau(0, 1).
%sau(1, 1).
%imp(1, 1).
%imp(0, 1).
%imp(0, 0).
%non(0).

%length([], 0)
%length([H|T], N) :- length(T, M), N is M + 1.

vars(X, [X]) :- atom(X).
vars(non(X), L) :- vars(X, L).
vars(si(A, B), L) :- vars(A, L1), vars(B, L2), union(L1, L2, L).
vars(sau(A, B), L) :- vars(A, L1), vars(B, L2), union(L1, L2, L).
vars(sau(A, B), L) :- vars(A, L1), vars(B, L2), union(L1, L2, L).
vars(imp(A, B), L) :- vars(A, L1), vars(B, L2), union(L1, L2, L).

val(V, E, A) :- member((V, A), E).
