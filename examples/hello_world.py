import bot

if __name__ == "__main__":
    bot = bot.Bot()

    with bot:
        with bot.camera as camera:
            image = camera.snap()