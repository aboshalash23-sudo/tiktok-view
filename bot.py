
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.environ["BOT_TOKEN"]
SITE_URL = os.environ["SITE_URL"]


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "هلا والله 👋\n\n"
        "أنا بوت تجربة أذونات المتصفح.\n"
        "أوامري:\n"
        "/site - رابط صفحة التجربة"
    )


async def site(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "هذه صفحة التجربة:\n"
        f"{SITE_URL}\n\n"
        "الكاميرا والموقع اختياريان، "
        "ولا تشارك بياناتك إلا وأنت تعرف وش راح يُرسل."
    )


def main():
    app = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("site", site))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
