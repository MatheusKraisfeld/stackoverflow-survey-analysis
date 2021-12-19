import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

import data

st.write("# Análise de pesquisa do Stack Overflow no ano de 2021")


def overview():
    st.write("---")
    st.write("## Overview")
    st.write(
        "##### Este trabalho de análise foi executado com base nos dados disponibilizados em [Stack Overflow Insights](https://insights.stackoverflow.com/survey).\
        Nesse link é possível visualizar o estudo realizado a partir dos dados coletados ano a ano, inclusive os dados referentes ao ano de 2021.\
        Além do estudo realizado a partir da pesquisa, é possível fazer o _download_ dos dados em formato _CSV_, sendo este o dataset utilizado para o desenvolvimento do estudo a seguir."
    )


def nivel_tecnico():
    st.write("---")
    branch = {
        "I am a developer by profession": "Professional",
        "I code primarily as a hobby": "Hobby",
        "I used to be a developer by profession, but no longer am": "Ex-professional",
        "I am not primarily a developer, but I write code sometimes as part of my work": "Adventurer",
        "I am a student who is learning to code": "Student",
        "None of these": "None of these",
    }

    st.write("# Nível técnico")
    st.write(
        "##### A coluna do dataset analisada foi a `MainBranch`. Os valores da coluna foram convertidos buscando ganho de processamento ao realizar as análises, e essa conversão está representada a seguir: "
    )
    st.write(branch)
    st.write(
        "##### Com a análise dessas informações, foi construído o seguinte gráfico:"
    )

    with st.expander("Nível técnico"):
        fig, ax = plt.subplots()
        graph = data.questao1()
        graph = graph.sort_values(ascending=True)
        ax.pie(graph.values, labels=graph.index)
        ax.legend(loc="lower right")
        plt.tight_layout()
        st.pyplot(fig)

    st.write(
        "##### Como podemos perceber, dentre os usuários que responderam a pesquisa, 69.7% se consideram profissionais.\
        Em contrapartida, com o menor índice, temos 0.61% que não se sentem representados por nenhuma das categorias citadas."
    )


# --------------------------------------------------------------------------------------------------------------------------------
def distr_por_localidade():
    st.write("---")
    st.write("# Distribuição das pessoas que responderam por localidade")
    st.write(
        "##### Para encontrar a distribuição de respostas por localidade, foi analisada a coluna `Country`, cujos valores são os nomes dos países das pessoas que responderam a pesquisa.\
        Dentre os países com maior número de respostas, foram selecionados os 20 países que lideraram esse rank."
    )

    with st.expander("Distribuição das pessoas que responderam por localidade"):
        fig, ax = plt.subplots()
        graph = data.questao2()
        ax.barh(graph.index, graph.values.squeeze())
        ax.set_xlabel("Quantidade de respostas")
        # ax.bar_label(ax.containers[0])
        st.pyplot(fig)

    st.write(
        "##### O gráfico mostra que o maior número de respostas foi dado nos Estados Unidos, sendo mais de 15 mil respostas. Já o Brasil aparece na sétima posição, com mais de 2 mil respostas."
    )


# --------------------------------------------------------------------------------------------------------------------------------
def distr_nivel_estudo():
    st.write("---")

    st.write("# Distribuição do nível de estudo dos participantes")
    st.write(
        "##### A análise do nível de estudo dos participantes foi feita com base na coluna `EdLevel`."
    )
    with st.expander("Distribuição do nível de estudo dos participantes"):
        fig, ax = plt.subplots()
        graph = data.questao3()
        ax.barh(graph.index, graph.values.squeeze())
        ax.set_xlabel("Quantidade de respostas")
        ax.bar_label(ax.containers[0])
        st.pyplot(fig)

    st.write(
        "##### Como podemos observar no gráfico, o grau de estudo com maior número de entrevistados é Bachelor's Degree, ou seja, Bacharel, com mais de 35 mil das pessoas que responderam ao questionário.\
        Em contrapartida, o grau com menor número de entrevistados é Professional Degree, o que seria o equivalente a um curso técnico no Brasil."
    )


# --------------------------------------------------------------------------------------------------------------------------------
def tempo_por_tipo_de_profissional():
    st.write("---")
    st.write("# Distribução de tempo de trabalho para cada tipo de profissional")
    st.write(
        "##### De acordo com a coluna `MainBranch`, e aplicando o mesmo tratamento de conversão dos dados da análise de quantidade de profissionais por nível técnico, foi feita a análise do tempo\
        de trabalho por tipo de profissional."
    )
    with st.expander("Distribução de tempo de trabalho para cada tipo de profissional"):
        fig, ax = plt.subplots()
        graph = data.questao4()
        print(graph.index)
        ax.hist(graph.index, 10, density=True, histtype="bar", stacked=True)
        plt.tight_layout()
        st.pyplot(fig)


