from django.test import TestCase
from members.tests.fixtures import make_gym
from members.tests import factories


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
