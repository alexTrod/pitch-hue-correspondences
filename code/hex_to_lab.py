#!/usr/bin/env python3
"""Convert sRGB hex to CIE LAB (D65). Used to populate phase1_collected_mappings.json."""
import json, math, sys

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def lin(v):
    return v / 12.92 if v <= 0.04045 else math.pow((v + 0.055) / 1.055, 2.4)

def rgb_to_xyz(r, g, b):
    r, g, b = lin(r), lin(g), lin(b)
    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041
    return x, y, z

def f(t):
    return math.pow(t, 1/3) if t > 0.008856 else (7.787 * t) + 16/116

def xyz_to_lab(x, y, z):
    xn, yn, zn = 0.95047, 1.0, 1.08883
    L = 116 * f(y / yn) - 16
    a = 500 * (f(x / xn) - f(y / yn))
    b = 200 * (f(y / yn) - f(z / zn))
    return round(L, 1), round(a, 1), round(b, 1)

def hex_to_lab(hex_str):
    r, g, b = hex_to_rgb(hex_str)
    x, y, z = rgb_to_xyz(r, g, b)
    L, a, b_val = xyz_to_lab(x, y, z)
    return {"L": L, "a": a, "b": b_val}

if __name__ == "__main__":
    for hex_str in sys.argv[1:]:
        lab = hex_to_lab(hex_str)
        print(json.dumps(lab))
