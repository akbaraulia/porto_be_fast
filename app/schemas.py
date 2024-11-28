from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# Schema untuk Biodata
class BiodataBase(BaseModel):
    nama_lengkap: str
    nama_panggilan: str
    stack: List[str]
    overview: str
    cv: str

class BiodataCreate(BiodataBase):
    pass

class Biodata(BiodataBase):
    id: int

    class Config:
        orm_mode = True

# Schema untuk Project
class ProjectBase(BaseModel):
    nama: str
    deskripsi: str
    stack: List[str]
    link_github: str
    link_page: Optional[str] = None
    image_url: List[str]

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True

# Schema untuk SubProject
class SubProjectBase(BaseModel):
    nama: str
    deskripsi: str
    stack: List[str]
    link_github: str
    link_page: Optional[str] = None
    image_url: List[str]

class SubProjectCreate(SubProjectBase):
    pass

class SubProject(SubProjectBase):
    id: int

    class Config:
        orm_mode = True

# Schema untuk Pendidikan
class PendidikanBase(BaseModel):
    nama_sekolah: str
    tahun_masuk: date
    tahun_keluar: date
    jurusan: str
    logo_url: str
    image_urls: Optional[List[str]] = None

class PendidikanCreate(PendidikanBase):
    pass

class Pendidikan(PendidikanBase):
    id: int

    class Config:
        orm_mode = True

# Schema untuk Pengalaman Kerja
class PengalamanKerjaBase(BaseModel):
    nama_instansi: str
    tahun_masuk: date
    tahun_keluar: date
    role: str
    description: str
    logo_url: str
    image_urls: Optional[List[str]] = None

class PengalamanKerjaCreate(PengalamanKerjaBase):
    pass

class PengalamanKerja(PengalamanKerjaBase):
    id: int

    class Config:
        orm_mode = True

# Schema untuk Email
class EmailBase(BaseModel):
    nama: str
    email: str
    message: str

class EmailCreate(EmailBase):
    pass

class Email(EmailBase):
    id: int

    class Config:
        orm_mode = True
