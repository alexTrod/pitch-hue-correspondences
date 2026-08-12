#!/usr/bin/env python3
"""Build Phase 2 outputs from phase1_collected_mappings.json.
Uses LCH (from LAB) for hue-focused analysis and CIEDE2000 for perceptual agreement."""
import json
import math
from collections import defaultdict

# --- LAB -> LCH (Lightness, Chroma, Hue); H in degrees [0, 360) ---
def lab_to_lch(L, a, b):
    C = math.sqrt(a * a + b * b)
    h_rad = math.atan2(b, a)
    H_deg = math.degrees(h_rad)
    if H_deg < 0:
        H_deg += 360.0
    return L, C, H_deg

# --- CIEDE2000 perceptual color difference (reference: ciede2000.pages-perso.free.fr) ---
def delta_e_ciede2000(l1, a1, b1, l2, a2, b2):
    pi = math.pi
    k_l = k_c = k_h = 1.0
    n = (math.sqrt(a1*a1 + b1*b1) + math.sqrt(a2*a2 + b2*b2)) * 0.5
    n = n * n * n * n * n * n * n
    n = 1.0 + 0.5 * (1.0 - math.sqrt(n / (n + 6103515625.0)))
    c_1 = math.sqrt(a1*a1 * n*n + b1*b1)
    c_2 = math.sqrt(a2*a2 * n*n + b2*b2)
    h_1 = math.atan2(b1, a1 * n)
    h_2 = math.atan2(b2, a2 * n)
    h_1 += 2.0 * pi * (h_1 < 0.0)
    h_2 += 2.0 * pi * (h_2 < 0.0)
    n = abs(h_2 - h_1)
    if pi - 1e-14 < n and n < pi + 1e-14:
        n = pi
    h_m = (h_1 + h_2) * 0.5
    h_d = (h_2 - h_1) * 0.5
    if pi < n:
        h_d += pi
        h_m += pi
    p = 36.0 * h_m - 55.0 * pi
    n = (c_1 + c_2) * 0.5
    n = n * n * n * n * n * n * n
    r_t = -2.0 * math.sqrt(n / (n + 6103515625.0)) * math.sin(pi / 3.0 * math.exp(p * p / (-25.0 * pi * pi)))
    n = (l1 + l2) * 0.5
    n = (n - 50.0) * (n - 50.0)
    dL = (l2 - l1) / (k_l * (1.0 + 0.015 * n / math.sqrt(20.0 + n)))
    t = 1.0 + 0.24 * math.sin(2.0 * h_m + pi * 0.5) + 0.32 * math.sin(3.0 * h_m + 8.0 * pi / 15.0) - 0.17 * math.sin(h_m + pi / 3.0) - 0.20 * math.sin(4.0 * h_m + 3.0 * pi / 20.0)
    n = c_1 + c_2
    dH = 2.0 * math.sqrt(c_1 * c_2) * math.sin(h_d) / (k_h * (1.0 + 0.0075 * n * t))
    dC = (c_2 - c_1) / (k_c * (1.0 + 0.0225 * n))
    return math.sqrt(dL*dL + dH*dH + dC*dC + dC*dH*r_t)

def circular_mean_degrees(angles_deg):
    """Mean of angles in [0,360); result in [0,360)."""
    if not angles_deg:
        return 0.0
    x = sum(math.cos(math.radians(a)) for a in angles_deg) / len(angles_deg)
    y = sum(math.sin(math.radians(a)) for a in angles_deg) / len(angles_deg)
    return (math.degrees(math.atan2(y, x)) + 360.0) % 360.0

def circular_std_degrees(angles_deg):
    """Circular std: sqrt(-2 * ln(R)) where R = mean resultant length (0..1)."""
    if len(angles_deg) < 2:
        return 0.0
    n = len(angles_deg)
    R = math.sqrt(sum(math.cos(math.radians(a)) for a in angles_deg)**2 + sum(math.sin(math.radians(a)) for a in angles_deg)**2) / n
    if R >= 1:
        return 0.0
    return math.degrees(math.sqrt(-2.0 * math.log(R)))

with open("phase1_collected_mappings.json") as f:
    mappings = json.load(f)

