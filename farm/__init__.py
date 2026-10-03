"""Module: crop
Defines the Crop parent class, holding behavior shared by all crops.
"""
# pylint: disable=too-few-public-methods


class Crop:
    """Base class for all crops, tracking grains and ripeness."""

    def __init__(self):
        self.grains = 0

    def ripe(self):
        """Return True if the crop has produced at least 15 grains."""
        return self.grains >= 15
