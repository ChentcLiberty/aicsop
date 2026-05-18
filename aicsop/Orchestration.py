import json
from Skills import parse_spec, generate_rtl, generate_testbench, coverage_fix, generate_notes
import os

os.makedirs("aicsop", exist_ok=True)

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

context_path = os.path.join("aicsop", "context.json")
with open(context_path, "w", encoding="utf-8") as f:
    json.dump(context, f, indent=2, ensure_ascii=False)

print("Context and notes generated in 'aicsop/' folder with UTF-8 encoding.")
