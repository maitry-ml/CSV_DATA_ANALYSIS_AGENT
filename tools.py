from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from pydantic import BaseModel

from langchain_google_genai import ChatGoogleGenerativeAI
from llm import llm

from utils import query_dataframe, df
from prompts import CODE_GENERATION_PROMPT, SUMMARY_PROMPT
from config import GEMINI_API_KEY, MODEL_NAME





# Helper Function
def answer_question(question: str) -> dict:
    """
    Generates Pandas code, executes it on the dataframe,
    and summarizes the result.
    """

    prompt = CODE_GENERATION_PROMPT.format(
        columns=df.columns.tolist(),
        question=question
    )

    response = llm.invoke(prompt)

    generated_code = (
        response.content
        .replace("```python", "")
        .replace("```", "")
        .strip()
    )

    result = query_dataframe(generated_code)

    summary_prompt = SUMMARY_PROMPT.format(
        question=question,
        result=result
    )

    summary = llm.invoke(summary_prompt)

    return {
        "generated_code": generated_code,
        "result": result,
        "summary": summary.content
    }




# Excel Query Tool

class QueryExcelInput(BaseModel):
    question: str


@tool(args_schema=QueryExcelInput)
def query_excel(question: str) -> str:
    """
    Use this tool to answer questions about the inventory dataset.
    """

    response = answer_question(question)

    return f"""
Generated Code:
{response["generated_code"]}

Result:
{response["result"]}

Summary:
{response["summary"]}
"""



# Search Tool

search = DuckDuckGoSearchRun()


class SearchWebInput(BaseModel):
    question: str


@tool(args_schema=SearchWebInput)
def search_web(question: str) -> str:
    """
    Use this tool for definitions, explanations, concepts,
    or questions that cannot be answered from the inventory dataset.
    """

    return search.invoke(question)
