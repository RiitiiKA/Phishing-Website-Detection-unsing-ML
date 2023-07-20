#importing libraries import joblib
import Inputscript #load the pickle
file classifier =
joblib.load('rf_final.pkl')
#input url print("Welcome to the phishing website detection
software ! \n\n") print("Enter url:\n") url = input()
# checking and predicting checkprediction =
Inputscript.main(url) prediction =
classifier.predict(checkprediction)
print(prediction) if(prediction == 1):
print("The site is a phishing site") else:
print("The site is not a phishing site")