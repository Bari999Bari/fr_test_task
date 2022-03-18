from django.forms import forms


def validate_phone_number(value):
    allowed_symbs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    valid = True
    for count, symb in enumerate(value):
        if (count == 0 and int(symb) != 7) or int(symb) not in allowed_symbs or len(value) != 11:
            valid = False
            break
    if valid == False:
        raise forms.ValidationError(
            'Некоректный формат номера',
            params={'value': value},
        )
