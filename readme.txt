これはエンジニアの情報収集を効率的に行うためのソフトウェアである。

使い方
　Windowsを搭載したPCでの実行環境を想定している。Webアプリケーションであるため、インターネットへのアクセスが必要となる。また、アプリの作成にはflaskを使用し、各ライブラリ等のインストールが必要となる。

Pythonの3.10.11のバージョンをインストールする必要がある。
次にコマンドプロンプトにおいて以下のコマンドでpipコマンドのアップグレードを行う。
$python -m pip install --upgrade pip

次に、アプリのファイルが置かれているディレクトリに移動し、以下のコマンドで必要なライブラリのインストールを行う。
$pip install -r requirements.txt
※上記のコマンドが上手く動作しない場合は以下のライブラリを個別にpipコマンドでインストールしてください。
ex) $pip install flask==2.0.3

ライブラリとバージョンのリストを以下に示す。
flask==2.0.3
flask-wtf==0.15.1
flask_sqlalchemy==2.5.1
flask_migrate==3.1.0
flask_login==0.5.0
pytz==2021.3
pillow==9.0.1
werkzeug==2.0.3
wtforms==2.3.3
jinja2==3.0.3
email-validator==1.1.3
SQLALchemy==1.4.44
beautifulsoup4==4.12.2
feedparser==6.0.10
requests==2.31.0

次にコマンドラインからapp.pyのあるディレクトリ下に移動し、以下のコマンドを実行する。
$python run app.py
コマンドラインに表示されるURLにアクセスすると、アプリを起動することができる。
