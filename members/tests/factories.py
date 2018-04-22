"""Factories for members app."""

from factory. django import DjangoModelFactory
from django.utils.timezone import datetime, timedelta
from members.models import Gym

DEFAULT_GYM_REGISTRATION_DATE = datetime(2018, 1, 1).date()
DEFAULT_GYM_REGISTRATION_UPTO = datetime(2018, 2, 1).date() 
DEFAULT_GYM_NAME = 'Hugo Gym'
DEFAULT_GYM_STATUS = 'paid'
DEFAULT_GYM_ADDRESS = 'Note Agites 322'


class GymFactory(DjangoModelFactory):
    """Create a Gym."""

    class Meta:
        model = Gym

    name = DEFAULT_GYM_NAME
    status = DEFAULT_GYM_STATUS
    address = DEFAULT_GYM_ADDRESS
    registration_date = DEFAULT_GYM_REGISTRATION_DATE
    registration_upto = DEFAULT_GYM_REGISTRATION_UPTO