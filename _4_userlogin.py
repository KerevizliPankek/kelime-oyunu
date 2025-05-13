from imports import *

def userLogin(password,username):
    modifiedname = username.replace("@","_at_").replace(".","_dot_")
    passhash = hashlib.sha256(password.encode()).hexdigest()
    user_ref = db.reference(f"/users/{modifiedname}")
    user_data = user_ref.get()
    if user_data:
        if passhash == user_data["password"]:
            print("Doğru şifre. Oturum başlatıldı.")
            return True
        else:
            print("Yanlış şifre. Tekrar deneyin.")
            return False
    else:
        print("Kullanıcı bulunamadı. yaratılıyor:")
        user_ref.set(
            {"password":passhash}
        )
        print("Kullanıcı oluştu. Oturum başlatıldı.")
        return True