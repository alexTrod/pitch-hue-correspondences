#!/usr/bin/env python3
"""Add missing pitch/key-to-colour sources from Spence & Di Stefano 2022 to phase1_collected_mappings.json."""
import json
import math
import sys
from pathlib import Path

# Reuse LAB conversion from hex_to_lab
sys.path.insert(0, str(Path(__file__).resolve().parent))
from hex_to_lab import hex_to_rgb, hex_to_lab

PITCH_CLASSES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
FREQ_HZ = {
    "C": 261.63, "C#": 277.18, "D": 293.66, "D#": 311.13, "E": 329.63, "F": 349.23,
    "F#": 369.99, "G": 392.00, "G#": 415.30, "A": 440.00, "A#": 466.16, "B": 493.88,
}


def hex_to_hsv(hex_str):
    r, g, b = (x / 255.0 for x in (int(hex_str[i:i+2], 16) for i in (1, 3, 5)))
    mx, mn = max(r, g, b), min(r, g, b)
    d = mx - mn
    v = round(mx * 100)
    s = round((d / mx * 100) if mx else 0)
    if d == 0:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / d) + 360) % 360
    elif mx == g:
        h = 60 * ((b - r) / d) + 120
    else:
        h = 60 * ((r - g) / d) + 240
    return round(h), s, v


def make_mapping(source_id, source_name, source_type, source_year, source_ref,
                 pitch_class, desc, rgb_hex, completeness="complete", confidence="medium",
                 context="", notes=""):
    lab = hex_to_lab(rgb_hex)
    h, s, v = hex_to_hsv(rgb_hex)
    return {
        "source_id": source_id,
        "source_name": source_name,
        "source_type": source_type,
        "source_year": source_year,
        "source_reference": source_ref,
        "pitch_class": pitch_class,
        "note_frequency_hz": FREQ_HZ[pitch_class],
        "color_assignment": {
            "original_description": desc,
            "original_color_space": "named",
            "lab": {
                "L": lab["L"], "a": lab["a"], "b": lab["b"],
                "notes": "Converted from sRGB " + rgb_hex + " via CIE XYZ D65"
            },
            "rgb_hex": rgb_hex,
            "hue_degree": h,
            "saturation_percent": s,
            "brightness_percent": v
        },
        "data_completeness": completeness,
        "confidence_in_mapping": confidence,
        "additional_context": context,
        "notes": notes
    }


def hue_to_hex(hue_deg, sat=100, val=100):
    """Approximate sRGB hex from HSV (H 0-360, S/V 0-100)."""
    c = (val / 100) * (sat / 100)
    x = c * (1 - abs((hue_deg / 60) % 2 - 1))
    m = (val / 100) - c
    if hue_deg < 60:
        r, g, b = c, x, 0
    elif hue_deg < 120:
        r, g, b = x, c, 0
    elif hue_deg < 180:
        r, g, b = 0, c, x
    elif hue_deg < 240:
        r, g, b = 0, x, c
    elif hue_deg < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    r = round((r + m) * 255)
    g = round((g + m) * 255)
    b = round((b + m) * 255)
    return "#{:02x}{:02x}{:02x}".format(min(255, r), min(255, g), min(255, b))


# --- New sources: list of (pitch_class, original_description, rgb_hex) ---

HELMHOLTZ_1867 = [
    ("G", "Red", "#e61919"),
    ("G#", "Red", "#e61919"),
    ("A", "Red", "#e61919"),
    ("A#", "Orange-red", "#ff4500"),
    ("B", "Orange", "#ff8c00"),
    ("C", "Yellow", "#ffd700"),
    ("C#", "Green", "#228b22"),
    ("D", "Greenish-blue", "#008b8b"),
    ("D#", "Cyanogen-blue", "#00bfff"),
    ("E", "Indigo-blue", "#4b0082"),
    ("F", "Violet", "#8b008b"),
    ("F#", "Ultra-violet", "#4b0082"),
]

FIELD_1835 = [
    ("C", "Red (low)", "#b22222"),
    ("C#", "Orange-red", "#ff4500"),
    ("D", "Orange", "#ff8c00"),
    ("D#", "Yellow", "#ffd700"),
    ("E", "Yellow-green", "#9acd32"),
    ("F", "Green", "#228b22"),
    ("F#", "Cyan-green", "#20b2aa"),
    ("G", "Blue", "#1e90ff"),
    ("G#", "Blue", "#1e90ff"),
    ("A", "Indigo", "#4b0082"),
    ("A#", "Violet", "#8b008b"),
    ("B", "Violet (high)", "#8b008b"),
]

FINN_1881 = [
    ("C", "Red", "#dc143c"),
    ("C#", "Sea green / blue-green", "#2e8b57"),
    ("D", "Orange", "#ff8c00"),
    ("D#", "Olive / yellow-green", "#808000"),
    ("E", "Yellow-green", "#9acd32"),
    ("F", "Green", "#228b22"),
    ("F#", "Orange", "#ff8c00"),
    ("G", "Turquoise blue", "#40e0d0"),
    ("G#", "Crimson", "#dc143c"),
    ("A", "Indigo", "#4b0082"),
    ("A#", "Agate / blue-violet", "#8a2be2"),
    ("B", "Purple", "#800080"),
]

