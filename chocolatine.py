import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv(dotenv_path=".env")


class Chocolatine(commands.Bot):
  def __init__(self):
    super().__init__(command_prefix="/")

  async def on_ready(self):
    print("Bot {self.user.display_name} is logged in.")


chocolatine = Chocolatine()
chocolatine.run(os.getenv("TOKEN"))
