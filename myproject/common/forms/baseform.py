__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

from django import forms


class BaseForm(forms.BaseForm):
    """
    The abstract form from which most other form should inherit to ensure common form functionality is support.
    """

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)

        for field in list(self.fields.values()):
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        abstract = True
