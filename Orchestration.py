import json
from Skills import parse_spec, generate_rtl, generate_testbench, coverage_fix, generate_notes

tasks = [
    {"name": "parse_spec", "func": parse_spec, "model": "free"},
    {"name": "generate_rtl", "func": generate_rtl, "model": "high"},
    {"name": "generate_testbench", "func": generate_testbench, "model": "free"},
    {"name": "coverage_fix", "func": coverage_fix, "model": "high"},
    {"name": "generate_notes", "func": generate_notes, "model": "free"}
]

context = {}
for task in tasks:
    print(f"Executing {task['name']} with model {task['model']}")
    result, success = task["func"](context, task["model"])
    context[task["name"]] = result
    if not success:
        context.setdefault("failure_log", []).append({task["name"]: result})

with open("context.json", "w") as f:
    json.dump(context, f, indent=2)
