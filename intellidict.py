import json
from difflib import get_close_matches as gcm
data= json.load(open("C:\\Users\\Hp\\Desktop\\076 data.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(gcm(w,data.keys()))>0:
        yn = input("Did you mean  %s instead? Enter Y if yes or N if No: " % gcm(w,data.keys())[0])
        if(yn.lower()=='y'):
            return data[gcm(w,data.keys())[0]]
        else:
         return "The word doesnt exist. Please Double check it"   
    else:
        return "The word doesnt exist. Please Double check it"
word=input("Enter word: ")
output=(translate(word))
if type(output)=='list':
    for item in output:
        print(item)
else:
    print(output)
