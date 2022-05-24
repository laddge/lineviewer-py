# lineviewer [ROOT]
AndroidでLINEのトークを既読付けずに見るツール

## インストール
**root権限が必要です**
Termuxなどのターミナルエミュレーターで実行してください

```
wget https://github.com/laddge/lineviewer/raw/master/dist/lineviewer
chmod a+x lineviewer
```

## 使い方
### トークルームのリストを表示

```
sudo ./lineviewer -l
```

### トーク内容を表示
0番のトーク履歴を全て表示:

```
sudo ./lineviewer -i 0
```

最新の10件だけ表示:

```
sudo ./lineviewer -i 0 -c 10
```
