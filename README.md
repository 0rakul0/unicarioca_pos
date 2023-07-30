# unicarioca_pos

## introdução
<br>
Com o que podemos chamar de marco da computação casual a liberação do ChatGPT para uso comercial em larga escala, desencadeou a corrida por novas formas de integração da computação com as inteligências artificias casuais, tais essas que vão de simples tarefas de uma simples conversa a funcionar como auxiliar de programação em qualquer linguagem de computação, hoje nós temos empresas como Meta e Google entre outras que estão nessa corrida em busca de espaço nessa nova categoria de uso casual.
<br>
O objetivo desse projeto é como utilizar a tecnologia do ChatGPT para APIs e como o implementar em projetos já em curso de desenvolvimento. 

<hr>

## planejamento
<br>
Para a base do nosso projeto é a interpretação de frases para detecção se os comentários sobre o assunto estão sendo positivos ou negativos, a implementação pode ser feita em perfils de usuários ( empresas ) do Instagram, facebook ou qualquer sistema que possa ter uma RPA para buscar os comentários, com isso o proposito é que tenha um feedback melhor para próximos eventos visto que as vezes temos milhares de comentários e analisar um a um leva um tempo considerável, já com essa analise de sentimentos via ChatGPT o tempo pode ser encurtado para um engajamento melhorado e até uma nova tomada de decisão do gestor.
<br>
Para acesso a página e comentários usaremos a linguagem Python.

### Pipeline:
- O implementador do ChatGPT irá apontar se o comentário é positivo, negativo ou neutro.

<hr>

## Prototipo
<br>
O modelo implementado foi o gpt-3.5-turbo – por já ter apresentado resultados muito bons ao longo do tempo.
<br>

### Esquema logico da classe sentimento:
- input_texto > analisador > resposta > positivo | negativo | neutro

### codigo
````python
import openai
from env import secret
openai.api_key = secret.API_KEY

class sentimento():
    def mensage(sefl,pergunta):
        resultado = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role":"user", 'content':pergunta}]
        )
        return resultado.choices

    def run(self, texto):
        prompt = f"qual o sentimento da frase {texto} é bom, ruim ou neutro?"

        resposta = self.mensage(prompt)

        resposta_str = ''.join(resposta[0]['message']['content'])

        palavras_positivas = ["bom", "ótimo", "positivo", "satisfação", "excelente", "incrível", "maravilhoso", "ótima",
                              "alegre", "feliz"]

        palavras_negativas = ["ruim", "horrível", "negativo", 'terrível', 'feio', "triste", "péssimo", "detestável",
                              "miserável", "lamentável"]

        resposta_lower = resposta_str.lower()

        if any(palavra in resposta_lower for palavra in palavras_positivas):
            resposta_sentimento = 'positivo'
        elif any(palavra in resposta_lower for palavra in palavras_negativas):
            resposta_sentimento = 'negativo'
        else:
            resposta_sentimento = 'neutro'

        return resposta_sentimento
````
### Formas de uso
````python

r = sentimento()
texto_teste = 'você está tão natural nessa foto, esse ensaio foi perfeito!!'
sent = r.run(texto=texto_teste)
print(sent)
````
<hr>

## Conclusão
<br>
A vantagem de usar o chatgpt como motor de NLP é que ele entende uma gama de outros idiomas, assim economizando tempo e esforço no desenvolvimento de outros motores de NLP de linguagem específica.
<br>
Vale lembrar que existem custos de se o utilizar e um tempo de uso de 3 meses.
<br>
Outras aplicações para análise de sentimentos pode ser usando o transformes existem muitos exemplos já pre-compilados no site do [Hugging Face – The AI community building the future](https://huggingface.co/ )