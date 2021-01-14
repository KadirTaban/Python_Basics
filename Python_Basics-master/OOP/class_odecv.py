#comment isminde bir sınıf oluşturunuz
#comment sınıfı username, text, likes, dislikes isminde özelliklere sahip olsun.
#5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırınız.

class comment:
    def __init__(self,username, yorum,likes=0,dislikes=0):
        self.username = username
        self.yorum = yorum
        self.likes=likes
        self.dislikes= dislikes


kullanıcı_1=comment("kadir","çok eğlenceli bir video",15,0)
kullanıcı_2=comment("nare","çok eğlenceli bir video",55,0)
kullanıcı_3=comment("sare","çok eğlenceli bir video",44,0)
comments=[kullanıcı_1,kullanıcı_2,kullanıcı_3]

for c in comments:
    print(f"{c.username}:{c.yorum}")
    print(f"likes:{c.likes} - dislikes: {c.dislikes}")

