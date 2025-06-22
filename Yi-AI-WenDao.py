# -*- coding: utf-8 -*-
"""
易经AI卜卦程序 GUI版
作者: AI (根据用户需求生成)
创建日期: 2024-05-21
最后修改: 2024-05-22 (添加配置保存、优化卦画和Prompt)
"""
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
import threading
import time
import json
import os
from openai import OpenAI

# --- 核心数据 ---

# 易经64卦数据
hexagrams = {
    "000000": {"name": "坤", "number": 2, "meaning": "柔顺、承载、包容。象征大地的品德，有极大的包容力。"},
    "000001": {"name": "复", "number": 24, "meaning": "回归、复苏。表示阳气始生，万物开始恢复生机。"},
    "000010": {"name": "师", "number": 7, "meaning": "军队、战争。象征组织和纪律，也表示面临挑战时的应对。"},
    "000011": {"name": "谦", "number": 15, "meaning": "谦虚、谦逊。象征不自满，能够虚心接受他人意见。"},
    "000100": {"name": "豫", "number": 16, "meaning": "愉悦、准备。表示预先准备，也有喜悦和满足的含义。"},
    "000101": {"name": "临", "number": 19, "meaning": "监督、统治。象征领导能力和管理才能。"},
    "000110": {"name": "明夷", "number": 36, "meaning": "受伤、困难。表示处于困境中，但也蕴含着希望和恢复的可能。"},
    "000111": {"name": "升", "number": 46, "meaning": "上升、进步。象征不断提升和发展。"},
    "001000": {"name": "比", "number": 8, "meaning": "亲密、团结。表示人与人之间的和谐关系。"},
    "001001": {"name": "屯", "number": 3, "meaning": "初创、困难。象征事物的开始阶段，充满挑战。"},
    "001010": {"name": "坎", "number": 29, "meaning": "险陷、困难。表示面临危险和挑战，但也蕴含着机会。"},
    "001011": {"name": "蒙", "number": 4, "meaning": "蒙昧、教育。象征无知需要学习和启蒙。"},
    "001100": {"name": "蹇", "number": 39, "meaning": "困难、阻碍。表示前进道路上遇到障碍。"},
    "001101": {"name": "解", "number": 40, "meaning": "解除、解决。象征问题得到解决，困境得到缓解。"},
    "001110": {"name": "涣", "number": 59, "meaning": "涣散、流通。表示分散和传播，也有消除疑虑的含义。"},
    "001111": {"name": "井", "number": 48, "meaning": "水井、供给。象征稳定的资源和支持。"},
    "010000": {"name": "剥", "number": 23, "meaning": "剥落、衰退。表示事物的衰落和消失。"},
    "010001": {"name": "颐", "number": 27, "meaning": "养育、养生。象征照顾和滋养自己及他人。"},
    "010010": {"name": "损", "number": 41, "meaning": "减少、损失。表示有所舍弃，也有自我牺牲的含义。"},
    "010011": {"name": "艮", "number": 52, "meaning": "止境、抑制。象征停止和控制，也有坚守的含义。"},
    "010100": {"name": "谦", "number": 15, "meaning": "谦虚、谦逊。象征不自满，能够虚心接受他人意见。"},
    "010101": {"name": "小过", "number": 62, "meaning": "轻微超过、小错误。表示略有偏差，但无大碍。"},
    "010110": {"name": "旅", "number": 56, "meaning": "旅行、流动。象征变化和移动，也有不安定的含义。"},
    "010111": {"name": "咸", "number": 31, "meaning": "感应、吸引。表示相互作用和情感交流。"},
    "011000": {"name": "晋", "number": 35, "meaning": "前进、提升。象征进步和发展。"},
    "011001": {"name": "萃", "number": 45, "meaning": "聚集、汇合。表示人们或事物的集合。"},
    "011010": {"name": "困", "number": 47, "meaning": "困境、限制。象征陷入困难和束缚。"},
    "011011": {"name": "渐", "number": 53, "meaning": "渐进、稳步。表示逐步发展和进步。"},
    "011100": {"name": "观", "number": 20, "meaning": "观察、审视。象征思考和评估。"},
    "011101": {"name": "大过", "number": 28, "meaning": "过度、超越。表示超过正常限度，也有突破的含义。"},
    "011110": {"name": "鼎", "number": 50, "meaning": "鼎器、稳定。象征权威和稳定。"},
    "011111": {"name": "巽", "number": 57, "meaning": "顺从、谦逊。表示温和地影响他人。"},
    "100000": {"name": "否", "number": 12, "meaning": "阻塞、不通。表示事物不顺利，处于停滞状态。"},
    "100001": {"name": "遁", "number": 33, "meaning": "退避、隐藏。象征暂时的撤退或回避。"},
    "100010": {"name": "讼", "number": 6, "meaning": "诉讼、争端。表示冲突和争议。"},
    "100011": {"name": "履", "number": 10, "meaning": "履行、实践。象征行动和实践。"},
    "100100": {"name": "无妄", "number": 25, "meaning": "意外、自然。表示意想不到的事情发生，也有自然无为的含义。"},
    "100101": {"name": "大畜", "number": 26, "meaning": "积累、积蓄。象征储存能量和资源。"},
    "100110": {"name": "睽", "number": 38, "meaning": "分离、对立。表示分歧和不和谐。"},
    "100111": {"name": "家人", "number": 37, "meaning": "家庭、亲情。象征家庭关系和内部和谐。"},
    "101000": {"name": "晋", "number": 35, "meaning": "前进、提升。象征进步和发展。"},
    "101001": {"name": "需", "number": 5, "meaning": "等待、需求。表示耐心等待和满足需求。"},
    "101010": {"name": "乾", "number": 1, "meaning": "刚健、创造。象征天的品德，具有强大的创造力。"},
    "101011": {"name": "大壮", "number": 34, "meaning": "强盛、壮大。表示力量强大，充满活力。"},
    "101100": {"name": "大有", "number": 14, "meaning": "富有、成就。象征成功和丰富。"},
    "101101": {"name": "夬", "number": 43, "meaning": "决断、突破。表示果断行动，突破障碍。"},
    "101110": {"name": "同人", "number": 13, "meaning": "和谐、团结。表示人与人之间的和谐与合作。"},
    "101111": {"name": "小畜", "number": 9, "meaning": "微小积累、限制。象征小的积累和暂时的限制。"},
    "110000": {"name": "明夷", "number": 36, "meaning": "受伤、困难。表示处于困境中，但也蕴含着希望和恢复的可能。"},
    "110001": {"name": "贲", "number": 22, "meaning": "装饰、美化。象征外在的修饰和内在的品质相结合。"},
    "110010": {"name": "既济", "number": 63, "meaning": "完成、成功。表示事情已经完成，但也提醒要保持谨慎。"},
    "110011": {"name": "噬嗑", "number": 21, "meaning": "咬合、决断。象征解决问题和做出决断。"},
    "110100": {"name": "丰", "number": 55, "meaning": "丰富、富足。表示繁荣和充实。"},
    "110101": {"name": "离", "number": 30, "meaning": "附着、光明。象征光明和热情，也有依附的含义。"},
    "110110": {"name": "革", "number": 49, "meaning": "变革、更新。表示重大的变化和改革。"},
    "110111": {"name": "同人", "number": 13, "meaning": "和谐、团结。表示人与人之间的和谐与合作。"},
    "111000": {"name": "临", "number": 19, "meaning": "监督、统治。象征领导能力和管理才能。"},
    "111001": {"name": "损", "number": 41, "meaning": "减少、损失。表示有所舍弃，也有自我牺牲的含义。"},
    "111010": {"name": "节", "number": 60, "meaning": "节制、适度。象征控制和平衡。"},
    "111011": {"name": "中孚", "number": 61, "meaning": "诚信、信任。表示内心的诚信和信任。"},
    "111100": {"name": "小过", "number": 62, "meaning": "轻微超过、小错误。表示略有偏差，但无大碍。"},
    "111101": {"name": "离", "number": 30, "meaning": "附着、光明。象征光明和热情，也有依附的含义。"},
    "111110": {"name": "未济", "number": 64, "meaning": "未完成、潜力。表示事情尚未完成，仍有发展的潜力。"},
    "111111": {"name": "乾", "number": 1, "meaning": "刚健、创造。象征天的品德，具有强大的创造力。"}
}

