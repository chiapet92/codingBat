# first_last6
# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False

def first_last6(nums):
  if (nums[0]==6 or nums[(len(nums)-1)]==6) :
    return True
  return False
#=======================================================================
# make_pi
# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
# make_pi() → [3, 1, 4]

def make_pi():
  return [3,1,4]

#=======================================================================
# common_end
# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True

def common_end(a, b):
  if (a[0]==b[0] or a[len(a)-1]==b[len(b)-1]) :
    return True
  return False

# =======================================================================
# rotate_right3
# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]

def rotate_left3(nums):
  a = nums[len(nums)-1]
  for num in reversed(range(len(nums)-1)):
    nums[num+1]=nums[num]
  nums[0] = a
  return nums

# =======================================================================
# middle_way
# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
# middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

def middle_way(a, b):
  return [a[1],b[1]]

# =======================================================================
# has23
# Given an int array length 2, return True if it contains a 2 or a 3.
# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

def has23(nums):
  for num in range(len(nums)) :
    if nums[num]==2 or nums[num]==3 :
      return True
  return False