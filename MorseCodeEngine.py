# Morse Code Generator/Translator
# Functions for creating or translating Morse code messages.

"""

THIS VERY ROUGH MORSE CODE ENCODER/TRANSLATOR
LEAD TO THE CREATION OF 'THE CODE ENGINE', A FLASK APP HOSTED ON HEROKU

PLEASE VISIT GITHUB.COM/ACECODES/CODESITE OR ENGINE.ACECODES.NET TO SEE A
MUCH MORE REFINED VERSION OF THIS CODE

"""


alphabet = {'0':'-----', '1':'.----', '2':'..---', '3':'...--',
'4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.', 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.','g':'--.','h':'....',
'i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.',
's':'...','t':'-','u':'..-','v':'..-','w':'.--','y':'-.--','z':'--..'}

punctuation = ['!', '?', '\'', ';', ','] # A list of punctuation marks

alpha_list = [] # Empty list that will hold only the alphanumeric characters from the alphabet dictionary
code_list = [] # Empty list that will hodl only the Morse code from the alphabet dictionary

# Looping through the dictionary to separate the alphanumerics and Morse code
for k, v in sorted(alphabet.items()): 
	alpha_list.append(k)
	code_list.append(v)

# Generates Morse code list from an English message
# The 'plain' flag is for messages that will not be turned into lists for use by 'MorseTranslate'
def MorseGenerate(text, plain=False):
	text = text.lower() # Make everything lower case, as case doesn't matter in Morse
	morse = [] # Create the list that will eventually hold the Morse code
	for letter in text: # Search the message for its match in Morse
		if letter in alphabet:
			morse.append(alphabet[letter])
		if letter == ' ' or letter in punctuation: # Attach punctuation or spaces as needed (periods are left out because . is 'e' in Morse)
			morse.append(letter)
	if plain != False:
		return ' '.join(morse)
	return morse

# Translates a message in Morse code into English
def MorseTranslate(morse):
	morse = list(morse) # Create a list out of the entered Morse code
	english = [] # Empty list for translation
	for code in morse: # Search the message for its match in English
		if code in code_list:
			x = code_list.index(code)
			english.append(alpha_list[x])
		if code == ' ' or code in punctuation: # Attach punctuation or spaces as needed
			english.append(code)
	return ''.join(english)

# Demonstrations
if __name__ == '__main__':
	message = MorseGenerate('Hello World!')
	message2 = MorseGenerate('Hey pal, let\'s hang out!')
	message3 = MorseGenerate('This message will not be translated by the function here!', plain=1)
	print(message)
	print(MorseTranslate(message))
	print(message2)
	print(MorseTranslate(message2))
	print(message3)