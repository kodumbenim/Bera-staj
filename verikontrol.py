from database import SessionLocal, Kullanici

db = SessionLocal()
kullanicilar = db.query(Kullanici).all()

for kullanici in kullanicilar:
    print(f"ID: {kullanici.id}, Email: {kullanici.email}, Şifre: {kullanici.sifre}")

db.close()
