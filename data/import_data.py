import json

question = {}
questions = {}

enunciado = 4
alternativa_correta = 5
alternativa_1 = 6
alternativa_2 = 7
alternativa_3 = 8
pula_linha = 6

with open("fazpergunta/data/sample.txt") as arquivo:
    sample = arquivo.readlines()

questions['etapa'] = sample[0].strip()
questions['modulo'] = sample[1].strip()
questions['problema'] = sample[2].strip()

n_linhas = 0
for linha in sample:
    n_linhas += 1
contador = 4 # primeira linha do enunciado da primeira pergunta
n_questao = 1

while contador <= n_linhas:
    q = "q_" + str(n_questao)
    question['enunciado'] = sample[contador].strip()
    question['a_correta'] = sample[contador + 1].strip()
    question['a_1'] = sample[contador + 2].strip()
    question['a_2'] = sample[contador + 3].strip()
    question['a_3'] = sample[contador + 4].strip()
    n_questao += 1
    contador += 6
    questions[q] = question.copy()
    question = {}


nome_arquivo = f"fazpergunta/data/{questions['etapa']}_{questions['modulo']}_{questions['problema']}.json"

with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
    json.dump(questions, arquivo_json, ensure_ascii=False)
