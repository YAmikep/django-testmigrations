from django.db import models
from django.utils.deconstruct import deconstructible


@deconstructible
class Value(object):
    def __init__(self, val):
        self.val = val

@deconstructible
class ValueManager(object):
    def __init__(self, values):
        self.values = values

value_manager = ValueManager(values=[Value(val=1), Value(val=2)])


class CustomField(models.CharField):

    def __init__(self, *args, **kwargs):
        self.value_manager = kwargs.pop('value_manager', None)

        super(CustomField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CustomField, self).deconstruct()
        if self.value_manager:
            kwargs['value_manager'] = self.value_manager
        return name, path, args, kwargs


class ModelA(models.Model):

    field1 = CustomField(value_manager=value_manager, max_length=50)
