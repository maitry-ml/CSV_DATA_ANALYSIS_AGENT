
#Making gemini generate pandas code from question

CODE_GENERATION_PROMPT = """
You are an expert Python and Pandas programmer.

The dataframe is called df.

The dataframe columns are:
{columns}

Write Python Pandas code to answer the user's question.

Rules:
- Return ONLY executable Python code.
- Do NOT include ```python or ``` fences.
- Do NOT print anything.
- Store the final answer in a variable called result.
- Use only the dataframe named df.

User Question:
{question}
"""




#Summarizing the result in english

SUMMARY_PROMPT = """
You are a helpful data analyst.

The user asked:{question}

The dataframe result is:{result}

Explain the answer in simple English.
Don't mention Python or Pandas.
"""