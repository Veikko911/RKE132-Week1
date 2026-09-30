#kirjutada programm, mis küsib kasutajalt nime ja tervitab teda nimepidi.

#Algus
#Küsi kasutajalt eesnimi
#Salvesta väärtus muutjujasse first name
#Väljastab tervitust: "Hello, <eesnimi>!
#Lõpp


first_name = input("Enter your first naime:")
print("Hello, " +  first_name + "!")

#f-string
print(f"Hello, {first_name}!")

#tehke nii, et programm küsib kasutajalt mitte ainult eesnime, vaid ka perekonnanine ja tervitab teda nime ja perekonnanimega.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Hello, {first_name} {last_name}!")