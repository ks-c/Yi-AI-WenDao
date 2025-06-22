# 问道AI (WenDao AI)

<div align="center">
  <img src="your_icon.ico" alt="WenDao AI Logo" width="150"/>
  <h1>问道AI</h1>
  <p><strong>一款融合了《易经》古老智慧与现代AI大语言模型的桌面卜卦应用</strong></p>
  <p>
    <a href="#"><img src="https://img.shields.io/badge/AI--Powered-Gemini%20%26%20Doubao-blueviolet" alt="AI-Powered"></a>
    <a href="#"><img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version"></a>
    <a href="#"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
    <a href="#"><img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg" alt="Platform"></a>
  </p>
</div>

---


**[English](./README_EN.md) | 中文**

**问道AI** 将传统的“掷钱法”卜卦过程数字化，并引入了强大的AI大语言模型，为你提供兼具传统韵味与现代视角的深度解读。无论你心中有何困惑，都可以通过这个应用，向古老的智慧寻求启示，并获得AI为你量身定制的分析与建议。

## ✨ 功能亮点

*   **传统卜卦模拟**: 完整模拟三枚铜钱的掷钱过程，自动生成**本卦**、**变爻**和**之卦**，结果清晰明了。
*   **多平台AI支持**: 用户可自由选择并配置 **硅基流动 (SiliconFlow)**、**算了么 (Suanli)**、**OpenAI** 等多个平台的大语言模型进行解读。
*   **深度AI解读**: 经过优化的Prompt，引导AI不仅解释卦象，更分析从“本卦”到“之卦”的**演变趋势**，提供更具深度和指导性的分析。
*   **美观的卦画显示**: 使用更具美感的字符绘制卦画，并清晰标注变爻，方便用户理解。
*   **个性化配置**: 自动保存用户设置（如API Key、所选平台和模型），下次打开即可使用，无需重复配置。
*   **用户友好的界面**: 基于 `tkinter` 构建的图形化界面，操作直观，三个独立的窗口分别展示卜卦过程、传统卦象和AI解读。
*   **跨平台运行**: 使用Python编写，可在 Windows, macOS, Linux 等多个操作系统上运行。

## 📖 使用指南
- **配置API**:
  - 在程序顶部的“**API与模型设置**”区域，填入你的 API Key。
  - 选择你希望使用的**平台 (如 OpenAI)**。
  - 选择对应的**模型 (如 gpt-4o)**。如果选择“自定义”，请在右侧输入框填写模型名称。
- **提出问题**:
  - 在“**操作**”区域的输入框中，写下你心中所想问的问题。
- **开始卜卦**:
  - 点击 “**开始卜卦**” 按钮。
  - 左侧窗口将实时显示掷钱过程和最终的卦象结果。
  - 如果勾选了“完成后自动获取AI解读”，程序会自动将结果发送给AI。
- **获取AI解读**:
  - AI的解读结果将显示在右侧的大窗口中。
  - 如果AI调用失败或你想重新获取解读，可以随时点击右下角的 “**请求AI解读**” 按钮。

## 📜 许可证
本项目采用 MIT License 开源。


## 🙏 致谢

*   感谢《易经》这部古老的智慧经典，它为本项目提供了核心思想与灵魂。
*   感谢各大AI平台（如 SiliconFlow, Suanli, OpenAI 等）提供的强大模型支持，让古老智慧得以与尖端科技对话。
*   特别感谢 **Google Gemini** 与字节跳动 **豆包大模型**，在项目构思、代码编写、功能迭代及文档撰写过程中提供了极大的帮助与灵感。

## 说明

以上内容由Gemini-2.5-pro生成
