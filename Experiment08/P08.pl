/*
1. burger is a food
2. sandwich is a food
3. pizza is a food
4. sandwich is a lunch
5. pizza is a dinner
6. Anything is a meal if it is a food

Answer queries:
    ● Is pizza a food?               - food(pizza).
    ● Which food is meal and lunch?  - meal(X) , lunch(X).
    ● Is sandwich a dinner?          - dinner(sandwich).
*/

food(burger).
food(sandwich).
food(pizza).
lunch(sandwich).
dinner(pizza).
meal(X) :- food(X).