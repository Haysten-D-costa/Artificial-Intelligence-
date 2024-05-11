/*
1. John likes Susie.
2. Everyone likes Susie.
3. John likes everybody.
4. John likes everybody and everybody likes john.
5. John likes Susie or John likes Mary.
6. John does not like pizza.
7. John likes Susie if John likes Mary.

Answer queries:
    ● Does John likes Susie? - likes(john, susie).
    ● Whom does John likes? - likes(john, X).
*/

likes(john, susie). 
likes(X, susie).
likes(john, X).
likes(X, john).
likes(john, susie).
likes(john, mary).
not(likes(john, pizza)).
likes(john, mary) :- likes(john, susie).