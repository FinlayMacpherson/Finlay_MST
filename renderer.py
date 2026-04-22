# --- Finlay Macpherson --- Data Structures and Algorithms Assessment ---
#Takes the final edges and points and renders them as a visual graph using SVG graphics


def render_svg(edges, filename="output.svg"):
    svg_content = ['<svg xmlns="http://www.w3.org/2000/svg" width="500" height="500">']

    # Draw lines
    for Weight, p1, p2 in edges:
        if isinstance(p1, tuple):
            x1, y1 = p1
            x2, y2 = p2
            svg_content.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="blue" />')

    # Draw points
    points = set()
    for _, p1, p2 in edges:
        if isinstance(p1, tuple): points.add(p1)
        if isinstance(p2, tuple): points.add(p2)

    for x, y in points:
        svg_content.append(f'<circle cx="{x}" cy="{y}" r="3" fill="red" />')

    svg_content.append('</svg>')

    with open(filename, 'w') as f:
        f.write('\n'.join(svg_content))
