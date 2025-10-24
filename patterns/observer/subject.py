""""
Description: A class to manage Subject class objects.
"""
__author__ = "Amanda Dadalt Makino"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from patterns.observer.observer import Observer

class Subject(ABC):
    """
    Subject class: Maintains subject data.
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        Initializes class attributes to argument values.
        """

        self._observers: list[Observer] = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Abstract method
        Implemented in subclass(es).
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Abstract method
        Implemented in subclass(es).
        """
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """
        Abstract method
        Implemented in subclass(es).
        """
        pass
