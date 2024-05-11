/*
1. Fido is a dog.
2. Rover is a dog.
3. Henry is a dog.
4. Felix is a cat.
5. Jane is a cat.
6. Anything is an animal if it is a dog.
    
Answer queries :
    ● Find names of the dog. - dog(X). 
    ● Find names of the cat. - cat(X).
    ● Who is the animal?     - animal(X). 
*/

dog(fido).
dog(rover).
dog(henry).
cat(felix).
cat(jane).
animal(X):-dog(X).