import pandas as pd

# filepath = "C:/Users/FerGo/OneDrive/ACIT/2022/02.2022/Dictionary/CSV files/F.csv"


def base_formater(filepath: str):
    base = pd.read_csv(filepath)

    base.columns = ["letter"]

    words_df = base["letter"].str.split(n=1, expand=True)
    words_df.columns = ["word", "definition"]
    definitions_df = words_df["definition"].str.split(")", n=1, expand=True)
    definitions_df.columns = ["uses", "definition"]

    dictionary = pd.DataFrame(words_df["word"])
    dictionary["uses"] = definitions_df["uses"]
    dictionary["definition"] = definitions_df["definition"]

    return dictionary

