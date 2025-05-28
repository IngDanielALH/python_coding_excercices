"""
You're given a list of time intervals during which students at a school need a laptop. These time intervals are
represented by pairs of integers [start, end], where
 0 <= start < end. However, start and end don't represent real times; therefore, they may be greater than 24.
No two students can use a laptop at the same time, but immediately after a student is done using a laptop,
another student can use that same laptop. For example, if one student rents a laptop during the time interval [0, 2],
another student can rent the same laptop during any time interval starting with 2.
Write a function that returns the minimum number of laptops that the school needs to rent such that all students will
always have access to a laptop when they need one.

Sample Input
times = [
  [0, 2],
  [1, 4],
  [4, 6],
  [0, 4],
  [7, 8],
  [9, 11],
  [3, 10],
]

Sample output
3
"""
import heapq

def laptopRentals(times):
    if not times:
        return 0

        # Ordenar por el tiempo de inicio
    times.sort(key=lambda x: x[0])

    # Min-heap para los tiempos de finalización
    min_heap = []
    heapq.heappush(min_heap, times[0][1]) # mete tiempo final

    for i in range(1, len(times)):
        if min_heap[0] <= times[i][0]:
            heapq.heappop(min_heap)  # Se libera una laptop

        heapq.heappush(min_heap, times[i][1])  # Se ocupa una laptop (o la misma)

    return len(min_heap)
