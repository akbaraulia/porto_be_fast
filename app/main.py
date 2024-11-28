from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas, database

app = FastAPI()

# Dependency untuk mendapatkan session DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint untuk CRUD Biodata
@app.post("/biodata/", response_model=schemas.Biodata)
def create_biodata(biodata: schemas.BiodataCreate, db: Session = Depends(get_db)):
    return crud.create_biodata(db=db, biodata=biodata)

@app.get("/biodata/{biodata_id}", response_model=schemas.Biodata)
def get_biodata(biodata_id: int, db: Session = Depends(get_db)):
    return crud.get_biodata(db=db, biodata_id=biodata_id)

@app.get("/biodata/", response_model=List[schemas.Biodata])
def get_all_biodata(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_biodata(db=db, skip=skip, limit=limit)

@app.put("/biodata/{biodata_id}", response_model=schemas.Biodata)
def update_biodata(biodata_id: int, biodata: schemas.BiodataCreate, db: Session = Depends(get_db)):
    return crud.update_biodata(db=db, biodata_id=biodata_id, biodata=biodata)

@app.delete("/biodata/{biodata_id}", response_model=schemas.Biodata)
def delete_biodata(biodata_id: int, db: Session = Depends(get_db)):
    return crud.delete_biodata(db=db, biodata_id=biodata_id)

# Endpoint untuk CRUD Project
@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)

@app.get("/projects/{project_id}", response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    return crud.get_project(db=db, project_id=project_id)

@app.get("/projects/", response_model=List[schemas.Project])
def get_all_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_projects(db=db, skip=skip, limit=limit)

@app.put("/projects/{project_id}", response_model=schemas.Project)
def update_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.update_project(db=db, project_id=project_id, project=project)

@app.delete("/projects/{project_id}", response_model=schemas.Project)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    return crud.delete_project(db=db, project_id=project_id)

# Endpoint untuk CRUD SubProject
@app.post("/subprojects/", response_model=schemas.SubProject)
def create_sub_project(sub_project: schemas.SubProjectCreate, db: Session = Depends(get_db)):
    return crud.create_sub_project(db=db, sub_project=sub_project)

@app.get("/subprojects/{sub_project_id}", response_model=schemas.SubProject)
def get_sub_project(sub_project_id: int, db: Session = Depends(get_db)):
    return crud.get_sub_project(db=db, sub_project_id=sub_project_id)

@app.get("/subprojects/", response_model=List[schemas.SubProject])
def get_all_sub_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_sub_projects(db=db, skip=skip, limit=limit)

@app.put("/subprojects/{sub_project_id}", response_model=schemas.SubProject)
def update_sub_project(sub_project_id: int, sub_project: schemas.SubProjectCreate, db: Session = Depends(get_db)):
    return crud.update_sub_project(db=db, sub_project_id=sub_project_id, sub_project=sub_project)

@app.delete("/subprojects/{sub_project_id}", response_model=schemas.SubProject)
def delete_sub_project(sub_project_id: int, db: Session = Depends(get_db)):
    return crud.delete_sub_project(db=db, sub_project_id=sub_project_id)

# Endpoint untuk CRUD Pendidikan
@app.post("/pendidikan/", response_model=schemas.Pendidikan)
def create_pendidikan(pendidikan: schemas.PendidikanCreate, db: Session = Depends(get_db)):
    return crud.create_pendidikan(db=db, pendidikan=pendidikan)

@app.get("/pendidikan/{pendidikan_id}", response_model=schemas.Pendidikan)
def get_pendidikan(pendidikan_id: int, db: Session = Depends(get_db)):
    return crud.get_pendidikan(db=db, pendidikan_id=pendidikan_id)

@app.get("/pendidikan/", response_model=List[schemas.Pendidikan])
def get_all_pendidikan(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_pendidikan(db=db, skip=skip, limit=limit)

@app.put("/pendidikan/{pendidikan_id}", response_model=schemas.Pendidikan)
def update_pendidikan(pendidikan_id: int, pendidikan: schemas.PendidikanCreate, db: Session = Depends(get_db)):
    return crud.update_pendidikan(db=db, pendidikan_id=pendidikan_id, pendidikan=pendidikan)

@app.delete("/pendidikan/{pendidikan_id}", response_model=schemas.Pendidikan)
def delete_pendidikan(pendidikan_id: int, db: Session = Depends(get_db)):
    return crud.delete_pendidikan(db=db, pendidikan_id=pendidikan_id)

# Endpoint untuk CRUD Pengalaman Kerja
@app.post("/pengalaman_kerja/", response_model=schemas.PengalamanKerja)
def create_pengalaman_kerja(pengalaman_kerja: schemas.PengalamanKerjaCreate, db: Session = Depends(get_db)):
    return crud.create_pengalaman_kerja(db=db, pengalaman_kerja=pengalaman_kerja)

@app.get("/pengalaman_kerja/{pengalaman_kerja_id}", response_model=schemas.PengalamanKerja)
def get_pengalaman_kerja(pengalaman_kerja_id: int, db: Session = Depends(get_db)):
    return crud.get_pengalaman_kerja(db=db, pengalaman_kerja_id=pengalaman_kerja_id)

@app.get("/pengalaman_kerja/", response_model=List[schemas.PengalamanKerja])
def get_all_pengalaman_kerja(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_pengalaman_kerja(db=db, skip=skip, limit=limit)

@app.put("/pengalaman_kerja/{pengalaman_kerja_id}", response_model=schemas.PengalamanKerja)
def update_pengalaman_kerja(pengalaman_kerja_id: int, pengalaman_kerja: schemas.PengalamanKerjaCreate, db: Session = Depends(get_db)):
    return crud.update_pengalaman_kerja(db=db, pengalaman_kerja_id=pengalaman_kerja_id, pengalaman_kerja=pengalaman_kerja)

@app.delete("/pengalaman_kerja/{pengalaman_kerja_id}", response_model=schemas.PengalamanKerja)
def delete_pengalaman_kerja(pengalaman_kerja_id: int, db: Session = Depends(get_db)):
    return crud.delete_pengalaman_kerja(db=db, pengalaman_kerja_id=pengalaman_kerja_id)

# Endpoint untuk CRUD Email
@app.post("/email/", response_model=schemas.Email)
def create_email(email: schemas.EmailCreate, db: Session = Depends(get_db)):
    return crud.create_email(db=db, email=email)

@app.get("/email/{email_id}", response_model=schemas.Email)
def get_email(email_id: int, db: Session = Depends(get_db)):
    return crud.get_email(db=db, email_id=email_id)

@app.get("/email/", response_model=List[schemas.Email])
def get_all_emails(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_emails(db=db, skip=skip, limit=limit)

@app.put("/email/{email_id}", response_model=schemas.Email)
def update_email(email_id: int, email: schemas.EmailCreate, db: Session = Depends(get_db)):
    return crud.update_email(db=db, email_id=email_id, email=email)

@app.delete("/email/{email_id}", response_model=schemas.Email)
def delete_email(email_id: int, db: Session = Depends(get_db)):
    return crud.delete_email(db=db, email_id=email_id)