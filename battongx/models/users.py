# -*- coding:utf8 -*-
# pylint: disable=E1101
import base64
import hashlib
import re
import datetime

from Crypto.Cipher import AES
from battongx import db

class Users(db.Model):
    """사용자 정보 테이블"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Stgring(32), nullable=False, unique=Tre)
    password = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    email = db.Column(db.String(320), nullable=False)
    provider = db.Column(db.String(32))
    provider_uid = db.Column(db.String(32))

    # expire_date = db.Column(db.Date, nullable=False, default='1970-01-01')
    balance = db.Column(db.Integer, nullable=False, default=0)  # user의 현재 잔고

    latitude = db.Column(db.Numeric(15, 10), nullable=False, default=0)
    longitude = db.Column(db.Numeric(15, 10), nullable=False, default=0)
    
    user_type = db.Column(db.Enum('RUNNER','EMPLOYER'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    profile_image = db.Column(db.String(320), nullable=True)
    retired_at = db.Column(db.DateTime)

    @property
    def password(self):
        raise AttributeError('`password` is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password = self.generate_password_hash(password)


    @staticmethod
    def generate_password_hash(password):
        pre_hashed = hashlib.sha512(('x3FpknhFyR' + password + 'a6E8kInyyW')
                                    .encode('utf8')).hexdigest()
        return hashlib.md5(pre_hashed.encode('utf8')).hexdigest()

    @staticmethod
    def check_password_hash(password_hashed, password):
        return password_hashed == Users.generate_password_hash(password)

    @staticmethod
    def verify_phone_number(phone_number):
        phone_pattern = re.compile(r'^[\d]{3}-[\d]{3,4}-[\d]{4}$')
        return phone_pattern.match(phone_number)

    @staticmethod
    def verify_email(email):
        email_pattern = re.compile(
            r'^[A-Z0-9a-z._%+-]{1,64}@[A-Za-z0-9.-]{2,}\.[A-Za-z0-9.-]{2,}$')
        return email_pattern.match(email)

    @staticmethod
    def verify_name(name):
        name_pattern = re.compile(r'^[가-힣]{2,5}$')
        return name_pattern.match(name)

    # def encrypt(self, key, billing_account):
    #     key = hashlib.sha256(key.encode()).digest()
    #     BS = 16
    #     pad = (lambda s: s + (BS - len(s) % BS)
    #            * chr(BS - len(s) % BS).encode())
    #     message = billing_account.encode()
    #     raw = pad(message)
    #     cipher = AES.new(key, AES.MODE_CBC, self.__iv().encode('utf-8'))
    #     enc = cipher.encrypt(raw)
    #     return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, key, enc):
        key = hashlib.sha256(key.encode()).digest()
        unpad = (lambda s: s[:-ord(s[len(s)-1:])])
        enc = base64.b64decode(enc)
        cipher = AES.new(key, AES.MODE_CBC, self.__iv().encode('utf-8'))
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')

    def __iv(self):
        return chr(0) * 16

    def get_user_object(self):
        user = {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'provider': self.provider if self.provider else None,
            'provider_uid': self.provider_uid if self.provider_uid else None,
            'balance': self.balance,
            'user_type': self.user_type,
            'latitude': float(self.latitude) if self.latitude else None,
            'longitude': float(self.longitude) if self.longitude else None,
            'profile_image': 'https://...../{}'.format(self.profile_image) if self.profile_image else None,
            'retired_at': str(self.retired_at),
            'created_at': str(self.created_at)
        }