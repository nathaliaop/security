ASCII_LETTER_A_LOWERCASE = 97 # OFFSET
ALPHABET_LENGTH = 26

SEQUENCE_LENGTH = 3

ALPHABET = [chr(letter) for letter in range(97, 97+26)]

PORTUGUESE_LETTERS_WITH_ACCENT = {
  'à': 'a',
  'á': 'a',
  'ã': 'a',
  'â': 'a',
  'é': 'e',
  'è': 'e',
  'ê': 'e',
  'í': 'i',
  'ì': 'i',
  'î': 'i',
  'ó': 'o',
  'ò': 'o',
  'ô': 'o',
  'ú': 'u',
  'ù': 'u',
  'û': 'u',
  'ç': 'c',
}

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

  decyphered_letter = (cyphertext_letter - keystream_letter) % ALPHABET_LENGTH

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


def map_sequence_frequency(cyphertext, sequence_length):
  sequence_frequency = {}
  for i in range(len(cyphertext) - sequence_length):
    if cyphertext[i:i+sequence_length] in sequence_frequency:
      sequence_frequency[cyphertext[i:i+sequence_length]] += 1
    else:
      sequence_frequency[cyphertext[i:i+sequence_length]] = 1

  return sequence_frequency

def fator_number(num):
  factors = []

  i = 1
  while i*i <= num:
    if num % i == 0:
      factors.append(i)

      if i != num//i:
        factors.append(num//i)

    i += 1

  factors.remove(1)

  return factors

def map_possible_keys(sequence_frequency):
  possible_keys = {}
  for _, value in sequence_frequency.items():
    for factor in fator_number(value):
      if factor in possible_keys:
        possible_keys[factor] += 1
      else:
        possible_keys[factor] = 1

  return sorted(possible_keys.items(), reverse=True, key=lambda kv: (kv[1], kv[0]))

def get_cyphertext_frequency_alphabet(cyphertext, key_length):
  percentage = []
  frequency = []

  for i in range(key_length):
    frequency.append(dict([(letter, 0) for letter in ALPHABET])) # frequency alphabet empty

    for j in range(i, len(cyphertext), key_length):
      frequency[i][cyphertext[j]] += 1
    
    percentage.append({})

    total_size = sum(frequency[i].values())
    
    for letter in ALPHABET:
      percentage[i][letter] = round((frequency[i][letter] * 100)/total_size, 3)

  return percentage

def break_cipher(cyphertext):
  cyphertext = cyphertext.lower().replace(';', '')

  sequence_frequency = map_sequence_frequency(cyphertext, SEQUENCE_LENGTH)
  possible_keys = map_possible_keys(sequence_frequency)

  print(possible_keys)

  key_length = 6

  cyphertext_frequency_alphabet = get_cyphertext_frequency_alphabet(cyphertext, key_length)
  
  for e in cyphertext_frequency_alphabet:
    print(e)
    print()

  alphabet_shift = [5, 18, 24, 7, 12, 9]

  cyphertext = list(cyphertext)
  for i in range(key_length):
    for j in range(i, len(cyphertext), key_length):
      cyphertext[j] = chr(((ord(cyphertext[j]) - ASCII_LETTER_A_LOWERCASE + alphabet_shift[i]) % ALPHABET_LENGTH) + ASCII_LETTER_A_LOWERCASE)

  # print(''.join(cyphertext))

  # ANOTAR NO RELATÓRIO: se o texto tivesse espaçamento e caracteres não criptografdos, isso facilitaria para quem está vendo...

def tmp():
  s = ''

  while True:
    try:
      s += input()
    except:
      break
  
  return s

def get_example_text_english():
  arquivo = open('little_prince_english.txt', 'r')

  text = ''.join(arquivo.readlines())

  arquivo.close()

  cleaned_text = ''
  for c in text.lower():
    if c in ALPHABET:
      cleaned_text += c
    elif c in PORTUGUESE_LETTERS_WITH_ACCENT:
      cleaned_text += PORTUGUESE_LETTERS_WITH_ACCENT[c]

  return cleaned_text

def get_example_text_portuguese():
  arquivo = open('pequeno_principe_português.txt', 'r', encoding='utf8')

  text = ''.join(arquivo.readlines())
  
  arquivo.close()

  cleaned_text = ''
  for c in text.lower():
    if c in ALPHABET:
      cleaned_text += c
    elif c in PORTUGUESE_LETTERS_WITH_ACCENT:
      cleaned_text += PORTUGUESE_LETTERS_WITH_ACCENT[c]

  return cleaned_text

def main():
  # test('victorchato', 'nathalialegal')
  # break_cipher('iivaockhlxu')
  cleaned_text = get_example_text_english()
  cleaned_text = get_example_text_portuguese()

  #print(cleaned_text)

  print(cleaned_text[:100])
  print(cryptography(cleaned_text, 'victor')[:100])

  break_cipher(cryptography(cleaned_text, 'victor'))

if __name__ == '__main__':
  main()
