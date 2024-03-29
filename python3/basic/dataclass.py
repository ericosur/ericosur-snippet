# coding: utf-8

from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    age: int
    city: str


def main():
    ''' main '''
    # Create an instance of the dataclass
    user_data = UserData("Bob", 25, "London")

    # Access data using dot notation
    print(user_data.age)  # Output: 25

if __name__ == '__main__':
    main()
