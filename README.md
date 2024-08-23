This Python script creates a simple Discord bot that fetches and shares random memes when prompted by a specific command. Here's a quick overview:

1. **Imports**: 
   - `discord`, `requests`, `json`, `os`, and `dotenv` are imported to interact with Discord, make API requests, handle JSON data, and manage environment variables.

2. **Loading the Bot Token**:
   - The bot token is loaded from a `.env` file using `load_dotenv()` and `os.getenv("DISCORD_TOKEN")`.

3. **Fetching Memes**:
   - The `get_meme()` function sends a GET request to the `meme-api` and returns a random meme URL.

4. **Bot Class (`MyClient`)**:
   - Extends `discord.Client`, with methods:
     - `on_ready()` prints a message when the bot is online.
     - `on_message(message)` responds to the `$meme` command by sending a random meme.

5. **Running the Bot**:
   - The bot is instantiated with message content intents enabled and then started using `client.run(Discord_Token)`.

This bot listens for the `$meme` command and responds with a random meme in any server where it's active.
