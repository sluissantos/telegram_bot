import asyncio
from telegram import Bot
from telegram.error import TelegramError
import argparse
import sys

# Substitua pelo token do seu bot
token = '7682976744:AAHtEmUeFnm43eBIRFhgdJn-27PzmLayIMg'

# Substitua pelo ID do chat do seu bot ou do usuário (número inteiro)
chat_id = 1142351974  # Certifique-se de usar um chat_id numérico

# Cria o objeto Bot com o token fornecido
bot = Bot(token)

# Função assíncrona para enviar a mensagem
async def send_message(message):
    try:
        await bot.send_message(chat_id=chat_id, text=message)
        print("Mensagem enviada com sucesso!")
        return 0  # Sucesso
    except TelegramError as e:
        print(f"Erro ao enviar mensagem: {e}")
        return 1  # Erro

# Função principal para rodar a tarefa assíncrona
async def main(message):
    return await send_message(message)

# Adiciona o suporte ao argumento --message
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enviar uma mensagem para o Telegram.")
    parser.add_argument(
        '--message', 
        required=True, 
        help='Mensagem a ser enviada para o Telegram.'
    )
    args = parser.parse_args()

    # Obtém o código de retorno e faz a saída
    result = asyncio.run(main(args.message))
    sys.exit(result)  # Sai com o código 0 (sucesso) ou 1 (erro)
