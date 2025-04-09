# **Ganga-2-1B Discord Bot**

GangaBot is a Discord chatbot powered by the **Ganga-2-1B language model**, designed to provide intelligent and conversational responses. This bot can be integrated into Discord servers and configured with ease.

---

## **Features**
- Text-based interaction using the Ganga-2-1B model.
- Secure configuration via environment variables.
- Easy setup for OAuth2 scopes and permissions.

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.8 or later installed on your system.
- A Discord bot token (available from the [Discord Developer Portal](https://discord.com/developers/applications)).
- Access to the Hugging Face model `LingoIITGN/ganga-2-1b`.

---

### **Installation**

#### **Step 1: Clone the Repository**
Clone this repository to your local machine:
- git clone https://github.com/iamindrayudh/Ganga-2-1B-Discord-Bot.git
- cd Ganga-2-1B-Discord-Bot

#### **Step 2: Create a Virtual Environment**
Create and activate a virtual environment:
- python3 -m venv venv
- source venv/bin/activate # On Windows: venv\Scripts\activate

#### **Step 3: Install Dependencies**
Install the required Python libraries:
- pip install -r requirements.txt

#### **Step 4: Configure Environment Variables**
Create a `.env` file in the root directory of your project:
- DISCORD_TOKEN=your_discord_bot_token_here
- Replace `your_discord_bot_token_here` with your actual bot token.

#### **Step 5: Run the Bot**
Start the bot using:
- python main.py

---

## **Discord Bot Permissions**

### **OAuth2 Scopes**
In the Discord Developer Portal, configure your bot's OAuth2 scopes as follows:
- **bot**: Required for enabling bot functionality in servers.
- **applications.commands**: Allows the bot to register slash commands.

### **Bot Permissions**
When generating an invite link for your bot, ensure you select permissions based on its functionality:
1. **Read Messages/View Channels**: Allows the bot to read messages in text channels.
2. **Send Messages**: Enables the bot to send replies.
3. (Optional) **Embed Links and Attach Files**: If your bot sends embedded responses or files.

To generate an invite link, go to the OAuth2 URL Generator in the Developer Portal, select `bot` and `applications.commands`, and assign appropriate permissions.

---

## **Usage**

### **Commands**
Once added to a server, interact with GangaBot by typing messages in text channels. The bot will process user input using the Ganga-2-1B model and respond intelligently.

---

## **Development Notes**

## **Project Structure**

The following is the structure of the GangaBot project:

- **`GangaBot/`**  
  - **`.env`**: Environment variables (excluded from GitHub).  
  - **`.gitignore`**: Specifies files and folders to ignore in Git.  
  - **`main.py`**: Main bot script containing the logic for the Discord bot.  
  - **`requirements.txt`**: Python dependencies required to run the bot.  
  - **`README.md`**: Project documentation, including setup instructions and usage details.  

### **Security**
Ensure sensitive information like API tokens is stored securely in `.env` files and excluded from version control using `.gitignore`.

---

## **License**
This project is licensed under the MIT License.

---

## **Contributing**
Feel free to fork this repository and submit pull requests for improvements or new features.

---

## **Acknowledgments**
Special thanks to [Hugging Face](https://huggingface.co/) for providing access to the Ganga-2-1B language model.
