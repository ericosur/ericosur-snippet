# coding: utf-8

'''
data classes like C struct
'''

from dataclasses import dataclass

@dataclass
class UserData:
    ''' data class '''
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
