/*
1. Pam is a parent of bob.
2. Tom is a parent of bob.
3. Tom is a parent of Liz.
4. Bob is a parent of Ann.
5. Bob is a parent of Pat.
6. Pat is a parent of Jim.

Answer queries : 
    ● Who is a grandparent of Jim?           - parent(X, jim), parent(Y, X).
    ● Who are Tom's grandchildren?           - parent(tom, X), parent(X, Y).
    ● Do Ann and Pat have a common parent?   - parent(X, ann), parent(X, pat).
    ● Who is Pat's parent?                   - parent(X, pat).
    ● Who is Pat's grandparent?              - parent(X, pat), parent(Y, X).
    ● Does Liz have a child?                 - parent(liz, X).
*/

parent(pam,bob). 
parent(tom,bob). 
parent(tom,liz). 
parent(bob,ann). 
parent(bob,pat). 
parent(pat,jim).