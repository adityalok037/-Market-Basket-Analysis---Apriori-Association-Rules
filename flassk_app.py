from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pickle files
with open('model pkl files/best_associations.pkl', 'rb') as f:
    best_df = pickle.load(f)

with open('model pkl files/medium_associations.pkl', 'rb') as f:
    medium_df = pickle.load(f)

with open('model pkl files/low_associations.pkl', 'rb') as f:
    low_df = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    product = request.form['product']
    
    # Filter the DataFrames based on the product
    best_results = best_df[best_df['Antecedents'].str.contains(product, case=False)]
    medium_results = medium_df[medium_df['Antecedents'].str.contains(product, case=False)]
    low_results = low_df[low_df['Antecedents'].str.contains(product, case=False)]
    
    return render_template('results.html', product=product, best_results=best_results, medium_results=medium_results, low_results=low_results)

if __name__ == '__main__':
    app.run(debug=True)  