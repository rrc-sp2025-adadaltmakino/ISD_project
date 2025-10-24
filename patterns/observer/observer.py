""""
Description: A class to manage Observer class objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Observer class: Maintains observer data.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Abstract method
        Implemented in subclass(es).
        """
        pass
