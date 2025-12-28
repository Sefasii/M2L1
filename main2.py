import random
selected = random.randint(1,20)
print(selected)
for i in range(5):
    sayi = int(input("1 ve 20 arasında bir sayı seçtim. 5 tahmin hakkın var. SEnce benim seçtiğim sayı ne?"))
    if sayi == selected:
        print("Tebrikler! Seçtiğim sayıyı buldun!")
        break
    elif sayi > selected:
        print("Seçtiğim sayı daha düşük!")
    else:
        print("Seçtiğim sayı daha yüksek!")
