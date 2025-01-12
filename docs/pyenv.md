# pyenv
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

---
[Back to index](index.md)