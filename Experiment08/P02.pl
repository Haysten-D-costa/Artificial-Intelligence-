/*
1. Fido is a dog.
2. Fido is large.
3. Rover is a dog.
4. Rover is large.
5. Tom is a dog.
6. Mary is a cat.
7. Bill is a cat.
8. Bill is large.
9. Anything is large animal if it is a dog and large.

Answer querie : 
    ● Who is the large animal. - largeanimal(X).
*/

dog(fido).
dog(rover).
dog(tom).
large(fido).
large(rover).
large(bill).
cat(mary).
cat(bill).
largeanimal(X):-dog(X), large(X).