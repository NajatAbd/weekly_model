import pandas as pd
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_error, r2_score
import json
#import seaborn as sns





def weekly_model():
    df = pd.read_csv('/Users/najat/Downloads/Amal_Daily_typs/V.csv')
      
    
    y=df['ICD10countCurrent']
    x=df[['0-19','100+','20-39','40-59','60-79','80-99','F','M','ICD10LastDay']]
     
    
    
    
    X_train, X_test, y_train, y_test =train_test_split(x, y, test_size=0.2,random_state=7)
        
        
     
    lm = linear_model.LinearRegression()
    
    lm.fit(X_train, y_train)
    predictions = lm.predict(X_test)
    scores = cross_val_score(lm, X_test, y_test, scoring='r2')
        
       
     
     
     
        # plot
    '''sns.regplot(x=y_test, y=predictions, line_kws={"color":"r","alpha":0.7,"lw":5})
    plt.title("ICD10 CODE: "+f[:-4])
    plt.xlabel("True Values")
    plt.ylabel("Predictions")   
    plt.show()
    '''
    
    print (" model Score:"+ str(r2_score(y_test, predictions)*100))
    print (" Model sqr err "+ str(mean_squared_error(y_test,predictions)))
    data = {"model_score": r2_score(y_test, predictions)*100,
            "model_squarerror": mean_squared_error(y_test,predictions)
            }
    
    with open('output_data/result.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
    return " model Score:"+ str(r2_score(y_test, predictions)*100)+"\n Model sqr err "+ str(mean_squared_error(y_test,predictions))
       




