import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class NumberValidator(object):
    def __init__(self, min_digits=0):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        if not len(re.findall('\d', password)) >= self.min_digits:
            raise ValidationError(
                _("La contraseña debe contener al menos %(min_digits)d  dígitos, 0-9."),
                code='password_no_number',
                params={'min_digits': self.min_digits},
            )

    def get_help_text(self):
        return _(
            "Su contraseña debe contener al menos %(min_digits)d dígitos, 0-9." % {'min_digits': self.min_digits}
        )




class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("La contraseña debe contener al menos 1 letra minúscula, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "Su contraseña debe contener al menos 1 letra minúscula, a-z."
        )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("La contraseña debe contener al menos 1 símbolo:" +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Su contraseña debe contener al menos 1 símbolo:" +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )