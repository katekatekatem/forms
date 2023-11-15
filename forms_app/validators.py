import datetime
import re


def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False


def validate_phone(phone_str):
    phone_regex = r'\+7 \d{3} \d{3} \d{2} \d{2}'
    return bool(re.fullmatch(phone_regex, phone_str))


def validate_email(email_str):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.fullmatch(email_regex, email_str))
