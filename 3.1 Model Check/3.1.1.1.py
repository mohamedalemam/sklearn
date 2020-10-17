#Import Libraries
from sklearn.model_selection import cross_validate
#----------------------------------------------------

#Applying Cross Validate :  
'''
model_selection.cross_validate(estimator, X, y=None, groups=None, scoring=None, cv=’warn’, n_jobs=None,
                               verbose=0,fit_params=None, pre_dispatch=‘2*n_jobs’, return_train_score=’warn’,
                               return_estimator=False,error_score=’raise-deprecating’)
'''

#  don't forget to define the model first !!!
CrossValidateValues1 = cross_validate(SelectedModel,X,y,cv=3,return_train_score = True)
CrossValidateValues2 = cross_validate(SelectedModel,X,y,cv=3,scoring=('r2','neg_mean_squared_error'))

# Showing Results
print('Train Score Value : ', CrossValidateValues1['train_score'])
print('Test Score Value : ', CrossValidateValues1['test_score'])
print('Fit Time : ', CrossValidateValues1['fit_time'])
print('Score Time : ', CrossValidateValues1['score_time'])
print('Train MSE Value : ', CrossValidateValues2['train_neg_mean_squared_error'])
print('Test MSE Value : ', CrossValidateValues2['test_neg_mean_squared_error'])
print('Train R2 Value : ', CrossValidateValues2['train_r2'])
print('Test R2 Value : ', CrossValidateValues2['test_r2'])