import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Data: CIBIL Score vs Loan Amount
data = {
    'cibil_score': [580, 620, 650, 680, 700, 720, 750, 780, 800, 580, 600, 750, 820, 690, 710],
    'loan_amount': [2, 3, 2.5, 5, 4, 6, 7, 8, 9, 1, 2, 5.5, 10, 4.5, 6.5],
    'eligible': [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

X = df[['cibil_score', 'loan_amount']]
y = df['eligible']

model = LogisticRegression()
model.fit(X, y)

print(f"Accuracy: {model.score(X,y)}")

# Graph - x=CIBIL, y=Loan Amount
colors = ['red' if e==0 else 'green' for e in df['eligible']]
plt.scatter(df['cibil_score'], df['loan_amount'], c=colors, s=100, edgecolors='black')
plt.xlabel('CIBIL Score (x-axis)')
plt.ylabel('Loan Amount (y-axis)')
plt.title('Loan Eligibility - Logistic Regression')
plt.savefig('loan_graph.png')
plt.show()