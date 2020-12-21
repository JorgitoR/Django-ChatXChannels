from django import forms


class MensateForm(forms.Form):
    mensaje = forms.CharField(
        widget = forms.CharField(
            widget = forms.TextInput(
                attrs = {"class": "TextMensaje", "placeholder":"Escribe Tu mensaje"}
            )
        )
    )