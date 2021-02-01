class First:
    @classmethod
    def get_name(cls):
        return 'First'

    # @staticmethod
    @classmethod
    def get_type(cls):  # "cls" is needed after decorator has been changed
        return 'Class'


class Second:
    @classmethod
    def get_name(cls):
        return 'Second'


class Third:
    @classmethod
    def get_programming_language(cls):
        return 'Python'


class ThreeDerived(First, Second, Third):
    @classmethod
    def get_programming_language(cls):
        return 'C++'


print(ThreeDerived.get_name())
print(ThreeDerived.get_programming_language())
print(ThreeDerived.get_type())
