from fastapi import FastAPI, Request, Form, Depends, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal, Kullanici  

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    kullanici = db.query(Kullanici).filter_by(email=email, sifre=password).first()
    if kullanici:
        
        return RedirectResponse(url="/panel", status_code=303)
    else:
       
        return templates.TemplateResponse("login.html", {
            "request": request,
            "hata": "E-posta veya şifre hatalı"
        })


@app.get("/panel", response_class=HTMLResponse)
def panel(
    request: Request,
    page: int = Query(1, ge=1),  
    db: Session = Depends(get_db)
):
    sayfa_basi = 5  
    toplam_kullanici = db.query(Kullanici).count()
    toplam_sayfa = (toplam_kullanici + sayfa_basi - 1) // sayfa_basi 

    
    kullanicilar = db.query(Kullanici)\
        .offset((page - 1) * sayfa_basi)\
        .limit(sayfa_basi)\
        .all()

    return templates.TemplateResponse("panel.html", {
        "request": request,
        "kullanicilar": kullanicilar,
        "page": page,
        "toplam_sayfa": toplam_sayfa
    })
