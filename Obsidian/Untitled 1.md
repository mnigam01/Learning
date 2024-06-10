
machine learning allows machines the capability to learn or do task without explicitly programming those.

machines learn from past data, machines adapt to new trends in data

supervised:
- classification
- regression
unsupervised:
- clustering
- dimensionality reduction
- recommendation
- generative models  models captures probability distribution of input data then can generate data
reinforcement 

problem understanding
data collection
data preprocessing
choosing model
training the model  (algorithm iteratively adjust parameters to minimize predicted vs actual result)
evaluating the model
fine tuning 
inference
deployment
monitoring


numerical vs categorical data vs ordinal data

data preprocessing: clean, transform and prepare data in a suitable format to be indigested by machine learning model.


dealing with outliers remove those use standard deviation, or replace those with mean or median
data normalization :- minmaxscaler, StandardScaler


remove duplicate rows, cols, 
to detect outliers we can create box plots, iqr, q1-1.5*igr q3+1.5*igr


![[Pasted image 20240601111223.png]]



unsupervised learning find some pattern in the data 

segment customers

anomaly detection
detect outliers or unusual data points
dimensionality reduction - compressing data without losing much information

![[Pasted image 20240601114826.png]]

data analyst: work on data cleaning, visualization and data reporting (findings) to non-business people
data scientist: works on above but also model building, focus on researching new algorithms as well. Work on different domain like maths, statistics, probability, etc.
ml engineer:- same work as data scientist but less focus on research.


AI: development of systems which can perform task that typically require human intelligence. 
Ml: subset of AI, involves developing algorithms that allow system to perform task based on data without being explicitly programmed.
Dl: subset of Ml, involves neural network for learning complex pattern from data. 



l1 regularization or lasso
![[Pasted image 20240601143337.png]]
![[Pasted image 20240601143434.png]]
l1 regularization helps in feature selection and controlling over fitting.


l2 regularization (ridge)
To avoid overfitting your model on training data like cross-validation sampling, reducing the number of features, pruning, regularization, etc.
![[Pasted image 20240601143551.png]]
The regularization parameter (lambda) penalizes all the parameters except intercept. Ridge regression adds “squared magnitude of the coefficient" as penalty term to the loss function.

lambda is a hyperparameter
lambda = 0 same model
lambda very large too much penalty thus now model may underfit
