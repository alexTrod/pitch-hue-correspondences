# Pitch–Hue Correspondences: A Quantitative Corpus Analysis

**Feldman AN, Kuruoglu EE** (2026).  
*Pitch–Hue Correspondences: A Quantitative Corpus Analysis of Three Centuries of Mapping Systems.*  
Submitted to *Attention, Perception, & Psychophysics*.

## Repository contents

| Path | Contents |
|------|----------|
| `data/phase1_collected_mappings.json` | 165 pitch–hue assignments from 15 primary sources, each with CIELAB coordinates |
| `data/pitch_hue_catalogue.json` | Full 70-system catalogue with metadata, family assignments, and retention status |
| `data/family_assignments.json` | Reasoning-family codes (F1–F8) for all 70 catalogue entries |
| `data/phase2_agreement_analysis.json` | Per-pitch-class CIEDE2000 agreement scores |
| `data/phase2_statistical_summary.json` | Global statistics: Rayleigh R, semitone–hue correlation, account summaries |
| `data/phase2_pitch_properties.json` | Frequency and interval properties for all 12 pitch classes |
| `data/phase1_sources_inventory.md` | Source metadata for the 15 primary sources |
| `data/phase2_patterns_report.md` | Narrative summary of Phase 2 analysis patterns |
| `code/hex_to_lab.py` | sRGB → CIE LAB converter (D65 illuminant, CIEDE2000-ready) |
| `code/add_missing_sources.py` | Adds 8 sources from Spence & Di Stefano (2022) to the phase 1 dataset |
| `code/build_phase2.py` | Runs CIEDE2000 agreement analysis, Rayleigh test, family scoring |
| `code/gen_dashboard.py` | Builds the self-contained interactive HTML dashboard |
| `code/dashboard_template.html` | Dashboard template (data injected by gen_dashboard.py) |
| `dashboard.html` | Pre-built interactive visualisation of all data (open in any browser) |
| `figures/tics_submission/` | Six submission-ready figure panels (300 dpi) |
| `figures/source_panels/` | Individual panels before two-panel assembly |
| `figures/families/` | Per-family consensus hue wheels (F1–F8) |
| `paper/` | Manuscript source (.tex, .bib), supplementary material, submission drafts |

## Reproducing the analysis

Requires Python 3.9+ with no external dependencies beyond the standard library.

```bash
# 1. Collect the primary dataset (already present; re-run to regenerate)
python code/add_missing_sources.py

# 2. Run Phase 2 agreement analysis
python code/build_phase2.py

# 3. Build the interactive dashboard
python code/gen_dashboard.py
# Opens dashboard.html in the project root
```

All input data (`data/phase1_collected_mappings.json`) and output files are
committed to this repository; the scripts are provided for full reproducibility.

## Data availability

All data files are in `data/`. The 70 source systems are cited in the paper's
reference list; no raw participant data were collected.

## Citation

> Feldman AN, Kuruoglu EE. Pitch–Hue Correspondences: A Quantitative Corpus
> Analysis of Three Centuries of Mapping Systems. *Attention, Perception, &
> Psychophysics*. 2026 (submitted).

## Licence

Data and code: CC BY 4.0. See [LICENSE](LICENSE).