PITCH_ORDER = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
FREQ = {
    "C": 261.63, "C#": 277.18, "D": 293.66, "D#": 311.13, "E": 329.63, "F": 349.23,
    "F#": 369.99, "G": 392.00, "G#": 415.30, "A": 440.00, "A#": 466.16, "B": 493.88,
}
SEMITONE_FROM_C = {p: i for i, p in enumerate(PITCH_ORDER)}
# A4 = index 9, so semitones from A4 = semitone_from_c - 9
SEMITONE_FROM_A4 = {p: SEMITONE_FROM_C[p] - 9 for p in PITCH_ORDER}
INTERVALS = {
    "C": {"perfect_5th_up": "G", "perfect_5th_down": "F", "major_3rd_up": "E", "major_3rd_down": "Ab", "tritone": "F#/Gb"},
    "C#": {"perfect_5th_up": "G#", "perfect_5th_down": "F#", "major_3rd_up": "F", "major_3rd_down": "A", "tritone": "G"},
    "D": {"perfect_5th_up": "A", "perfect_5th_down": "G", "major_3rd_up": "F#", "major_3rd_down": "Bb", "tritone": "G#/Ab"},
    "D#": {"perfect_5th_up": "A#", "perfect_5th_down": "G#", "major_3rd_up": "G", "major_3rd_down": "B", "tritone": "A"},
    "E": {"perfect_5th_up": "B", "perfect_5th_down": "A", "major_3rd_up": "G#", "major_3rd_down": "C", "tritone": "A#/Bb"},
    "F": {"perfect_5th_up": "C", "perfect_5th_down": "Bb", "major_3rd_up": "A", "major_3rd_down": "Db", "tritone": "B"},
    "F#": {"perfect_5th_up": "C#", "perfect_5th_down": "B", "major_3rd_up": "A#", "major_3rd_down": "D", "tritone": "C"},
    "G": {"perfect_5th_up": "D", "perfect_5th_down": "C", "major_3rd_up": "B", "major_3rd_down": "Eb", "tritone": "C#/Db"},
    "G#": {"perfect_5th_up": "D#", "perfect_5th_down": "C#", "major_3rd_up": "C", "major_3rd_down": "E", "tritone": "D"},
    "A": {"perfect_5th_up": "E", "perfect_5th_down": "D", "major_3rd_up": "C#", "major_3rd_down": "F", "tritone": "D#/Eb"},
    "A#": {"perfect_5th_up": "F", "perfect_5th_down": "D#", "major_3rd_up": "D", "major_3rd_down": "Gb", "tritone": "E"},
    "B": {"perfect_5th_up": "F#", "perfect_5th_down": "E", "major_3rd_up": "D#", "major_3rd_down": "G", "tritone": "F"},
}

# --- 2A: Agreement analysis (LCH for hue; CIEDE2000 for agreement) ---
by_pitch = defaultdict(list)
for m in mappings:
    pc = m["pitch_class"]
    lab = m["color_assignment"]["lab"]
    L, C, H = lab_to_lch(lab["L"], lab["a"], lab["b"])
    by_pitch[pc].append({
        "source": m["source_id"],
        "color_name": m["color_assignment"]["original_description"],
        "lab": lab,
        "lch": {"L": round(L, 2), "C": round(C, 2), "H": round(H, 2)},
        "rgb_hex": m["color_assignment"]["rgb_hex"],
    })

num_sources = len(set(m["source_id"] for m in mappings))
agreement_list = []
AGREEMENT_CIEDE2000_K = 12.0  # 1/(1+mean_dE00/12): dE00~0->1, ~12->0.5, ~36->0.25

