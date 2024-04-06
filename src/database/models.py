import peewee

database = peewee.SqliteDatabase('src/database/database.db')


class BaseModel(peewee.Model):
    class Meta:
        database = database


class UserLogin(BaseModel):
    login = peewee.CharField()
    password = peewee.CharField()


class Patient(BaseModel):
    fullname = peewee.CharField()
    passport = peewee.IntegerField()
    birth_date = peewee.DateField()
    gender = peewee.CharField()
    address = peewee.CharField()
    phone_number = peewee.IntegerField()
    email = peewee.CharField()
    last_visit_date = peewee.DateTimeField()
    polis_id = peewee.IntegerField()


class MedicalPolis(BaseModel):
    patient_id = peewee.ForeignKeyField(Patient, related_name='patient_polis_id')
    polis_id = peewee.IntegerField()
    polis_end_date = peewee.DateField()


class MedicalCard(BaseModel):
    patient_id = peewee.ForeignKeyField(Patient, related_name='patient_medical_card_id')
    card_id = peewee.IntegerField()
    created_date = peewee.DateField()


class Staff(BaseModel):
    login_id = peewee.ForeignKeyField(UserLogin, related_name='staff_user_id')
    fullname = peewee.CharField()


class Services(BaseModel):
    patient_id = peewee.ForeignKeyField(Patient, related_name='patient_services_id')
    date = peewee.DateField()
    doctor = peewee.ForeignKeyField(Staff, related_name='doctor_services_id')
    typeof = peewee.CharField()
    name = peewee.CharField()
    result = peewee.TextField()


database.create_tables([
    UserLogin,
    Patient,
    MedicalPolis,
    MedicalCard,
    Staff,
    Services
])
