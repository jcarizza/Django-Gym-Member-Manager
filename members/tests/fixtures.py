"""Fixtures for members tests."""

from members.tests.factories import (
    GymFactory,
    StaffMemberFactory,
)


def make_gym(*args, **kwargs):
    """Returns a gym instance."""
    gym = GymFactory(*args, **kwargs)
    gym.save()
    return gym


def make_staff_member(*args, **kwargs):
    """Returns a staff member."""
    staff_member = StaffMemberFactory(*args, **kwargs)
    staff_member.save()
    return staff_member
