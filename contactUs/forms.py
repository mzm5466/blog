from django.forms import ModelForm
from contactUs.models import Email
class EmailForm(ModelForm):
    class Meta:
        model=Email
        fields='__all__'