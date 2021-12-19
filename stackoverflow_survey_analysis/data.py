from pathlib import Path

import numpy as np
import pandas as pd

df_survey = pd.read_csv("stackoverflow-2021/survey_results_public.csv")
new_df = pd.read_csv("stackoverflow-2021/survey_results_public.csv")
# 0 - Tratamento dos dados
"""df_survey["YearsCodePro"] = df_survey["YearsCodePro"].fillna(0)
df_survey["YearsCodePro"] = (
    df_survey["YearsCodePro"]
    .replace("Less than 1 year", 0)
    .replace("More than 50 years", 51)
).astype(int)
"""
col_numbers = [
    "ResponseId",
    "YearsCode",
    "YearsCodePro",
    "CompTotal",
    "ConvertedCompYearly",
]
df_survey.loc[:, col_numbers] = df_survey.loc[:, col_numbers].apply(
    pd.to_numeric, args=("coerce",), axis="index"
)
mean_na_numbers = df_survey[col_numbers].apply(pd.Series.mean, axis="index").astype(int)

for col in col_numbers:
    df_survey.get(col).fillna(mean_na_numbers.get(col), inplace=True)

col_string = tuple(set(df_survey.columns) - set(col_numbers))
df_survey.loc[:, col_string] = df_survey.loc[:, col_string].astype("string")

branch = {
    "I am a developer by profession": "Professional",
    "I code primarily as a hobby": "Hobby",
    "I used to be a developer by profession, but no longer am": "Ex-professional",
    "I am not primarily a developer, but I write code sometimes as part of my work": "Adventurer",
    "I am a student who is learning to code": "Student",
    "None of these": "None of these",
}
df_survey["MainBranchSimplified"] = pd.Series(
    df_survey["MainBranch"].apply(lambda x: branch.get(x, "not_informed")),
    dtype=pd.StringDtype(),
)
df_survey.drop(labels="MainBranch", axis="columns", inplace=True)

# 1 - Porcentagem das pessoas que responderam que se consideram profissionais, não profissionais, estudante, hobby...
def questao1():
    # pd.options.display.float_format = "{:.2%}".format
    # print(MainBranchSimplified.value_counts(normalize=True))
    return round(
        df_survey["MainBranchSimplified"].value_counts(normalize=True).multiply(100), 2
    )


# 2 - Distribuição das pessoas que responderam por localidade (top 20). Qual o país que teve maior participação?
def questao2():
    """print(
        df_survey.groupby(["Country"])
        .size()
        .to_frame("Size")
        .sort_values("Size", ascending=False)[:21]
    )"""
    return (
        df_survey.groupby(["Country"])
        .size()
        .to_frame("Size")
        .sort_values("Size", ascending=True)
        .tail(20)
    )


# 3 - Qual a distribuição nível de estudo dos participantes?
def questao3():
    # print(df_survey.groupby(["EdLevel"]).size().to_frame("Size"))
    return df_survey.groupby(["EdLevel"]).size().to_frame("Size").sort_values("Size")


# 4 - Qual a distribução de tempo de trabalho para cada tipo de profissional respondido na questão 1
def questao4():
    codePro = (
        df_survey.groupby(["MainBranchSimplified", "YearsCodePro"])
        .agg(count_years=("YearsCodePro", "count"))
        .sort_values("count_years", ascending=True)
    )
    return codePro


# 5 - Das pessoas que trabalham profissionalmente:
def questao5():
    # Qual a profissão delas?

    professionals = df_survey[df_survey["MainBranchSimplified"] == "Professional"]
    # print(professionals["Employment"])
    employment = (
        professionals.groupby(["Employment"])
        .size()
        .to_frame("Size")
        .sort_values("Size", ascending=True)
    )

    # Qual a escolaridade?
    # print(professionals["EdLevel"])
    edLevel = (
        professionals.groupby(["EdLevel"])
        .size()
        .to_frame("Size")
        .sort_values("Size", ascending=True)
    )

    # Qual o tamanho das empresas?
    # print(professionals["OrgSize"])
    orgSize = (
        professionals.groupby(["OrgSize"])
        .size()
        .to_frame("Size")
        .sort_values("Size", ascending=True)
    )

    return [employment, edLevel, orgSize]


