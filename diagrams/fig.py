"""Shared drawing helpers for the figures of nmt-math.

Every figure is a module NN-name.py with figure(lang) -> (Fig, label, caption).
Coordinates of mathematical figures are computed from the formula the page
states, never placed by eye. Series rules (AGENTS.md rule 18): a canvas 320
units wide, labels of at least 12 units, colour from currentColor so the
figure follows the day/night theme; the accent uses the page variable --acc.
"""
import html
import math

W = 320


def esc(s):
    return html.escape(str(s), quote=True)


class Fig:
    def __init__(self, h):
        self.h = h
        self.parts = []

    def add(self, s):
        self.parts.append(s)

    def line(self, x1, y1, x2, y2, w=1.4, dash=None, op=1.0, accent=False):
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        st = ' style="stroke:var(--acc)"' if accent else ''
        self.add('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="currentColor" stroke-width="%s"%s opacity="%s"%s/>'
                 % (x1, y1, x2, y2, w, d, op, st))

    def arrow(self, x1, y1, x2, y2, w=1.4, accent=False, head=7):
        self.line(x1, y1, x2, y2, w, accent=accent)
        a = math.atan2(y2 - y1, x2 - x1)
        p1 = (x2 - head * math.cos(a - 0.4), y2 - head * math.sin(a - 0.4))
        p2 = (x2 - head * math.cos(a + 0.4), y2 - head * math.sin(a + 0.4))
        st = ' style="fill:var(--acc)"' if accent else ''
        self.add('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="currentColor"%s/>' % (x2, y2, p1[0], p1[1], p2[0], p2[1], st))

    def poly(self, pts, close=False, w=1.6, fill_op=0.0, accent=False, dash=None, op=1.0):
        tag = 'polygon' if close else 'polyline'
        pts_s = ' '.join('%.1f,%.1f' % p for p in pts)
        fill = 'currentColor' if fill_op else 'none'
        st = ' style="stroke:var(--acc)%s"' % (';fill:var(--acc)' if fill_op else '') if accent else ''
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        self.add('<%s points="%s" fill="%s" fill-opacity="%s" stroke="currentColor" stroke-width="%s"%s opacity="%s"%s/>'
                 % (tag, pts_s, fill, fill_op, w, d, op, st))

    def circle(self, cx, cy, r, w=1.4, fill_op=0.0, dot=False, accent=False, dash=None):
        if dot:
            st = ' style="fill:var(--acc)"' if accent else ''
            self.add('<circle cx="%.1f" cy="%.1f" r="%s" fill="currentColor"%s/>' % (cx, cy, r, st))
            return
        st = ' style="stroke:var(--acc)"' if accent else ''
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        self.add('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="currentColor" fill-opacity="%s" stroke="currentColor" stroke-width="%s"%s%s/>'
                 % (cx, cy, r, fill_op, w, d, st))

    def rect(self, x, y, w, h, rx=6, fill_op=0.05, dash=None, accent=False, sw=1.2):
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        st = ' style="stroke:var(--acc)"' if accent else ''
        self.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%s" fill="currentColor" fill-opacity="%s" stroke="currentColor" stroke-width="%s"%s%s/>'
                 % (x, y, w, h, rx, fill_op, sw, d, st))

    def text(self, x, y, s, size=13, anchor='start', op=1.0, italic=False, bold=False, accent=False):
        extra = ''
        if anchor != 'start':
            extra += ' text-anchor="%s"' % anchor
        if italic:
            extra += ' font-style="italic"'
        if bold:
            extra += ' font-weight="700"'
        st = ' style="fill:var(--acc)"' if accent else ''
        self.add('<text x="%.1f" y="%.1f" fill="currentColor" font-size="%s" opacity="%s"%s%s>%s</text>'
                 % (x, y, size, op, extra, st, esc(s)))

    def svg(self, label):
        return ('<svg viewBox="0 0 %d %d" width="100%%" style="max-width:320px;height:auto;display:block;margin:0 auto" '
                'role="img" aria-label="%s">\n        %s\n      </svg>' % (W, self.h, esc(label), '\n        '.join(self.parts)))


class Plot:
    """A box on the canvas with mathematical coordinates inside it."""

    def __init__(self, fig, x0, y0, w, h, xmin, xmax, ymin, ymax):
        self.f, self.x0, self.y0, self.w, self.h = fig, x0, y0, w, h
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax

    def px(self, x):
        return self.x0 + (x - self.xmin) / (self.xmax - self.xmin) * self.w

    def py(self, y):
        return self.y0 + (self.ymax - y) / (self.ymax - self.ymin) * self.h

    def pt(self, x, y):
        return (self.px(x), self.py(y))

    def axes(self, xlabel='x', ylabel='y', ticks_x=(), ticks_y=()):
        f = self.f
        y_axis = self.px(0) if self.xmin <= 0 <= self.xmax else self.x0
        x_axis = self.py(0) if self.ymin <= 0 <= self.ymax else self.y0 + self.h
        f.arrow(self.x0, x_axis, self.x0 + self.w, x_axis, w=1)
        f.arrow(y_axis, self.y0 + self.h, y_axis, self.y0, w=1)
        f.text(self.x0 + self.w - 4, x_axis + 16, xlabel, size=13, anchor='end', italic=True)
        f.text(y_axis + 8, self.y0 + 12, ylabel, size=13, italic=True)
        for t in ticks_x:
            x = self.px(t)
            f.line(x, x_axis - 3, x, x_axis + 3, w=1)
            f.text(x, x_axis + 16, fmt(t), size=12, anchor='middle', op=0.8)
        for t in ticks_y:
            y = self.py(t)
            f.line(y_axis - 3, y, y_axis + 3, y, w=1)
            f.text(y_axis - 6, y + 4, fmt(t), size=12, anchor='end', op=0.8)

    def curve(self, fn, a, b, n=120, **kw):
        pts = []
        for i in range(n + 1):
            x = a + (b - a) * i / n
            y = fn(x)
            if y is None or not (self.ymin - 1e-9 <= y <= self.ymax + 1e-9):
                if len(pts) > 1:
                    self.f.poly(pts, **kw)
                pts = []
                continue
            pts.append(self.pt(x, y))
        if len(pts) > 1:
            self.f.poly(pts, **kw)


def fmt(v):
    s = ('%g' % v).replace('-', '−')
    return s.replace('.', ',')
