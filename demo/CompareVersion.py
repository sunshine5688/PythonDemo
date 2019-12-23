

def compareVersion(version1, version2):
    if(version1 == version2):
        return 0
    arr1 = version1.split('.')
    arr2 = version2.split('.')

    for index in range(0,3):
       if(arr1[index] > arr2[index]):
           return 1
       if(arr1[index] < arr2[index]):
           return -1

if __name__ == '__main__':
    print(compareVersion('2.0.3','1.1000.1'))