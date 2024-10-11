#games playfrom sendiri
import pygame

#play linked

kliklink = ("https://portofolio-dwi-bakti-n-dev-liard.vercel.app/")
print (kliklink)

#format data
textkedepan = "{} , {} , {} , {}" .format ("Mainkan" , "Games" , "Quizz" , "Sekarang")
print (textkedepan)


#space data 
a = ""
b = a[:5]
print (a)
print ("🤖",a[:5] + 'isi guys data diri kalian',"🤖")

#ini adalah data isi
print("=================================")
print("🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱")
print("😭😭😭😭 Yamethe 😭😭😭😭")
#input data diri
nama = input ("Masukan Nama Anda :")
umur = int(input("Masukan Kelas Anda :"))
print("Umur Succesful input date",umur)
email = input("Masukan Email Anda :")
print("==================================")
#nama yang terdetect

print("nama :"+str(nama))
print("Umur :"+str(umur))
print("email :"+str(email))

print ("==================================================")
print ("========= Mulai Lah Quiz Sekarang Guys ===========")

#ini pertanyaan
questions = ("\033[0;34m Siapa Pencipta Kevin Systrom dan Mike Krieger ? \n",
"\033[0;34m Siapakah Marck Zuckerberg ? \n",
"\033[0;34m siapakah penemu listrik pertama kali ? \n",
"\033[0;34m Siapakah President Pertama ? \n",
"\033[0;34m siapakah Ceo Github ? \n",
"\033[0;34m siapakah Ceo Sanyo ? \n",
"\033[0;34m siapakah Ceo Honda ? \n")
#ini jawabanya
options = (("A. Pencipta Facebook", "B. Pencipta Twitter", "C. Pencipta Github", "D. Pencipta Listrik" , "E.Pencipta Instagram"),
("A. Ceo iG", "B. Ceo Facebook", "C. Ceo Twiter", "D. Ceo Perusahaan" , "E. Ceo Kominfo"),
("A. Nikola", "B. Smith", "C. Gorgeo Smith", "D. Hydroptectonik" , "E. Jordan"),
("A. Soeharto", "B. Soepomo", "C. Obama", "D. Soekarno" , "E. Bung Tomo"),
("A. Thomas Dohmke", "B. Venussios", "C. Alexandre", "D. Mars" , "hartono"),
("A. Merciana", "B. Nagawa", "C. kagawa", "D. masik" ,"E. Megawa"),
("A. Toshiro Sami", "B. Toshiro Eliiot", "C. Toshiro Makis", "D. Toshiro Mibes" , "E. Toshiro Mibe"))
#ini hasil dari jawabanya
answers = ("E", "B", "A", "D", "A" , "B" , "E" ,"a" , "b" , "c" , "d" , "e") 
User = []
score = 0
qust_score = 0
for question in questions:
    print("==================================================")
    print(question)
    for option in options[qust_score]:
        print(option)

    guess = input("Enter (A, B, C, D , E): ").upper()
    User.append(guess)
    if guess == answers[qust_score]:
        score += 1
        print("\033[0;33m Jawaban Anda Benar 👾\n")
    else:
        print("\033[0;32m Jawaban Anda Salah 😣 \n")
        print(f"{answers[qust_score]} is the correct answer")
    qust_score += 1

print("========================================")
print("🏆🏆   Tampilkan Hasil Kuiz   🏆🏆    ")
print("========================================")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in User:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")


print("==================================================================")
print("🏆🏆   Tampilkan Perkalian pembagian dan penjumblahan   🏆🏆    ")
print("==================================================================")


perhitungan = float(input("Isilah bialangan random ini :"))
perhitungan2 = float(input("isilah bilangan random ini :"))
result = perhitungan / perhitungan2
print ("hasil pembagian adalah : "+str (result))

perhitungan3 = float(input("Isilah bialangan random ini :"))
perhitungan4 = float(input("isilah bilangan random ini :"))
result = perhitungan3 * perhitungan4
print ("hasil pembagian adalah : "+str (result))

perhitungan5 = float(input("Isilah bialangan random ini :"))
perhitungan6 = float(input("isilah bilangan random ini :"))
result = perhitungan5 + perhitungan6
print ("hasil pembagian adalah : "+str (result))

print("==================================================================")
print("🏆🏆   Jawaban Anda sudah Terverivikasi admin otw cek   🏆🏆    ")
print("==================================================================\n")

print ('Nama Anda Telah Mengikuti Quizz : ', nama)
print ('Umur Anda Yang Telah Terdata : ', umur)
print ('Email Anda Telah Di isi : ', email)

print ("=================================================================")