strings = ['a', 'b' , 'c' , 'd']

def basicOps():
  strings.append('x') #O(1)
  print(strings)

  strings.pop() #O(1)
  print(strings)

  strings.insert(2 , 'y') #O(n)
  print(strings)

# basicOps()


strToRev = "Hi This is Biswadeep"

def reverseString(str):
  if str and len(str) > 0:
    print(str[::-1])


def reverseString2(str):
  strLen = len(str)
  strList = list(str)
  revArr = []
  if str and strLen > 0:
    for char in range(strLen -1 , -1 , -1):
      revArr.append(strList[char])
  print(''.join(revArr))

# reverseString2(strToRev)

arr1 = [1,3,4,8]
arr2 = [4,6,30,31]

def mergeSortedArray(arr1 , arr2):
  arr1Len = len(arr1)
  arr2Len = len(arr2)

  if arr1Len == 0 or arr2Len == 0 :
    print(arr1 + arr2)
  
  mergedArray = []

  arr1Idx = 0
  arr2Idx = 0

  def pushFromArray(arr , idx):
    mergedArray.append(arr[idx])

  while arr1Idx < arr1Len and arr2Idx < arr2Len :
    if arr1[arr1Idx] < arr2[arr2Idx]:
      pushFromArray(arr1,arr1Idx)
      arr1Idx += 1
    else :
      pushFromArray(arr2,arr2Idx)
      arr2Idx += 1

  print(mergedArray + arr1[arr1Idx::] + arr2[arr2Idx::])

# mergeSortedArray(arr1 , arr2)

