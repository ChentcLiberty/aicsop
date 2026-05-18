import os
import json

# 项目根目录
project_root = os.path.join(os.getcwd(), "aicsop")
os.makedirs(project_root, exist_ok=True)

# 创建子目录
dirs = ["docs", "diagrams"]
for d in dirs:
    os.makedirs(os.path.join(project_root, d), exist_ok=True)

# 文件内容
files_content = {
    "Skills.py": "...",  # 填入之前的 Skills.py 代码
    "Orchestration.py": "...",  # 填入之前的 Orchestration.py 代码
    "full_learning_resources.md": "# AICSoP 学习资源与智能体 SOP 完整指南\n\n(整合书籍、课程、开源项目、NVIDIA EDA、AI agent SOP)",
    "update_guide.md": "# AICSoP 项目更新指南\n\n(指导 Markdown 文件更新、实验笔记提交和 SOP 流程)",
    "context.json": "{}",
    "IC_fragment_notes.md": "### IC碎片笔记\n(示例笔记内容)",
    "README.md": "# AICSoP - 学生版多模型智能体实验套件\n\n(项目概述、使用说明、资源索引)",
}

# 创建文件
for filename, content in files_content.items():
    file_path = os.path.join(project_root, filename if filename.endswith(".py") or filename.endswith(".md") else f"docs/{filename}")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"AICSoP 项目已生成在: {project_root}")
print("运行 'Orchestration.py' 即可生成最新 Context 和 Markdown 碎片笔记。")