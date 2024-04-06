import flet


class AuthComponent(flet.UserControl):
    login_button = flet.FilledButton(text='Войти')
    login_field = flet.TextField(label='Логин')
    password_field = flet.TextField(label='Пароль', password=True, can_reveal_password=True)

    def build(self):
        login_page = flet.Column(
            controls=[
                self.login_field,
                self.password_field,
                flet.Row(
                    controls=[
                        self.login_button
                    ],
                    alignment=flet.MainAxisAlignment.CENTER
                ),
                flet.Row(
                    controls=[
                        flet.TextButton(
                            text='Создать аккаунт'
                        )
                    ],
                    alignment=flet.MainAxisAlignment.CENTER
                )
            ]
        )
        return login_page