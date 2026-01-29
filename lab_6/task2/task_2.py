from utils import File

class PhoneBook:
    def __init__(self, actions: list[str]) -> None:
        self.book = {}
        self.answer = []
        self.actions = actions

    def add_key(self, phone: int, name: str) -> None:
        h = hash(phone)
        self.book[h] = name


    def delete_key(self, phone: int) -> None:
        h = hash(phone)
        if h in self.book.keys():
            self.book.pop(h)
        else:
            pass

    def check_key(self, phone: int) -> None:
        h = hash(phone)
        if h in self.book.keys():
            self.answer += [self.book[h]]
        else:
            self.answer += ['not found']

    def distribute(self) -> list[str]:
        for a in self.actions:
            arg = a.split(" ")
            command, phone = arg[0], int(arg[1])
            if command == "add":
                name = arg[2]
                self.add_key(phone, name)
            elif command == "del":
                self.delete_key(phone)
            elif command == "find":
                self.check_key(phone)
            else:
                pass
        return self.answer

def limit(count: int, commands: list[str]) -> bool:
    if 1 <= count == len(commands) <= 10**5:
        for c in commands:
            c = c.split(" ")
            if len(c) == 2:
                action, phone = c
                if action in ["add", "del", "find"] and len(phone) <= 7 and phone.isnumeric():
                    continue
                else:
                    return False
            if len(c) == 3:
                action, phone, name = c
                if (action in ["add", "del", "find"] and len(phone) <= 7 and phone.isnumeric()
                        and len(name) <= 15 and name.isalpha()):
                    continue
                else:
                    return False
    else:
        return False
    return True

def phone_book_txt():
    f = File(__file__)
    arguments = f.read()
    count = int(arguments[0])
    commands = arguments[1:count+1]
    if limit(count, commands):
        arg = PhoneBook(commands).distribute()
        answer = "\n".join(arg)
        f.write(answer)

if __name__ == "__main__":
    phone_book_txt()