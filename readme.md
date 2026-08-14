# 📚 AI学习助手

基于大语言模型 + RAG 技术打造的智能学习助手。

用户可以上传 PDF 教材，系统自动建立知识库，并基于教材内容进行智能问答。


## ✨ 功能特点

- 📄 PDF 文档解析
- 🔍 文档向量化检索
- 🧠 RAG（检索增强生成）
- 🤖 千问大语言模型回答
- 🌐 Gradio Web界面
- 📚 基于教材内容精准问答


## 🏗️ 技术架构


PDF教材

↓

文本切分

↓

Embedding向量模型

↓

Chroma向量数据库

↓

检索相关知识

↓

千问大模型

↓

生成回答



## 📂 项目结构


AI学习助手

├── main.py # Web界面
├── ai_chat.py # 大模型调用
├── rag.py # RAG检索
├── pdf_reader.py # PDF解析
├── summary.py # 文档总结
├── study_tools.py # 学习工具
├── requirements.txt # 依赖
└── .gitignore



## 🚀 使用方法


### 1. 安装依赖

```bash
pip install -r requirements.txt

2. 配置API

创建：

.env

填写：

DASHSCOPE_API_KEY=你的千问API_KEY
3. 启动
python main.py

打开：

http://127.0.0.1:7860
🛠️ 技术栈
Python
Gradio
LangChain
ChromaDB
HuggingFace Embedding
Qwen API
📌 后续计划
 多PDF知识库管理
 AI自动生成学习笔记
 自动生成考试题
 显示答案来源页码
 用户登录系统
License

MIT


---

保存。

---

## 第二步：提交 README

回到 VS Code 终端：

```powershell
git add README.md

然后：

git commit -m "add project README"

应该看到：

[master xxxx] add project README
