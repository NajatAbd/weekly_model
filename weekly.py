import json
#import seaborn as sns





def weekly_model():
    
    print("HEY!!")
    
    data = {"model_score": 100,
            "model_squarerror": 10}        
    
    with open('result.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
            
    print("WRONG!")
       
weekly_model()



