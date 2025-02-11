"""
The developers of Amazon are working on a prototype for a simple load-balancing algorithm. There are num_servers servers
numbered from 0 to num_servers - 1 and the initial number of requests assigned to each server is 0.

In the iᵗʰ second, a request comes from IP hash of request[i], and it must be assigned to the server with the minimum
number of requests amongst the first request[i] servers. For example, if request[i] = 4, the request must be assigned to
the server with the minimum number of requests amongst the servers with id [0, 1, 2, 3]. If there are multiple servers
with the same minimum number of requests, choose the one with the minimum id. When a request is assigned to a server,
its number of requests increases by 1.

Given num_servers and the array request, for each request, find the id of the server it is assigned to.
Example

Suppose num_servers = 5, n = 5 and request = [3, 2, 3, 2, 4].

Aquí tienes el texto extraído de la imagen:

---

### The requests are processed as follows:

| Request IP Hash | Server Request Allocation | Assigned to | Remarks |
|---------------|--------------------------|------------|---------|
| **3** | [0, 0, 0, 0, 0] | **0** | The request must be assigned to the server with the minimum number of requests
                                    amongst the first 3 servers. Since all the first three servers have 0 requests
                                    assigned, it is assigned to the one with the minimum id, i.e., the server with id 0.
| **2** | [1, 0, 0, 0, 0] | **1** | The request must be assigned to the server with the minimum number of requests
                                    amongst the first 2 servers. Since server 1 has 0 requests assigned, which is less
                                    than server 0 with 1 request, it is assigned to server 1.
| **3** | [1, 1, 0, 0, 0] | **2** | Amongst the first 3 servers, the one with the minimum requests is server 2.
| **2** | [1, 1, 1, 0, 0] | **0** | Both of the first two servers have the same number of requests assigned. Hence,
                                    the request is assigned to server 0 as it has the minimum id.
| **4** | [2, 1, 1, 0, 0] | **3** | The request must be assigned to the server with the minimum number of requests
                                    amongst the first 4 servers. The server with minimum requests is server 3.



Hence the answer is [0, 1, 2, 0, 3]
"""