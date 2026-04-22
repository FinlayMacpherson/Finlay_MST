# --- Finlay Macpherson --- Data Structures and Algorithms Assessment ---


import numpy as np
from graph import Graph
from mst import KruskalMST
from renderer import render_svg

def main():
    g = Graph()

    for Point in np.loadtxt("points.csv", delimiter=","):
        g.AddPoints(Point)

    Edges = g.GetEdges()

    MST = KruskalMST(Edges).Compute()

    render_svg(MST).Render("output.svg")

    print(f"MST computed with {len(MST)} edges. Saved to output.svg.")

if __name__ == "__main__":
    main()