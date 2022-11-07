from application import db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from flask import current_app
from datetime import datetime


class Retailer(db.Model):
    __tablename__ = 'retailers'
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    address = db.Column(db.String(300), nullable=True)
    password_hash = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean, nullable=True)
    email_confirmed_at = db.Column(db.DateTime, nullable=True, default=None)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    confirmation_email_sent_at = db.Column(
        db.DateTime, nullable=True, default=datetime.now)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_confirmation_token(self):
        secret_key = current_app.config['SECRET_KEY']
        salt = current_app.config['EMAIL_CONFIRMATION_SALT']
        serializer = URLSafeTimedSerializer(secret_key)
        return serializer.dumps(self.email, salt=salt)

    def is_eligible_for_resend(self):
        allowed_time_difference_in_seconds = current_app.config[
            'EMAIL_CONFIRMATION_TOKEN_MAX_AGE_SECONDS']
        current_time = datetime.now()
        time_difference = current_time - self.confirmation_email_sent_at
        time_difference_in_seconds = time_difference.total_seconds()
        if time_difference_in_seconds > allowed_time_difference_in_seconds:
            return True
        return False

    @staticmethod
    def verify_confirmation_token(token):
        try:
            secret_key = current_app.config['SECRET_KEY']
            salt = current_app.config['EMAIL_CONFIRMATION_SALT']
            max_age = current_app.config['EMAIL_CONFIRMATION_TOKEN_MAX_AGE_SECONDS']
            serializer = URLSafeTimedSerializer(secret_key)
            email = serializer.loads(token, salt=salt, max_age=max_age)
        except:
            return False
        return email