LIND_1900 = [
    ("C", "Red", "#cd0000"),
    ("C#", "Red-orange", "#ff4500"),
    ("D", "Orange", "#ff8c00"),
    ("D#", "Orange-yellow", "#daa520"),
    ("E", "Yellow", "#ffd700"),
    ("F", "Green", "#228b22"),
    ("F#", "Green-blue", "#20b2aa"),
    ("G", "Blue", "#1e90ff"),
    ("G#", "Blue-indigo", "#4169e1"),
    ("A", "Indigo", "#4b0082"),
    ("A#", "Indigo-violet", "#6a5acd"),
    ("B", "Violet", "#8b008b"),
]

MARYON_C1920 = [
    ("C", "Red", "#dc143c"),
    ("C#", "Red-orange", "#ff4500"),
    ("D", "Orange", "#ff8c00"),
    ("D#", "Orange-yellow", "#daa520"),
    ("E", "Yellow", "#ffd700"),
    ("F", "Yellow-green", "#9acd32"),
    ("F#", "Green", "#228b22"),
    ("G", "Blue-green", "#008b8b"),
    ("G#", "Blue", "#1e90ff"),
    ("A", "Blue-violet", "#8a2be2"),
    ("A#", "Violet", "#8b008b"),
    ("B", "Violet-red", "#c71585"),
]

RIMSKY_KORSAKOV = [
    ("C", "White", "#ffffff"),
    ("C#", "Darkish warm", "#8b4513"),
    ("D", "Yellowish", "#ffd700"),
    ("D#", "Grey-bluish", "#708090"),
    ("E", "Blue / sapphire", "#191970"),
    ("F", "Green", "#228b22"),
    ("F#", "Greyish-green", "#556b2f"),
    ("G", "Brownish-gold", "#daa520"),
    ("G#", "Greyish-violet", "#9370db"),
    ("A", "Pink", "#ffc0cb"),
    ("A#", "Darkish", "#2f2f2f"),
    ("B", "Dark blue", "#00008b"),
]

# Wells 1980: 12 hues, C=0 red, tritone opposite
WELLS_1980 = [
    (pc, f"Hue {i * 30}°", hue_to_hex(i * 30))
    for i, pc in enumerate(PITCH_CLASSES)
]

# Pridmore 1992: C = Cyan (180°), so C#=210, ... F#=0, ...
PRIDMORE_1992 = [
    (pc, f"Hue {(180 + i * 30) % 360}°", hue_to_hex((180 + i * 30) % 360))
    for i, pc in enumerate(PITCH_CLASSES)
]

SOURCES = [
    ("helmholtz_1867", "Hermann von Helmholtz", "scientist/theorist", 1867,
     "Helmholtz, H. (1867). Handbuch der physiologischen Optik; pitch–spectrum mapping (Spence & Di Stefano 2022).",
     HELMHOLTZ_1867, "complete", "high", "", "Spectrum: G/A red to f violet, g–b ultra-violet."),
    ("field_1835", "Field", "theorist", 1835,
     "Field, G. (1835). Chromatics; colour–music (Spence & Di Stefano 2022 Fig. 2).",
     FIELD_1835, "inferred", "low", "General low-to-high = dark-to-light; spectrum inferred.", "No explicit note table; inferred from description."),
    ("finn_1881", "Finn", "theorist", 1881,
     "Finn, H. (1881). Chromatic scale–colour table (Spence & Di Stefano 2022 Table 2).",
     FINN_1881, "complete", "high", "", ""),
    ("lind_1900", "Lind", "theorist", 1900,
     "Lind, R. (1900). Pitch (Hz) to light frequency; C red 476×10^8 Hz (Spence & Di Stefano 2022).",
     LIND_1900, "complete", "medium", "Diatonic from paper; chromatics interpolated.", "Lind gave diatonic C–B; chromatics inferred."),
    ("maryon_c1920", "Maryon", "theorist", 1920,
     "Maryon, E. (c.1920). Chromatic scale–colour (Spence & Di Stefano 2022 Table 2).",
     MARYON_C1920, "complete", "high", "", ""),
    ("rimsky_korsakov", "Rimsky-Korsakov", "composer/theorist", 1900,
     "Rimsky-Korsakov; key–colour (Spence & Di Stefano 2022 Table 5). Major keys to colours.",
     RIMSKY_KORSAKOV, "complete", "high", "Key-to-colour; pitch_class = key tonic.", "Encoded as tonic pitch class."),
    ("wells_1980", "Wells", "theorist", 1980,
     "Wells, A. (1980). 12 half-steps to 12 hues; complementarity/tritone (Spence & Di Stefano 2022).",
     WELLS_1980, "complete", "medium", "Structural hue circle; C=0° red.", ""),
    ("pridmore_1992", "Pridmore", "theorist", 1992,
     "Pridmore, R.W. (1992). Octave cycle = hue cycle; C = cyan (Spence & Di Stefano 2022). Transducer for deaf.",
     PRIDMORE_1992, "complete", "medium", "C = cyan (180°); structural.", ""),
]


def main():
    base = Path(__file__).resolve().parent
    path = base / "phase1_collected_mappings.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    existing = len(data)

    for sid, sname, stype, year, ref, rows, compl, conf, ctx, nts in SOURCES:
        for pitch_class, desc, hex_val in rows:
            entry = make_mapping(
                sid, sname, stype, year, ref,
                pitch_class, desc, hex_val,
                completeness=compl, confidence=conf, context=ctx, notes=nts
            )
            data.append(entry)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Added {len(data) - existing} mappings ({existing} -> {len(data)} total).")


if __name__ == "__main__":
    main()