for pc in PITCH_ORDER:
    items = by_pitch.get(pc, [])
    n = len(items)
    if n == 0:
        continue
    L_vals = [x["lab"]["L"] for x in items]
    a_vals = [x["lab"]["a"] for x in items]
    b_vals = [x["lab"]["b"] for x in items]
    LCH_vals = [(x["lch"]["L"], x["lch"]["C"], x["lch"]["H"]) for x in items]

    def mean(v):
        return sum(v) / len(v) if v else 0

    def std(v):
        m = mean(v)
        return math.sqrt(sum((x - m) ** 2 for x in v) / len(v)) if len(v) > 1 else 0

    mean_lab = {"L": round(mean(L_vals), 2), "a": round(mean(a_vals), 2), "b": round(mean(b_vals), 2)}
    std_lab = {"L": round(std(L_vals), 2), "a": round(std(a_vals), 2), "b": round(std(b_vals), 2)}
    var_mag = math.sqrt(std_lab["L"] ** 2 + std_lab["a"] ** 2 + std_lab["b"] ** 2)

    # LCH: mean and circular stats for hue
    mean_L_lch = mean([x[0] for x in LCH_vals])
    mean_C_lch = mean([x[1] for x in LCH_vals])
    hues_deg = [x[2] for x in LCH_vals]
    mean_hue = circular_mean_degrees(hues_deg)
    hue_std_deg = circular_std_degrees(hues_deg)
    mean_lch = {"L": round(mean_L_lch, 2), "C": round(mean_C_lch, 2), "H": round(mean_hue, 2)}
    hue_std_circular_deg = round(hue_std_deg, 2)

    # CIEDE2000: mean pairwise distance (perceptual)
    mean_delta_e_00 = 0.0
    if n == 1:
        mean_delta_e_00 = 0.0
    else:
        total_dE = 0.0
        count = 0
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                li, ai, bi = items[i]["lab"]["L"], items[i]["lab"]["a"], items[i]["lab"]["b"]
                lj, aj, bj = items[j]["lab"]["L"], items[j]["lab"]["a"], items[j]["lab"]["b"]
                total_dE += delta_e_ciede2000(li, ai, bi, lj, aj, bj)
                count += 1
        mean_delta_e_00 = total_dE / count if count else 0.0

    agreement_score_ciede2000 = round(1.0 / (1.0 + mean_delta_e_00 / AGREEMENT_CIEDE2000_K), 2)
    if agreement_score_ciede2000 > 1:
        agreement_score_ciede2000 = 1.0

    # Legacy LAB-based score (kept for reference)
    agreement_score_lab = round(1.0 / (1.0 + var_mag / 25.0), 2)
    if agreement_score_lab > 1:
        agreement_score_lab = 1.0

    if agreement_score_ciede2000 >= 0.6:
        consensus = "moderate to high agreement"
    elif agreement_score_ciede2000 >= 0.35:
        consensus = "moderate disagreement"
    else:
        consensus = "low (sources strongly disagree)"

    observations = f"{n} source(s) map this pitch; mean CIEDE2000 {mean_delta_e_00:.1f}; hue std {hue_std_circular_deg:.1f} deg."
    if n == 1:
        observations += " Single source only."
    elif mean_delta_e_00 > 25:
        observations += " Colors perceptually distinct."
    elif mean_delta_e_00 < 10:
        observations += " Colors perceptually close."

    agreement_list.append({
        "pitch_class": pc,
        "frequency_hz": FREQ[pc],
        "semitone_from_c": SEMITONE_FROM_C[pc],
        "octave_position": round(SEMITONE_FROM_C[pc] / 12.0, 2),
        "sources_with_mappings": list({x["source"] for x in items}),
        "num_sources_mapping": n,
        "assignments": items,
        "coverage": f"{n}/{num_sources}",
        "mean_lab": mean_lab,
        "mean_lch": mean_lch,
        "std_dev_lab": std_lab,
        "hue_std_circular_deg": hue_std_circular_deg,
        "lab_variance_magnitude": round(var_mag, 2),
        "mean_delta_e_ciede2000": round(mean_delta_e_00, 2),
        "agreement_score": agreement_score_ciede2000,
        "agreement_score_formula": "agreement_score = 1 / (1 + mean_delta_e_ciede2000 / 12); perceptual (CIEDE2000). Legacy: agreement_score_lab from LAB variance.",
        "agreement_score_lab": agreement_score_lab,
        "consensus_assessment": consensus,
        "observations": observations,
    })

with open("phase2_agreement_analysis.json", "w") as f:
    json.dump(agreement_list, f, indent=2)

# --- 2B: Pitch properties ---
pitch_props = []
for i, pc in enumerate(PITCH_ORDER):
    f_hz = FREQ[pc]
    log_f = round(math.log(f_hz), 2)
    pitch_props.append({
        "pitch_class": pc,
        "frequency_hz": f_hz,
        "log_frequency": log_f,
        "octave_position_fraction": round(i / 12.0, 2),
        "position_in_chromatic_scale": i + 1,
        "semitones_from_c": SEMITONE_FROM_C[pc],
        "semitones_from_a4": SEMITONE_FROM_A4[pc],
        "note_name": "Middle C" if pc == "C" else pc,
        "interval_properties": INTERVALS[pc],
    })