# --------------------------------------------------------------------------------------------------------------------------------
def trabalham_profissionalmente():
    st.write("---")
    st.write("# Das pessoas que trabalham profissionalmente...")
    st.write(
        "##### Com base na coluna `MainBranch`, foram selecionadas as pessoas que declararam trabalhar profissionalmente. \
        Para a análise da profissão, foi utilizada a coluna `Employment`. Já para analisar o nível de escolaridade, a coluna do dataset foi `EdLevel`. \
        Por fim, para a análise do tamanho das empresas, foi utilizada a coluna `OrgSize`."
    )
    graph = data.questao5()

    st.write("## Profissão")
    with st.expander("Profissão"):
        fig, ax = plt.subplots()
        ax.barh(graph[0].index, graph[0].values.squeeze())
        ax.set_xlabel("Quantidade de respostas")
        ax.bar_label(ax.containers[0])
        st.pyplot(fig)

    st.write("## Escolaridade")
    with st.expander("Escolaridade"):
        fig, ax = plt.subplots()
        ax.barh(graph[1].index, graph[1].values.squeeze())
        ax.set_xlabel("Quantidade de respostas")
        ax.bar_label(ax.containers[0])
        st.pyplot(fig)

    st.write("## Tamanho das empresas")
    with st.expander("Tamanho das empresas"):
        fig, ax = plt.subplots()
        ax.barh(graph[2].index, graph[2].values.squeeze())
        ax.set_xlabel("Quantidade de respostas")
        ax.bar_label(ax.containers[0])
        st.pyplot(fig)

    st.write(
        "##### Para o gráfico da profissão, observamos que o maior número de entrevistados, mais de 46 mil, se enquadra na categoria Employed full-time, trabalhador em tempo integral. \
        Já no gráfico de escolaridade, mais de 28 mil das pessoas que responderam a pesquisa se encaixam na categoria Bachelor's Degree, que seria o grau de graduaçao completa. \
        Por fim, o gráfico de tamanho das empresas nos mostra que mais de 11 mil dos entrevistados trabalham em empresas com 20 a 99 funcionários."
    )


# --------------------------------------------------------------------------------------------------------------------------------
def media_salarial():
    st.write("---")
    st.write("# Média salarial")
    st.write(
        "##### Para analisar a média salarial das pessoas que responderam ao questionário, foi utilizada a coluna `ConvertedCompYearly`."
    )

    with st.expander("Média salarial"):
        fig, ax = plt.subplots()
        graph = data.questao6()
        st.write(graph)


# --------------------------------------------------------------------------------------------------------------------------------
def salario_paises_mais_responderam():
    st.write("---")
    st.write("# Salário nos 5 países que mais responderam")
    st.write(
        "##### Para essa análise, foram selecionados atráves da coluna `Country`, os países com maior número de respostas. \
        Em seguida, foi calculada a média de salário recebido nesses países utilizando a coluna `ConvertedCompYearly`."
    )
    with st.expander("Salário nos 5 países que mais responderam"):
        fig, ax = plt.subplots()
        graph = data.questao7()
        graph = graph.sort_values(ascending=True)
        ax.barh(graph.index, graph.values.squeeze())
        ax.set_xlabel("Valor do salário")
        ax.bar_label(ax.containers[0])
        st.pyplot(fig)
    st.write(
        "##### Como podemos observar, os Estados Unidos possuem a maior média salarial entre os países que mais responderam."
    )


# --------------------------------------------------------------------------------------------------------------------------------
def porcentagem_python():
    st.write("---")
    st.write("# Porcentagem das pessoas que trabalham com Python")
    st.write(
        "##### Buscando a porcentagem das pessoas que responderam e trabalham com Python, foi analisada a coluna `LanguageHaveWorkedWith`, \
        e calculada a porcentagem em relação ao total de respostas."
    )
    with st.expander("Porcentagem das pessoas que trabalham com Python"):
        graph = data.questao8()
        st.write(f"{graph}%")


