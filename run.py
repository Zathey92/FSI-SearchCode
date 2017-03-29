# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)


print search.breadth_first_graph_search(ab).path()
print search.depth_first_graph_search(ab).path()
print search.iterative_deepening_search(ab).path()
print search.depth_limited_search(ab).path()

#branch and bound no informed search
print search.best_first_graph_search(ab,f=lambda n:n.path_cost).path()
print search.branch_bound_search(ab).path()

#branch and bound informed search
print search.branch_bound_subestimation_search(ab).path()


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
