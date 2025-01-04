# Jarvis Voice Assistant 🚀

Welcome to **Jarvis Voice Assistant**, a Python-based personal assistant designed to make your life easier! Whether you want to search the web, play a song, get weather updates, or simply have fun with jokes, Jarvis is here to help. 🌟

---

## Features ✨

- 🖋️ **Open and Close Applications**
  - Open Notepad, Command Prompt, Microsoft Word, and more.

- 📸 **Camera Functionality**
  - Open the webcam to capture photos or videos.

- 🎥 **Media Entertainment**
  - Play random movies from a specific folder.
  - Play songs directly on YouTube.

- 🌐 **Web Utilities**
  - Search on Google, YouTube, and Wikipedia with voice commands.

- 🌦️ **Weather Updates**
  - Fetch real-time weather data for your preferred city.

- 📧 **Messaging**
  - Send WhatsApp messages to your contacts.

- ⏰ **Reminders and Scheduling**
  - Set custom reminders.

- 🤣 **Entertainment**
  - Tell jokes to lighten up your mood.

- 💻 **System Operations**
  - Shutdown, restart, or put your system to sleep.

---

## Installation 🛠️

Follow these steps to set up Jarvis on your local machine:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Astik83/JarvisProject.git
   cd JarvisProject
   ```

2. **Install Dependencies**

   Ensure you have Python 3.8+ installed. Then, run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**

   - Replace `weather_api_key` in the code with your OpenWeatherMap API key.

4. **Run the Program**

   ```bash
   python jarvis.py
   ```

---

## How to Use 🗣️

1. **Start the Program**
   - Jarvis will greet you and await your commands.

2. **Give Voice Commands**
   - Examples:
     - "Open Notepad"
     - "Search on Google"
     - "What's the weather like?"
     - "Play [song name] on YouTube"

3. **Enjoy the Interaction!**

---

## Requirements 🧰

- **Python 3.8+**
- **Dependencies** (Install via `requirements.txt`):
  - `speechrecognition`
  - `pyttsx3`
  - `opencv-python`
  - `pywhatkit`
  - `pyjokes`
  - `wikipedia`

---

## Contact List 🧑‍🤝‍🧑

Add your contacts to the `contact_list` dictionary in the script for sending WhatsApp messages:

```python
contact_list = {
    "aastik": "+91",
    "dad": "+977",
    "archana": "+91",
    "anisha": "+977",
    "pankaj": "+977",
    "shivam": "+91"
}






Developed by **Astik Shah** with 💻 and ❤️.

