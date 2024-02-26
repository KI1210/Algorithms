import timeit
import importlib

from randomArray import getRandomArray

sortAlgoArr = [
    ("Merge Sort.merge", "mergeSort"),
    ("Quick Sort.quick", "quickSort")
]

# randArr = getRandomArray(10)

n = 100
samples = 100

for algo in sortAlgoArr:
    module = importlib.import_module(algo[0])
    func = getattr(module, algo[1])

    elapsedTime = timeit.timeit(lambda: func(
        getRandomArray(n)), number=samples)

    print("Time elapsed with n={} for {} : {}".format(
        n, algo[0], elapsedTime / samples))
