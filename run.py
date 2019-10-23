"""
@file         run.py
@description  サーバ立ち上げ用ファイル

@author       RightCode Inc.
@contact      https://rightcode.co.jp/contact
@license      MIT LICENSE
"""

from urls import app
import uvicorn

if __name__ == '__main__':
    # コンソールで [$ uvicorn run:app --reload]でも可
    uvicorn.run(app=app)
