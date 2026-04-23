# --- Finlay Macpherson --- Data Structures and Algorithms Assessment ---
# implements Kruskal's algorithm to compute the MST

class KruskalMST:
    def __init__(Self, Edges):
        # this could have been written out as a full function but a lambda has been used for simplicity
        Self.Edges = sorted(Edges, key=lambda e: e[0])


    def Find(Self, Parent, Node):
        #Walks up the tree until it finds the parent node
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

        #This section initalises the parents for each node
        #Then initalises the ranks of each tree by height
        #then creates a list to store the edges of the tree
        Parent = {n: n for n in Nodes}
        Rank = {n:0 for n in Nodes}
        MST = []

        #Iterates through the edges to check weights
        for Weight, P1, P2 in Self.Edges:
            Node1 = tuple(P1)
            Node2 = tuple(P2)

            #Check if nodes belong to different sets
            if Self.Find(Parent, Node1) != Self.Find(Parent, Node2):
                MST.append((Weight, P1, P2)) #Add edges to MST as it connects 2 previously disconnected components
                Self.Union(Parent, Rank, Node1, Node2) #Merges the two sets containing Node1 and Node2

        return MST
