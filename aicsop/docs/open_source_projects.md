# AICSoP 开源芯片项目清单

本文件整理了国内外优质开源芯片项目，强调 **完整 Spec、文档和验证资源**，适合 AI agent SOP 练习、架构验证和 IC 设计学习。

---

## 1️⃣ 国内优质开源芯片项目

| 项目 | 类型 | 特点 | 链接 |
|------|------|------|------|
| 玄铁 openC906 / openE906 / openC910 / openE902 | RISC-V CPU 核心 | 完整 RTL + Spec + Testbench，适合硬件验证 | [GitHub](https://github.com/OpenXiangshan/XiangShan) |
| 开源香山 CPU | RISC-V 核心 | 高性能、工业级，完整文档和测试套件 | [XiangShan GitHub](https://github.com/OpenXiangshan/XiangShan) |
| 一生一芯 Open SoC | SoC | 带完整 IP + 总线架构 + Spec 文档 | [GitLink](https://www.gitlink.org.cn/zone/OSchip) |
| MLVP 开放验证平台 | Verification 教学 | 提供完整实验 Spec、RTL、测试数据 | [MLVP Docs](https://open-verify.cc/mlvp/docs/) |

---

## 2️⃣ 国际高质量开源项目

| 项目 | 类型 | 特点 | 链接 |
|------|------|------|------|
| Chipyard | RISC-V SoC 平台 | UC Berkeley 开源，完整 RTL、Spec、Testbench、自动化验证 | [GitHub](https://github.com/ucb-bar/chipyard) |
| Rocket Chip Generator | RISC-V SOC | 自动生成 SOC 核心，带完整 Spec | [GitHub](https://github.com/chipsalliance/rocket-chip) |
| OpenROAD | ASIC 自动化工具 | 全流程开源后端工具，支持 RTL → GDSII | [GitHub](https://github.com/The-OpenROAD-Project/OpenROAD) |
| OpenPiton + Ariane | 多核 RISC-V | 包含 CPU 核心 + 测试套件 | [GitHub](https://github.com/PrincetonUniversity/openpiton) |
| LiteX SoC / LiteX-VexRiscv | FPGA / SoC | 完整 FPGA SoC 架构，RTL + Spec | [GitHub](https://github.com/enjoy-digital/litex) |
| OpenHW Group | RISC-V CPU | 高质量 CPU 核心，工业参考设计 | [OpenHW](https://github.com/openhwgroup) |

---

## 3️⃣ NVIDIA 相关 EDA 自动化资源

| 内容 | 说明 | 链接 |
|------|------|------|
| NVIDIA Design Automation Research Group | GPU + AI 驱动 EDA 自动化研究 | [Research](https://research.nvidia.com/labs/electronic-design-automation/?utm_source=chatgpt.com) |
| NVIDIA Documentation Hub | 官方文档，NeMo / NIM / CUDA-X / Agent Toolkit | [Docs](https://docs.nvidia.com/?utm_source=chatgpt.com) |
| NVIDIA 与 Cadence/Synopsys/Siemens 合作 | AI agent + GPU 加速 EDA 工具链 | [新闻](https://nvidianews.nvidia.com/news/nvidia-and-global-industrial-software-giants-bring-design-engineering-and-manufacturing-into-the-ai-era?utm_source=chatgpt.com) |
| AutoEDA | LLM agent 自动化 EDA 流实验 | [arxiv](https://arxiv.org/abs/2508.01012?utm_source=chatgpt.com) |
| ChatEDA | LLM 驱动 EDA 自动化 agent | [arxiv](https://arxiv.org/abs/2308.10204?utm_source=chatgpt.com) |
| GUI Agent for EDA | GUI agent 与 EDA 工具交互自动化 | [arxiv](https://arxiv.org/abs/2512.11611?utm_source=chatgpt.com) |

---

## 4️⃣ 使用建议

1. **国内入门**：玄铁 openC906 / 香山 CPU + MLVP 平台，练习 RTL → Testbench → Verification  
2. **进阶**：Chipyard / Rocket Chip / OpenROAD / OpenPiton，练习 SoC 集成与 AI agent SOP  
3. **AI agent 系统化**：R2 芯片智能体 + Python agent，实现 Skills、Context、Orchestration 流程  
4. **碎片化记录**：Obsidian / Zettelkasten 保存 Spec、IP、测试经验和 AI 输出  
5. **NVIDIA EDA 自动化**：GPU + LLM agent 自动化实验，结合论文和开源工具提升工业理解

---

## 5️⃣ 总结

- 本清单覆盖 **国内外最优质开源芯片项目**  
- 每个项目尽量包含 **完整 Spec、Testbench、文档**  
- 结合 AI agent SOP 可以练习从 **RTL → Coverage → Verification → SoC** 的完整流程  
- 适合边做边学芯片架构、验证、IC 设计方法论  