# HEW
バックエンド制作はこちらのブランチを使います。

現状10/31
・FlaskのBlueprint機能を使って会員認証、画像アップロードができるようになった
・画像アップロードはログインしてからでないとエラーが出る
・DBはMySQLを使用、apps/config.pyより自分の環境に合わせて
　「mysql+pymysql://{user}:{password}@{host}/{db_name}」と設定すれば同期されるはず。
