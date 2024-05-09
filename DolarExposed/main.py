import requests
import tweepy
import time
import datetime

consumer_key = 'sWGA4nCq8b5VIPeqTTosrg719'
consumer_secret = 'yWX2XUxHnL3pZSREflXKNeXlPwFVYn4BigtE33M9Nb378OvQIZ'
access_token = '1785330303986196481-rdFZyKE4cjnOV5neRVsKLY5aMlxtkV'
access_token_secret = 'rP0Hb0Rs58DNTMPaIpZMzpMPpVLx4iXIcfcZrvSKRwTrr'

auth = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

intervalo_verificacao = 7200
horario_inicio = "09:30"
horario_termino = "18:00"


def obter_cotacao_dolar():
    try:
        url_cotacao = "https://api.invertexto.com/v1/currency/USD_BRL?token=7628|bjKqMASWARNfzV0hhMCQM8BeoYf0uQdW"
        response = requests.get(url_cotacao)
        dados_cotacao = response.json()
        if response.status_code == 200 and "USD_BRL" in dados_cotacao:
            valor_dolar = dados_cotacao["USD_BRL"]["price"]
            valor_formatado = "{:.2f}".format(valor_dolar)
            return valor_formatado
        else:
            print(f"Erro ao obter dados do dólar: {dados_cotacao}")
            return None

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None


def publicar_tweet(valor_dolar):
    texto_tweet = f"Dólar agora: R$ {valor_dolar} 🎯"
    try:
        auth.create_tweet(text=texto_tweet)
        print(f"Tweet publicado: {texto_tweet}")
    except Exception as e:
        print(f"Erro ao publicar tweet: {e}")
while True:
    agora = datetime.datetime.now()
    horario_atual = agora.strftime("%H:%M")
    if horario_inicio <= horario_atual <= horario_termino:
        valor_dolar = obter_cotacao_dolar()
        if valor_dolar:
            publicar_tweet(valor_dolar)
   
    time.sleep(intervalo_verificacao)
