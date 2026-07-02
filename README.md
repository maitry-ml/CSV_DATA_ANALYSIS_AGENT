An AI-powered assistant that answers questions about any CSV dataset using natural language. The application automatically decides whether to:

- Query the uploaded CSV using Pandas
- Search the web for general knowledge questions
- Maintain conversation context using memory

Built using LangGraph, LangChain, Gemini, and Streamlit.



------------------------- TECH STACK ----------------------------
-Python
-Streamlit
-LangGraph
-LangChain
-Google Gemini
-Pandas
-DuckDuckGo Search
-Pydantic




-----------------------PROJECT STRUCTURE ----------------------------

CSV_DATA_ANALYSIS_AGENT/
│
├── app.py                # Streamlit interface
├── agent.py              # LangGraph ReAct agent
├── tools.py              # Custom tools
├── prompts.py            # LLM prompts
├── utils.py              # Data loading & Pandas execution
├── llm.py                # Gemini model initialization
├── config.py             # Configuration
├── inventory.csv         # Example dataset
├── requirements.txt
└── README.md

------------------------DEMO-----------------------------------------
Video Link : https://drive.google.com/file/d/1zya76lX9N2LYeVoiq6jBYxysYunpSvW9/view?usp=sharing
