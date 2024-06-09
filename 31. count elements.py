def count_elements(arr):
    element_set = set(arr)
    count = 0
    
    for x in arr:
        if x + 1 in element_set:
            count += 1
            
    return count

print(count_elements([1, 2, 3]))        
print(count_elements([1, 1, 3, 3, 5, 5, 7, 7]))  
print(count_elements([0, 1, 2, 2, 3]))  

#Time complexity:O(n)
#Space complexity:O(n)
