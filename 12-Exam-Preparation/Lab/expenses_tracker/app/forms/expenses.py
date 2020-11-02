from django import forms
from app.models import Expense
from app.forms.common import DisabledFormMixin


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class DeleteExpenseForm(ExpenseForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)