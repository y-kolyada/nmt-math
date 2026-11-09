"""A bar chart with a value axis, shared by the chart figures of block 2."""


def bars(f, names, values, lo, hi, step, x0=50, y0=14, w=250, h=160, broken=False):
    """Bars from lo to their value on an axis lo..hi labelled every step. Returns the bar tops."""
    py = lambda v: y0 + h - (v - lo) / (hi - lo) * h
    for v in range(lo, hi + 1, step):
        f.line(x0, py(v), x0 + w, py(v), w=0.8, op=0.25)
        f.text(x0 - 8, py(v) + 4, str(v), size=12, anchor='end', op=0.85)
    f.line(x0, y0 + h, x0 + w, y0 + h, w=1.2)
    f.line(x0, y0 - 4, x0, y0 + h, w=1.2)
    if broken:
        # a zigzag on the axis: it does not start at zero
        z = y0 + h + 10
        f.poly([(x0 - 6, z - 2), (x0, z - 6), (x0 + 6, z - 2)], w=1.2)
        f.poly([(x0 - 6, z + 3), (x0, z - 1), (x0 + 6, z + 3)], w=1.2)
    n = len(values)
    slot = w / n
    tops = []
    for i, (name, v) in enumerate(zip(names, values)):
        x = x0 + slot * i + slot * 0.2
        f.rect(x, py(v), slot * 0.6, py(lo) - py(v), rx=2, fill_op=0.25, accent=True, sw=1.2)
        f.text(x + slot * 0.3, y0 + h + (30 if broken else 18), name, size=12, anchor='middle')
        tops.append((x + slot * 0.3, py(v)))
    return tops
