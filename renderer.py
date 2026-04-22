# --- Finlay Macpherson --- Data Structures and Algorithms Assessment ---
#Takes the final edges and points and renders them as a visual graph using SVG graphics


class SVGRenderer:  # ✅ Use 'class', not 'def'
    def __init__(self, Edges):  # ✅ Indented under class
        self.edges = Edges

    def Render(self, filename="output.svg"):  # ✅ Indented under class
        svg_content = ['<svg xmlns="http://www.w3.org/2000/svg" width="500" height="500">']

        def to_coords(p):
            if hasattr(p, '__iter__'):  # Check if it's iterable (array or list)
                return list(p)
            return p

            # Draw lines

        for Weight, p1, p2 in self.edges:
            # Convert to list to ensure we can index them
            c1 = to_coords(p1)
            c2 = to_coords(p2)

            x1, y1 = c1[0], c1[1]
            x2, y2 = c2[0], c2[1]

            svg_content.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="blue" stroke-width="2" />')

            # Draw points
        points = set()
        for _, p1, p2 in self.edges:
            c1 = to_coords(p1)
            c2 = to_coords(p2)
            # Convert to tuple for the set (lists are not hashable)
            points.add(tuple(c1))
            points.add(tuple(c2))

        for x, y in points:
            svg_content.append(f'<circle cx="{x}" cy="{y}" r="4" fill="red" />')

        svg_content.append('</svg>')

        with open(filename, 'w') as f:
            f.write('\n'.join(svg_content))

        print(f"SVG saved to {filename} with {len(points)} points.")