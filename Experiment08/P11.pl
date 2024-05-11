/*
Consider the following knowledge base:
    1) Marcus was a man.
    2) Marcus was a pompeian.
    3) All pompeians were roman.
    4) Caesar was a ruler.
    5) All romans were either loyal to Caesar or hated him.
    6) People only try to assassinate ruler whom they are not loyal to.
    7) Marcus tried to assassinate Caesar.
    8) All mens are people.

Answer the following queries using prolog:
    ● Who tried to assassinate ruler?   - tryassassinate(X, Y), ruler(Y).
    ● Was Marcus loyal to Caesar?       - loyal(marcus, caesar).
    ● Whom did Marcus hate?             - hate(marcus, X).
*/

man(marcus).
loyal(X, Y).
hate(X, Y).
pompeian(marcus).
roman(X) :- loyal(X, carsar) ; hate(X, caesar).
pompeian(X) :- roman(X).
ruler(caesar).
tryassassinate(marcus, caesar).
tryassassinate(X, Y) :- not(loyal(X, Y)).
people(X) :- man(X).
