# AICSoP 学习资源清单

## 1️⃣ 核心书籍（理论与方法论）
| 类别 | 书籍 | 价值说明 |
|------|------|----------|
| 系统与方法论 | 钱学森《系统工程论》 | 系统思维，工程方法论基础 |
| 系统与方法论 | 金观涛《系统科学方法论导论》 | 方法论与复杂系统管理 |
| 芯片设计 / 计算机体系结构 | 《计算机体系结构：量化研究方法》 | 芯片设计原理和性能分析 |
| AI 芯片案例 | 《创新者的窘境》 | 技术演化与创新决策 |
| 工程心法 | 冯唐《成事心法》 | 工程与项目管理思维 |
| 芯片工程实务 | 《控制论与科学方法论》 | 对复杂系统控制、验证方法的理解 |

---

## 2️⃣ EDA / 芯片 AI 实践课程
| 来源 | 课程 / 资源 | 说明 |
|------|------------|------|
| 小鹅通 / 付费 | R2 芯片智能体课程（500元） | 工业级 AI agent 方法，结合 RTL、SoC、Verification |
| 官方 / 免费 | Synopsys / Cadence / Mentor 官方教程 | RTL 验证、覆盖率分析、SoC 集成 |
| Coursera / edX | FPGA / ASIC / VLSI 设计课程 | 国际课程，免费听讲 + 作业 |
| YouTube / B站 | 芯片验证实战视频 | 学习流程 Orchestration + RTL + Coverage + Testbench |

---

## 3️⃣ GitHub 高质量开源项目
| 项目 | 说明 |
|------|------|
| [Chipyard](https://github.com/ucb-bar/chipyard) | UC Berkeley，RISC-V SoC 开源平台 |
| [Rocket Chip Generator](https://github.com/chipsalliance/rocket-chip) | 自动生成可验证 RISC-V SOC |
| [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) | 全自动 ASIC 后端工具链 |
| [AutoFPGA](https://github.com/openfpga/OpenFPGA) | FPGA 自动化生成和验证环境 |
| [EDA Utilities](https://github.com/topics/eda) | 工具脚本、仿真流程示例 |

---

## 4️⃣ 学习路线建议
1. **理论基础**：系统工程论 + 芯片体系结构  
2. **EDA 实践 + 开源平台**：Chipyard / Rocket Chip / OpenROAD / AutoFPGA  
3. **AI agent 系统化训练**：R2 芯片智能体课程或自建 Python agent  
4. **碎片知识积累**：Obsidian / Zettelkasten + GitHub 代码片段 / 流程截图  

---

## 5️⃣ 课程与资源选择建议
- 如果预算充足：R2 课程可以快速系统化掌握工业级 AI agent 流程  
- 如果自学能力强：可以组合 GitHub 开源项目 + 官方 EDA 文档 + Python agent 实验，成本更低  
- 所有资源建议结合实际项目练习，边做边积累 IC / 芯片验证经验