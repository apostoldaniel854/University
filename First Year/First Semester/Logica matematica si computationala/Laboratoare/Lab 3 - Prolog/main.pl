%checking if a number is a palindrome
rev([], []).
rev([H|Tailx], M) :- rev(Tailx, U), append(U, [H], M).
palindrome(L) :- rev(L, L).

%removing duplicates from a list
remove_duplicates([], []).
remove_duplicates([H|T], U) :- remove_duplicates(T, U), member(H, U).
remove_duplicates([H|T], [H|U]) :- remove_duplicates(T, U), not(member(H, U)).

%find if a number can be found a certain amount of times in the list
atimes(_, [], 0).
atimes(X, [H|T], W) :- atimes(X, T, Y), X =:= H, W is Y + 1.
atimes(X, [H|T], Y) :- atimes(X, T, Y), not(X =:= H).

%insertion sort
%L1 is sorted
insert(X, [], [X]).
insert(X, [H|T],[X|[H|T]]) :- X < H.
insert(X, [H|T], [H|M]) :- X >= H, insert(X, T, M).
insertsort([],[]).
insertsort([H|T],L) :- insertsort(T,L1), insert(H,L1,L).

%quicksort
split(_, [], [], []).
split(X, [H|T], [H|A], B) :- X > H, split(X, T, A, B).
split(X, [H|T], A, [H|B]) :- X =< H, split(X, T, A, B).
quicksort([],[]).
quicksort([H|T],L) :-split(H,T,A,B), quicksort(A,M), quicksort(B,N), append(M,[H|N],L).

%parcurgere arbori binari
srd(vid,[]).
srd(arb(R,T,U),L) :- srd(T,L1), srd(U,L2), append(L1,[R|L2],L).

%inserare in arbore binar de cautare
bt_ins(X, vid, arb(X, vid, vid)).
bt_ins(X, arb(ROOT, LEFT, RIGHT), arb(ROOT, V, RIGHT)) :- X < ROOT, bt_ins(X, LEFT, V).
bt_ins(X, arb(ROOT, LEFT, RIGHT), arb(ROOT, LEFT, V)) :- X >= ROOT, bt_ins(X, RIGHT, V).

% lista -> abore binar de cautare
bt_list([], vid).
bt_list([H|T], V) :- bt_list(T, W), bt_ins(H, W, V).

% sortarea unei liste folosind arbori binari de cautare
bt_sort(L, X) :- bt_list(L, T),  srd(T, X).
