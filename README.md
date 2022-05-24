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

```
# output
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx hoge
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx fuga
...
```

### トーク内容を表示
トーク履歴を全て表示:

```
sudo ./lineviewer -i xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

最新の10件だけ表示:

```
sudo ./lineviewer -i xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -c 10
```
