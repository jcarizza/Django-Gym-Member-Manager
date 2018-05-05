"""Factories for members app."""

from factory import SubFactory
from factory.django import DjangoModelFactory
from django.utils.timezone import datetime
from members.models import (
    Gym,
    StaffMember,
)

DEFAULT_GYM_REGISTRATION_DATE = datetime(2018, 1, 1).date()
DEFAULT_GYM_REGISTRATION_UPTO = datetime(2018, 2, 1).date()
DEFAULT_GYM_NAME = 'Hugo Gym'
DEFAULT_GYM_STATUS = 'paid'
DEFAULT_GYM_ADDRESS = 'Note Agites 322'
STAFF_MEMBER_FIRST_NAME = 'John'
STAFF_MEMBER_LAST_NAME = 'Doe'
STAFF_MEMBER_CELLPHONE = '+54 099 12345678'
STAFF_MEMBER_ADDRESS = 'Secret street 123'
STAFF_MEMBER_EMAIL = 'john@doe.com'


class GymFactory(DjangoModelFactory):
    """Create a Gym."""

    class Meta:  # pylint: disable=C0111
        model = Gym

    name = DEFAULT_GYM_NAME
    status = DEFAULT_GYM_STATUS
    address = DEFAULT_GYM_ADDRESS
    registration_date = DEFAULT_GYM_REGISTRATION_DATE
    registration_upto = DEFAULT_GYM_REGISTRATION_UPTO


class StaffMemberFactory(DjangoModelFactory):
    """Create a staff member."""

    class Meta: # pylint: disable=C0111
        model = StaffMember

    first_name = STAFF_MEMBER_FIRST_NAME
    last_name = STAFF_MEMBER_LAST_NAME
    email = STAFF_MEMBER_EMAIL
    is_owner = True
    gym = SubFactory(GymFactory)
