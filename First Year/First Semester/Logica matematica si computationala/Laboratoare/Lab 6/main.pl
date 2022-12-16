%creata a list
listN([],0).
listN([a|T], N) :- N > 0, M is N - 1, listN(T,M).

%reversing a list -> R is the reversed List
reva(L,R) :- revah(L,[],R).
revah([], R, R).
revah([H|T], S, N) :- revah(T,[H|S],N).

revd(L,R) :- revdh(L,(R,[])).
revdh([],(R,R)).
revdh([H|T],(N,S)) :- revdh(T,(N,[H|S])).

%flattening a list using append
flatten([], []).
flatten([H|T], ANS) :- is_list(H), flatten(H, L), flatten(T, R), append(L, R, ANS).
flatten([H|T], [H|ANS]) :- flatten(T, ANS).

%flattening a list using difflists
flattenbetter(L, ANS) :- flattendif(L, (ANS, [])).
flattendif([], (ANS, ANS)). 
flattendif([H|T], (R, S)) :- 
    is_list(H), 
    flattendif(H, (R, X)),
    flattendif(T, (X, S)).
flattendif([H|T], ([H|R], S)) :- not(is_list(H)), flattendif(T, (R, S)).
% (R - X) + (X - S) = (R - S)

% normal quicksort from lab 4
quicksort([],[]).
quicksort([H|T],L) :- split(H,T,A,B), quicksort(A,M),
quicksort(B,N), append(M,[H|N],L).
split(_,[],[],[]).
split(X,[H|T],[H|A],B) :- H < X, split(X,T,A,B).
split(X,[H|T],A,[H|B]) :- H >= X, split(X,T,A,B).

% quicksort using difflists
quicksortbetter(L, ANS) :- quicksortdif(L, (ANS, [])).
quicksortdif([], (ANS, ANS)).
quicksortdif([H|T],(R, S)) :- split(H, T, A, B), quicksortdif(A, (R,[H|X])), quicksortdif(B, (X,S)). 
% (R - (H|X) + (X - S) = (R - H|S)

% formal language derived by this gramatics

sent(R) :- np(A), vp(B), append(A,B,R).
np(R) :- dete(A), n(B), append(A,B,R).
vp(R) :- tv(A), np(B), append(A,B,R).
vp(R) :- v(R).
dete([the]). dete([a]). dete([every]).
n([teacher]). n([doctor]). n([park]).
tv([likes]). v([walks]).

% the same with difflists

sentd(R) :- sentdh((R,[])).
sentdh((R,S)) :- npdh((R,Z)), vpdh((Z,S)).
npdh((R,S)) :- detedh((R,Z)), ndh((Z,S)).
vpdh((R,S)) :- tvdh((R,Z)), npdh((Z,S)).
vpdh((R,S)) :- vdh((R,S)).
detedh(([the|S],S)). detedh(([a|S],S)).
detedh(([every|S],S)).
ndh(([teacher|S],S)). ndh(([doctor|S],S)).
ndh(([park|S],S)).
tvdh(([likes|S],S)). vdh(([walks|S],S)).

% defining a gramatic with its special syntax
sentgh --> np, vp.
np --> dete, n.
vp --> tv, np.
vp --> v.
dete --> [the]. dete --> [a]. dete --> [every].
n --> [teacher]. n --> [doctor]. n --> [park].
tv --> [likes]. v --> [walks].
