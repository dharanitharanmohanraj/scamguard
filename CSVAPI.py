import pandas as pd
import re

class CSVOperations:
    def __init__(self, filename=None):
        self.filename = filename
        self.df = None
    
    def read_csv(self):
        try:
            self.df = pd.read_csv(self.filename)
            #print("CSV read successfully")
        except Exception as e:
            print(f"{self.filename} read unsuccessful: {e}")
    
    def display_csv_contents(self):
        if self.df is not None:
            print(f"\nContents of {self.filename}:")
            print(self.df.head(10))
        else:
            print("No data to display")
    
    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text
    
    def clean_csv(self):
        try:
            self.df['label'] = self.df['label'].map({'Scam': 1, 'Not Scam': 0})
            self.df['clean_text'] = self.df['message_text'].apply(self.clean_text)
            #print("CSV cleaned successfully")
        except Exception as e:
            print(f"Clean unsuccessful: {e}")
