from random import randint

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
