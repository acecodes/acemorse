# AceMorse
### Morse code library for Python 2.x & 3.x

---
Example usage:

    from acemorse import MorseCode
    
    text = 'Hello world!'
    
    print('Original text: {}'.format(text))
    message = MorseCode.generate(text)
    
    print('Morse code: {}'.format(message))
    translate = MorseCode.translate(message)
    
    print('Back to English: {}'.format(translate))