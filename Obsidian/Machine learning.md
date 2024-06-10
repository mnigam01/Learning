


ols (ordinary least square)
help in selecting more significant feature columns which impact dependent variable(target)
The higher the t-value for the feature, the more significant the feature is to the output variable. And also, the p-value plays a rule in rejecting the Null hypothesis(Null hypothesis stating the features has zero significance on the target variable.). If the p-value is less than 0.05(95% confidence interval) for a feature, then we can consider the feature to be significant.


p value less than 0.05 say we significant evidence to reject null hypothesis (like drug is not effective)
p value >= 0.05, less evidence to reject null hypothesis



what is R2
![[Pasted image 20240601144419.png]]

How many junk independent variables or important independent variable or impactful independent variable you add to your model, the R-Squared value will always increase. It will never decrease with the addition of a newly independent variable, whether it could be an impactful, non-impactful, or bad variable, so we need another way to measure equivalent R2, which penalizes our model with any junk independent variable.

So, we calculate the Adjusted R-Square with a better adjustment in the formula of generic R-square.
![[Pasted image 20240601144635.png]]

mean squared error (MSE)
mse = sum(yhat-yi)^2/(2*m)


gradient descent helps in finding minima of cost function. we take baby step in direction of steepest descend and continue the iterative process. Initially we need to start at some point. we start with all parameter value to be 0. For cost function not like bell curve if we choose different start value we may get different local minima.


alpha is learning rate in range [0,1]


batch gradient descent - using / feeding all the data to algorithm for training.

![[Pasted image 20240601211053.png]]

![[Pasted image 20240601212907.png]]

![[Pasted image 20240601213026.png]]

![[Pasted image 20240601213136.png]]

![[Pasted image 20240601213235.png]]

feature scaling helps gradient descent to run faster or converge quickly

![[Pasted image 20240601213924.png]]


normal mse cost function won't work for logistic regression
hence using different cost function
![[Pasted image 20240602104059.png]]

partial differential for cost function of logistic regression. it is same as linear regression
![[Pasted image 20240602104440.png]]

overfitting
get more training data
select less features
regularization

![[Pasted image 20240602114028.png]]

multi class classification (one vs all)
let say i have 3 classes i train 3 classifiers behind the scene. then for a new point i get prediction from all 3 classifier whichever gives the highest prediction we assign it to that class


forward propagation
architecture

![[Pasted image 20240602143856.png]]
optimizer backpropogation


![[Pasted image 20240602173646.png]]
![[Pasted image 20240602173809.png]]
![[Pasted image 20240602173849.png]]

![[Pasted image 20240602174005.png]]
![[Pasted image 20240602174313.png]]

![[Pasted image 20240602181016.png]]

derivative of sigmod range from 0 to 0.25
now each value of 0.25 gets multiplied like in above pic,  which is very small value


![[Pasted image 20240602182921.png]]

in hidden layer use relu, prerelu 
and in output layer for classification sigmoid or softmax 

![[Pasted image 20240602183033.png]]

in regression in output layer use linear activation function


in sigmoid we had trouble of vanishing gradient
then in tanh also same vanishing gradient issue
relu solved the issue but for negative values differential is 0 so updated weight is equal to new weight


see activation.zip file for reference.


in forward propagation instead of passing records one by one you'll tell i'll pass some batch i.e., no or rows loss will be calculated for that. Cost function is nothing but summation of all losses

for regression (loss/cost function)
mse
mae
huber loss (mixture of mse and mae)


for classification (loss/cost function)
cross entropy -> binary cross entropy (for binary classification) and categorical cross entropy (for multi class classification)
![[Pasted image 20240602191000.png]]

![[Pasted image 20240602192205.png]]
![[Pasted image 20240602192319.png]]
![[Pasted image 20240602192254.png]]

clustering
customer segmentation


r2 can be negative also if numerator is greater than denominator

assumption in linear regression
data is normal distributed
linearity
multi collinearity


in logistic regression we can't use the same cost function as linear regression.

because the hypothesis h = 1+(1+e-z)   z = theta0 + theta1*x
this hypothesis is a non convex function
so gradient descent will be stuck in a local minima

![[Pasted image 20240603121619.png]]


Naive bayes

![[Pasted image 20240603135841.png]]

![[Pasted image 20240603135908.png]]

![[Pasted image 20240603135922.png]]

![[Pasted image 20240603140247.png]]

knn
words bad
if outliers or imbalanced dataset

decision tree
![[Pasted image 20240603141157.png]]

![[Pasted image 20240603141553.png]]

pure split: all yes or all no (everything belong to one category)   no need to split more
![[Pasted image 20240603141723.png]]
if the node is impure we'll split it based on other columns or features until we get a pure split

![[Pasted image 20240603142011.png]]

entropy is randomness so 0 entropy means pure split
![[Pasted image 20240603142505.png]]
entropy is between 0 and 1. max value 1 happens at 0.5 and 0 happens at 0 and 1

![[Pasted image 20240603142436.png]]

![[Pasted image 20240603142912.png]]

![[Pasted image 20240603143026.png]]

![[Pasted image 20240603143132.png]]
![[Pasted image 20240603143218.png]]

![[Pasted image 20240603143446.png]]

![[Pasted image 20240603143456.png]]

pruning

hyperparameter: max_depth, max_leaf nodes


ensemble technique :- using multiple ml algorithms

bagging we have data we create multiple models we select some samples from data and give these sample to mode 1 again choose sample from data give to model 2 and so on . it may happen data give to model 1 has some intersection rows with data given to any other model
![[Pasted image 20240603150153.png]]

in bagging we have all models in parallel while in boosting we have models in sequential order one after another
![[Pasted image 20240603150556.png]]
![[Pasted image 20240603150728.png]]

in random forest row sampling and feature sampling is done
![[Pasted image 20240603151043.png]]

interview question 
is normalization required in decision tree or random forest
No
is normalization required in KNN
yes because we use distance based 

is random forest prone to outliers
no -> since we are dividing the space into smaller subspace so these outliers get squeezed into some leaf and also we are using random sampling and feature selection we reduces the impact of outliers

is knn impacted by outliers
yes



ADA BOOST
first we assign weight equal weights that is 1/no. of rows

then we create a decision tree like thing, which feature to choose we can use information gain here. we will only 1 depth since it has only one depth we call it stumps

![[Pasted image 20240603153244.png]]

no you give all records to f1 to classify. the records which get wrong prediction. you try to increase the weight so the go to next week learner conversly the record which get correct prediction you decrease their weight


k means clustering
![[Pasted image 20240603160500.png]]

![[Pasted image 20240603160822.png]]

which takes more time hierarchial or kmeans?
hierarchial clustering because we need to create the dendo gram and if we have lots of data it becomes computally expensive


validate clustering models using silhouete score
-1 to 1  more value is towards +1 the good the model is. -1 towards score means bad model.


dbscan clustering 

if you want to skip the cluster you can use this 

![[Pasted image 20240603161941.png]]
if a center of circle has >= min point inside then it is core else border point.
Noise point is no point in side circle then it will be treated as outliers

use dbscan as it is superior
https://www.youtube.com/@DataTrained/videos


gradient descent (GD)
pass all records in forward propagation.

1 forward and 1 backward pass is 1 epoch
issue with GD need huge memory to load miiliions of records

SGD stochastic gradiet descent
pass single single records in forward propagation
![[Pasted image 20240603173050.png]]


mini batch sgd
![[Pasted image 20240603173246.png]]

Adagrad (learning rate keep on changing)

rmsprop (only smoothing)

adam (learning rate change + smoothening)
