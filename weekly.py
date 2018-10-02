import json
import pandas as pd

#import seaborn as sns





def weekly_model():
    
    print("HEY!!")
    data = [{'name': 'vikash', 'age': 27}, {'name': 'Satyam', 'age': 14}]
    df = pd.DataFrame.from_dict(data, orient='columns')
    df.to_csv('models_folder/47/result.csv', sep='\t')
    '''
    data = {"model_score": 100,
            "model_squarerror": 10}        
    with open('models_folder/47/result.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
    '''        
    print("WRONG!")
       
weekly_model()



