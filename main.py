import os
from dotenv import load_dotenv
import logging

from notifications import Email

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD_APP = os.getenv("PASSWORD_APP")

logging.basicConfig(
    filename="buscador_precos.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s no arquivo %(filename)s e função %(funcName)s na linha %(lineno)d:  %(message)s",
)

def main():
    lista_produtos = [
        {"nome": "Produto 1", "preco": "R$ 500,00", "loja": "Loja A", "link": "#"},
        {"nome": "Produto 2", "preco": "R$ 150,00", "loja": "Loja B", "link": "#"},
        {"nome": "Produto 3", "preco": "R$ 300,00", "loja": "Loja C", "link": "#"},
        {"nome": "Produto 4", "preco": "R$ 799,99", "loja": "Loja D", "link": "#"},
    ]
    email = Email(EMAIL, PASSWORD_APP, logging)
    email.enviar_email("gleyson.rcosta@gmail.com", lista_produtos)

if __name__ == "__main__":
    main()