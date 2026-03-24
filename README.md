# 🤖 Mood-Based AI Chatbot

An interactive AI chatbot that adapts its personality based on user-selected moods and provides engaging, dynamic conversations.

🌐 **Live App:** https://llmchatbotusingmood.streamlit.app/

---

## 🚀 Features

* 🎭 **Multiple AI Personalities**

  * 😐 Normal (Professional & Neutral)
  * 😊 Happy (Cheerful & Positive)
  * 😡 Angry (Aggressive Tone)
  * 😂 Funny (Humorous Responses)
  * 😢 Sad (Emotional Tone)

* 🎨 **Dynamic UI**

  * Background changes based on selected mood
  * Styled chat bubbles for better UX

* 💬 **Real-time Chat**

  * Powered by Mistral AI via LangChain
  * Maintains conversation context

* 🔄 **Session Memory**

  * Keeps chat history during session
  * Resets when mood changes

* 🧹 **Reset Functionality**

  * Clear conversation with one click

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM Integration:** Mistral AI (via LangChain)
* **Environment Management:** python-dotenv

---

## 📦 Installation (Run Locally)

```bash
git clone https://github.com/jayaSiP/LLMChatbot.git
cd LLMChatbot
pip install -r requirements.txt
```

### 🔑 Set API Key

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run UIchat.py
```

---

## 🌐 Deployment

This app is deployed on **Streamlit Cloud**.

To deploy your own:

1. Push code to GitHub
2. Connect repo on Streamlit Cloud
3. Add API key in **Secrets**:

   ```toml
   MISTRAL_API_KEY = "your_api_key_here"
   ```

---

## 📸 Preview

Try different moods and see how:

* Responses change tone 🎭
* UI adapts visually 🎨
* Conversations feel more engaging 💬

---

## 👩‍💻 Author

**Jaya Singh**

* 📧 Email: [Jayaaworks@gmail.com](mailto:Jayaaworks@gmail.com)
* 🔗 GitHub: https://github.com/jayaSiP

---

## 💡 Future Enhancements

* 🔍 Auto mood detection from user input
* 🎤 Voice-based interaction
* 📊 Chat analytics dashboard
* 🎯 Use-case based modes (Interview Prep, Study Assistant)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!

---
