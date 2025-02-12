"""
Amazon Web Services (AWS) is a cloud computing platform with multiple servers. One of the servers is assigned to serve
customer requests. There are nn customer requests placed sequentially in a queue, where the ithith request has a
maximum waiting time denoted by wait[i]wait[i]. That is, if the ithith request is not served within wait[i]wait[i]
seconds, then the request expires and it is removed from the queue. The server processes the request following the
First In First Out (FIFO) principle. The 1st1st request is processed first, and the nthnth request is served last.
At each second, the first request in the queue is processed. At the next second, the processed request and any expired
requests are removed from the queue.

Given the maximum waiting time of each request denoted by the array wait, find the number of requests present in the
queue at every second until it is empty.

Note:
If a request is served at some time instant tt, it will be counted for that instant and is removed at the next instant.
The first request is processed at time = 0. A request expires without being processed when time = wait[i]. It must
be processed while time < wait[i]. See the example below for wait[3]wait[3].
The initial queue represents all requests at time = 0 in the order they must be processed.

Example:

The number of requests is n=4n=4, and their maximum wait times are wait = [2, 2, 3, 1].
time = 0 seconds, the 1st request is served. The number of requests in the queue is 4. queue = [1, 2, 3, 4].
time = 1 second, request 1 is removed because it is processed, request 4 (wait[3] = 1) is removed because
    time = wait[3] = 1, which exceeds its maximum waiting time. Also, request 2 is served.
    The number of requests in the queue at time = 1 second is 2. queue = [2, 3].
time = 2 seconds, request 2 is removed because it is processed, request 3 is served. The number of requests in the queue
    is 1. queue = [3].
time = 3 seconds, request 3 is removed because it is processed. The number of requests in the queue is 0.
    queue = [empty].

The answer is [4, 2, 1, 0].
"""


def findRequestsInQueue(requests):
    pass
