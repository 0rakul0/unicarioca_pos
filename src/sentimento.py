import openai
import os

openai.api_key = '<sua chave de api>'

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


if __name__ == "__main__":
    r = sentimento()
    texto_teste = 'você está tão natural nessa foto, esse ensaio foi perfeito!!'
    sent = r.run(texto=texto_teste)
    print(sent)