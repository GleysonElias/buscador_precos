from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

class Email:
    def __init__(self, email, password, logging):
        self.__email = email
        self.__password = password
        self.__servidor_smtp = "smtp.gmail.com"
        self.__porta = 587
        self.__logging = logging

    def formatar_html(self, lista_produtos):

        html = "<h2>Alerta de Preço - Buscador de Preços</h2>"

        for produto in lista_produtos:
            nome = produto["nome"]
            preco = produto["preco"]
            loja = produto["loja"]
            link = produto["link"]

            html += f"""
                <div>
                    <h3>{nome}</h3>
                    <p>Preço: {preco}</p>
                    <p>Loja: {loja}</p>
                    <a href="{link}">Ver Produto</a>
                </div>
            """
        
        return(html)

    def enviar_email(self, cliente_email, lista_produtos=[]):
        data_atual = datetime.now()
        data_formatada = data_atual.strftime("%d/%m/%Y")

        mensagem = MIMEMultipart()
        mensagem["From"] = self.__email
        mensagem["To"] = cliente_email
        mensagem["Subject"] = f"Alerta de preço - Buscador de Preços - Dia {data_formatada}"
        print(f"Enviando email para {cliente_email}... no dia {data_formatada}")
        
        corpo_html = self.formatar_html(lista_produtos)
        mensagem.attach(MIMEText(corpo_html, "html"))

        try:
            servidor = SMTP(self.__servidor_smtp, self.__porta)
            servidor.starttls()
            servidor.login(self.__email, self.__password)
            servidor.sendmail(self.__email, cliente_email, mensagem.as_string())
            servidor.quit()
            self.__logging.info(
                f"Email enviado com sucesso para {cliente_email} no dia {data_formatada}"
                )
        except Exception as e:
            self.__logging.error(f"Erro ao conectar ao servidor SMTP: {e}")
