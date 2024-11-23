from abc import ABC, abstractmethod

class Provider(ABC):

    @abstractmethod
    def list_by_query(self):
        pass

    @abstractmethod
    def get_by_name(self):
        pass