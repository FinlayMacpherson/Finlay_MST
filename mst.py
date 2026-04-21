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
        Nodes = list({tuple(p) for _, P1, P2 in Self.Edges for p in (P1, P2)})
        Parent = {n: n for n in Nodes}
        Rank = {n:0 for n in Nodes}
        MST = []

        for Weight, P1, P2 in Self.Edges:
            if Self.Find(Parent, tuple(P1)) != Self.Find(Parent, tuple(P2)):
                MST.append(Weight)
                Self.Union(Parent, Rank, tuple(P1), tuple(P2))
                MST.append((Weight, P1, P2))

        return MST
