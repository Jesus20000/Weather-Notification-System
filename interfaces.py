from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass