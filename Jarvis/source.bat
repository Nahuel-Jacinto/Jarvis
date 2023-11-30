@echo off
cd .\sources
python-3.10.4-amd64.exe
pip install --upgrade pip --user
pip install PyAudio-0.2.11-cp310-cp310-win_amd64.whl --user
pip install SpeechRecognition-3.8.1-py2.py3-none-any.whl --user
pip install pyttsx3-2.90-py3-none-any.whl --user
pause>nul