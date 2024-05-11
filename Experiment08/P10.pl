/*
Consider the following knowledge base :
    1) Charlie is suffering from fever.
    2) Charlie is suffering from running nose.
    3) Charlie is suffering from headache.
    4) Micky is suffering from cough, headache, running nose and sneezing.
    5) Branda is suffering from fever and rash.
    6) A patient is hypothesis having flu if he is suffering from headache, body ache, fever, running nose, cough and conjunctives.
    7) A patient is hypothesis having measles if he is suffering from fever, cough, conjunctives, running nose and rash.
    8) A patient is hypothesis having whooping cough if he is suffering from cough, sneezing, and running nose.

Answer the following queries using prolog :
    a) Who is suffering from fever?                                         - suffering(X, fever).
    b) Which symptoms Branda is suffering from?                             - suffering(branda, X).
    c) Find the common patients with symptoms headache and running nose.    - suffering(X, headache) , suffering(X, runningnose). 
    d) Find the common symptom of Charlie and Micky.                        - suffering(charlie, X) , suffering(micky, X).
*/

suffering(charlie, fever).
suffering(charlie, runningnose).
suffering(charlie, headache).
suffering(micky, cough).
suffering(micky, headache).
suffering(micky, runningnose).
suffering(micky, sneezing).
suffering(branda, fever).
suffering(branda, rash).
hypothesis(X, flu) :- suffering(X, headache), suffering(X, bodyache), suffering(X, fever), suffering(X, runningnose), suffering(X, cough), suffering(X, conjunctives).
hypothesis(X, measles) :- suffering(X, fever), suffering(X, cough), suffering(X, conjunctives), suffering(X, runningnose), suffering(X, rash).
hypothesis(X, whoopingcough) :- suffering(X, cough), suffering(X, sneezing), suffering(X, runningnose).