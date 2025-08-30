

- AHC***フォルダを作成
- 移動する
- zipファイルをコピーする
- zipファイルをunzip
-
- root\tool\run.pyをrun.py をコピーする
```
mkdir ahc043
cd ahc043
wget https://img.atcoder.jp/ahc043/de43f43a9c.zip
unzip de43f43a9c.zip
cp ../tool/run.py run.py
```


<AHC*** フォルダ>
  ├── run.py
  ├── main**.py
  └── <tools> or <tools_x86_64-pc-windows-gnu>
         ├── in/****.txt          # テスト入力
         ├── out/****.txt         # テスト出力
         └── target/release/vis.exe   # ローカルテスタ実行ファイル
https://zenn.dev/ikoma_3/articles/5c04ab03935f71