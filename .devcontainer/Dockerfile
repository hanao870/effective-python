FROM python:3.10.5

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    # リンター. pycodestyle(pep8 スタイルチェック), pyflakes(論理エラーのチェック), mccabe(複雑度チェック) をまとめたツール
    flake8==4.0.1 \
    # 静的型チェックツール
    mypy==0.961 \
    # プログラムの静的セキュリティチェックツール
    bandit==1.7.4 \
    # PEP 257 で規定されている docstring のリンター
    pydocstyle==6.1.1 \
    # PEP8 準拠の Pytho コードフォーマッタ
    black==22.3.0 \
    # import の並びを整形するフォーマッタ
    isort==5.10.1 \
    # コミット前の検証ツール. git hook を使用
    pre-commit==2.19.0

RUN apt-get update \
    && apt-get install -y --no-install-recommends rubygems \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV TZ Asia/Tokyo