# subLegalBench_experiment_1
This repository contains all files and codes needed to perform the subLegalBench_experiment_1

Experimento_subLegalBench_1:

Neste experimento não rodaremos todas as tasks do LegalBench, mas apenas um subset. A este conjunto demos o nome de subLegalBench.

Também não usaremos todos os datasets do LawInstruct, mas apenas um subset, chamado de subLawInstruct.

O subLegalBench é, ainda, subdividido em dois grupos de tasks (LJT e PET): um que usa linguajar (LJT - Legal Jargon Tasks) jurídico e outro que usa linguajar comum (PET - Plain English Tasks). A ideia é avaliar se métodos de instruct fine-tuning desempenham de maneira diferente quando o senso comum não é suficiente para executar a task corretamente. Intuitivamente, me parece que, nas tasks que necessitarem de conhecimento específico de domínio, o instruct fine-tuning deverá injetar conhecimento novo e, portanto, desempenhar melhor.

Quanto a isso, o paper do LawInstruct traz um resultado muito interessante (que os autores não conseguiram explicar plenamente, apenas conjecturar possíveis causas): em algumas tasks, o modelo treinado no domínio legal teve performance inferior ao baseline. 
Um teste interessante a fazer aqui é verificar se tal comportamento se repete com o Llama 2 - 7b. Sendo o caso, podemos testar se o data selection é capaz de fazer o modelo treinado desempenhar melhor que o baseline (sem ajuste de domínio)

Vários testes são possíveis:
Fazer uma poda agressiva no SaulLM para usar no lugar do GPT2 (Superfiltering) para calcular o IFD (Instruction Following Difficulty);
Usar embedding do LegalBERT (no lugar do sentence-transformer) para calcular diversidade;
incorporar tf-idf no data selection.




Os métodos de data selection que serão testados são:
M1 - Superfiltering
M2 - Superfiltering.D
M3 - Random
M4 - tfidf + LegalBERT (nosso)

