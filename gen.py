import os
import json

project_root = "aicsop"
dirs = ["diagrams", "docs"]

# 创建文件夹
os.makedirs(project_root, exist_ok=True)
for d in dirs:
    os.makedirs(os.path.join(project_root, d), exist_ok=True)

# 文件内容
files_content = {
    'README.md': "# AICSoP - 学生版多模型智能体实验套件\n\n项目概述：\n- 多模型任务拆解\n- Context 管理 + 自学习闭环\n- 碎片知识库生成\n- GitHub/EDA课程资源整合\n",
    'Orchestration.py': '''import json
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
''',
    'Skills.py': '''from random import randint

def parse_spec(context, model_type):
    print(f"[{model_type}] parse_spec running")
    result = {"modules": ["ALU", "RegFile"], "interfaces": ["AXI", "APB"]}
    return result, True

def generate_rtl(context, model_type):
    print(f"[{model_type}] generate_rtl running")
    result = {"rtl_files": ["alu.v", "regfile.v"]}
    return result, True

def generate_testbench(context, model_type):
    print(f"[{model_type}] generate_testbench running")
    result = {"testbench": ["alu_tb.v", "regfile_tb.v"]}
    return result, True

def coverage_fix(context, model_type):
    print(f"[{model_type}] coverage_fix running")
    success = randint(0,1)
    result = {"coverage": "95%" if success else "80%", "fixes": ["alu_signal_fix" if success else "alu_signal_fix_pending"]}
    return result, success

def generate_notes(context, model_type):
    notes = f"""### IC 碎片笔记
Spec解析: {context.get('parse_spec')}
RTL生成: {context.get('generate_rtl')}
Testbench: {context.get('generate_testbench')}
覆盖率修复: {context.get('coverage_fix')}
失败记录: {context.get('failure_log', '无')}
"""
    with open("IC_fragment_notes.md", "w") as f:
        f.write(notes)
    return notes, True
''',
    'context.json': '{}',
    'IC_fragment_notes.md': '### IC碎片笔记\n(示例笔记内容)\n',
    'ExternalResources.py': '# 用于抓取 GitHub/EDA课程/文档资源的示例脚本\n',
    'requirements.txt': 'requests\nopenai\n',
    'diagrams/system_flow.png': '',
    'diagrams/modules_flow.png': '',
    'docs/design_notes.md': '# 系统设计文档\n详细说明每个模块功能及流程\n',
    'docs/usage_guide.md': '# 使用指南\n如何在Colab/本地运行实验套件\n'
}

# 创建文件
for path, content in files_content.items():
    file_path = os.path.join(project_root, path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(content)

print(f"项目生成完成，目录: {os.path.abspath(project_root)}")