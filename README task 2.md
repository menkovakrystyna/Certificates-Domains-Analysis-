# Certificates-Domains-Analysis-
Before creating a model I took into account some rules that might be helpful for detecting fishing accounts.

In document Task 2 - analysis rules:
core idea was to make a primary research to reveal what certain rules might be considered as fishing domains.
- creating group of rules that influence the detection of fishing/non fishing accounts
- applying all these rules as flags indicators and convert them as additional columns with separate 0/1 outputs. 
- creating a new csv file that has binary columns with rules and domains. 
- spliting the scv files into train and test sets.
- then for a train set I added an additional variable - Result, it means, that if domain have at least one rull - as  1, than the result consider to be a fishing domain (output)

Explanation of the rules:
1. weird_symbols_flag - searches if there is a dollar sign in our domain, if yes, we consider. it as fishing (1)
2. dots_5numbers_flag - if domain have more than 5 dots 
4. defis_2number_flag - if there are more than 3 '-'
5. ip_flag- if there are less than 12 numbers in the domain goes one after another splitted with dots
6. num_flag - if there are numbers splitted with '-' sighn
7. num_nosplit_flag - if there are numbers in the domain not splitted with dots
8. weird_word_flag - if there are some weird signs
9. length - if the lengh of the domain more than 40

In document Task - 2 Model
- Applying logistic regression and predicting the test20 csv domains.
- finding most inportant variables that influence whether the domain is fishin or not:
#the most importsnt feature that detect the fishing accounts are 
#dots_5numbers_flag - in domain there are more than 5 dots
#length - the lengh of the domain is more or equalls 40 symbolls
#num_nosplit_flag - there are less than 20 numbers, goes one by one in the domain
#defis_2number_flag -contains more or equalls 3 '-' in domain

- apling a trained model to a document test20.csv that contains only domains and flags indicators. 
- Store an aoutput whether the domain is fishing or not in a new file Prediction of Fishing Domains.csv.
