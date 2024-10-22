from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError(
                "Довжина значення не може бути більше ніж 10 символів")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value: str):
        self.phones.append(Phone(value))

    def remove_phone(self, value: str):
        for i in self.phones:
            if i.value == value:
                self.phones.remove(i)

    def find_phone(self, value: str):
        for i in self.phones:
            if i.value == value:
                return i.value

    def edit_phone(self, started_value: str, new_value: str):
        counter = 0
        for i in self.phones:
            if i.value == started_value:
                break
            counter += 1
        if counter < len(self.phones):
            self.phones[counter] = Phone(new_value)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = list(
            map(lambda x: x.value, record.phones))

    def find(self, name: str):
        record = Record(name)
        phones = self.data.get(name)
        for i in phones:
            record.add_phone(i)
        return record

    def delete(self, value: str):
        del self.data[value]
