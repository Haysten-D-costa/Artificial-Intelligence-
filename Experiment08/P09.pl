/*
1. charlie studies csc135
2. olivia studies csc135
3. jack studies csc131
4. arthur studies csc134
5. kirke teaches csc135
6. collins teaches csc131
7. collins teaches csc171
8. juniper teaches csc134
9. X is a professor of Y if X teaches C and Y studies C.

Answer queries:
    ● What does charlie study?                  - studies(charlie, X).
    ● Who are the students of professor kirke.  - teaches(kirke, X) , studies(Y, X).
*/

studies(charlie, csc135).
studies(olivia, csc135).
studies(jack, csc131).
studies(arthur, csc134).
teaches(kirke, csc135).
teaches(collins, csc131).
teaches(collins, csc171).
teaches(juniper, csc134).
professor(X, Y) :- teaches(X, C) , studies(Y, C).