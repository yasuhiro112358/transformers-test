## 依存関係の管理
```bash
# 依存パッケージのインストール
pip install transformers

# 依存パッケージの保存
# インストールしたパッケージをrequirements.txtに保存できる
pip freeze > requirements.txt

# 依存パッケージのインストール
# requirements.txtに記載されたパッケージをインストールできる
pip install -r requirements.txt

# 依存パッケージのアップデート
pip list --outdated
pip install --upgrade transformers
```

## pyenvを使用したPythonバージョンの管理
- Python自体のバージョン管理を行うツール
- インストールしたPythonバージョンを切り替えることができる
- インストールしたPythonバージョンの一覧表示や現在のPythonバージョンの表示ができる

```bash
# インストール（macOSの場合）
brew update
brew install pyenv

# 指定したPythonバージョンをインストール
# インストール場所は~/.pyenv/versions/以下
pyenv install 3.10.12

# インストールしたPythonバージョンの一覧表示
pyenv versions

# 現在のPythonバージョンの表示
pyenv version

# インストールしたPythonバージョンの切り替え
# .python-versionに設定内容が記述される
pyenv local 3.10.12
```


## 仮想環境の作成
- 仮想環境を作成することで、プロジェクトごとに環境を分けることができる
- 仮想環境を有効化することで、プロジェクトごとに異なる依存パッケージを使用できる
- Python標準ライブラリのvenvモジュールを使用することで、仮想環境を作成できる
- Python自体のバージョン管理は、pyenvで行う

```bash
# 仮想環境の作成
# -mオプションは指定されたモジュール（この場合はvenv）を実行するために使用される
# venvは作成する仮想環境のディレクトリ名
python3 -m venv venv

# 仮想環境の有効化
source venv/bin/activate

# 仮想環境の無効化
deactivate
```









## pyenvを使用したPythonバージョンと仮想環境の管理
```bash
# pyenvを使用したPythonバージョンと仮想環境の管理
# .python-versionファイルを作成し、使用するPythonバージョンを記述
echo "3.10.12" > .python-version

# 必要な依存関係のインストール（macOSの場合）
brew update
brew install pyenv

# 指定したPythonバージョンをインストール
# インストール場所は~/.pyenv/versions/以下
pyenv install 3.10.12

# pyenv-virtualenvをインストール
brew install pyenv-virtualenv

# シェルの設定ファイルに追加
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"


# 仮想環境の作成
# 仮想環境の作成場所は~/.pyenv/versions/以下
pyenv virtualenv 3.10.12 transformers-test-env

# 仮想環境の削除
pyenv uninstall transformers-test-env

# 仮想環境の有効化
pyenv activate transformers-test-env

# 仮想環境の無効化
pyenv deactivate

# 仮想環境の有効化の確認
# 仮想環境の有効化が成功している場合、仮想環境のパスが表示される
echo $VIRTUAL_ENV


# プロジェクトで仮想環境を使用
pyenv local transformers-test-env


# 依存パッケージのインストール
pip install -r requirements.txt


# 仮想環境の一覧表示
pyenv versions

# 現在のPythonバージョンの表示
pyenv version


```