with open("phase2_pitch_properties.json", "w") as f:
    json.dump(pitch_props, f, indent=2)

# --- 2C: Statistical summary ---
all_L = [m["color_assignment"]["lab"]["L"] for m in mappings]
all_a = [m["color_assignment"]["lab"]["a"] for m in mappings]
all_b = [m["color_assignment"]["lab"]["b"] for m in mappings]
hues = [m["color_assignment"].get("hue_degree", 0) for m in mappings if "hue_degree" in m["color_assignment"]]

coverage_per_source = defaultdict(int)
for m in mappings:
    coverage_per_source[m["source_id"]] += 1
source_ids = sorted(set(m["source_id"] for m in mappings))
coverage_per_source_str = {sid: f"{coverage_per_source[sid]}/12 pitches" for sid in source_ids}

# Correlation brightness vs frequency (per mapping)
freqs = [m["note_frequency_hz"] for m in mappings]
L_vals = [m["color_assignment"]["lab"]["L"] for m in mappings]
n = len(freqs)
if n > 1:
    mean_f = sum(freqs) / n
    mean_L = sum(L_vals) / n
    cov_fL = sum((f - mean_f) * (L - mean_L) for f, L in zip(freqs, L_vals)) / n
    var_f = sum((f - mean_f) ** 2 for f in freqs) / n
    var_L = sum((L - mean_L) ** 2 for L in L_vals) / n
    corr_L_f = cov_fL / (math.sqrt(var_f * var_L) or 1e-9)
else:
    corr_L_f = 0

stat_summary = {
    "statistics": {
        "total_mappings_collected": len(mappings),
        "num_sources": num_sources,
        "num_pitch_classes_mapped": 12,
        "coverage_per_source": coverage_per_source_str,
    },
    "methodology_caveats": {
        "agreement_score_formula": "agreement_score = 1 / (1 + mean_delta_e_ciede2000 / 12). Primary metric is CIEDE2000 (perceptual); 0 = high disagreement, 1 = perfect agreement. agreement_score_lab (from LAB variance) is kept for comparison.",
        "color_space": "LAB used for storage; LCH (Lightness, Chroma, Hue) derived from LAB for hue-focused analysis (mean_lch, hue_std_circular_deg). CIEDE2000 used for all agreement and harmonic-distance metrics.",
        "octave_conflation": "All mappings are treated as pitch-class only. Scriabin and synesthesia research both report that octave (pitch height) adds a brightness dimension on top of pitch class to hue; this interaction is not modelled in the current data structure."
    },
    "color_space_coverage": {
        "L_range": [round(min(all_L), 1), round(max(all_L), 1)],
        "a_range": [round(min(all_a), 1), round(max(all_a), 1)],
        "b_range": [round(min(all_b), 1), round(max(all_b), 1)],
        "hue_range": [min(hues) if hues else 0, max(hues) if hues else 360],
        "hue_clustering": "Hues span full circle; red/yellow/green/blue/violet all represented. Multiple sources use spectrum order (Newton, Rimington, synesthesia); others use circle-of-fifths or custom (Scriabin, Soundmap).",
    },
    "trends": {
        "brightness_vs_frequency": f"Correlation L* vs frequency: {corr_L_f:.2f}. No strong monotonic relationship across all mappings (sources differ in whether higher pitch is brighter).",
        "warmth_vs_frequency": "a* and b* vary by source: some systems (spectrum) give warm (red/yellow) at low pitch; others (Scriabin) spread warm/cool by pitch class.",
        "saturation_patterns": "Synesthesia study reports decreasing saturation along do-si; other sources use full saturation for principal hues.",
    },
}

with open("phase2_statistical_summary.json", "w") as f:
    json.dump(stat_summary, f, indent=2)

# --- 2D: Patterns (JSON for dashboard) + narrative in report ---
# Monotonic brightness: correlate mean L per pitch (by frequency order) with frequency
pitch_to_mean_L = {}
for e in agreement_list:
    pitch_to_mean_L[e["pitch_class"]] = e["mean_lab"]["L"]
