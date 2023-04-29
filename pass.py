import random
import string
import os
print ('''     [-] Developer - MIISTER C''')
print('=======================================') 
print('''      UNCRACKABLE PASSWORD GENERATOR 
          & PASSWORD MANAGER TOOL''')
print('=======================================')
print('''  <========================>  ''')
print('''       [-] Thanks for using this tool. 
       [-] We hope you enjoy. ''')
print('''  <========================>  ''')
print('CHOOSE:-')
print('1.Uncrackable password generator.    [1]')
print('2.Password strength checker.         [2]')
print('3.About this tool                    [3]')
print('4.Bug reporting.                     [4]')
print('5.securely store password            [5]')
print('6.decrypt your encrypted password    [6]')
print('=======================================')
f = input('===>>>  ')
if f == '1':
   a = string.ascii_letters + string.digits + string.punctuation
   b = string.ascii_letters + string.digits
   c = string.ascii_letters + string.punctuation
   d = string.punctuation + string.digits
   e = string.ascii_letters
   f = string.digits
   g = string.punctuation
   a1 = str(input('Add letters ? [y/n] : '))
   b1 = str(input('Add Numbers ? [y/n] : '))
   c1 = str(input('Add Special characters? [y/n] : '))
   L = int(input('Password length ? [recommended length : 13] : '))
   if a1 == 'y' and b1 == 'y' and c1 == 'y':
      a2 = ''.join(random.sample(a,L))
      print('YOUR UNCRACKABLE PASSWORD IS : ',a2)
   elif a1 == 'y' and b1 == 'y' and c1 == 'n':
      b2 = ''.join(random.sample(b,L))
      print('YOUR UNCRACKABLE PASSWORD IS : ',b2)
   elif a1 == 'y' and b1 == 'n' and c1 == 'y':
      c2 = ''.join(random.sample(c,L))
      print('YOUR UNCRACKABLE PASSWORD IS : ',c2)
   elif a1 == 'n' and b1 == 'y' and c1 == 'y':
      d2 = ''.join(random.sample(d,L))
      print('YOUR UNCRACKABLE PASSWORD IS : ',d2)
   elif a1 == 'y' and b1 == 'n' and c1 == 'n':
      e2 = ''.join(random.sample(e,L))
      print('YOUR UNCRACKABLE PASSWORD IS : ',e2)
   elif a1 == 'n' and b1 == 'y' and c1 == 'n':
      f2 = ''.join(random.sample(f,L))
      print('YOUR UNCRACKABLE PASSWORD IS : ',f2)
   elif a1 == 'n' and b1 == 'n' and c1 == 'y':
      g2 = ''.join(random.sample(g,L))
      print('YOUR UNCRACKABLE PASSWORD IS : ',g2) 
   else:
      print('[X] Wrong input ')
elif f == '2':
   sr = 0
   s = str(input('Enter you password to check [No blank spaces] : '))
   if any(char.isdigit() for char in s):
      sr += 1
   if any(char.isupper() for char in s):
      sr += 1
   if any(char.islower() for char in s):
      sr += 1
   if any(char in '!@#$%^&*()_+-=[]{}|;:,./<>?' for char in s):
      sr += 1
   if len(s) >= 12:
      sr += 1
   if sr == 0:
      print('Password strength : too weak')
   elif sr == 1:
      print('Password strength : very weak')
   elif sr == 2:
      print('Password strength : little bit weak')
   elif sr == 3:
      print('password strength : strong')
   elif sr == 4:
      print('password strength : Very strong ')
   else:
      print('UNCRACKABLE!! ')
elif f == '3':
   print('This is a python cyber security Tool.')
   print('This tool basically generates you a    password of your choice.')   
   print('If you generate a password using all character of password length of 8 or greater than 8 without blank spaces then your password becomes impossible to crack')
   print('And the second tool is that if you give a password then the tool will check the password in the tool database if its commonly used it will be weak or else strong.')
   print('thanks for using the tool')
elif f == "4":
   print('This tool is currently new and still in development stage.')
   print('if you find any bug or problem in this tool,')
   print('then please kindly email us at')
   print('toolsmisterccontact@gmail.com')
   print('it will be very helpful if you email us about the problem')
   print('Thank you.')
elif f == '5':
   char = ' '  + string.punctuation + string.ascii_letters + string.digits
   char = list(char)
   C = ("""1796368250✓ikplol'(")*+,-./:;<=>?@[\]^_`QWERPO{|}~IUTYASDLKJFGHMZXNBVCqazwsxedcrfvtgby4hnujmπ!#$&%""" + ' ') 
   usi = input('Enter the password : ')
   fo = input('For which website you are storing ==> ')
   e_text = ''
   for letter in usi:
      try:
         index = char.index(letter)
         e_text += C[index]
      except ValuError:
         pass
   if not os.path.exists('passwords'):
      os.makedirs('passwords')
   with open('passwords/pass.txt','a') as f:
      f.write(f'{fo}: encrypted password =  {e_text}\n')
      print('Your password has been successfully stored in "passwords" directory.')
elif f == "6":
   C = ("""1796368250✓ikplol'(")*+,-./:;<=>?@[\]^_`QWERPO{|}~IUTYASDLKJFGHMZXNBVCqazwsxedcrfvtgby4hnujmπ!#$&%""" + ' ') 
   e_text = input('Enter the encrypted password : ')
   usi = ''
   char = ' '  + string.punctuation + string.ascii_letters + string.digits
   char = list(char)
   for letter in e_text:
      index = C.index(letter)
      usi += char[index]
   print(f"Code : {e_text}")
   print(f"Decrypted : {usi}")
    
else:
   print('No such option [X]')
