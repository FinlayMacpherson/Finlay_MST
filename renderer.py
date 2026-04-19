# --- Finlay Macpherson --- Data Structures and Algorithms Assessment ---
#Takes the final edges and points and renders them as a visual graph using SVG graphics

import matplotlib.pyplot as plt

class SVGRenderer:
    def __init__(self, edges):
        self.edges = edges