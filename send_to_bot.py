import os 
from dotenv import load_dotenv
import asyncio
from telegram import Bot
from telegram.error import TelegramError
import argparse

# Carregar as variáveis do arquivo config.env
load_dotenv("config.env")

# Obtém os valores do token e chat ID
token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

# Valida se os dados foram carregados corretamente
if not token or not chat_id:
    raise ValueError("Token ou Chat ID não encontrados no arquivo config.env")

# Cria o objeto Bot com o token fornecido
bot = Bot(token)

# Função assíncrona para enviar a mensagem
async def send_message(message):
    try:
        await bot.send_message(chat_id=chat_id, text=message)
        print("Mensagem enviada com sucesso!")
    except TelegramError as e:
        print(f"Erro ao enviar mensagem: {e}")

# Função principal para rodar a tarefa assíncrona
async def main(message):
    await send_message(message)

# Adiciona o suporte ao argumento --message
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enviar uma mensagem para o Telegram.")
    parser.add_argument(
        '--message', 
        required=True, 
        help='Mensagem a ser enviada para o Telegram.'
    )
    args = parser.parse_args()

    asyncio.run(main(args.message))
