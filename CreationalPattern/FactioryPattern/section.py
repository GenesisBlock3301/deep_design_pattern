from abc import ABC, abstractmethod


class Section(ABC):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal section")


class AlbumSection(Section):
    def describe(self):
        print("Album section")


class PatentSection(Section):
    def describe(self):
        print("Pettent section")


class PublicationSection(Section):
    def describe(self):
        print("Publication section")