# API平台和模型配置
API_CONFIG = {
    "硅基流动 (SiliconFlow)": {
        "base_url": "https://api.siliconflow.cn/v1/",
        "models": ["deepseek-ai/DeepSeek-V3", "deepseek-ai/DeepSeek-R1", "自定义"]
    },
    "算了么 (Suanli)": {
        "base_url": "https://api.suanli.cn/v1",
        "models": ["free:QwQ-32B", "free:Qwen3-30B-A3B", "deepseek-r1", "deepseek-v3", "自定义"]
    },
    "OpenAI": {
        "base_url": "https://api.openai.com/v1",
        "models": ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo", "自定义"]
    }
}
CONFIG_FILE = "config.json"

class IChingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("易经AI卜卦程序")
        self.root.geometry("900x800")

        self.current_divination_result = None

        self.create_widgets()
        self.load_config()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        # ... (UI创建代码与之前版本基本一致, 只是布局微调) ...
        # --- 1. 设置区域 ---
        settings_frame = ttk.LabelFrame(self.root, text="API与模型设置", padding=10)
        settings_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(settings_frame, text="API Key:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.api_key_entry = ttk.Entry(settings_frame, width=40, show="*")
        self.api_key_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ttk.Label(settings_frame, text="选择平台:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.platform_var = tk.StringVar()
        self.platform_combo = ttk.Combobox(settings_frame, textvariable=self.platform_var, values=list(API_CONFIG.keys()), state="readonly")
        self.platform_combo.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.platform_combo.bind("<<ComboboxSelected>>", self.update_models)
        ttk.Label(settings_frame, text="选择模型:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.model_var = tk.StringVar()
        self.model_combo = ttk.Combobox(settings_frame, textvariable=self.model_var, state="readonly")
        self.model_combo.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.model_combo.bind("<<ComboboxSelected>>", self.toggle_custom_model_entry)
        ttk.Label(settings_frame, text="自定义模型:").grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.custom_model_entry = ttk.Entry(settings_frame, width=20, state="disabled")
        self.custom_model_entry.grid(row=2, column=3, padx=5, pady=5, sticky="ew")
        settings_frame.columnconfigure(1, weight=1)
        self.update_models()

        # --- 2. 操作区域 ---
        action_frame = ttk.LabelFrame(self.root, text="操作", padding=10)
        action_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(action_frame, text="您的问题:").pack(side="left", padx=5)
        self.question_entry = ttk.Entry(action_frame)
        self.question_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.auto_ai_var = tk.BooleanVar(value=True)
        self.auto_ai_check = ttk.Checkbutton(action_frame, text="完成后自动获取AI解读", variable=self.auto_ai_var)
        self.auto_ai_check.pack(side="left", padx=10)
        self.start_button = ttk.Button(action_frame, text="开始卜卦", command=self.start_divination_thread)
        self.start_button.pack(side="right", padx=5)

        # --- 3. 输出区域 ---
        output_frame = ttk.Frame(self.root, padding=10)
        output_frame.pack(fill="both", expand=True, padx=10, pady=5)
        output_frame.rowconfigure(0, weight=1)
        output_frame.columnconfigure(0, weight=2)
        output_frame.columnconfigure(1, weight=3)
        left_frame = ttk.Frame(output_frame)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        left_frame.rowconfigure(0, weight=1)
        left_frame.rowconfigure(1, weight=1)
        left_frame.columnconfigure(0, weight=1)
        toss_frame = ttk.LabelFrame(left_frame, text="掷钱法过程")
        toss_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
        self.toss_text = scrolledtext.ScrolledText(toss_frame, wrap=tk.WORD, state="disabled", height=10)
        self.toss_text.pack(fill="both", expand=True, padx=5, pady=5)
        hex_frame = ttk.LabelFrame(left_frame, text="最终卦象和解释")
        hex_frame.grid(row=1, column=0, sticky="nsew")
        self.hex_text = scrolledtext.ScrolledText(hex_frame, wrap=tk.WORD, state="disabled", height=10, font=("Courier New", 10))
        self.hex_text.pack(fill="both", expand=True, padx=5, pady=5)
        ai_frame = ttk.LabelFrame(output_frame, text="大模型的解释")
        ai_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
        self.ai_text = scrolledtext.ScrolledText(ai_frame, wrap=tk.WORD, state="disabled")
        self.ai_text.pack(fill="both", expand=True, padx=5, pady=5)

        # --- 4. AI操作区域 ---
        ai_action_frame = ttk.Frame(self.root, padding=(10,0,10,10))
        ai_action_frame.pack(fill="x")
        self.ai_request_button = ttk.Button(ai_action_frame, text="请求AI解读", state="disabled", command=self.start_ai_request_thread)
        self.ai_request_button.pack(side="right")

    def on_closing(self):
        """关闭窗口时保存配置"""
        self.save_config()
        self.root.destroy()

    def save_config(self):
        """保存当前配置到文件"""
        config = {
            "api_key": self.api_key_entry.get(),
            "platform": self.platform_var.get(),
            "model": self.model_var.get(),
            "custom_model": self.custom_model_entry.get()
        }
        try:
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4)
        except Exception as e:
            print(f"保存配置失败: {e}")

    def load_config(self):
        """从文件加载配置"""
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                self.api_key_entry.delete(0, tk.END)
                self.api_key_entry.insert(0, config.get("api_key", ""))
                self.platform_var.set(config.get("platform", list(API_CONFIG.keys())[0]))
                self.update_models() # 更新模型列表
                self.model_var.set(config.get("model", self.model_combo["values"][0]))
                self.toggle_custom_model_entry()
                if self.model_var.get() == "自定义":
                    self.custom_model_entry.insert(0, config.get("custom_model", ""))
        except Exception as e:
            messagebox.showerror("加载配置失败", f"无法加载配置文件: {e}")

    def set_buttons_state(self, state):
        self.start_button.config(state=state)
        if state == "normal" and self.current_divination_result:
            self.ai_request_button.config(state="normal")
        else:
            self.ai_request_button.config(state="disabled")

    def start_divination_thread(self):
        self.set_buttons_state("disabled")
        self.clear_outputs()
        self.current_divination_result = None
        thread = threading.Thread(target=self.run_divination_process)
        thread.daemon = True
        thread.start()

    def run_divination_process(self):
        try:
            self.root.after(0, lambda: self.insert_text(self.toss_text, "开始模拟掷钱法占卜...\n\n"))
            toss_results = []
            original_code_list = []
            
            for i in range(6):
                self.root.after(0, lambda i=i: self.insert_text(self.toss_text, f"第{i+1}次掷钱...\n"))
                time.sleep(0.5)
                
                heads = sum([random.randint(0, 1) for _ in range(3)])
                if heads == 0: result, code, is_changing = "老阴 (-    -) ×", '0', True
                elif heads == 1: result, code, is_changing = "少阴 (-    -)", '0', False
                elif heads == 2: result, code, is_changing = "少阳 (———)", '1', False
                else: result, code, is_changing = "老阳 (———) ▢", '1', True
                
                toss_results.append({"text": result, "is_changing": is_changing})
                original_code_list.append(code)
                self.root.after(0, lambda result=result: self.insert_text(self.toss_text, f"结果: {result}\n"))
                time.sleep(0.2)

            # --- 计算本卦和之卦 ---
            original_hex_code = "".join(original_code_list)
            changed_hex_code_list = [
                str(1 - int(code)) if toss['is_changing'] else code
                for code, toss in zip(original_code_list, toss_results)
            ]
            changed_hex_code = "".join(changed_hex_code_list)
            
            self.current_divination_result = {
                "toss_results": toss_results,
                "original_code": original_hex_code,
                "changed_code": changed_hex_code
            }

            interpretation_text = self.interpret_hexagram(self.current_divination_result)
            self.root.after(0, lambda: self.insert_text(self.hex_text, interpretation_text))

            if self.auto_ai_var.get():
                self.start_ai_request_thread(is_auto=True)
            else:
                self.root.after(0, lambda: self.set_buttons_state("normal"))

        except Exception as e:
            error_message = f"发生错误: {e}"
            self.root.after(0, lambda: messagebox.showerror("运行时错误", error_message))
            self.root.after(0, lambda: self.set_buttons_state("normal"))

    def interpret_hexagram(self, result_data):
        """生成优化后的卦象解释文本"""
        original_hex = hexagrams.get(result_data["original_code"], {"name": "未知", "number": "?", "meaning": "无"})
        changed_hex = hexagrams.get(result_data["changed_code"], {"name": "未知", "number": "?", "meaning": "无"})
        
        lines = []
        changing_lines_indices = []
        for i, toss in enumerate(reversed(result_data["toss_results"])):
            line_char = "━━━" if "———" in toss["text"] else "━  ━"
            indicator = ""
            if toss["is_changing"]:
                indicator = " <--- 变"
                changing_lines_indices.append(f"{6-i}爻")
            lines.append(f"{line_char}  {indicator}")
        
        text = f"本卦: {original_hex['name']} (第{original_hex['number']}卦)\n"
        text += "---------------------\n"
        text += "\n".join(lines) + "\n"
        text += "---------------------\n"
        text += f"卦辞: {original_hex['meaning']}\n\n"

        if result_data["original_code"] != result_data["changed_code"]:
            text += f"变爻: {', '.join(changing_lines_indices)}\n"
            text += f"之卦: {changed_hex['name']} (第{changed_hex['number']}卦)\n"
            text += f"之卦卦辞: {changed_hex['meaning']}\n"
        else:
            text += "无变爻，事态稳定。\n"
        
        return text

    def start_ai_request_thread(self, is_auto=False):
        if not self.current_divination_result:
            messagebox.showwarning("提示", "请先完成一次卜卦，再请求AI解读。")
            return
        if not self.api_key_entry.get():
            messagebox.showerror("错误", "请输入您的API Key！")
            if not is_auto: self.set_buttons_state("normal")
            return
        
        self.set_buttons_state("disabled")
        self.root.after(0, lambda: self.ai_text.config(state="normal"))
        self.root.after(0, lambda: self.ai_text.delete(1.0, tk.END))
        self.root.after(0, lambda: self.insert_text(self.ai_text, "正在连接AI，请稍候...\n\n"))
        thread = threading.Thread(target=self.run_ai_request_process)
        thread.daemon = True
        thread.start()

    def run_ai_request_process(self):
        try:
            ai_interpretation = self.generate_ai_interpretation()
            self.root.after(0, lambda: self.ai_text.config(state="normal"))
            self.root.after(0, lambda: self.ai_text.delete(1.0, tk.END))
            self.root.after(0, lambda: self.insert_text(self.ai_text, ai_interpretation))
        except Exception as e:
            error_message = f"调用AI时发生错误: {e}"
            self.root.after(0, lambda: self.insert_text(self.ai_text, f"\n\n{error_message}"))
            self.root.after(0, lambda: messagebox.showerror("AI调用错误", error_message))
        finally:
            self.root.after(0, lambda: self.set_buttons_state("normal"))

    def generate_ai_interpretation(self):
        """调用大模型生成AI解读，使用优化后的Prompt"""
        # ... (获取API, 模型等信息) ...
        api_key = self.api_key_entry.get()
        platform_name = self.platform_var.get()
        model_name = self.model_var.get()
        if model_name == "自定义":
            model_name = self.custom_model_entry.get()
            if not model_name: return "错误：选择了自定义模型，但未填写模型名称。"
        base_url = API_CONFIG[platform_name]["base_url"]
        question = self.question_entry.get() or "我没有具体问题，请为我解读此卦。"

        # --- 准备Prompt所需信息 ---
        result_data = self.current_divination_result
        original_hex = hexagrams.get(result_data["original_code"])
        changed_hex = hexagrams.get(result_data["changed_code"])
        
        changing_lines_info = []
        for i, toss in enumerate(result_data["toss_results"]):
            if toss["is_changing"]:
                changing_lines_info.append(f"第{i+1}爻 ({toss['text']})")
        
        prompt_parts = [
            "你是一位将《易经》古老智慧与现代生活紧密结合的深度解读专家。请基于用户提供的信息，进行一次全面而富有启发性的分析。\n",
            f"**1. 用户的问题:**\n“{question}”\n",
            "**2. 卜卦结果:**",
            f"   - **本卦 (当前状态):** {original_hex['name']}卦 (第{original_hex['number']}卦)",
            f"     - 卦辞: {original_hex['meaning']}\n"
        ]

        if changing_lines_info:
            prompt_parts.extend([
                f"   - **变爻 (动态因素):** {', '.join(changing_lines_info)}",
                f"   - **之卦 (发展趋势):** {changed_hex['name']}卦 (第{changed_hex['number']}卦)",
                f"     - 卦辞: {changed_hex['meaning']}\n"
            ])
        else:
            prompt_parts.append("   - **变爻:** 无。事态目前处于稳定状态。\n")

        prompt_parts.extend([
            "**3. 解读要求:**",
            "请综合以上所有信息，特别是从 **本卦** 到 **之卦** 的演变趋势，为用户提供以下分析：",
            "   - **核心洞察:** 针对用户的问题，这个卦象组合最关键的启示是什么？当前的核心矛盾或机遇在哪里？",
            "   - **现状详析:** 结合'本卦'，详细分析用户目前的处境、心态和外部环境。",
            "   - **未来走向与建议:** 结合'之卦'和'变爻'，预测事态可能的发展方向。我应该采取什么具体行动，或保持何种心态来趋吉避凶？",
            "   - **智慧锦囊:** 从这个卦象变化中，可以提炼出怎样的人生哲学或长远智慧？\n",
            "请用清晰、富有同理心且具有指导性的语言进行阐述。"
        ])
        
        prompt = "\n".join(prompt_parts)
        
        client = OpenAI(api_key=api_key, base_url=base_url)
        try:
            completion = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": "你是一位精通《易经》并富有现代智慧的导师。输出环境不能渲染markdown，使用纯文本格式输出即可"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6, max_tokens=1000, timeout=120
            )
            return completion.choices[0].message.content
        except Exception as e:
            raise Exception(f"{e}")

    # --- 其他辅助函数 ---
    def update_models(self, event=None):
        platform = self.platform_var.get()
        if platform:
            models = API_CONFIG[platform]["models"]
            self.model_combo["values"] = models
            self.model_var.set(models[0])
            self.toggle_custom_model_entry()

    def toggle_custom_model_entry(self, event=None):
        if self.model_var.get() == "自定义":
            self.custom_model_entry.config(state="normal")
        else:
            self.custom_model_entry.config(state="disabled")
            self.custom_model_entry.delete(0, tk.END)

    def insert_text(self, widget, text):
        widget.config(state="normal")
        widget.insert(tk.END, text)
        widget.config(state="disabled")
        widget.see(tk.END)

    def clear_outputs(self):
        for widget in [self.toss_text, self.hex_text, self.ai_text]:
            widget.config(state="normal")
            widget.delete(1.0, tk.END)
            widget.config(state="disabled")

# --- 主程序入口 ---
if __name__ == "__main__":
    root = tk.Tk()
    app = IChingApp(root)
    root.mainloop()