import warnings
warnings.simplefilter("ignore", FutureWarning)
from CSVAPI import CSVOperations
from MLtraining import MLOperations
from LLMAssistant import LLMAssistant



def predict_scam(message, CSV, ML):
    cleaned = CSV.clean_text(message)
    vec = ML.vectorizer.transform([cleaned])
    prob = ML.model.predict_proba(vec)[0][1]
    #prediction = ML.model.predict(vec)[0]
    if prob > 0.7:
        return "Scam"
    elif prob < 0.3:
        return "Not Scam"
    else:
        return "Uncertain"

def run():
    #CSV file operations
    filename = 'scamdata.csv'
    CSV = CSVOperations(filename)
    CSV.read_csv()
    CSV.clean_csv()
    #CSV.display_csv_contents()

    #ML training and prediction
    ML = MLOperations(CSV)
    ML.MLTraining()
    ML.MLPredict()

    LLM = LLMAssistant()


    print ("I am an AI SCAM assitant who classifies messages as Scam 🚨 or Not Scam ✅")
    print ("Type quit to exit")
    while True:
        user_query = input ("Enter your message : ")
        if user_query.lower() == "quit":
            print ("Bye Bye")
            break
        if user_query:
            response = predict_scam(user_query, CSV, ML)
            if response in ("Scam", "Uncertain"):
                message = LLM.send_message(user_query)
                print (f"spam or not spam : {message.final_label}")
                print (f"message intent : {message.intent}")
                print (f"reason : {message.reason}")
            else:
                print ("Not Scam ✅")

        
if __name__ == '__main__':
    run()