import pandas as pd
from config import FILE_PATH


def load_dataframe():
    """Loading the inventory dataset and clean the column names."""

    df = pd.read_csv(FILE_PATH)

    df.columns = (
        df.columns
          .str.replace("\n", " ", regex=False)
          .str.replace("  ", " ", regex=False)
          .str.strip()
    )

    return df



df = load_dataframe()




def query_dataframe(code: str):
    """Executes generated pandas code on the inventory dataframe.
       The generated code must store its final answer 
       in a variable called 'result'."""
       
    local_vars = {"df": df}

    try:
        exec(code, {}, local_vars)

        if "result" in local_vars:
            return local_vars["result"]

        return "Code executed successfully."

    except Exception as e:
        return str(e)