from sqlalchemy.orm import Session
from . import models, schemas

# CRUD untuk Biodata
def create_biodata(db: Session, biodata: schemas.BiodataCreate):
    db_biodata = models.Biodata(**biodata.dict())
    db.add(db_biodata)
    db.commit()
    db.refresh(db_biodata)
    return db_biodata

def get_biodata(db: Session, biodata_id: int):
    return db.query(models.Biodata).filter(models.Biodata.id == biodata_id).first()

def get_all_biodata(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Biodata).offset(skip).limit(limit).all()

def update_biodata(db: Session, biodata_id: int, biodata: schemas.BiodataCreate):
    db_biodata = db.query(models.Biodata).filter(models.Biodata.id == biodata_id).first()
    if db_biodata:
        for key, value in biodata.dict().items():
            setattr(db_biodata, key, value)
        db.commit()
        db.refresh(db_biodata)
    return db_biodata

def delete_biodata(db: Session, biodata_id: int):
    db_biodata = db.query(models.Biodata).filter(models.Biodata.id == biodata_id).first()
    if db_biodata:
        db.delete(db_biodata)
        db.commit()
    return db_biodata

# CRUD untuk Project
def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

def get_all_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()

def update_project(db: Session, project_id: int, project: schemas.ProjectCreate):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_project:
        for key, value in project.dict().items():
            setattr(db_project, key, value)
        db.commit()
        db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_project:
        db.delete(db_project)
        db.commit()
    return db_project

# CRUD untuk SubProject
def create_sub_project(db: Session, sub_project: schemas.SubProjectCreate):
    db_sub_project = models.SubProject(**sub_project.dict())
    db.add(db_sub_project)
    db.commit()
    db.refresh(db_sub_project)
    return db_sub_project

def get_sub_project(db: Session, sub_project_id: int):
    return db.query(models.SubProject).filter(models.SubProject.id == sub_project_id).first()

def get_all_sub_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SubProject).offset(skip).limit(limit).all()

def update_sub_project(db: Session, sub_project_id: int, sub_project: schemas.SubProjectCreate):
    db_sub_project = db.query(models.SubProject).filter(models.SubProject.id == sub_project_id).first()
    if db_sub_project:
        for key, value in sub_project.dict().items():
            setattr(db_sub_project, key, value)
        db.commit()
        db.refresh(db_sub_project)
    return db_sub_project

def delete_sub_project(db: Session, sub_project_id: int):
    db_sub_project = db.query(models.SubProject).filter(models.SubProject.id == sub_project_id).first()
    if db_sub_project:
        db.delete(db_sub_project)
        db.commit()
    return db_sub_project

# CRUD untuk Pendidikan
def create_pendidikan(db: Session, pendidikan: schemas.PendidikanCreate):
    db_pendidikan = models.Pendidikan(**pendidikan.dict())
    db.add(db_pendidikan)
    db.commit()
    db.refresh(db_pendidikan)
    return db_pendidikan

def get_pendidikan(db: Session, pendidikan_id: int):
    return db.query(models.Pendidikan).filter(models.Pendidikan.id == pendidikan_id).first()

def get_all_pendidikan(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pendidikan).offset(skip).limit(limit).all()

def update_pendidikan(db: Session, pendidikan_id: int, pendidikan: schemas.PendidikanCreate):
    db_pendidikan = db.query(models.Pendidikan).filter(models.Pendidikan.id == pendidikan_id).first()
    if db_pendidikan:
        for key, value in pendidikan.dict().items():
            setattr(db_pendidikan, key, value)
        db.commit()
        db.refresh(db_pendidikan)
    return db_pendidikan

def delete_pendidikan(db: Session, pendidikan_id: int):
    db_pendidikan = db.query(models.Pendidikan).filter(models.Pendidikan.id == pendidikan_id).first()
    if db_pendidikan:
        db.delete(db_pendidikan)
        db.commit()
    return db_pendidikan

# CRUD untuk Pengalaman Kerja
def create_pengalaman_kerja(db: Session, pengalaman_kerja: schemas.PengalamanKerjaCreate):
    db_pengalaman_kerja = models.PengalamanKerja(**pengalaman_kerja.dict())
    db.add(db_pengalaman_kerja)
    db.commit()
    db.refresh(db_pengalaman_kerja)
    return db_pengalaman_kerja

def get_pengalaman_kerja(db: Session, pengalaman_kerja_id: int):
    return db.query(models.PengalamanKerja).filter(models.PengalamanKerja.id == pengalaman_kerja_id).first()

def get_all_pengalaman_kerja(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PengalamanKerja).offset(skip).limit(limit).all()

def update_pengalaman_kerja(db: Session, pengalaman_kerja_id: int, pengalaman_kerja: schemas.PengalamanKerjaCreate):
    db_pengalaman_kerja = db.query(models.PengalamanKerja).filter(models.PengalamanKerja.id == pengalaman_kerja_id).first()
    if db_pengalaman_kerja:
        for key, value in pengalaman_kerja.dict().items():
            setattr(db_pengalaman_kerja, key, value)
        db.commit()
        db.refresh(db_pengalaman_kerja)
    return db_pengalaman_kerja

def delete_pengalaman_kerja(db: Session, pengalaman_kerja_id: int):
    db_pengalaman_kerja = db.query(models.PengalamanKerja).filter(models.PengalamanKerja.id == pengalaman_kerja_id).first()
    if db_pengalaman_kerja:
        db.delete(db_pengalaman_kerja)
        db.commit()
    return db_pengalaman_kerja

# CRUD untuk Email
def create_email(db: Session, email: schemas.EmailCreate):
    db_email = models.Email(**email.dict())
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email

def get_email(db: Session, email_id: int):
    return db.query(models.Email).filter(models.Email.id == email_id).first()

def get_all_emails(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Email).offset(skip).limit(limit).all()

def update_email(db: Session, email_id: int, email: schemas.EmailCreate):
    db_email = db.query(models.Email).filter(models.Email.id == email_id).first()
    if db_email:
        for key, value in email.dict().items():
            setattr(db_email, key, value)
        db.commit()
        db.refresh(db_email)
    return db_email

def delete_email(db: Session, email_id: int):
    db_email = db.query(models.Email).filter(models.Email.id == email_id).first()
    if db_email:
        db.delete(db_email)
        db.commit()
    return db_email