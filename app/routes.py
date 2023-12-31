# routes for the flask app

from app import app
from app.forms import ContactForm
from flask import render_template


# index or home route
@app.route('/')
def index():
    return render_template('index.html')

# contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # creating a form instance to be used
    form = ContactForm()

    # this will check that the form was submitted succesfully
    # when validation checks are run against the input
    if form.validate_on_submit:
        # prints out the data dict from form class
        print(form.data)
    return render_template('contact.html', form=form)