
/*
Consider the following knowledge base :
    1. Moderate cough is a symptom of flu.
    2. Chills is a symptom of flu.
    3. Severe body ache is a symptom of flu.
    4. Running nose is a symptom of flu.
    5. Chills is a symptom of chickenpox.
    6. High fever is a symptom of chickenpox.
    7. Mild body ache is a symptom of cold.
    8. Running nose is a symptom of cold.
    9. Chills is a symptom of cold.

Answer the following queries using prolog :
    ● Get the list of all the diseases for which running nose is a symptom.         - symptom(runningnose, X).
    ● Find all the symptoms for disease cold.                                       - symptom(X, cold).
    ● Find out if there are any diseases with symptom chills.                       - symptom(chills, X).
    ● Find out all the possible diseases with symptom mild body ache or runny nose. - symptom(mildbosyache, X) ; symptom(runningnose, X).
    ● Which are the common symptoms for cold and flu.                               - symptom(X, cold) , symptom(X, flu).
*/

symptom(moderatecough, flu).
symptom(chills, flu).
symptom(severebodyache, flu).
symptom(runningnose, flu).
symptom(chills, chickenpox).
symptom(highfever, chickenpox).
symptom(mildbodyache, cold).
symptom(runningnose, cold).
symptom(chills, cold).