import pandas as pd

def grade(score):
    if score >= 80: return "A"
    elif score >= 70: return "B"
    elif score >= 60: return "C"
    elif score >= 50: return "D"
    else: return "F"

def process_results(filepath):
    df = pd.read_excel(filepath)

    df["CA"] = df["emt1"] + df["emt2"] + df["assignment"] + df["project"]
    df["total"] = df["CA"] + df["exam"]
    df["grade"] = df["total"].apply(grade)

    cumulative = df.groupby("name")["total"].mean().reset_index(name="cumulative_average")
    df = df.merge(cumulative, on="name")

    ranks = cumulative.sort_values("cumulative_average", ascending=False).reset_index(drop=True)
    ranks["position"] = ranks.index + 1

    df = df.merge(ranks, on="name")

    return df
