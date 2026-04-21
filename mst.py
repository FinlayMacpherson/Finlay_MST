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
        Nodes = list({p for _, p1, p2 in Self.Edges for p in (p1, p2)})
        Parent = {n: n for n in Nodes}
        Rank = {n:0 for n in Nodes}
        MST = []

        for Weight, p1, p2 in Self.Edges:
            if Self.Find(Parent, p1) != Self.Find(Parent, p2):
                Self.Union(Parent, Rank, p1, p2)
                MST.append((Weight, p1, p2))

        return MST
