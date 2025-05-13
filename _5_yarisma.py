from datetime import datetime, timedelta 
import random

def game(sorular):
    endtime = datetime.now() + timedelta(seconds=300)
    score = 0
    print(endtime)

    for en,i in enumerate(sorular): 
        hints= 0
        flag = 0
        harflist = [ "_" for h in i["madde"] ]
        hintlist = []
        kalanharf=len(i["madde"])
        while kalanharf>0:
            print(f"Soru {en+1}:{i["anlam"]}:")
            print(" ".join(harflist))
            cevap = input("harf almak için 'x' yazın: ")
            if cevap==i["madde"]:
                score += (kalanharf)*100
                print(f"Skor: {score}")
                kalanharf=0
            elif cevap=="x":
                hintlist = [id for id,ch in enumerate(harflist) if ch=="_"]
                kalanharf-=1
                score -= 100
                rngharf = random.choice(hintlist)
                print(rngharf)
                harflist[rngharf] = i["madde"][rngharf]
            else:
                score -= (kalanharf) * 100
                print(f"Skor: {score}")
                kalanharf=0
        if datetime.now() > endtime:
            print("Süre doldu.")
            break
    remaining = max(0,int((endtime - datetime.now()).total_seconds()))
    totals = score + remaining*30
    print(f"\n\n\nOyun bitti. Skorunuz: {score} Puan + {remaining}s*30: {totals}")
    return totals