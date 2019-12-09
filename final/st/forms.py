from django.forms import ModelForm
from .models import st_model

class st_form(ModelForm):
    class Meta:
        model = st_model
        fields = '__all__'



