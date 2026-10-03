"""Module: rice
Defines the Rice crop class.
"""
from farm.crop import Crop


class Rice(Crop):
    """A rice crop that produces 5 grains each time it is watered,
    and can also be transplanted for an extra 10 grains."""

    def water(self):
        """Water the rice crop, adding 5 grains."""
        self.grains += 5

    def transplant(self):
        """Transplant the rice crop, adding 10 grains."""
        self.grains += 10
"""Module: rice
Defines the Rice crop class.
"""
from farm.crop import Crop


class Rice(Crop):
    """A rice crop that produces 5 grains each time it is watered,
    and can also be transplanted for an extra 10 grains."""

    def water(self):
        """Water the rice crop, adding 5 grains."""
        self.grains += 5

    def transplant(self):
        """Transplant the rice crop, adding 10 grains."""
        self.grains += 10
