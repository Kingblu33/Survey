from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models.usersModel import User
from flask_mail import Mail, Message

# app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# mail = Mail(app)


@ app.route('/2rt/<int:Customer_id>/<int:rating>')
def results(Customer_id, rating):
    id = Customer_id
    rat = rating
    data = {
        'idfeeback': id,
        'Rating': rat,
    }
    User.updateFeedback(data)
    return render_template("submit.html", id=id)


@ app.route("/", methods=['GET', 'POST'])
def default():
    # Calls method to get all users from the database where email hasn't been sent
    users = User.getUsers()
    if request.method == 'POST':
        count = 0
        for user in users:

            app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
            app.config['MAIL_PORT'] = user['MailPort']
            app.config['MAIL_USERNAME'] = user['MailUser']
            app.config['MAIL_PASSWORD'] = user['MailPass']
            if user['MailTsl'] == 1:
                app.config['MAIL_USE_TLS'] = True
            else:
                app.config['MAIL_USE_TLS'] = False
        # ********************************************************************
            if user['MailSsl'] == 1:
                app.config['MAIL_USE_SSL'] = True
            else:
                app.config['MAIL_USE_SSL'] = False
            mail = Mail(app)
            count += 1
            msg = Message("Customer Satisfactory Survery",
                          sender=user['MailUser'], recipients=[user['CustEmail']])
            msg.html = render_template(
                'mail.html', user=user)
            mail.send(msg)
            data = {
                'idfeeback': user['idfeeback']
            }
            User.updateEmailSent(data)
        return render_template("submit.html")
    return render_template("testDb.html", users=users)
