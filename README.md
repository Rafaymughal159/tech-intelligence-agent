# 🤖 Daily Tech Intelligence Scout

An autonomous AI agent designed to scrape GitHub Trending repositories and generate intelligent technical summaries using the **Gemini 2.5 Flash** model. This project emphasizes resilient system architecture and modern AI SDK orchestration.

## 🚀 Key Features
- **Automated Web Scraping**: Extracts real-time data from GitHub’s trending pages using `BeautifulSoup4`.
- **Resilient AI Logic**: Implemented a custom **Retry-with-Backoff** mechanism to gracefully handle `429 Rate Limits` and `503 Service Unavailable` errors[cite: 1].
- **Adaptive Model Selection**: Logic designed to dynamically query and switch between model versions (2.0 vs 2.5) based on real-time API availability[cite: 1].
- **Secure Configuration**: Uses `python-dotenv` to isolate sensitive API credentials from the codebase, following industry security standards[cite: 1].

## 🛠️ Tech Stack
- **Language**: Python 3.10+[cite: 1]
- **AI SDK**: Google GenAI (Gemini 2.0/2.5)[cite: 1]
- **Libraries**: BeautifulSoup4, Requests, Python-Dotenv[cite: 1]
- **Automation**: GitHub Actions (Daily Cron Schedule)[cite: 1]

## 🧠 Engineering Challenges & Solutions
### 1. SDK Migration & API Drift
Successfully migrated from the deprecated `google-generativeai` package to the 2026-standard `google-genai` SDK, ensuring long-term project stability[cite: 1].

### 2. Quota Management
Implemented a recursive retry loop that detects `RESOURCE_EXHAUSTED` errors and waits for quota resets, ensuring the agent completes its task even during high-traffic periods[cite: 1].

### 3. Environment Variable Conflicts
Resolved system-level authentication collisions by enforcing local `.env` overrides, a critical practice for multi-project development environments[cite: 1].

## ⚙️ Setup & Installation
1. **Clone the repo**:
   ```bash
   git clone [[[https://github.com/Rafaymughal159/tech-intelligence-agent.git](https://github.com/Rafaymughal159/tech-intelligence-agent.git)](https://github.com/Rafaymughal159/tech-intelligence-agent.git)](https://github.com/Rafaymughal159/tech-intelligence-agent.git)
   cd tech-intelligence-agent


## Setup Virtual Environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # venv\Scripts\activate on Windows
    pip install -r requirements.txt

**Configure API Key**:
   Create a `.env` file and add:
   ```text
   GEMINI_API_KEY=your_key_here
 ```
 
## Run the Agent:
```bash
    python main.py
