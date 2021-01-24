from gtts import gTTS

User_input = input("Enter your text: ")
User_input1 = User_input

language = "en"
#Converting text to speech and choosing speed as fast
voice = gTTS(text=User_input1, lang=language, slow=False)

voice.save('prdel.mp3')
