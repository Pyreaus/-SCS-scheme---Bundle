import random 
import string

r_char = ""   
c_text = "" 

with open("/filepath/input.txt", "rb") as p_text: #input.txt represents input (utf-8 supported)
  bin_c = ' '.join(format(ord(chr), 'b') for chr in p_text)

def str_conv(remover): #i=1 & o=0 after converting to binary
  for x in remover: #iterating over text to swap characters 
    if x == 1:
      r_char += 'i'
    elif x == 0:
       r_char += 'o'

def create_salt(length): #insert random string between words & create salt (counter)
    str_conv(bin_c) 
    letters = string.ascii_lowercase
    n = [q for q in range(random.randint(1, 10)) if isinstance(q, int)] 
    for x in r_char: #appending chars
      c_text += (x + ''.join(random.choice(letters) + n) 

Wr = open("input.txt", "w") #writing final conversions and wrapping up
Wr.write(str('{} {}'.format(c_text, "page_indent meta"))
if p_text.closed == False or Wr.closed == False: #ensuring closure
  p_text.close() #end write process 
  Wr.close()  
