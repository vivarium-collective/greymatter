class Node():
    def __init__(self, id, attributes):
        self.id = id
        self.attributes = attributes

    def __repr__(self):
        return f'{self.id}: {self.attributes}'


class Edge():
    def __init__(self, id, ports, attributes):
        self.id = id
        self.ports = ports
        self.attributes = attributes

    def __repr__(self):
        return f'{self.id} - {self.ports}: {self.attributes}'


class Graph():
    def __init__(self, nodes, edges):
        self.nodes = {}
        for node_id, node_data in nodes.items():
            node = Node(
                node_id,
                node_data['attributes'])
            self.nodes[node_id] = node

        # TODO: add a reference from the Node to the edges
        #   that point at them
        self.edges = {}
        for edge_id, edge_data in edges.items():
            direct_ports = {}
            for port_name, port_references in edge_data['ports'].items():
                direct_references = [
                    self.nodes[reference]
                    for reference in port_references]
                direct_ports[port_name] = direct_references

            edge = Edge(
                edge_id,
                direct_ports,
                edge_data['attributes'])
            self.edges[edge_id] = edge


def example_graph():
    nodes = {
        'substrate-1': {
            'attributes': {'mass': 1.1}},
        'substrate-2': {
            'attributes': {'mass': 33.3}},
        'product-1': {
            'attributes': {'mass': 9.9}},
        'product-2': {
            'attributes': {'mass': 13}},
        'Enzyme': {
            'attributes': {'mass': 44}}}

    edges = {
        'Reaction': {
            'ports': {
                'substrates': ['substrate-1', 'substrate-2'],
                'products': ['product-1', 'product-2'],
                'enzymes': ['Enzyme']},
            'attributes': {
                'rate': 0.01}}}

    return {
        'nodes': nodes,
        'edges': edges}


def test_example():
    example = example_graph()
    print('substrates are!')
    print(example['edges']['Reaction']['ports']['substrates'])

    graph = Graph(
        example['nodes'],
        example['edges'])

    print(graph.edges)

    import ipdb; ipdb.set_trace()


if __name__ == '__main__':
    test_example()
    
