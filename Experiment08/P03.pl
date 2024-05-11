/*
1) Charlie is a parent of James.
2) Elizabeth is a parent of James.
3) George is a parent of Sophia.
4) Catherine is a parent of Sophia.
5) Charlie is a parent of kith.

Answer queries:
    ● Was George the parent of Sophia.    - parent(george, sophia).
    ● Who are Jame's parents?             - parent(X, james).
    ● Who are the childrens of Charlie?   - parent(charlie, X).
    ● Who is a parent of whom?            - parent(X, Y).
*/

parent(charlie, james).
parent(elizabeth, james).
parent(george, sophia).
parent(catherine, sophia).
parent(charlie, kith).