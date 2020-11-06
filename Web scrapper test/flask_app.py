from flask import Flask, render_template, url_for, flash, redirect
from forms import UserInputForm
# from flask_sqlalchemy import SQLAlchemy
import os
import useAPI

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)

# class UserInput(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     threshold_value = db.Column(db.Integer(20), nullable=False)
#     time_ago = db.Column(db.Integer(20), nullable=False)

#     def __repr__(self):
#         return f"User('{self.threshold_value}', '{self.time_ago}')"



transactions = []
# # sample data
#     {
#         'hash': 'dummy hash',
#         'from': 'from 1',
#         'to': 'to 1',
#         'value' : '100',
#     },
#     {
#         'hash': 'dummy hash 2',
#         'from': 'from 2',
#         'to': 'to 2',
#         'value': '200',
#     }
# ]


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UserInputForm()
    if form.validate_on_submit():
        threshold_value = form.threshold_value.data
        time_ago = form.time_ago.data
        start_block = useAPI.get_start_block(time_ago, 0) # haven't incoperated mins yet
        df = useAPI.get_transfer_events(start_block, threshold_value)
        # transactions = df.to_dict('records')
        transactions.clear()
        transactions.extend(df.to_dict('records'))
        # print(transactions)
    return render_template('home.html', transactions=transactions, form=form)

@app.route('/about')
def about():
    return '<h1> About </h1>'


if __name__ == '__main__':
    app.run(debug=True)
