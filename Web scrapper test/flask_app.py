from flask import Flask, render_template, url_for, flash, redirect, Response
from forms import UserInputForm
# from flask_sqlalchemy import SQLAlchemy
import os
import useAPI
import clean_transactions

import io
from matplot import plot_histogram
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

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
full_transactions = []
fig = ''
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
def update_transactions(form):
    threshold_value = form.threshold_value.data
    time_ago = form.time_ago.data
    start_block = useAPI.get_start_block(
        time_ago, 0)  # haven't incoperated mins yet
    df = useAPI.get_transfer_events(start_block, threshold_value)
    # update transactions 
    display_df = clean_transactions.display_df(df)
    transactions.clear()
    transactions.extend(display_df.to_dict('records'))
    # return matplot
    global fig
    fig = plot_histogram(df)
    # return fig


BASE_URL = "https://etherscan.io/"
CONTRACT = "0xaf9f549774ecedbd0966c52f250acc548d3f36e5"
req_address = "?a="

def build_url(data, col):
    if col == 'hash':
        return BASE_URL + 'tx/' + data
    else: 
        return BASE_URL + 'token/' + CONTRACT + req_address + data

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UserInputForm()
    fig_exist = False
    if form.validate_on_submit():
        update_transactions(form)
        fig_exist = True
    return render_template('home.html', transactions=transactions, fig_exist=fig_exist, form=form)

@app.route('/fig')
def fig():
    # fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

# Do I need to go outside_flask/ thing?
@app.route('/go_to_etherscan/<col>/<data>')
def go_to_etherscan(data, col): 
    url = build_url(data, col)
    return redirect(url, code=302)
    

@app.route('/about')
def about():
    return '<h1> About </h1>'


if __name__ == '__main__':
    app.run(debug=True)
