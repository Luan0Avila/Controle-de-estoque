from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import add_placeholder, strong_password


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_placeholder(self.fields['password'], 'Digite sua senha')
        add_placeholder(self.fields['password_repeat'], 'Repita sua senha')

    first_name = forms.CharField(
        error_messages={'required': 'Digite seu primeiro nome'},
        label='First name'
    )

    last_name = forms.CharField(
        error_messages={'required': 'Digite seu sobrenome'},
        label='Last name'
    )
    
    email = forms.EmailField(
        error_messages={'required': 'E-mail é obrigatório'},
        label='E-mail',
        help_text='O e-mail deve ser valido',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Digite sua senha',
        },
        help_text=(
            'A senha deve ter pelo menos uma letra maiúscula, '
            'uma letra minúscula, um número e no mínimo 8 caracteres.'
        ),
        validators=[strong_password],
        label='Password'
    )

    password_repeat = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password (repeat)',
        error_messages={
            'required': 'Por favor repita sua senha',
        },
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'o e-mail digitado já está em uso', code='invalid',
            )
        return email
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password != password_repeat:
            password_confirmation_error = ValidationError(
                'As senhas não coincidem',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password_repeat': [
                    password_confirmation_error,
                ],
            })