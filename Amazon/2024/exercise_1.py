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


def getServerIds(num_servers, requests):
    # Inicializamos un diccionario para llevar el control de las solicitudes por servidor
    servers = {i: 0 for i in range(num_servers)}
    assigned_servers = []

    for request_i in requests:
        if request_i == 0:
            # Si request_i es 0, solo podemos elegir el servidor 0
            chosen_server = 0
        else:
            # Filtrar servidores dentro del rango permitido (0 a request_i - 1)
            valid_servers = {k: v for k, v in servers.items() if k < request_i}

            # Ordenar servidores por menor número de solicitudes y luego por menor ID
            sorted_servers = sorted(valid_servers.items(), key=lambda x: (x[1], x[0]))

            # Elegir el servidor con menor carga (el primer elemento de la lista ordenada)
            chosen_server = sorted_servers[0][0]

        # Incrementar la carga del servidor elegido
        servers[chosen_server] += 1

        # Guardar la asignación del servidor
        assigned_servers.append(chosen_server)

    return assigned_servers
