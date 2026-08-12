# Pitch-Hue Crossmodal Mapping Agent Prompt (Phase 1 & 2 + Dashboard)

## Objective
You are a research agent tasked with systematically collecting and analyzing pitch-to-hue mappings for a crossmodal perception thesis. Your goal is to:

1. **Phase 1**: Comprehensively collect all known pitch-hue mappings from established scientists, artists, and researchers
2. **Phase 2**: Extract commonalities and identify patterns across these mappings
3. **Dashboard**: Create an interactive HTML dashboard for exploring the data

**Output: Structured JSON data + an interactive dashboard for exploration and analysis.**

---

## Phase 1: Collect & Codify Existing Mappings

### Task
Search for and extract ALL pitch-hue mappings from credible, well-known sources. The criterion is: the source must be an established scientist, artist, composer, or researcher with documented work.

### Known Sources to Include (but not limited to)
- **Alexander Scriabin** (composer, color-music system)
- **Wassily Kandinsky** (artist, synesthesia principles)
- **Isaac Newton** (spectrum-music analogies)
- **Synesthesia research studies** (peer-reviewed empirical data from multiple sources)
- **Historical color-music theorists** (Babbitt, Zicarelli, Peacock, etc.)
- **Contemporary color-sound mapping research** (recent studies, datasets)
- Any other documented mapping systems you can identify

### Codification Format
For EACH mapping found, codify as follows:

```json
{
  "source_id": "scriabin_primary",
  "source_name": "Alexander Scriabin",
  "source_type": "composer/theorist",
  "source_year": 1911,
  "source_reference": "[Full citation/URL if available]",
  "pitch_class": "C",
  "note_frequency_hz": 261.63,
  "color_assignment": {
    "original_description": "Red",
    "original_color_space": "spectrum/RGB/hue/named",
    "lab": {
      "L": 45,
      "a": 50,
      "b": 30,
      "notes": "Converted from [method]"
    },
    "rgb_hex": "#ff0000",
    "hue_degree": 0,
    "saturation_percent": 100,
    "brightness_percent": 50
  },
  "data_completeness": "complete/partial/inferred",
  "confidence_in_mapping": "high/medium/low",
  "additional_context": "[Any additional info about this mapping]",
  "notes": "Original system described in [specific work]; LAB conversion method: [describe]"
}
```

### Requirements
- **Collect as many sources as possible** (aim for 5-10+ distinct documented systems)
- **For each pitch class** that is mapped in a source, create a separate entry
- **Convert to LAB space** from original color descriptions, documenting your conversion method
- **Flag data quality**: Is the mapping explicit/direct, or inferred from written descriptions?
- **Preserve original context**: Note the original color space, naming, and any qualifications
- **Include frequency data**: For each pitch class, compute the standard frequency (A4=440 Hz)

### Output for Phase 1
- `phase1_collected_mappings.json`: All codified mappings from all sources
- `phase1_sources_inventory.md`: Metadata on each source (name, year, type, completeness, coverage)

---

## Phase 2: Extract Commonalities & Patterns

### Task
Analyze the collected mappings to identify what pitch-hue associations are **consistent** across sources.

### Analysis Components

