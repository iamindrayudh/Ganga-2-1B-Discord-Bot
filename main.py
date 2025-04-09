import os
from dotenv import load_dotenv
import discord
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load environment variables from .env file
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    raise ValueError("Discord token not found in environment variables!")

# Load model and tokenizer
print("Loading Ganga-2-1B model...")
tokenizer = AutoTokenizer.from_pretrained("LingoIITGN/ganga-2-1b")
model = AutoModelForCausalLM.from_pretrained(
    "LingoIITGN/ganga-2-1b",
    device_map="auto",  # Automatically map the model to available devices (requires Accelerate)
    low_cpu_mem_usage=True  # Optimize memory usage
)
print("Model loaded successfully!")

# Initialize Discord client with intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable message content intent for reading messages

client = discord.Client(intents=intents)

# Event: Bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user}!")

# Event: Message received
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Process user input and generate response using Ganga-2-1B model
    user_input = message.content.strip()
    print(f"User Input: {user_input}")

    try:
        # Encode the user input with necessary tokens for the model
        input_ids = tokenizer.encode(f"<bos><user>{user_input}<assistant>", return_tensors="pt").to(model.device)
        
        # Generate output from the model
        outputs = model.generate(input_ids, max_new_tokens=100, do_sample=False)
        
        # Decode only the newly generated tokens (clean response)
        generated_tokens = outputs[0][input_ids.shape[-1]:]  # Slice out only new tokens
        bot_response = tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()
        
        print(f"Bot Response: {bot_response}")

        # Send only the bot's response back to Discord channel
        await message.channel.send(bot_response)

    except Exception as e:
        print(f"Error generating response: {e}")
        await message.channel.send("Sorry, I encountered an error while processing your request.")

# Run bot with token from environment variables
client.run(DISCORD_TOKEN)
