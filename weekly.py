import json
#import seaborn as sns





def weekly_model():
    
    print("HEY!!")
    
    data = {"model_score": 100,
            "model_squarerror": 10}        
    try:
        with open('result.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
    except:
        print("WRONG!")
       
weekly_model()



