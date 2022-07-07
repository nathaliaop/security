ASCII_LETTER_A_LOWERCASE = 97
ALPHABET_LENGTH = 26

FREQUENCY_ALPHABET_ENGLISH = {
  'a': 8.167,
  'b': 1.492,
  'c': 2.782,
  'd': 4.253,
  'e': 12.702,
  'f': 2.228,
  'g': 2.015,
  'h': 6.094,
  'i': 6.966,
  'j': 0.153,
  'k': 0.772,
  'l': 4.025,
  'm': 2.406,
  'n': 6.749,
  'o': 7.507,
  'p': 1.929,
  'q': 0.095,
  'r': 5.987,
  's': 6.327,
  't': 9.056,
  'u': 2.758,
  'v': 0.978,
  'w': 2.360,
  'x': 0.150,
  'y': 1.974,
  'z': 0.074,
}

FREQUENCY_ALPHABET_PORTUGUESE = {
  'a': 14.63,
  'b': 1.04,
  'c': 3.88,
  'd': 4.99,
  'e': 12.57,
  'f': 1.02,
  'g': 1.30,
  'h': 1.28,
  'i': 6.18,
  'j': 0.40,
  'k': 0.02,
  'l': 2.78,
  'm': 4.74,
  'n': 5.05,
  'o': 10.73,
  'p': 2.52,
  'q': 1.20,
  'r': 6.53,
  's': 7.81,
  't': 4.34,
  'u': 4.63,
  'v': 1.67,
  'w': 0.01,
  'x': 0.21,
  'y': 0.01,
  'z': 0.47,
}


def generate_keystream(key, plaintext_length):
  return key * (plaintext_length//len(key)) + key[:(plaintext_length % len(key))]


def convert_letter_from_ascii(letter):
  return ord(letter) - ASCII_LETTER_A_LOWERCASE


def cryptography_letter(plaintext_letter, keystream_letter):
  plaintext_letter = convert_letter_from_ascii(plaintext_letter)
  keystream_letter = convert_letter_from_ascii(keystream_letter)

  cyphered_letter = (plaintext_letter + keystream_letter) % ALPHABET_LENGTH

  return chr(cyphered_letter + ASCII_LETTER_A_LOWERCASE)


def decryptography_letter(cyphertext_letter, keystream_letter):
  cyphertext_letter = convert_letter_from_ascii(cyphertext_letter)
  keystream_letter = convert_letter_from_ascii(keystream_letter)

  decyphered_letter = (cyphertext_letter -
             keystream_letter) % ALPHABET_LENGTH

  return chr(decyphered_letter + ASCII_LETTER_A_LOWERCASE)


def cryptography(plaintext, key):
  keystream = generate_keystream(key, len(plaintext))

  cyphertext = ''
  for i in range(len(plaintext)):
    cyphertext += cryptography_letter(plaintext[i], keystream[i])

  return cyphertext


def decryptography(cyphertext, key):
  keystream = generate_keystream(key, len(cyphertext))

  decypheredtext = ''
  for i in range(len(cyphertext)):
    decypheredtext += decryptography_letter(cyphertext[i], keystream[i])

  return decypheredtext


def test(plaintext, key):
  cyphertext = cryptography(plaintext, key)
  decypheredtext = decryptography(cyphertext, key)

  print(cyphertext)
  print(decypheredtext)


def break_cipher(cyphertext):
  pass

  # PARTE 2

def main():
  # test('victorchato', 'nathalialegal')
  break_cipher('iivaockhlxu')

if __name__ == '__main__':
  main()
