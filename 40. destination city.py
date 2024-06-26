def destCity(paths):
    start_cities = set()
    
    for path in paths:
        start_cities.add(path[0])
    
    for path in paths:
        if path[1] not in start_cities:
            return path[1]

paths1 = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
print(destCity(paths1))  # Output: "Sao Paulo"

paths2 = [["B", "C"], ["D", "B"], ["C", "A"]]
print(destCity(paths2))  # Output: "A"

paths3 = [["A", "Z"]]
print(destCity(paths3))  # Output: "Z"

#Time complexity:O(n)
#Space complexity:O(n)
