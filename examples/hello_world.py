import time

import bot

if __name__ == "__main__":
    bot = bot.Bot()

    with bot:
        with bot.camera as camera:
            time.sleep(5)

            image = camera.snap()
            image.show()