# 6 - Média salarial das pessoas que responderam
def questao6():
    # print(df_survey["ConvertedCompYearly"].mean())
    return "${:,.2f}".format(round(df_survey["ConvertedCompYearly"].mean(), 2))


# 7 - Pegando os 5 países que mais responderam o questionário, qual é o salário destas pessoas?
def questao7():
    countries = (
        df_survey.groupby(["Country"])
        .size()
        .to_frame("Size")
        .sort_values("Size", ascending=False)
        .head(5)
    )
    data = df_survey.loc[df_survey["Country"].isin(countries.index.values)]
    data = data.groupby(["Country"])["ConvertedCompYearly"].mean()
    return data


# 8 - Qual a porcentagem das pessoas que trabalham com python?
def questao8():
    return round(
        df_survey[df_survey["LanguageHaveWorkedWith"].str.contains("Python")].shape[0]
        / df_survey.shape[0]
        * 100,
        2,
    )


# 9 - Sobre python:
def questao9():
    # Qual o nível de salário globalmente?
    python_devs = df_survey[df_survey["LanguageHaveWorkedWith"].str.contains("Python")]
    # print("${:,.2f}".format(round(python_devs["ConvertedCompYearly"].mean(), 2)))
    salarioGlobalmente = "${:,.2f}".format(
        round(python_devs["ConvertedCompYearly"].mean(), 2)
    )

    # E para o Brasil?
    # print("${:,.2f}".format(round(python_devs[python_devs["Country"] == "Brazil"]["ConvertedCompYearly"].mean(),2,)))
    salarioBrasil = "${:,.2f}".format(
        round(
            python_devs[python_devs["Country"] == "Brazil"][
                "ConvertedCompYearly"
            ].mean(),
            2,
        )
    )

    # Qual a média salarial para os 5 países que mais participaram?
    countries = (
        df_survey.groupby(["Country"])
        .size()
        .sort_values(ascending=False)
        .head(5)
        .index.values
    )
    python_devs_in_countries = python_devs[python_devs["Country"].isin(countries)]
    data = python_devs_in_countries.groupby(["Country"])["ConvertedCompYearly"].mean()
    data = data.sort_values(ascending=True)

    return [salarioGlobalmente, salarioBrasil, data]


# 10 - De todas as pessoas, qual o sistema operacional utilizado por elas?
def questao10():
    return (
        df_survey.groupby(["OpSys"])
        .size()
        .to_frame("Size")
        .sort_values("Size", ascending=True)
    )


# 11 - Das pessoas que trabalham com python, qual a distribuição de sistema operacional utilizado por elas
def questao11():
    python_devs = df_survey[df_survey["LanguageHaveWorkedWith"].str.contains("Python")]
    return (
        python_devs.groupby(["OpSys"])
        .size()
        .to_frame("Size")
        .sort_values("Size", ascending="True")
    )


# 12 - Qual a média de idade das pessoas que responderam? / Qual a faixa etária com mais pessoas que responderam?
def questao12():
    return (
        df_survey.groupby(["Age"])
        .size()
        .to_frame("Quantidade de respostas")
        .sort_values("Quantidade de respostas", ascending=False)
        .head(1)
    )


# 13 - E em python? Qual a média de idade? / Qual a faixa etária com mais pessoas?
def questao13():
    python_devs = df_survey[df_survey["LanguageHaveWorkedWith"].str.contains("Python")]
    return (
        python_devs.groupby(["Age"])
        .size()
        .to_frame("Quantidade de respostas")
        .sort_values("Quantidade de respostas", ascending=False)
        .head(1)
    )
