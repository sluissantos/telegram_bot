import os
from dotenv import load_dotenv
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters
import nest_asyncio


# Carrega variáveis do arquivo .env
load_dotenv("config.env")

# Corrige o problema de loops concorrentes
nest_asyncio.apply()

# Substitua pelo token do seu bot (recomenda-se usar variáveis de ambiente)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Defina isso no ambiente ou em um arquivo .env
if not TOKEN:
    raise ValueError(
        "O token do bot não foi configurado. "
        "Defina a variável TELEGRAM_BOT_TOKEN no ambiente ou em um arquivo .env."
    )

# Nome do arquivo onde as mensagens serão salvas
FILE_NAME = "mensagens_recebidas.txt"

# Função chamada quando o bot recebe uma mensagem
async def handle_message(update: Update, context):
    user_message = update.message.text
    chat_id = update.message.chat_id
    print(f"Mensagem recebida de {chat_id}: {user_message}")

    # Salva a mensagem no arquivo
    try:
        with open(FILE_NAME, "a") as file:
            file.write(f"Chat ID: {chat_id} - Mensagem: {user_message}\n")
        print("Mensagem registrada no arquivo.")
    except IOError as e:
        print(f"Erro ao salvar mensagem no arquivo: {e}")

    # Envia uma confirmação para o usuário
    await context.bot.send_message(chat_id=chat_id, text="Mensagem registrada no PC! ✅")

# Função principal para configurar e rodar o bot
async def main():
    # Cria a aplicação do bot
    application = Application.builder().token(TOKEN).build()

    # Adiciona o manipulador para mensagens de texto
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    application.add_handler(message_handler)

    print("Bot iniciado. Pressione Ctrl+C para sair.")
    await application.run_polling()

# Execução direta
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot encerrado pelo usuário.")
    except RuntimeError as e:
        print(f"Erro ao executar o bot: {e}")
