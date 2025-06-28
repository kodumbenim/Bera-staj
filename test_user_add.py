from database import SessionLocal, Kullanici

db = SessionLocal()

kullanici = Kullanici(email="aaaaaa06@gmail.com", sifre="1234")
db.add(kullanici)
db.commit()
db.close()

print("Kullanıcı eklendi.")
