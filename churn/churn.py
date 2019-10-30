# Imports
import re
import pickle
import numpy as np
from xgboost import XGBClassifier
from flask import Flask, render_template, request, url_for


app = Flask(__name__) #creating the Flask class object
if not hasattr(app, 'extensions'):
    app.extensions = {}
with open('xgboost.pkl', 'rb') as f:
    app.extensions['xg'] = pickle.load(f)

@app.route('/') #decorator drfines the
def index():
    return render_template('index.html')

@app.route('/query', methods = ['POST'])
def query():
    from transform_data import transform_data
    query = transform_data(request.form['query'])
    input_values = np.array(list(query.values())).reshape(1, -1)
    prediction = app.extensions['xg'].predict(input_values)
    prob = app.extensions['xg'].predict_proba(input_values)
    return render_template('query.html', prediction=prediction[0],
                            stay=round(prob[0, 0],3), leave=round(prob[0, 1],3))

# @app.route('/search', methods = ['POST'])
# def search():
#     def clean_input(value):
#         """Cleans out any non-word characters and adds percent signs
#         for searcing."""
#         return '%' + re.sub(r'(\W|[0-9])', '', value) + '%'
#
#     def get_terms(search_term):
#         """Splits a search term and retuns the first term surrounded by
#         percent signs. The result is to be used in an SQL query."""
#         term = search_term.split(' ')[0]
#         clean_term = clean_input(term)
#         return tuple([clean_term])
#
#     def query_name(cur, search_terms):
#         """Returns the results of a name query."""
#         full_name = get_terms(search_terms)
#
#         results = cur.execute("""SELECT first_name, last_name, churn as at_risk
#                                  FROM customers
#                                  WHERE first_name like ?""",
#                                  full_name)
#         names = list(map(lambda x: x[0], cur.description))
#         return (names, list(results))
#
#     con = con = sqlite3.connect("/Users/scott/test/flask/churn/customer.db")
#     cur = con.cursor()
#     search_string = request.form['search']
#     results = query_name(cur, search_string)
#     return render_template('search.html', search_string=results)

@app.route('/upload', methods = ['POST'])
def upload():
   return render_template('upload.html')

@app.route('/history')
def history():
   return render_template('history.html')

def about():
    return "This is about page"

def clean_input(input):
    pass

app.add_url_rule("/about","about",about)

if __name__ =='__main__':
    app.run(debug = False)
