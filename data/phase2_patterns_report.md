# Phase 2: Patterns Report

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
