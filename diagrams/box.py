"""A rectangular box in an oblique projection, shared by the box figures of block 13."""


def box(f, a, b, c, A=(46, 200), s=18, depth=0.5, names=True):
    """a along AB (to the right), b along AD (into the depth), c along AA1 (up). Returns the vertices."""
    dx, dy = b * s * depth * 0.8, -b * s * depth * 0.6
    A_ = A
    B = (A_[0] + a * s, A_[1])
    D = (A_[0] + dx, A_[1] + dy)
    C = (B[0] + dx, B[1] + dy)
    up = lambda p: (p[0], p[1] - c * s)
    A1, B1, C1, D1 = up(A_), up(B), up(C), up(D)
    for p, q in ((A_, D), (D, C), (D, D1)):
        f.line(*p, *q, w=1.3, dash='5 4', op=0.8)
    for p, q in ((A_, B), (B, C), (A_, A1), (B, B1), (C, C1), (A1, B1), (B1, C1), (C1, D1), (D1, A1)):
        f.line(*p, *q, w=1.8)
    v = {'A': A_, 'B': B, 'C': C, 'D': D, 'A₁': A1, 'B₁': B1, 'C₁': C1, 'D₁': D1}
    if names:
        for name, dxy in (('A', (-14, 14)), ('B', (4, 16)), ('C', (8, 6)), ('D', (-16, -4)),
                          ('A₁', (-22, 0)), ('B₁', (-8, -8)), ('C₁', (8, -2)), ('D₁', (-8, -8))):
            p = v[name]
            f.text(p[0] + dxy[0], p[1] + dxy[1], name, size=14, italic=True)
    return v
