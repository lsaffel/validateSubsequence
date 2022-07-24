# Validate subsequence
# Given two non-empty arrays of integers, write a function that
# determines whether the second array is a subsequence
# of the first one.
# A subsequence of an array is a set of numbers that aren't necessarily
# adjacent in the array, but that are in the same order
# as they appear in the array. For instance, the numbers [1,3,4] form
# a subsequence of the array [1,2,3,4] and so do the numbers [2,4].
# Note that a single number in an array and the array itself
# are both valid subsequences of the array.

# this works. Two alternate solutions below that - one with a while loop, one with a for loop.

# This should also be:
# O(n) time, O(1) space

def isValidSubsequence(array, sequence):
    arrayPtr = 0
    sequencePtr = 0

    sequenceInArray = False

    # array =    [1,5,3]    length = 3
    # sequence = [1,4]

    # array =    [1,5,7]
    # sequence = [1,7]

    # array =    [7]
    # sequence = [4]

    arrayLength = len(array)
    sequenceLength = len(sequence)

    # do while both pointers are not past the end of either array
    while arrayPtr < arrayLength and sequencePtr < sequenceLength and not sequenceInArray:
        # compare the elements at arrayPtr and sequencePtr
        # if they are the same, increment both

        if array[arrayPtr] == sequence[sequencePtr]:
            sequencePtr += 1
            if sequencePtr == sequenceLength:
                return True

        # only the arrayPtr increments if they are not the same
        arrayPtr += 1

    # if both pointers are past the end of the arrays then return True
    #     else return False

    if arrayPtr == arrayLength and sequencePtr == sequenceLength:
        return True
    else:
        return False

#-----------------------------------------------------------------------------
# AE solution - with while loop
# O(n) time, O(1) space
def isValidSubsequenceWhile2(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

#-----------------------------------------------------------------------------
# AE solution - with for loop
# O(n) time, O(1) space
def isValidSubsequenceFor(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break       # or can have "return True" here instead of break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)
#-----------------------------------------------------------------------------

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print([3, 1, 8], [3,1], "The result is:", isValidSubsequence([3, 1, 8], [3,1]))
    print([3, 1, 8], [3,7], "The result is:", isValidSubsequence([3, 1, 8], [3,7]))
    print([3, 1, 5, 8], [1,8], "The result is:", isValidSubsequence([3, 1, 8], [3,1]))
    print([12], [12], "The result is:", isValidSubsequence([12], [12]))

    print([3, 1, 8], [3, 1], "The AE while result is:", isValidSubsequenceWhile2([3, 1, 8], [3, 1]))
    print([3, 1, 8], [3,7], "The AE while result is:", isValidSubsequenceWhile2([3, 1, 8], [3,7]))
    print([3, 1, 5, 8], [1,8], "The AE while result is:", isValidSubsequenceWhile2([3, 1, 8], [3,1]))
    print([12], [12], "The AE while result is:", isValidSubsequenceWhile2([12], [12]))

    print([3, 1, 8], [3, 1], "The AE for result is:", isValidSubsequenceFor([3, 1, 8], [3, 1]))
    print([3, 1, 8], [3,7], "The AE for result is:", isValidSubsequenceFor([3, 1, 8], [3,7]))
    print([3, 1, 5, 8], [1,8], "The AE for result is:", isValidSubsequenceFor([3, 1, 8], [3,1]))
    print([12], [12], "The AE for result is:", isValidSubsequenceFor([12], [12]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
