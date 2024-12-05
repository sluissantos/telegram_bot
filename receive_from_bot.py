import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters
import nest_asyncio

# Corrige o problema de loops concorrentes
nest_asyncio.apply()

# Substitua pelo token do seu bot
TOKEN = '7682976744:AAHtEmUeFnm43eBIRFhgdJn-27PzmLayIMg'

# Função chamada quando o bot recebe uma mensagem
async def handle_message(update: Update, context):
    user_message = update.message.text
    chat_id = update.message.chat_id
    print(f"Mensagem recebida de {chat_id}: {user_message}")
    with open("mensagens_recebidas.txt", "a") as file:
        file.write(f"Chat ID: {chat_id} - Mensagem: {user_message}\n")
    await context.bot.send_message(chat_id=chat_id, text="Mensagem registrada no PC! ✅")

# Função principal para configurar e rodar o bot
async def main():
    application = Application.builder().token(TOKEN).build()
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    application.add_handler(message_handler)
    print("Bot iniciado. Pressione Ctrl+C para sair.")
    await application.run_polling()

# Execução direta
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (RuntimeError, KeyboardInterrupt) as e:
        print(f"Bot encerrado. Motivo: {e}")
