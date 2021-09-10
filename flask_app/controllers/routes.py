from flask import render_template, redirect, request, flash
from flask_app import app
from flask_app.models.email import Email

@app.route('/')
def index():
    return redirect('/emails')

@app.route('/emails')
def home():
    return render_template("index.html")

@app.route('/email/save', methods=["POST"])
def save_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.save(request.form)
    print(f"Saved {request.form}")
    flash(f"Your email addres({request.form['email']}) is valid! Thankyou.")
    return redirect('/emails/success')

@app.route('/email/delete/<int:email_id>')
def delete(email_id):
    data = {
        'id': email_id,
    }
    Email.delete(data)
    return redirect('/emails/success')

@app.route('/emails/success')
def validation_success():
    return render_template("success.html", emails = Email.get_all())