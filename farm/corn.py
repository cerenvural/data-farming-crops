"""Module: corn
Defines the Corn crop class.
"""
from farm.crop import Crop


class Corn(Crop):
    """A corn crop that produces 10 grains each time it is watered."""

    def water(self):
        """Water the corn crop, adding 10 grains."""
        self.grains += 10
