#!/usr/bin/python
#
# reference from: http://www.thegeekstuff.com/2017/07/python-for-loop-examples/
#

def test_for_loop(checkname):
    names = ["john", "lisa", "raj", "jacob"]
    for nn in names:
        if nn == checkname:
            break
        print(nn)
    else:
        print("==> all items processed at for-loop")

    print("--end--")

def show_list_in_list():
    two_sets = [["moon", "monkey", "money"], ["pill", "police", "person"]]
    for word_list in two_sets:
        for word in word_list:
            print(word)

if __name__ == "__main__":
    print("test#1 ==>" )
    test_for_loop("no-such-name")
    print("test#2 ==>")
    test_for_loop("raj")
    print("list in list ==>")
    show_list_in_list()