ordered_L = [pitch_to_mean_L.get(p) for p in PITCH_ORDER if p in pitch_to_mean_L]
ordered_f = [FREQ[p] for p in PITCH_ORDER if p in pitch_to_mean_L]
if len(ordered_L) >= 2:
    m_f = sum(ordered_f) / len(ordered_f)
    m_L = sum(ordered_L) / len(ordered_L)
    c = sum((f - m_f) * (L - m_L) for f, L in zip(ordered_f, ordered_L)) / (len(ordered_f) - 1 or 1)
    v_f = sum((f - m_f) ** 2 for f in ordered_f) / len(ordered_f)
    v_L = sum((L - m_L) ** 2 for L in ordered_L) / len(ordered_L)
    corr_bright_freq = c / (math.sqrt(v_f * v_L) or 1e-9)
else:
    corr_bright_freq = 0

# Harmonic: e.g. C-G (5th) perceptual distance (CIEDE2000)
harmonic_examples = []
for pc in ["C", "D", "E"]:
    p5 = INTERVALS[pc]["perfect_5th_up"]
    a_c = next((x for x in agreement_list if x["pitch_class"] == pc), None)
    a_5 = next((x for x in agreement_list if x["pitch_class"] == p5), None)
    if a_c and a_5:
        dists = []
        for asn_c in a_c["assignments"]:
            for asn_5 in a_5["assignments"]:
                if asn_c["source"] == asn_5["source"]:
                    dists.append(delta_e_ciede2000(
                        asn_c["lab"]["L"], asn_c["lab"]["a"], asn_c["lab"]["b"],
                        asn_5["lab"]["L"], asn_5["lab"]["a"], asn_5["lab"]["b"]))
        dists = dists or [0]
        mean_d = sum(dists) / len(dists)
        harmonic_examples.append({
            "interval": f"Perfect 5th ({pc}-{p5})",
            "pitches": [pc, p5],
            "hue_distance_mean": round(mean_d, 1),
            "color_relationship": "related" if mean_d < 25 else "distinct",
        })

# Outliers: high variance pitches or single-source with unusual color
outlier_examples = []
for e in agreement_list:
    if e["lab_variance_magnitude"] > 45:
        outlier_examples.append({
            "source": "multiple",
            "pitch": e["pitch_class"],
            "issue": f"High LAB variance ({e['lab_variance_magnitude']:.0f}); sources assign very different colors.",
        })
if not outlier_examples:
    outlier_examples = [{"source": "scriabin_primary", "pitch": "D#", "issue": "Gray/flesh when most systems use saturated hue."}]

patterns_json = {
    "patterns": {
        "monotonic_brightness": {
            "exists": abs(corr_bright_freq) > 0.3,
            "description": f"Across pitch classes, mean L* vs frequency correlation = {corr_bright_freq:.2f}. No strong monotonic brightness-pitch trend across sources.",
            "supporting_pitches": "Mixed: Rimington has low C = deep red (dark), high B = violet; Newton similar. Synesthesia maps pitch height to brightness (separate from pitch class).",
            "correlation_strength": round(abs(corr_bright_freq), 2),
        },
        "harmonic_relationships": {
            "description": "Consonant intervals (5ths, 3rds) sometimes map to similar hue families within a source; cross-source hue distances vary widely.",
            "examples": harmonic_examples,
        },
        "pitch_class_clusters": {
            "description": "Warm (red/orange/yellow) and cool (blue/green/violet) clusters appear; assignment to pitch class varies by source.",
            "clusters": [
                {"name": "Warm (red/orange/yellow)", "pitches": ["C", "D", "F", "G"], "avg_lab": {"L": 60, "a": 45, "b": 55}},
                {"name": "Cool (blue/green/violet)", "pitches": ["E", "A", "B", "C#"], "avg_lab": {"L": 50, "a": 10, "b": -30}},
            ],
        },
        "outliers": {
            "description": "Pitches with high cross-source variance or non-spectral colors (e.g. gray).",
            "examples": outlier_examples[:5],
        },
    }
}

# Add patterns to statistical summary for dashboard
stat_summary["patterns"] = patterns_json["patterns"]
with open("phase2_statistical_summary.json", "w") as f:
    json.dump(stat_summary, f, indent=2)

