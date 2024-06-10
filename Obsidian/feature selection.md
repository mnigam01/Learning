one hot encoding using
get_dummies
i we have let say 20 categorical columnns and each column contains >100 categories we may end up with lots of feature columns. One solution is take 10(changeable) most frequent categories from all columns and keep everything as some 11 category or dropped since we drop first column of one hot encoding
https://www.youtube.com/watch?v=6WDFfaYtN6s&list=PLZoTAELRMXVPwYGE2PXD3x0bfKnR0cJjN&index=1


ordinal categories i.e., rank do label encoding

Target guided ordinal Encoding
![[Pasted image 20240602212848.png]]
![[Pasted image 20240602212905.png]]
![[Pasted image 20240602212913.png]]

now sort the last column genre_... or mean. Give first category as 1, 2, 3 and so on. 
romance  1
nonfiction 2
sci fi 3
and so on


mean encoding
groupy based on category and take mean like above picture only. Now replace these category with their respective mean or drop category column and just take last column

count encoding  (Nominal Variable)
when i have large number of label in a categoryical column we can replace those category by the count they appeared in the column



# Missing Value in categorical
treat that column as target use other column to to train a classifier, use those rows where value is absent as test data now predict it and fill it instead of None

2. use clustering, let say this column has 2 category and some missing data. Use other columns and use clustering algorithm to cluster it. Now create a new column telling which row belongs to which cluster. Now observe for category 1 how many are cluster 1 and how many cluster 2. now based on this we can change None to category 1 or 2.


Handling missing values
mean/median/mode imputation   (disadvantage change or distortion in original variance)
random sample imputation (advantage less distortion in variance)
capturing nan value with a new feature
end of distribution imputation
arbitrary imputation
frequent category imputation