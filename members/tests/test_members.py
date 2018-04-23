"""Test members app."""

from django.test import TestCase
from members.tests import factories
from members.models import (
    Gym,
    StaffMember,
)
from members.tests.fixtures import (
    make_gym,
    make_staff_member,
)


class GymTests(TestCase):
    """Test a gym."""

    def test_make_gym_test_fixture(self):
        """Test create a new gym using members.fixture."""
        gym = make_gym()
        self.assertTrue(gym.id is not None)
        self.assertEqual(gym.name, factories.DEFAULT_GYM_NAME)
        self.assertEqual(gym.status, factories.DEFAULT_GYM_STATUS)
        self.assertEqual(gym.address, factories.DEFAULT_GYM_ADDRESS)
        self.assertEqual(gym.registration_date, factories.DEFAULT_GYM_REGISTRATION_DATE)
        self.assertEqual(gym.registration_upto, factories.DEFAULT_GYM_REGISTRATION_UPTO)

        gym2 = make_gym(name='pepe', address='godoy 123')
        self.assertEqual(gym2.name, 'pepe')
        self.assertEqual(gym2.address, 'godoy 123')

    def test_add_staff_member_into_gym(self):
        """Test add a staff member into a gym."""


class GymStaffTests(TestCase):
    """Test a member."""

    def test_make_staff_member_fixture(self):
        """Test create a new gym staff member."""
        staff_member = make_staff_member()
        self.assertEqual(staff_member.first_name, factories.STAFF_MEMBER_FIRST_NAME)
        self.assertEqual(staff_member.last_name, factories.STAFF_MEMBER_LAST_NAME)
        self.assertEqual(staff_member.cellphone, factories.STAFF_MEMBER_CELLPHONE)
        self.assertEqual(staff_member.email, factories.STAFF_MEMBER_EMAIL)
        self.assertTrue(staff_member.is_owner)

        # staff_member has a gym assigned
        self.assertTrue(staff_member.gym is not None)

        # Gym can be deleted, and staff_member will persist
        gym = staff_member.gym
        Gym.objects.get(id=gym.id).delete()  # pylint: disable=E1101
        self.assertFalse(Gym.objects.filter(id=gym.id).exists())  # pylint: disable=E1101
        self.assertTrue(StaffMember.objects.filter(id=staff_member.id).exists())  # pylint: disable=E1101

        # staff_member has no gym at all
        staff_member = StaffMember.objects.get(id=staff_member.id)  # pylint: disable=E1101
        self.assertEqual(staff_member.gym, None)

        # i can create a staff_member without a gym
        staff_member = make_staff_member(gym=None)
        self.assertEqual(staff_member.gym, None)
