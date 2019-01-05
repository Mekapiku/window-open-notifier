# Windows Open Notifier

## これは何？
[Leafee](https://leafee.me/)の画面キャプチャから無理やりJSONファイルを生成するやつです．

## 使い方
1. iPhone4sを用意します
* 脱獄して，[Veency](https://cydia.saurik.com/info/veency/)などのVNCサーバを導入します
* [VNC Snapshot](http://vncsnapshot.sourceforge.net/)などでiPhone4sの画面を撮影します
* このスクリプトを動かします
    * `brew install opencv numpy pyenv`
    * `pyenv install 3.7.0`
    * `pyenv global 3.7.0`
    * `pip install opencv-python matplotlib`
* 現在の窓の開閉状況をJSONで出力できます

## 実行
```
python app.py out.json screenshot.png 3

ARGV[1] : 出力結果(json)ファイル名
ARGV[2] : iPhone4sの画面画像
ARGV[3] : 利用しているleafee magの個数
```

## 出力結果(例)
```
{
    "mags": [
        {
            "id": 0,
            "state": "locked"
        },
        {
            "id": 1,
            "state": "locked"
        },
        {
            "id": 2,
            "state": "locked"
        }
    ]
}
```

## その他
[Leafeeシングルプラン](https://leafee.me/price)に加入したほうが早いし安いし便利です．
