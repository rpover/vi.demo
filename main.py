import flet
import flet as ft
from src.database.models import *
from src.client.auth_component import AuthComponent


def main(page: ft.Page):
    doctor_id = 0

    def on_login_click(event: flet.ControlEvent):
        global doctor_id
        user = UserLogin.get_or_none(
            UserLogin.login == auth_component.login_field.value, UserLogin.password == auth_component.password_field.value
        )

        if user:
            doctor_id = user.id
            auth_component.visible = False
            patient_data_component.visible = True
            page.update()

        else:
            print('Неверные данные')

    def show_client_data(event: flet.ControlEvent):
        data = Patient.get(Patient.fullname == patient_data_component.controls[0].value)
        alert_dialog = flet.AlertDialog(content=flet.Text(data.__dict__.values()))
        page.dialog = alert_dialog
        alert_dialog.open=True
        page.update()

    def show_records(event: flet.ControlEvent):
        global doctor_id
        if doctor_id == 0: return

        data = Patient.get(Patient.fullname == patient_data_component.controls[0].value)
        doctor = Staff.get_by_id(doctor_id)
        record = Services.select().where(Services.doctor == doctor, Services.patient_id == data)
        d = []
        for s in record:
            d.append(s.__dict__)

        alert_dialog = flet.AlertDialog(content=flet.Text(str(d)))
        page.dialog = alert_dialog
        alert_dialog.open = True
        page.update()

    page.window_width = 800
    page.window_height = 600
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.update()

    auth_component = AuthComponent()

    auth_component.login_button.on_click = on_login_click

    patient_data_component = flet.Column(
        controls=[
            flet.TextField(label='Имя пациента'),
            flet.Row(
                alignment=flet.MainAxisAlignment.CENTER,
                controls=[flet.FilledButton(text='Показать информацию', on_click=show_client_data)]
            ),
            flet.Row(
                alignment=flet.MainAxisAlignment.CENTER,
                controls=[flet.FilledButton(text='Просмотр записей пациентов', on_click=show_records)]
            ),

        ],
        visible=False,
        alignment=flet.MainAxisAlignment.CENTER
    )

    page.add(
        flet.Column(
            controls=[auth_component, patient_data_component]
        )
    )


ft.app(main)
