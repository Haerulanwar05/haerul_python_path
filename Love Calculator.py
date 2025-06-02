'''
Tulis program untuk menguji kecocokan antara dua orang.

Ambil nama kedua orang tersebut dan periksa berapa kali huruf dalam kata TRUE muncul. Kemudian periksa berapa kali huruf dalam kata LOVE muncul. Kemudian gabungkan angka-angka ini untuk membuat angka 2 digit.
For Love Scores less than 10 or greater than 85, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 70, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
'''
# Syntax
name1 = input("Masukan nama anda? ").lower()
name2 = input("Masukan nama pasangan anda? ").lower()

score_t = name1.count("t")
score_t2 = name2.count("t")
score_r = name1.count("r")
score_r2 = name2.count("r")
score_u = name1.count("u")
score_u2 = name2.count("u")
score_e = name1.count("e")
score_e2 = name2.count("e")

score_l = name1.count("l")
score_l2 = name2.count("l")
score_o = name1.count("o")
score_o2 = name2.count("o")
score_v = name1.count("v")
score_v2 = name2.count("v")
score_E = name1.count("e")
score_E2 = name2.count("e")

score_true = str(score_t + score_t2 + score_r + score_r2 + score_u + score_u2 + score_e + score_e2)
score_love = str(score_l + score_l2 + score_o + score_o2 + score_v + score_v2 + score_E + score_E2)
Score_All = score_true + score_love

if int(Score_All) < 10 or int(Score_All) > 85:
    print(f"Your score is {Score_All}, you go together like coke and mentos.")
elif 40 <= int(Score_All) >= 70 :
    print(f"Your score is {Score_All}, you are alright together.")
else:
    print(f"Your score is {Score_All}.")

