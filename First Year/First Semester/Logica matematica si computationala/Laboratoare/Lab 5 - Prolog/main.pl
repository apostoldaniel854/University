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
%ex 1
vars(X, [X]) :- atom(X).
vars(non(X), L) :- vars(X, L).
vars(si(A, B), L) :- vars(A, L1), vars(B, L2), union(L1, L2, L).
vars(sau(A, B), L) :- vars(A, L1), vars(B, L2), union(L1, L2, L).
vars(sau(A, B), L) :- vars(A, L1), vars(B, L2), union(L1, L2, L).
vars(imp(A, B), L) :- vars(A, L1), vars(B, L2), union(L1, L2, L).

%ex 2
val(V, E, A) :- member((V, A), E).

%ex 3
bnon(0, 1).
bnon(1, 0).
bsi(1, 1, 1).
bsi(1, 0, 0).
bsi(0, 1, 0).
bsi(0, 0, 0).
bimp(1, 0, 0).
bimp(1, 1, 1).
bimp(0, 0, 1).
bimp(0, 1, 1).
bsau(1, 1, 1).
bsau(1, 0, 1).
bsau(0, 1, 1).
bsau(0, 0, 0).

%ex 4
eval(X, E, A) :- atom(X), val(X, E, A).
eval(imp(X, Y), E, A) :- eval(X, E, A1), eval(Y, E, A2),
    bimp(A1, A2, A).
eval(non(X), E, A) :- eval(X, E, A1), bnon(A1, A).
eval(sau(X, Y), E, A) :- eval(X, E, A1), eval(Y, E, A2), bsau(A1, A2, A).
eval(si(X, Y), E, A) :- eval(X, E, A1), eval(Y, E, A2), bsi(A1, A2, A).

%ex 5
evals(_, [], []).
evals(X, [HE|TE], [HA|TA]) :- evals(X, TE, TA), eval(X, HE, HA).

%ex6
addx(_, [], []).
addx(X, [E|T], [[(X, 0)|E], [(X, 1)|E]|L]) :- addx(X, T, L).
evs([], [[]]).
evs([X|T], L) :- evs(T, L1), addx(X, L1, L). 

%ex7
all_evals(X, Y) :- vars(X, V), evs(V, E), evals(X, E, Y).
%ex8
all_ones([]).
all_ones([1|Y]) :- all_ones(Y).
taut(X) :- all_evals(X, Y), all_ones(Y).

