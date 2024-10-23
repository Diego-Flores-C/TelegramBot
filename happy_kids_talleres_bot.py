import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7690606521:AAGqfNHuZ6pAuUc3uujHE1cFDKro3JDpVdY'  # Reemplaza con tu API token

# Configuración básica
logging.basicConfig(level=logging.INFO)

# Definir un comando básico
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text='¡Hola! Soy tu bot.')


# Crear la aplicación
app = ApplicationBuilder().token(TOKEN).build()

# Agregar comando
app.add_handler(CommandHandler('start', start))

# Iniciar el bot
app.run_polling()