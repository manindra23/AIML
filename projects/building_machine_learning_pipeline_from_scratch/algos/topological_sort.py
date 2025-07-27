def topological_sort(digraph):
    # calculate indegree for all nodes
    indegree = {node: 0 for node in digraph}
    for node in digraph:
        for adjacent_node in digraph[node]["next"]:
            if adjacent_node not in indegree:
                raise Exception(f"Node '{adjacent_node}' not defined")
            indegree[adjacent_node] += 1

    # get zero-indegree nodes
    zero_indegree_nodes = [node for node in digraph if indegree[node] == 0]

    # sort
    sorted_nodes = []
    while len(zero_indegree_nodes) > 0:
        # add a zero-indegree node to the sorted array
        node = zero_indegree_nodes.pop()
        sorted_nodes.append(node)

        # decrement the indegree of all adjacent nodes
        for adjacent_node in digraph[node]["next"]:
            indegree[adjacent_node] -= 1
            if indegree[adjacent_node] == 0:
                zero_indegree_nodes.append(adjacent_node)

    if len(sorted_nodes) != len(digraph):
        raise Exception("Tasks do not form a DAG")

    return sorted_nodes


if __name__ == "__main__":
    # define a DAG
    dag = {
        "task_a": {"next": ["task_b"]},
        "task_e": {"next": []},
        "task_c": {"next": ["task_e"]},
        "task_d": {"next": ["task_e"]},
        "task_b": {"next": ["task_c", "task_d"]},
    }

    print("DAG:")
    try:
        sorted_graph = topological_sort(dag)
        print(sorted_graph)
    except Exception as error:
        print(error)

    # define a graph that is not a DAG. note that "task_e" connects back to
    # "task_b"
    not_a_dag = {
        "task_a": {"next": ["task_b"]},
        "task_e": {"next": ["task_b"]},
        "task_c": {"next": ["task_e"]},
        "task_d": {"next": ["task_e"]},
        "task_b": {"next": ["task_c", "task_d"]},
    }

    print("Not a DAG:")
    try:
        sorted_graph = topological_sort(not_a_dag)
        print(sorted_graph)
    except Exception as error:
        print(error)