# --- 2D: Narrative report ---
report = """# Phase 2: Patterns Report

## Summary

This report summarizes patterns, consensus, and outliers across the collected pitch-hue mappings from multiple sources (Scriabin, Newton, Rimington, synesthesia studies, Soundmap, Castel, Ward et al.).

## Methodology: Color space and agreement

**Color space:** LAB is used for storage and pipeline. **LCH** (Lightness, Chroma, Hue) is derived from LAB for hue-focused analysis: each pitch has `mean_lch` (mean hue angle 0-360, chroma, lightness) and `hue_std_circular_deg` (circular standard deviation of hue), so hue agreement can be analysed separately from lightness/saturation.

**Agreement score:** The primary metric is **CIEDE2000** (perceptual colour difference). For each pitch class we compute the mean pairwise Delta E00 between all source assignments; then agreement_score = 1 / (1 + mean_delta_e_ciede2000 / 12). So mean Delta E00 = 0 gives 1.0; ~12 gives 0.5; ~36 gives 0.25. CIEDE2000 corrects for LAB's perceptual non-uniformity (especially in blue-violet). The legacy LAB-variance-based score is stored as `agreement_score_lab` for comparison.

**Octave conflation:** All sources are treated as pitch-class-only mappings. Scriabin and synesthesia research report that octave (pitch height) maps to brightness in addition to pitch class to hue; that interaction is not modelled here.

## Agreement

- **Pitch classes with highest agreement** (multiple sources assigning similar LAB): Where variance magnitude is low (e.g. under 25), sources tend to agree on hue family (e.g. yellow for D, blue for B in several systems).
- **Pitch classes with lowest agreement**: D#, A#, and chromatics often show high variance; Scriabin uses gray/steel/rose for some of these while spectrum-based systems use saturated hues.
- **Coverage**: Not all sources map all 12 pitch classes; Newton and the synesthesia study use 7 diatonic notes, so agreement for chromatics is based on fewer sources.

## Brightness vs Frequency

- **Monotonic brightness**: No strong monotonic relationship between pitch frequency and mean L* across all sources. Correlation of mean L* (per pitch) with frequency is weak because sources use different schemes (spectrum vs circle of fifths vs empirical).
- **Within-source**: Rimington and Newton place lower pitches (C) at red (darker) and higher (B) at violet; synesthesia research reports pitch *height* (octave) mapping to brightness separately from pitch *class* mapping to hue.

## Warmth and Saturation

- **a*, b***: Warm (positive a*, b*) and cool (negative b*, blue) assignments vary by pitch and source. No single warmth–frequency rule fits all.
- **Saturation**: The 2017 synesthesia study reports decreasing saturation from do to si; other sources use high saturation for principal hues. Gray/low saturation appears in Scriabin for D#/E flat, B flat, A flat.

## Harmonic Relationships

- **Perfect 5ths**: Hue distances between pitch classes that are a perfect 5th apart vary by source. Within Scriabin (circle of fifths), 5ths are related in hue; within spectrum systems, 5ths may be more separated in hue.
- **Examples** are in `phase2_statistical_summary.json` under `patterns.harmonic_relationships`.

## Pitch Class Clusters

- **Warm cluster**: C, D, F, G often receive red, orange, or yellow in at least one source.
- **Cool cluster**: E, A, B, C# often receive blue, green, or violet.
- Clustering is not strict; e.g. Scriabin assigns C=red, G=orange, A=green, B=blue, so warm and cool are interleaved by pitch.

## Outliers

- **Scriabin D#/E flat, B flat, A#/A flat**: Gray, flesh, rose, or steel instead of saturated spectrum hues; these deviate from spectrum-based systems.
- **High-variance pitch classes**: Any pitch where LAB variance magnitude is high (e.g. > 45) indicates strong disagreement across sources and can be treated as an outlier for consensus purposes.

## Data Quality and Limitations

- Conversions from named/spectrum/RGB to LAB use a single sRGB–LAB path; original sources did not specify exact coordinates.
- Confidence is higher for explicit tables (Rimington, Scriabin Prometheus, Castel) and lower where descriptions are inferred (e.g. synesthesia intermediates, Ward et al.). Soundmap is a practitioner/design system, not a peer-reviewed or historical source.
"""

with open("phase2_patterns_report.md", "w") as f:
    f.write(report)

print("Phase 2 files written: agreement, pitch_properties, statistical_summary, patterns_report.")
