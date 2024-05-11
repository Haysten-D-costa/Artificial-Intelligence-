/*
1. Tom is a cat
2. Kunal loves to eat Pasta
3. Hair is black
4. Nawaz loves to play games
5. Pratyusha is lazy.
6. Lili is happy if she dances.
7. Tom is hungry if he is searching for food.
8. Jack and Bili are friends if both of them love to play cricket.
9. Ryan will go to play if school is closed, and he is free.

Answer queries:
    ● Who loves to eat pasta?  - loveseat(X, pasta).
    ● Who is lazy?             - lazy(X).
    ● Who loves to play game?  - lovesplay(X, games).
    ● Is Lili happy?           - happy(lili).
    ● Will Ryan go to play?    - go(ryan, play).
*/

cat(tom).
loveseat(kunal, pasta).
hair(black).
lovesplay(nawaz, games).
lazy(pratyusha).
dances(lily).
closed(school).
free(ryan).
searching(tom, food).
happy(lily) :- dances(lily).
hungry(tom) :- searching(tom, food).
friends(jack, bili) :- lovesplay(jack, cricket) , lovesplay(bili, cricket).
go(ryan, play) :- closed(school), free(ryan).