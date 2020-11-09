from flask import Flask, render_template, url_for, flash, redirect, Response
from forms import UserInputForm
import os
import useAPI
import clean_transactions
from url_builder import build_url

import io
from matplot import plot_histogram
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from transactions import Transactions

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


# Need to declare this out here?
transactions = Transactions()


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
    display = False
    if form.validate_on_submit():
        transactions.update_transactions(form)
        display = True
    return render_template('home.html', transactions=transactions, display=display, form=form)

@app.route('/fig')
def fig():
    fig = transactions.fig
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
    app.run(debug=False)
