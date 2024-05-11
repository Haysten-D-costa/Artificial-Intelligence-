/*
1) jia is a woman.
2) john is a man.
3) john is healthy.
4) jia is healthy.
5) john is wealthy.
6) anyone is a traveler if he is healthy and wealthy.
7) anyone can travel if he is a traveler.

Answer queries.
    ● Who can travel?              - cantravel(X).
    ● Who is healthy and wealthy?  - healthy(X) , wealthy(X). 
*/

woman(jia).
man(john).
healthy(john).
healthy(jia).
wealthy(john).
traveller(X) :- healthy(X) , wealthy(X).
cantravel(X) :- traveller(X).