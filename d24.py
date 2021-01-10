with open('d24.in1', 'r') as f:
    content = f.read()
routes = content.split('\n')
print()
grid = {[]}
# maybe https://stackoverflow.com/questions/2459402/hexagonal-grid-coordinates-to-pixel-coordinates


from itertools import product


def cartesian_product(arr1, arr2):
    # return the list of all the computed tuple
    # using the product() method
    return list(product(arr1, arr2))


# Driver Function
if __name__ == "__main__":
    arr1 = [1, 2, 3]
    arr2 = [5, 6, 7]
    print(cartesian_product(arr1, arr2))

for route in routes:
    print(route)
