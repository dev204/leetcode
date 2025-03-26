'''
You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order.
Return the median value among all elements of the two arrays.
Your solution must run in O(log (m+n)) time
'''

# we don't need to actually merge the two arrays , we just need to figure out numbers in the first half of the
# final merged sorted array and numbers in second half
# A = [1,2,3,4,5] 5 ele B =[123455678] 8 ele, we need to find first 6 elements (left side of the arr will be roughly equal to this)
# total = 13, half = 6 (round down)
# let's get half of the elements of A or whatever the smaller arr is , so middle of A is element 3
# similarly for B we don't need to run BS we can say half num of elements - 3 = 3 ie first 3 elements
# now A = [1,2,3] and B = [1 2 3] make up first portion of subarray, then need to confirm if we found the right partition
# last element of A partition <= first element of B second half, and last ele of B partition <= first ele of A second half
# if this condition holds true then we are good and median would be min(first ele of A or B) from the second halves resp
# otherwise we continue on binary search on A (smaller arr) to find the correct partition
# we need to update our pointers, if we need extra elements from A we shift l=mid+1 else we do r=mid-1
# basically if we increase elements from A our num of elements from B get reduced and lead us to right partition
# and vice versa depending on border elements
# lastly if total ele is odd we take min of 2 elements from right partition elements in A and B
# if total is even ele we take min of left partition of both A and B to get correct boundry ele and
# max of first elements on right partition for A and B, divide both up to get the result

# tc O(log min(n,m)) sc O(1)

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    # what are the total elements and first half elements of the final merged arr
    first_half = total // 2

    # we don't need to actually merge the two arrays
    # we just need to figure out first half of the merged sorted array

    #    l   m   r
    # A [1,2,3,4,5]
    #    ----- : this half is part of the first half
    # B [3,4,5,6,7,8,9,10]

    # we run binary search on the smaller array
    if len(B) < len(A):
        A, B = B, A
    l, r = 0, len(A) - 1

    # we know this loop will break eventually as median exists & we will find it eventually
    while True:
        # we need two pointers for arr A and B -> i and j
        i = (l + r) // 2
        # we know that elements upto A[i] should belong in first half of the
        # final merged (and sorted) array
        j = first_half - i - 2  # we subtract 2 bcos arrays are index based and 1 for each arr

        #    l   m   r
        # A [1,2,3,4,5] i = 0 + 5 // 2 = 2
        #    ----- : this half is part of the first_half
        # .      Al,Ar
        # total = 13 first_half = 6
        # B [3,4,5,6,7,8,9,10] j = 6 - 2 - 2 = 2 index
        #       bl,br
        Aleft = A[i] if i >= 0 else float("-infinity")  # if i is out of bounds
        Aright = A[i + 1] if (i + 1) < len(A) else float(
            "infinity")  # if i+1 is out of bounds we want all elements of A to be part of left partition
        Bleft = B[j] if j >= 0 else float("-infinity")  # we set -infi to indicate Aleft is not part of the A arr
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        # the partition is correct if below is true
        if Aleft <= Bright and Bleft <= Aright:
            # odd
            if total % 2:
                return min(Aright, Bright)  # min because imagine in final sorted & merged arr we need left most element
            # even
            # max bcos we want right most value of left half, min because we want the left most value of right half
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2  # these are the two values in the middle
        # in case we don't find median
        elif Aleft > Bright:  # too many elements from A and Aleft is too big
            r = i - 1
        else:
            l = i + 1

