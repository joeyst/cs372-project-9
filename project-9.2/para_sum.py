import threading

ranges = [
  [10, 20],
  [1, 5],
  [70, 80],
  [27, 92],
  [0, 16]
]

# => `O(N)` to calculate sum of range 
def sum_range(start, finish):
  return int(((finish - start + 1) * start) + (((finish - start) * (finish - start + 1)) / 2))

# mutate array; used from multiple threads 
def set_sum(start, finish, index, arr):
  arr[index] = sum_range(start, finish)

# gets sums and mutates same array in parallel 
def get_sums(vals=ranges):
  sums = [0] * len(vals)
  [threading.Thread(target=set_sum, args=[*pair, index, sums]).start() for index, pair in enumerate(vals)]
  return sums

# returns sums and sum of sums. Fantastic name, yeah? 
def get_sums_and_sum_sum(vals=ranges):
  sums = get_sums(vals)
  return sums, sum(sums)

def print_all(vals=ranges): 
  [print(data) for data in get_sums_and_sum_sum(vals)]

print_all()