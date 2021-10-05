#!/usr/bin/python3
# coding: utf-8

'''
Python 3 program to find the longest repeated
non-overlapping substring

Returns the longest repeating non-overlapping
substring in str

This code is contributed by ita_c
'''

def longestRepeatedSubstring(msg):
    ''' longest repeated sub string '''
    n = len(msg)
    LCSRe = [[0 for x in range(n + 1)]
                for y in range(n + 1)]

    res = "" # To store result
    res_length = 0 # To store length of result

    # building table in bottom-up manner
    index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):

            # (j-i) > LCSRe[i-1][j-1] to remove
            # overlapping
            if msg[i - 1] == msg[j - 1] and LCSRe[i - 1][j - 1] < (j - i):
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1

                # updating maximum length of the
                # substring and updating the finishing
                # index of the suffix
                if LCSRe[i][j] > res_length:
                    res_length = LCSRe[i][j]
                    index = max(i, index)

            else:
                LCSRe[i][j] = 0

    # If we have non-empty result, then insert
    # all characters from first character to
    # last character of string
    if res_length > 0:
        for i in range(index - res_length + 1,
                                    index + 1):
            res = res + msg[i - 1]

    return res

def main():
    ''' main '''
    text = "geeksforgeeks"
    print(longestRepeatedSubstring(text))


# Driver Code
if __name__ == "__main__":
    main()