#### 2A: Pitch-by-Pitch Agreement Analysis
For each pitch class (C, C#, D, ... B), generate:

```json
{
  "pitch_class": "C",
  "frequency_hz": 261.63,
  "semitone_from_c": 0,
  "octave_position": 0.0,
  "sources_with_mappings": ["scriabin_primary", "kandinsky_system", "synesthesia_2020"],
  "num_sources_mapping": 3,
  "assignments": [
    {
      "source": "scriabin_primary",
      "color_name": "Red",
      "lab": {"L": 45, "a": 50, "b": 30},
      "rgb_hex": "#ff0000"
    },
    {
      "source": "kandinsky_system",
      "color_name": "Dark/Black",
      "lab": {"L": 20, "a": 0, "b": 0},
      "rgb_hex": "#000000"
    }
  ],
  "coverage": "50%",
  "mean_lab": {
    "L": 32.5,
    "a": 25,
    "b": 15
  },
  "std_dev_lab": {
    "L": 12.5,
    "a": 25,
    "b": 15
  },
  "lab_variance_magnitude": 23.5,
  "agreement_score": 0.4,
  "consensus_assessment": "low (sources strongly disagree)",
  "observations": "[What patterns or differences do you see across sources?]"
}
```

**Agreement Score**: 0-1 scale based on variance in LAB space (0=high disagreement, 1=perfect agreement)

#### 2B: Pitch Property Analysis
Create a structured file with pitch properties:

```json
{
  "pitch_class": "C",
  "frequency_hz": 261.63,
  "log_frequency": 5.57,
  "octave_position_fraction": 0.0,
  "position_in_chromatic_scale": 0,
  "semitones_from_c": 0,
  "semitones_from_a4": -57,
  "note_name": "Middle C",
  "interval_properties": {
    "perfect_5th_up": "G",
    "perfect_5th_down": "F",
    "major_3rd_up": "E",
    "major_3rd_down": "Ab",
    "tritone": "F#/Gb"
  }
}
```

#### 2C: Aggregate Color Statistics
Compute across all mappings:

```json
{
  "statistics": {
    "total_mappings_collected": 120,
    "num_sources": 8,
    "num_pitch_classes_mapped": 12,
    "coverage_per_source": {
      "scriabin_primary": "12/12 pitches",
      "kandinsky_system": "5/12 pitches",
      "synesthesia_2020": "8/12 pitches"
    }
  },
  "color_space_coverage": {
    "L_range": [20, 85],
    "a_range": [-30, 50],
    "b_range": [-40, 50],
    "hue_range": [0, 360],
    "hue_clustering": "[Identify if hues cluster or distribute evenly]"
  },
  "trends": {
    "brightness_vs_frequency": "[Does L* correlate with pitch frequency? correlation coefficient, direction]",
    "warmth_vs_frequency": "[Does a*, b* show patterns with pitch?]",
    "saturation_patterns": "[Any saturation trends?]"
  }
}
```

#### 2D: Pattern Identification Summary

```json
{
  "patterns": {
    "monotonic_brightness": {
      "exists": true/false,
      "description": "[Does brightness increase/decrease monotonically with pitch?]",
      "supporting_pitches": "[Which pitch pairs support or contradict this?]",
      "correlation_strength": 0.75
    },
    "harmonic_relationships": {
      "description": "[Do consonant intervals map to related hues?]",
      "examples": [
        {
          "interval": "Perfect 5th (C-G)",
          "pitches": ["C", "G"],
          "hue_distance_mean": 45,
          "color_relationship": "somewhat related"
        }
      ]
    },
    "pitch_class_clusters": {
      "description": "[Do pitch classes group into color families?]",
      "clusters": [
        {
          "name": "Warm pitches",
          "pitches": ["C", "F", "G"],
          "avg_lab": {"L": 50, "a": 30, "b": 20}
        }
      ]
    },
    "outliers": {
      "description": "[Which mappings deviate significantly from patterns?]",
      "examples": [
        {
          "source": "kandinsky_system",
          "pitch": "B",
          "issue": "Maps to dark color when frequency suggests bright"
        }
      ]
    }
  }
}
```

### Output for Phase 2
- `phase2_agreement_analysis.json`: Pitch-by-pitch agreement scores and source comparisons
- `phase2_pitch_properties.json`: Sound properties for all 12 pitch classes
- `phase2_statistical_summary.json`: Aggregate color statistics and trends
- `phase2_patterns_report.md`: Narrative summary of patterns, trends, consensus, outliers

---

## Dashboard Generation

### Task
Create an **interactive HTML dashboard** that visualizes all Phase 1 and Phase 2 data. The dashboard should allow the researcher to explore mappings, sources, pitches, and patterns intuitively.

### Dashboard Features

#### 1. **Overview Panel**
- Summary statistics (total mappings, sources, coverage)
- Key patterns identified
- List of all sources with completeness indicators

#### 2. **Source Explorer**
- Browse each source individually
- View all mappings from a source in table format
- Visualize source mappings in color wheel and LAB space
- Compare two sources side-by-side

#### 3. **Pitch Explorer**
- For each pitch class (C-B):
  - Show frequency, interval relationships
  - List all sources that map this pitch
  - Visualize assignments in LAB space (scatter plot)
  - Show mean color and variance
  - Display agreement/confidence score

#### 4. **Mapping Visualizations**
- **Color Wheel**: All mapped colors arranged by hue (one ring per source or aggregated)
- **LAB Space 3D Plot**: All mappings in LAB color space, colored by pitch class
- **Brightness vs Frequency Graph**: Scatter plot of pitch frequency vs. L* value
- **Pitch-Color Grid**: 12x[num_sources] grid showing each pitch's color in each source

#### 5. **Agreement & Patterns Panel**
- **Pitch Agreement Scores**: Bar chart showing agreement/confidence for each pitch class
- **Harmonic Relationship Analysis**: Hue distances between consonant intervals (5ths, 3rds, etc.)
- **Trend Analysis**: Graphs showing brightness trends, warmth patterns, etc.
- **Outlier Identification**: Highlight mappings that deviate from detected patterns

#### 6. **Comparison Tools**
- **Source vs Source**: Compare hue assignments across two sources
- **Pitch vs Pitch**: Compare how different pitch classes are mapped in different sources
- **Pattern Filter**: Highlight mappings that follow/violate detected patterns

#### 7. **Data Export**
- Download JSON files (collected mappings, statistics, patterns)
- Download CSV of all pitch-hue mappings
- Export selected visualizations as images

### Dashboard Technical Requirements
- **Single HTML file** (self-contained, can open in any browser)
- **Interactive elements**: dropdowns, filters, toggles to switch views
- **Color-accurate visualization**: Use LAB to RGB conversion for accurate color display
- **Responsive design**: Works on desktop
- **No external dependencies**: Use vanilla JavaScript or lightweight libraries only (Chart.js, Plotly.js, or similar)

### Dashboard Structure (Suggested)
```
┌─────────────────────────────────────────────────────┐
│  PITCH-HUE MAPPING EXPLORER DASHBOARD               │
├─────────────────────────────────────────────────────┤
│  [Overview] [Source Explorer] [Pitch Explorer]      │
│  [Visualizations] [Patterns] [Compare]              │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [Main Visualization Area]                          │
│                                                     │
│  [Controls/Filters Panel] [Data Panel]              │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Example Data Embedded in Dashboard
- All JSON files (collected_mappings, agreement_analysis, pitch_properties, statistical_summary) embedded as JavaScript data objects
- Dashboard reads from these objects to render visualizations dynamically

---

## Overall Output Structure

### Files to Generate

1. **phase1_collected_mappings.json**
   - All codified mappings from all sources with LAB conversions

2. **phase1_sources_inventory.md**
   - Metadata on each source (name, year, type, completeness, coverage)

3. **phase2_agreement_analysis.json**
   - Pitch-by-pitch agreement scores, mean LAB, variance, source comparisons

4. **phase2_pitch_properties.json**
   - Sound properties (frequency, intervals, position) for all 12 pitch classes

5. **phase2_statistical_summary.json**
   - Aggregate color statistics, color space coverage, trends

6. **phase2_patterns_report.md**
   - Narrative: patterns identified, trends, consensus, outliers, correlations

7. **dashboard.html**
   - Interactive HTML dashboard with all visualizations and controls
   - Embeds all JSON data internally for self-contained exploration
   - Fully self-contained: open dashboard.html in any browser; no server or template file needed. dashboard_template.html is used only to regenerate dashboard.html (run `python3 gen_dashboard.py`).

---

## Key Principles

✅ **Data-driven**: Collect first; analyze patterns without imposing structure  
✅ **Comprehensive**: Collect as many sources as possible  
✅ **Transparent**: Document all conversions, assumptions, and data quality  
✅ **Exploratory**: Let patterns emerge; identify both consensus and disagreement  
✅ **Navigable**: Dashboard enables intuitive exploration without requiring code knowledge  
✅ **Honest**: Flag uncertainties, conflicts, and limitations  

---

## Begin Execution

**Priority order:**
1. **Phase 1**: Conduct thorough search and collection. Codify each mapping carefully with source metadata and LAB conversions. Generate `phase1_collected_mappings.json` and `phase1_sources_inventory.md`.

2. **Phase 2**: Analyze the collected data. For each pitch class, compute agreement scores, mean LAB, variance. Identify patterns and trends. Generate all Phase 2 JSON and markdown outputs.

3. **Dashboard**: Using data from Phase 1 and 2, create a comprehensive interactive HTML dashboard. Embed the JSON data and implement all visualization panels described above.

**Quality checklist:**
- ✅ Phase 1: All mappings codified with source metadata, LAB values, confidence scores, and conversion methods documented
- ✅ Phase 2: Agreement analysis complete; patterns identified with evidence; all statistics computed
- ✅ Dashboard: All panels functional; visualizations accurate; data controls work smoothly