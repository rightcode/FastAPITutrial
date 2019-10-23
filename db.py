"""
@file         db.py
@description  データベース設定用ファイル

@author       RightCode Inc.
@contact      https://rightcode.co.jp/contact
@license      MIT LICENSE
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
RDB_PATH = 'sqlite:///db.sqlite3'
ECHO_LOG = False  # セッションを行う度にログを表示させたければTrue

engine = create_engine(
   RDB_PATH, echo=ECHO_LOG
)

Session = sessionmaker(bind=engine)
session = Session()
