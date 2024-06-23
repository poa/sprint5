from faker import Faker


def gen_name():
    fake = Faker(["ru_RU"])
    name = fake.name()
    return name


def gen_email():
    fake = Faker(["ru_RU"])
    email = fake.email()
    return email


def gen_passwd():
    fake = Faker()
    passwd = fake.password(length=8, special_chars=False)
    return passwd
