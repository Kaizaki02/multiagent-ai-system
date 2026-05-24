# 🔬 Multi-Agent AI Research Assistant

A modular AI-powered research assistant built using LangChain, Gemini, Tavily, and Streamlit.

This system orchestrates multiple specialized AI agents to:

* search the web for recent information
* scrape and extract clean content
* generate structured research reports
* critique and evaluate the final report

---

# ✨ Features

✅ Multi-agent architecture
✅ Real-time web research
✅ Intelligent webpage scraping
✅ AI-generated research reports
✅ Automated critique & scoring
✅ Interactive Streamlit interface
✅ Modular and extensible design

---

# 🧠 Multi-Agent Workflow

The system is composed of four specialized agents working together in a pipeline:

```text
User Topic
    ↓
🔍 Search Agent
    ↓
📄 Reader Agent
    ↓
✍️ Writer Agent
    ↓
🧐 Critic Agent
    ↓
Final Research Report + Evaluation
```

### Agent Responsibilities

| Agent           | Responsibility                                 |
| --------------- | ---------------------------------------------- |
| 🔍 Search Agent | Finds recent and reliable sources using Tavily |
| 📄 Reader Agent | Scrapes and extracts clean webpage content     |
| ✍️ Writer Agent | Generates structured research reports          |
| 🧐 Critic Agent | Evaluates and critiques the generated report   |

---

# 🛠️ Tech Stack

* Python 3.11+
* LangChain
* Streamlit
* Google Gemini
* Tavily Search API
* BeautifulSoup
* Readability
* Trafilatura
* Requests
* python-dotenv

---

# 📁 Project Structure

```text
multiagent-ai-system/
│
├── app.py                      # Streamlit UI
├── main.py                     # practising through this file so that i can understand code is working or not 
├── requirements.txt
├── .env
│
├── src/
│   ├── agents/
│   │   └── agents.py           # Agent definitions & prompts
│   │
│   ├── pipelines/
│   │   └── pipeline.py         # Workflow orchestration
│   │
│   └── tools/
│       └── tools.py            # Search & scraping tools
│
└── assets/
    └── architecture.png
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/multiagent-ai-system.git
cd multiagent-ai-system
```

---

# 🐍 Create Environment

## Option 1 — Conda Environment (Recommended)

```bash
conda create -n langagent python=3.12
conda activate langagent
```

---

## Option 2 — Virtual Environment

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# ▶️ Run the Application

## Streamlit Web App

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## CLI Version

```bash
python main.py
```

---

# 🧠 What the System Does

1. Accepts a research topic from the user
2. Searches the web for relevant sources
3. Scrapes and cleans webpage content
4. Generates a detailed research report
5. Critiques and scores the report

---

# 📸 UI Preview

Add screenshots here later:

```text
assets/ui-preview.png
```

---

# ⚡ Example Research Topics

* Future of AI Agents
* AGI Development Roadmap
* Latest Research in Quantum Computing
* AI in Healthcare
* Robotics and Automation Trends

---

# 🔮 Future Improvements

* Async multi-agent execution
* Vector database memory
* RAG integration
* PDF export support
* Multi-source verification
* Agent memory persistence
* LangGraph integration
* Deployment support

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

# 🔐 Security Notes

Never upload your `.env` file or API keys to GitHub.

Add this to `.gitignore`:

```text
.env
__pycache__/
*.pyc
```

---

# 📄 License

This project is licensed under the terms specified in the `LICENSE` file.

---

# ⭐ Acknowledgements

Built using:

* LangChain
* Streamlit
* Google Gemini
* Tavily Search API

---

# 👨‍💻 Author

Developed as a multi-agent AI research system project using modern LLM orchestration techniques.
