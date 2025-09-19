NOVEL - The Python Voice Assistant
!


A simple, command-line based voice assistant built in Python. NOVEL can understand voice commands to perform a variety of tasks, such as opening websites, launching local applications, and engaging in basic conversation.

🚀 Features
Voice-Controlled: Fully operated through voice commands.

Web Browsing: Opens popular websites like Google, YouTube, GitHub, Netflix, and more.

Application Launcher: Starts local applications such as Notepad, Calculator, Camera, and File Explorer.

Basic Conversation: Responds to greetings and can provide information about itself.

Time Inquiry: Tells you the current time.

Smart Fallback: Offers to search Google for any commands it doesn't recognize.

Text-to-Speech: Provides clear voice feedback for all its actions.

🛠️ Technologies & Libraries Used
This project is built with Python and relies on the following core libraries:

Python 3.x

speech_recognition: For converting spoken language into text.

pyttsx3: For converting text into speech.

webbrowser: To open and control web browsers.

os: To interact with the operating system (e.g., start applications).

📋 Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.7+: You can download it from python.org.

pip: Python's package installer (usually comes with Python).

A working microphone connected to your computer.

⚙️ Installation & Setup
Follow these steps to get your local copy of NOVEL up and running.

Clone the repository:
cd NOVEL-Voice-Assistant

Install the required Python packages:

pip install speechrecognition pyttsx3

Install PyAudio (for microphone access):
The speech_recognition library requires PyAudio to access the microphone. It can sometimes be tricky to install.

On Windows:

pip install pyaudio

If you encounter errors, you may need to install it from a Wheel file. Download the appropriate .whl file for your Python version and system architecture from UCl's Unofficial Python Binaries page and then run pip install PyAudio-0.2.11-cp3X-cp3Xm-win_amd64.whl.

On macOS:

brew install portaudio
pip install pyaudio

On Linux (Debian/Ubuntu):

sudo apt-get install python3-pyaudio

▶️ How to Run
Once the setup is complete, you can start the assistant by running the main script from your terminal:

python novel_assistant.py

The assistant will greet you, and the console will print "Listening..." when it's ready for a command.

🗣️ Example Commands
Here are some commands you can try:

"Hello NOVEL"

"What's the time?"

"Open YouTube"

"Open Notepad"

"Who programmed you?"

"Open GitHub"

"Thank you" (to end the session)

If you say something NOVEL doesn't understand, it will ask if you'd like to search for it on Google. Just say "yes" to proceed.

🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

👤 Author
Akash Pandey

📜 License
This project is open-source and available to everyone.
