from sqlalchemy import Column, Integer, String, Text, Date, ARRAY
from sqlalchemy.orm import relationship
from .database import Base

# Model untuk Biodata
class Biodata(Base):
    __tablename__ = 'biodata'

    id = Column(Integer, primary_key=True, index=True)
    nama_lengkap = Column(String, index=True)
    nama_panggilan = Column(String)
    stack = Column(ARRAY(String))
    overview = Column(Text)
    cv = Column(String)

# Model untuk Project
class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    deskripsi = Column(Text)
    stack = Column(ARRAY(String))
    link_github = Column(String)
    link_page = Column(String)
    image_url = Column(ARRAY(String))

# Model untuk SubProject
class SubProject(Base):
    __tablename__ = 'sub_project'

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    deskripsi = Column(Text)
    stack = Column(ARRAY(String))
    link_github = Column(String)
    link_page = Column(String)
    image_url = Column(ARRAY(String))
    project_id = Column(Integer, index=True)  # Foreign Key ke project

# Model untuk Pendidikan
class Pendidikan(Base):
    __tablename__ = 'pendidikan'

    id = Column(Integer, primary_key=True, index=True)
    nama_sekolah = Column(String)
    tahun_masuk = Column(Date)
    tahun_keluar = Column(Date)
    jurusan = Column(String)
    logo_url = Column(String)
    image_urls = Column(ARRAY(String))

# Model untuk Pengalaman Kerja
class PengalamanKerja(Base):
    __tablename__ = 'pengalaman_kerja'

    id = Column(Integer, primary_key=True, index=True)
    nama_instansi = Column(String)
    tahun_masuk = Column(Date)
    tahun_keluar = Column(Date)
    role = Column(String)
    description = Column(Text)
    logo_url = Column(String)
    image_urls = Column(ARRAY(String))

# Model untuk Email
class Email(Base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String)
    email = Column(String)
    message = Column(Text)
