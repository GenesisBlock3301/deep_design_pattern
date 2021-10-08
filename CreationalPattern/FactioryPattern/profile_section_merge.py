from abc import ABC, abstractmethod
from section import PersonalSection, AlbumSection, PatentSection, PublicationSection


class Profile(ABC):
    def __init__(self) -> None:
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSection(self, section):
        self.sections.append(section)


class Linkdin(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(PatentSection())
        self.addSection(PublicationSection())


class Facebook(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(PatentSection())
        self.addSection(PublicationSection())


# if __name__ == "__main__":
#     profile_type = input()
profile = Linkdin()
for section in profile.sections:
    section.describe()

