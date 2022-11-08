from application import db
from application.auth.forms import RegistrationForm, LoginForm, ResendConfirmationMailForm
from application.auth.models import Retailer
from application.auth.constants import *
from lib.response import Response
from lib.response_status_codes import *
from lib.mailer import send_confirmation_email
from datetime import datetime
from flask_jwt_extended import create_access_token

def register():
    form = RegistrationForm()
    if form.validate():
        retailer_data = {}
        retailer_data['name'] = form.name.data
        retailer_data['email'] = form.email.data
        retailer_data['address'] = form.address.data
        retailer_data['is_active'] = False
        retailer = Retailer(**retailer_data)
        retailer.set_password(form.password.data)
        db.session.add(retailer)
        db.session.commit()
        send_confirmation_email(retailer)
        return Response.success(data=retailer.id)

    return Response.error(data=form.errors, error_code=500)


def login():
    form = LoginForm()
    if form.validate():
        retailer = Retailer.query.filter_by(email=form.email.data).first()
        if retailer is None or (not retailer.check_password(form.password.data)):
            return Response.error(data={}, message=INVALID_DATA, status_code=UNAUTHORIZED_ACCESS)

        access_token = create_access_token(retailer.id)
        response_data = {
            'jwt_token': access_token
        }
        return Response.success(data=response_data, message=LOGIN_SUCCESSFUL, status_code=REQUEST_COMPLETED)

    return Response.error(data=form.errors, message=INVALID_DATA, status_code=UNAUTHORIZED_ACCESS)


def confirm_email(token):
    email = Retailer.verify_confirmation_token(token)
    if email:
        retailer = Retailer.query.filter_by(email=email).first()
        retailer.is_active = True
        retailer.email_confirmed_at = datetime.now()
        db.session.add(retailer)
        db.session.commit()
        return Response.success(data='Account confirmed Successfully. Now you can login!')

    return Response.error(data='Token Invalid. Please get another confirmation link!', error_code=500)


def resend_confirmation_email():
    form = ResendConfirmationMailForm()
    if form.validate():
        retailer = Retailer.query.filter_by(email=form.email.data).first()

        if not retailer:
            return Response.error(data='Account Not Found!', error_code=500)

        if retailer.is_eligible_for_resend():
            send_confirmation_email(retailer)
            retailer.confirmation_email_sent_at = datetime.now()
            return Response.success(data='Confirmation Mail Sent Successfully!')
        else:
            return Response.error(data='Please wait for few minutes and try again...!', error_code=500)

    return Response.error(data='Invalid Email Input', error_code=500)
