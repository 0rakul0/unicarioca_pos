# unicarioca_pos

## introdução
<br>
Com o que podemos chamar de marco da computação casual a liberação do ChatGPT para uso comercial em larga escala, desencadeou a corrida por novas formas de integração da computação com as inteligências artificias casuais, tais essas que vão de simples tarefas de uma simples conversa a funcionar como auxiliar de programação em qualquer linguagem de computação, hoje nós temos empresas como Meta e Google entre outras que estão nessa corrida em busca de espaço nessa nova categoria de uso casual.
<br>
O objetivo desse projeto é como utilizar a tecnologia do ChatGPT para APIs e como o implementar em projetos já em curso de desenvolvimento. E compará-la a outros métodos como LSTM e VADER ambos funcionando como ferramenta de análise de sentimentos, para uso de analisar comentários vindos do Instagram ou outra rede social.
<br>
A base de dados utilizada é a X antigo Twitter para analisar comentários de voos em inglês.
<br>
está na pasta de twitters
<hr>

## planejamento
<br>
Para a base do nosso projeto é a interpretação de frases para detecção se os comentários sobre o assunto estão sendo positivos ou negativos, a implementação pode ser feita em perfils de usuários (empresas) do Instagram, facebook ou qualquer sistema que possa ter uma RPA para buscar os comentários, com isso o propósito é que tenha um feedback melhor para próximos eventos visto que as vezes temos milhares de comentários e analisar um a um leva um tempo considerável.
<br>
A proposta do trabalho é ver qual o melhor analisador de sentimentos assim comparar as respostas entre ChatGPT e um analisador NLP, já com essa análise de sentimentos o tempo pode ser encurtado para um engajamento melhorado e até uma nova tomada de decisão do gestor, de qual tecnologia implementar em suas redes Sociais.
<br>
Para acesso a os comentários usaremos uma base de dados fornecida pela empresa, também usaremos outras bases de treino para validar nosso analisador assim conseguindo uma acurácia melhor do analisador.
<br>
De linguagem de programação será usado o python, visto que temos um amplo auxílio de libs e referencias.

### Pipeline:
- O implementador do ChatGPT irá apontar se o comentário é positivo, negativo ou neutro.
<br>
Como o ChatGPT já interpreta o texto no idioma que o texto é introduzido, não é necessidade de um tratamento prévio como os outros modelos.
### Esquema logico da classe sentimento:
- input_texto > analisador > resposta > positivo | negativo | neutro
<hr>

## Controle e Monitoramento
<br>
O modelo implementado foi o gpt-3.5-turbo – por já ter apresentado resultados muito bons ao longo do tempo, porém tivemos que implementar regras em suas saídas pedindo para ele limitar as respostas em somente três categorias positivo, negativo ou neutro.
<br>
Sem essas restrições de resposta ele tem uma alta perda de acurácia, mas quando damos regras de como ele tem que analisar a frase ele nos retorna 99% de acerto.
<br>
Já o modelo LSTM, tivemos uma acurácia de 70% dos casos visto que LSTM tem um problema de manter informações de contexto, além de um custo computacional muito alto. Sendo necessário treinar o modelo com GPU.
<br>
Os modelos de VADER e SUPERVISIONADO mostraram ter uma acurácia abaixo de 45%, sendo estes. 
<br>
Modelo Supervisionado tendo uma acurácia de 41%.
<br>
Modelo Vader (modelo por regras) acurácia de 44%


| Modelo            | Acurácia |
|-------------------|----------|
| Sem restrições    | 99%      |
| LSTM              | 70%      |
| VADER             | 44%      |
| SUPERVISIONADO    | 41%      |


| Software       | Versão/Configuração  |
|----------------|----------------------|
| Tensorflow     | >= 2.0               |
| NLTK           |                      |
| Python         | 3.9                  |

| Hardware       | Configuração         |
|----------------|----------------------|
| Processador    | Ryzen 7 2700x        |
| Memória RAM    | 16 GB                |
| GPU            | RTX 3050             |

## Conclusão
<br>
A vantagem de usar o ChatGPT como motor de NLP, é que ele entende uma gama de outros idiomas, assim economizando tempo e esforço no desenvolvimento de outros motores de NLP de linguagem específica.
<br>
Vale lembrar que existem custos de se o utilizar e um tempo de uso de 3 meses, mas para uso de implementação rápida é uma excelente escolha.