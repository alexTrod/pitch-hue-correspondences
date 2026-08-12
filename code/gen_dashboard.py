#!/usr/bin/env python3
"""Generate dashboard.html with embedded Phase 1 and Phase 2 JSON."""
import json

with open("phase1_collected_mappings.json") as f:
    phase1 = json.load(f)
with open("phase2_agreement_analysis.json") as f:
    phase2_agreement = json.load(f)
with open("phase2_pitch_properties.json") as f:
    phase2_pitch = json.load(f)
with open("phase2_statistical_summary.json") as f:
    phase2_stats = json.load(f)

# Escape for embedding in script tag (no </script> in string)
def js_escape(s):
    return json.dumps(s, ensure_ascii=False)

data_js = f"""const phase1_collected_mappings = {js_escape(phase1)};
const phase2_agreement_analysis = {js_escape(phase2_agreement)};
const phase2_pitch_properties = {js_escape(phase2_pitch)};
const phase2_statistical_summary = {js_escape(phase2_stats)};"""

# Read the dashboard template (HTML without data) and replace DATA_PLACEHOLDER
# For now we write the full HTML from this script
with open("dashboard_template.html") as t:
    html = t.read()
html = html.replace("/* DATA_PLACEHOLDER */", data_js)
with open("dashboard.html", "w") as out:
    out.write(html)
print("dashboard.html written")
