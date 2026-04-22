# --- Finlay Macpherson --- Data Structures and Algorithms Assessment ---
# implements Kruskal's algorithm to compute the MST

class KruskalMST:
    def __init__(Self, Edges):
        Self.Edges = sorted(Edges, key=lambda e: e[0])

    def Find(Self, Parent, Node):
        if Parent[Node] != Node:
            Parent[Node] = Self.Find(Parent, Parent[Node])
        return Parent[Node]

    def Union(Self, Parent, Rank, a, b):
        ra, rb = Self.Find(Parent, a), Self.Find(Parent, b)
        if Rank[ra] < Rank[rb]:
            Parent[ra] = rb
        elif Rank[ra] > Rank[rb]:
            Parent[rb] = ra
        else:
            Parent[rb] = ra
            Rank[ra] += 1

    def Compute(Self):
        Nodes = set()
        for _, P1, P2 in Self.Edges:
            Nodes.add(tuple(P1)) #Converting lists to tuples so they can be added to a set
            Nodes.add(tuple(P2))
        Nodes = list(Nodes)


        Parent = {n: n for n in Nodes}
        Rank = {n:0 for n in Nodes}
        MST = []

        for Weight, P1, P2 in Self.Edges:
            Node1 = tuple(P1)
            Node2 = tuple(P2)

            if Self.Find(Parent, Node1) != Self.Find(Parent, Node2):
                MST.append((Weight, P1, P2))
                Self.Union(Parent, Rank, Node1, Node2)

        return MST
