# AtCoder 環境
[AtCoder](https://atcoder.jp/) のツール

## setup
- 設定
```
$ cd atcoder
$ pip install -e .
```

## Features
- サンプルケースを取得して、テンプレート準備
```sh
$ at https://atcoder.jp/contests/abc234/tasks/abc234_a d
```
- サンプルケースのテストを実行
```sh
$ at https://atcoder.jp/contests/abc234/tasks/abc234_a t
```
- コードを提出(Pypy)
```sh
$ at https://atcoder.jp/contests/abc234/tasks/abc234_a s
```
- コードを提出(Python3)
```sh
$ at https://atcoder.jp/contests/abc234/tasks/abc234_a ss
```

## On contest
- tool/contest_id.txt の中身を変える
```sh
$ setconid abc234
```
```txt:contest_id.txt
con_root="https://atcoder.jp/contests"
con_id="abc234"
```
- コンテスト中
```sh
$ pya [command]
$ pyb [command]
...
$ pyf [command]
```

## Requirements
[online-judge-tools](https://github.com/kmyk/online-judge-tools)