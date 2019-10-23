"""
@file         create_table.py
@description  データベース作成およびサンプルデータ挿入用ファイル

@author       RightCode Inc.
@contact      https://rightcode.co.jp/contact
@license      MIT LICENSE
"""

from models import *
import db
import os


if __name__ == "__main__":
    path = SQLITE3_NAME
    if not os.path.isfile(path):

        # テーブルを作成する
        Base.metadata.create_all(db.engine)

    # サンプルユーザ(admin)を作成
    admin = User(username='admin', password='fastapi', mail='hoge@example.com')
    db.session.add(admin)  # 追加
    db.session.commit()  # データベースにコミット

    # サンプルタスク
    task = Task(
        user_id=admin.id,
        content='太郎とランチ',
        deadline=datetime(2019, 10, 21, 12, 00, 00),
    )
    db.session.add(task)
    db.session.commit()

    db.session.close()  # セッションを閉じる
