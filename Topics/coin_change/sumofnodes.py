#!/usr/bin/python3
# coding: utf-8

'''
https://www.geeksforgeeks.org/sum-nodes-binary-tree/

Python3 Program to print sum of all
the elements of a binary tree

Binary Tree Node
This code is contributed by Shubham Singh(SHUBHAMSINGH10)

utility that allocates a new Node with the given key
'''

from typing import TypeVar

Node = TypeVar('Node')

# pylint: disable=invalid-name
class newNode:
    ''' Construct to create a new node '''
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

# Function to find sum of all the element
def addBT(root: Node) -> int:
    ''' to traverse all nodes and sum up '''
    if root is None:
        return 0
    return root.key + addBT(root.left) + addBT(root.right)

# Driver Code
def main():
    ''' main '''
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(8)

    node_sum = addBT(root)
    print("Sum of all the nodes is:", node_sum)

if __name__ == '__main__':
    main()
