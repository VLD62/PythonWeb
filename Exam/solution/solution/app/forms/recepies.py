from django import forms
from app.models import Recipe
from app.forms.common import DisabledFormMixin


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class DeleteRecipeForm(RecipeForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)