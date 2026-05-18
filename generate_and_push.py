import os
import json
import subprocess

# ----------------------------
# 项目目录
# ----------------------------
project_root = os.path.join(os.getcwd(), "aicsop")
os.makedirs(project_root, exist_ok=True)
docs_dir = os.path.join(project_root, "docs")
os.makedirs(docs_dir, exist_ok=True)
diagrams_dir = os.path.join(project_root, "diagrams")
os.makedirs(diagrams_dir, exist_ok=True)

# ----------------------------
# 文件内容
# ----------------------------
files_content = {
    "Skills.py": "...",  # 填入之前 Skills.py 代码
    "Orchestration.py": "...",  # 填入之前 Orchestration.py 代码
    "full_learning_resources.md": "# AICSoP 学习资源与智能体 SOP 完整指南\n\n(整合书籍、课程、开源项目、NVIDIA EDA、AI agent SOP)",
    "update_guide.md": "# AICSoP 项目更新指南\n\n(指导 Markdown 文件更新、实验笔记提交和 SOP 流程)",
    "context.json": "{}",
    "IC_fragment_notes.md": "### IC碎片笔记\n(示例笔记内容)",
    "README.md": "# AICSoP - 学生版多模型智能体实验套件\n\n(项目概述、使用说明、资源索引)"
}

# ----------------------------
# 创建文件
# ----------------------------
for filename, content in files_content.items():
    if filename.endswith(".md"):
        file_path = os.path.join(docs_dir, filename)
    else:
        file_path = os.path.join(project_root, filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("项目文件已生成。")

# ----------------------------
# 执行 Orchestration.py 生成 Context 和笔记
# ----------------------------
subprocess.run(f"py {os.path.join(project_root,'Orchestration.py')}", shell=True)

# ----------------------------
# Git 操作：add -> commit -> push
# ----------------------------
try:
    subprocess.run("git add .", shell=True, check=True)
    subprocess.run('git commit -m "Auto-update: generate project + resources + notes"', shell=True, check=True)
    subprocess.run("git push", shell=True, check=True)
    print("Git 上传完成 ✅")
except subprocess.CalledProcessError:
    print("Git 操作失败，请确认远程仓库已配置，并且 SSH 已认证。")