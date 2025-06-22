# WenDao AI (问道)

English | [中文](./README.md)

WenDao AI digitalizes the traditional "coin tossing" divination process and integrates powerful AI Large Language Models to provide you with deep interpretations that have both traditional charm and a modern perspective. Whatever puzzles you, you can use this application to seek inspiration from ancient wisdom and receive analysis and suggestions tailored for you by AI.

## ✨ Feature Highlights

- **Traditional Divination Simulation**: Fully simulates the three-coin toss method, automatically generating the Primary Hexagram, Changing Lines, and the Resulting Hexagram with clear results.

- **Multi-Platform AI Support**: Users can freely choose and configure Large Language Models from various platforms, including SiliconFlow, Suanli, and OpenAI.

- **In-Depth AI Interpretation**: An optimized prompt guides the AI to not just explain the hexagrams but also to analyze the evolutionary trend from the "Primary" to the "Resulting" hexagram, offering more profound and actionable insights.

- **Aesthetic Hexagram Display**: Uses visually appealing characters to draw the hexagrams and clearly marks the changing lines for easy understanding.

- **Personalized Configuration**: Automatically saves user settings (like API Key, selected platform, and model) for immediate use on the next launch, no reconfiguration needed.

- **User-Friendly Interface**: A graphical interface built with tkinter, featuring intuitive controls and three separate panes for the divination process, traditional results, and AI interpretation.

- **Cross-Platform Compatibility**: Written in Python, it can run on multiple operating systems like Windows, macOS, and Linux.

## 🚀 Quick Start

### 1. Prerequisites

- Ensure you have Python 3.8 or a higher version installed.

- Using a virtual environment is highly recommended to avoid package conflicts.

### 2. Installation

Clone this repository to your local machine:  

```
git clone [https://github.com/your_username/WenDao-AI.git](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fyour_username%2FWenDao-AI.git)
```

```
cd WenDao-AI

Create and activate a virtual environment:
```

# Windows

```
python -m venv venv  
.\venv\Scripts\activate
```

### 3. Running the Application

Run the main application script:  
python iching_ai_app.py

## 📖 Usage Guide

1. **Configure API**:
   
   - In the "API & Model Settings" section at the top, enter your API Key.
   
   - Select the Platform you wish to use (e.g., OpenAI).
   
   - Choose the corresponding Model (e.g., gpt-4o). If you select "Custom", fill in the model name in the input field to the right.

2. **Ask Your Question**:
   
   - In the "Action" section, type the question you have in mind into the input box.

3. **Start Divination**:
   
   - Click the "Start Divination" button.
   
   - The left-side panes will display the real-time coin-tossing process and the final hexagram results.
   
   - If "Automatically get AI interpretation" is checked, the application will automatically send the results to the AI.

4. **Get AI Interpretation**:
   
   - The AI's interpretation will appear in the large pane on the right.
   
   - If the AI call fails or you want a new interpretation, you can click the "Request AI Interpretation" button at any time.

## 📦 Packaging for Distribution

If you want to run this application on a computer without a Python environment, you can package it into a standalone executable file (e.g., for Windows).

1. **Install PyInstaller**:  
   pip install pyinstaller

2. **(Optional) Install UPX to reduce file size**:
   
   - Download and extract it from the UPX GitHub Releases.
   
   - Add the path to upx.exe to your system's environment variables, or simply copy it into the project's root directory.

3. **Execute the Packaging Command**:  
   Using a .spec file is recommended for fine-grained control and a smaller output.
   
   a. **Generate .spec file**:  
   pyinstaller --windowed --name WenDao-AI iching_ai_app.py
   
   b. **Edit WenDao-AI.spec**:  
   In the Analysis section, add non-essential modules like ['tkinter.test', 'unittest', 'sqlite3'] to the excludes list.  
   In the EXE section, ensure upx=True.
   
   c. **Package using the .spec file**:  
   pyinstaller --onefile WenDao-AI.spec

After packaging is complete, you will find the WenDao-AI.exe file in the dist folder.

## 🙏 Acknowledgements

- Thanks to the I Ching for its ancient and profound wisdom.

- Thanks to the various AI platforms for their powerful model support.

## 📜 License

This project is licensed under the MIT License.
