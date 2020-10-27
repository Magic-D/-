# -*- coding: utf-8 -*-
kyuyo = int(input("給与所得を入力: "))
zatu = int(input("雑所得を入力: "))
keihi = int(input("経費を入力: "))
if_gakusei = str(input("学生ですか？YesまたはNo: "))

class Zeihou:
    def __init__(self, kisokoujo, kyuyoshotokukoujo, zeiritu, kintouwari, kinrou_gakusei_koujo, shotoku_jougen):
        self.kiso_koujo = kisokoujo
        self.kyuyoshotoku_koujo = kyuyoshotokukoujo
        self.zeiritu = zeiritu
        self.kintou_wari = kintouwari
        self.kinrou_gakusei_koujo = kinrou_gakusei_koujo
        self.shotoku_jougen = shotoku_jougen
        self.kyuyo_shotoku = self.calculation(self.kyuyoshotoku_koujo, kyuyo)
        self.zatu_shotoku = self.calculation(keihi, zatu)
        if if_gakusei == "Yes" and self.kyuyo_shotoku + self.zatu_shotoku <= self.shotoku_jougen and self.zatu_shotoku <= 100000:
            print("勤労学生控除が使えます")
            self.kazei_hyoujun_gaku = self.calculation(self.kiso_koujo + self.kinrou_gakusei_koujo, self.kyuyo_shotoku + self.zatu_shotoku)
        else:
            self.kazei_hyoujun_gaku = self.calculation(self.kiso_koujo, self.kyuyo_shotoku + self.zatu_shotoku)
        self.shotoku_wari = self.kazei_hyoujun_gaku * self.zeiritu

    def calculation(self, koujo, income):
        if income > koujo:
            return income - koujo
        else:
            return 0

    

shotokuzei = Zeihou(480000, 550000, 0.05, 0, 270000, 750000)
akita = Zeihou(330000, 650000, 0.1, 5800, 260000, 650000)

print("所得税について")
print("課税標準額は"+ str(shotokuzei.kazei_hyoujun_gaku)+"円です。")
print("所得税は" + str(shotokuzei.shotoku_wari) + "円です")
print("復興特別税を含めると" + str(shotokuzei.shotoku_wari * 1.021) + "円です")

print("秋田県秋田市の住民税について")
print("課税標準額は"+ str(akita.kazei_hyoujun_gaku)+ "円です。")
akita.shotoku_wari = akita.shotoku_wari - (akita.kazei_hyoujun_gaku * 0.05)
print("所得割額は" + str(akita.shotoku_wari) + "円です")
if akita.kazei_hyoujun_gaku > 0:
    print("均等均等割額は" + str(akita.kintou_wari) + "円です")
    print("住民税は" + str(akita.shotoku_wari + akita.kintou_wari) + "円です")
else:
    print("住民税は非課税です")