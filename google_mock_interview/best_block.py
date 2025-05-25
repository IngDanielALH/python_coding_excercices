"""
Given a list of requirements, find the best block with the lowest distance to fulfill all the requirements
"""


def get_min_distances(blocks, req):
    n = len(blocks)
    min_distances = [float("inf")] * n
    closest_req_idx = float("inf")

    for i in range(n):
        if blocks[i][req]:
            closest_req_idx = i
        min_distances[i] = abs(i - closest_req_idx)

    closest_req_idx = float("inf")
    for i in reversed(range(n)):
        if blocks[i][req]:
            closest_req_idx = i
        min_distances[i] = min(min_distances[i], abs(i - closest_req_idx))

    return min_distances


def get_best_block(blocks, reqs):
    n = len(blocks)

    distances_per_req = [get_min_distances(blocks, req) for req in reqs]

    max_distances_at_blocks = [
        max(distances[i] for distances in distances_per_req)
        for i in range(n)
    ]

    return max_distances_at_blocks.index(min(max_distances_at_blocks))
