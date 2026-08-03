"""
Entrenamiento de modelo base para clasificar facturas P2P.
Este script genera model.pkl a partir de datos de ejemplo.
"""
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

DATA = [
    ('Purchase order for office supplies', 'PO Invoice'),
    ('PO invoice for raw materials', 'PO Invoice'),
    ('Supplier invoice related to purchase order', 'PO Invoice'),
    ('Invoice with purchase order number', 'PO Invoice'),
    ('Hotel reimbursement', 'Non PO Invoice'),
    ('Travel expense reimbursement', 'Non PO Invoice'),
    ('Utility bill without purchase order', 'Non PO Invoice'),
    ('Consulting expense without PO', 'Non PO Invoice'),
    ('Credit note from supplier', 'Credit Memo'),
    ('Supplier credit memo for returned goods', 'Credit Memo'),
    ('Credit adjustment for invoice correction', 'Credit Memo'),
    ('Refund note issued by vendor', 'Credit Memo')
]

def main():
    df = pd.DataFrame(DATA, columns=['text', 'label'])
    X_train, X_test, y_train, y_test = train_test_split(
        df['text'], df['label'], test_size=0.25, random_state=42, stratify=df['label']
    )
    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('classifier', LogisticRegression(max_iter=1000))
    ])
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))
    joblib.dump(model, 'model/model.pkl')
    df.to_csv('model/train.csv', index=False)
    print('Modelo guardado en model/model.pkl')

if __name__ == '__main__':
    main()
