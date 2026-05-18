import os
import subprocess

# =========================
# 配置部分（请修改为你的 GitHub 信息）
# =========================
GITHUB_USERNAME = "ChentcLiberty"           # 你的 GitHub 用户名
REPO_NAME = "aicsop"                        # 仓库名
REPO_URL = f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"  # GitHub 仓库 URL
PROJECT_DIR = "aicsop"                      # 本地项目文件夹

# =========================
# 上传流程
# =========================
def run_command(cmd, cwd=None):
    """运行系统命令并打印输出"""
    result = subprocess.run(cmd, cwd=cwd, shell=True)
    if result.returncode != 0:
        print(f"命令失败: {cmd}")
    return result.returncode

def git_upload():
    if not os.path.exists(PROJECT_DIR):
        print(f"项目目录 {PROJECT_DIR} 不存在，请先生成项目文件夹")
        return

    print(f"开始上传项目 {PROJECT_DIR} 到 GitHub 仓库 {REPO_URL}...")

    # 1. 初始化 Git 仓库
    run_command("git init", cwd=PROJECT_DIR)

    # 2. 添加远程仓库
    run_command(f"git remote add origin {REPO_URL}", cwd=PROJECT_DIR)

    # 3. 添加所有文件
    run_command("git add .", cwd=PROJECT_DIR)

    # 4. 提交
    run_command('git commit -m "Initial commit: student multi-model AI chip agent"', cwd=PROJECT_DIR)

    # 5. 设置主分支并推送
    run_command("git branch -M main", cwd=PROJECT_DIR)
    run_command("git push -u origin main", cwd=PROJECT_DIR)

    print("上传完成 ✅")

if __name__ == "__main__":
    git_upload()