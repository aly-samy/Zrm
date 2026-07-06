import json

with open('intelligence_results.json', 'r') as f:
    intel = json.load(f)

scores = intel['health_scores']

with open('Constitutional Reviews/Discovery/17_REPOSITORY_HEALTH_SCORE.md', 'w') as f:
    f.write("# 17 REPOSITORY HEALTH SCORE\n\n")
    f.write("| Category | Score (0-10) | Recommendation |\n")
    f.write("| --- | --- | --- |\n")
    f.write(f"| Naming consistency | {scores['Naming consistency']} | Implement Canonical Naming Standard (Report 12) |\n")
    f.write(f"| Version consistency | {scores['Version consistency']} | Consolidate duplicates (Report 11) |\n")
    f.write(f"| Reference integrity | {scores['Reference integrity']} | Resolve missing dependencies (Report 15) |\n")
    f.write(f"| Hierarchy integrity | {scores['Hierarchy integrity']} | Adopt proposed restructure (Report 09) |\n")
    f.write(f"| Duplication | {scores['Duplication']} | Aggressive archival of legacy versions |\n")
    f.write(f"| Discoverability | {scores['Discoverability']} | Centralize Foundation and Constitution layers |\n")
    f.write(f"| AI readability | {scores['AI readability']} | Maintain semantic indices and metadata blocks |\n")
    f.write(f"| Human readability | {scores['Human readability']} | Simplify directory nesting for core specs |\n")
    f.write(f"| Technical debt | {scores['Technical debt']} | Formalize the Supersession Register (SR-001) as the truth arbiter |\n")
