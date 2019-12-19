from heapq import heappop, heappush, heapify
def minCost(ropes) -> int:
  if not ropes: return 0
  if len(ropes) == 1: return ropes[0]
  heapify(ropes)
  cost = 0
  while len(ropes) > 1:
    a, b = heappop(ropes), heappop(ropes)
    cost += a+b
    if ropes:
      heappush(ropes, a+b)
  return cost

print(minCost([1, 5,2 ,10, 35, 89]))
