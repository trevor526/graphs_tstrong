import heapq

def dijkstra(graph, source):
    dist = {source: 0}
    path = {}
    visited = set()
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph.get(u, {}).items():
            nd = d + w
            if v not in dist or nd < dist[v]:
                dist[v] = nd
                path[v] = u
                heapq.heappush(pq, (nd, v))

    return dist, path