"""Fixtures for members tests."""

from members.tests.factories import GymFactory


def make_gym(*args, **kwargs):
    """Returns a gym instance."""
    gym = GymFactory(*args, **kwargs)
    gym.save()
    return gym