# --------------------------------------------------------------------------------------------------------------------------------
def sobre_python():
    st.write("# Sobre python...")
    st.write(
        "##### Buscando encontrar as pessoas que trabalham com Python, primeiramente foi analisada a coluna `LanguageHaveWorkedWith` para encontrar todos os desenvolvedores Python. \
        Para analisar o nível de salário globalmente, foi calculada a média de salário disponibilizada na coluna `ConvertedCompYearly` para os desenvolvedores selecionados anteriormente. \
        Já para o nível de salário no Brasil, foi utilizada a coluna `Country` para encontrar as pessoas que responderam e residem no país. \
        Para analisar a média salarial nos 5 países que mais participaram da pesquisa, foram selecionados todos os desenvolvedores Python que residem nos 5 países que mais responderam, segundo a \
        contagem de respostas pela coluna `Country`. Em seguida, calculou-se a média dos salários."
    )
    graph = data.questao9()

    st.write("## Nível de salário globalmente")
    with st.expander("Nível de salário globalmente"):
        st.write(graph[0])

    st.write("## Nível de salário no Brasil")
    with st.expander("Nível de salário no Brasil"):
        st.write(graph[1])

    st.write("## Média salarial para os 5 países que mais participaram")
    with st.expander("Média salarial para os 5 países que mais participaram"):
        fig, ax = plt.subplots()
        ax.barh(graph[2].index, graph[2].values.squeeze())
        ax.set_xlabel("Valor do salário")
        ax.bar_label(ax.containers[0])
        st.pyplot(fig)

    st.write("##### ")


# --------------------------------------------------------------------------------------------------------------------------------
def sistemas_operacionais():
    st.write("---")
    st.write("# Sistemas operacionais utilizados")
    st.write(
        "##### Para listar os sistemas operacionais utilizados, foram selecionados os valores únicos da coluna `OpSys`."
    )
    with st.expander("Sistemas operacionais utilizados"):
        fig, ax = plt.subplots()
        graph = data.questao10()
        ax.barh(graph.index, graph.values.squeeze())
        ax.set_xlabel("Quantidade de respostas")
        ax.bar_label(ax.containers[0])
        st.pyplot(fig)

    st.write(
        "##### Como podemos observar, mais de 37 mil pessoas responderam ser usuárias de Windows, seguidos por aproximadamente 20 mil usuários de MacOS e 20 mil de sistemas baseados em Linux."
    )


# --------------------------------------------------------------------------------------------------------------------------------
def python_sistemas_operacionais():
    st.write("---")
    st.write(
        "# Distribuição de sistema operacional utilizado por desenvolvedores Python"
    )
    st.write(
        "##### Para essa análise, primeiramente foram selecionados os desenvolvedores Python através da coluna `LanguageHaveWorkedWith`. \
        Em seguida, foram selecionados os sistemas operacionais segundo a coluna `OpSys`."
    )
    with st.expander(
        "Distribuição de sistema operacional utilizado por desenvolvedores Python"
    ):
        fig, ax = plt.subplots()
        graph = data.questao11()
        ax.barh(graph.index, graph.values.squeeze())
        ax.set_xlabel("Quantidade de respostas")
        ax.bar_label(ax.containers[0])
        st.pyplot(fig)

    st.write(
        "##### Como está representado no gráfico, mais de 15 mil desenvolvedores Python utilizam o sistema operacional Windows, seguidos por mais de 12 mil usuários de sistemas baseados em Linux."
    )


# --------------------------------------------------------------------------------------------------------------------------------
def faixa_etaria():
    st.write("---")
    st.write("# Faixa etária com mais pessoas que responderam")
    st.write(
        "##### Buscando encontrar a faixa etária com maior número de respostas, foi utilizada a coluna `Age`. \
        Os valores foram ordenados e a faixa etária com maior número de respostas foi selecionada."
    )
    with st.expander("Faixa etária com mais pessoas que responderam"):
        graph = data.questao12()
        st.write(graph)


# --------------------------------------------------------------------------------------------------------------------------------
def faixa_etaria_python():
    st.write("---")
    st.write("# Faixa etária com mais desenvolvedores Python")
    st.write(
        "##### Para encontrar a faixa etária com maior número de desenvolvedores Python, inicialmente foram selecionados todos os desenvolvedores Python através da coluna `LanguageHaveWorkedWith`. \
        Em seguida, foi selecionada a faixa etária com maior número de respostas segundo a coluna `Age`."
    )
    with st.expander("Faixa etária com mais desenvolvedores Python"):
        graph = data.questao13()
        st.write(graph)


def exibir_estudo():
    overview()
    nivel_tecnico()
    distr_por_localidade()
    distr_nivel_estudo()
    tempo_por_tipo_de_profissional()
    trabalham_profissionalmente()
    media_salarial()
    salario_paises_mais_responderam()
    porcentagem_python()
    sobre_python()
    sistemas_operacionais()
    python_sistemas_operacionais()
    faixa_etaria()
    faixa_etaria_python()


exibir_estudo()
