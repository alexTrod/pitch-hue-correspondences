# Pitch–Hue Correspondences: A Quantitative Meta-Analysis

**Feldman AN, Kuruoglu EE** (2025).  
*Pitch–Hue Correspondences: A Quantitative Meta-Analysis of Three Centuries of Mapping Systems.*  
Trends in Cognitive Sciences (submitted).

## Repository contents

| Directory | Contents |
|-----------|----------|
| `data/` | Colour catalogue, pairwise CIEDE2000 distance matrices, bootstrap baseline samples |
| `code/` | Analysis scripts (colour standardisation, agreement scoring, family analysis, four theoretical accounts, FDR correction) |
| `figures/tics_submission/` | Figure panels as submitted |
| `paper/` | LaTeX source, supplementary material, TICS submission draft |

## Reproducing the results

```bash
pip install -r code/requirements.txt
python code/01_standardise_colours.py
python code/02_compute_agreement.py
python code/03_family_analysis.py
python code/04_structural_account.py
python code/05_semantic_account.py
python code/06_hedonic_account.py
python code/07_fdr_correction.py
```

## Data availability

Data files (catalogue, distance matrices, bootstrap samples) are in `data/`.  
All 70 source systems are cited in the paper's reference list.

## Citation

If you use this dataset or pipeline, please cite:

> Feldman AN, Kuruoglu EE. Pitch–Hue Correspondences: A Quantitative Meta-Analysis  
> of Three Centuries of Mapping Systems. *Trends in Cognitive Sciences*. 2025 (submitted).

## Licence

Data and code: CC BY 4.0. See [LICENSE](LICENSE).
