"""Extensions to mincePy and the mincePy GUI"""

from . import forms


def get_types():
    """Provide a list of all historian types"""
    types = list()
    types.extend(forms.MINCEPY_TYPES)

    return types
