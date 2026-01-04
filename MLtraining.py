from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

class MLOperations:
    def __init__(self, csv_ops):
        self.csv_ops = csv_ops
        self.df = csv_ops.df

        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()
    
    def MLTraining(self):
        X = self.df['clean_text']   # messages
        y = self.df['label']        # scam or not
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
            )
        self.X_train_vec = self.vectorizer.fit_transform(self.X_train)
        self.X_test_vec = self.vectorizer.transform(self.X_test)
        self.model.fit(self.X_train_vec, self.y_train)

    def MLPredict(self):
        y_pred = self.model.predict(self.X_test_vec)
        accuracy = accuracy_score(self.y_test, y_pred)
        #print("Accuracy:", accuracy)

