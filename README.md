# Leafee API

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

## 設定
```
[file_path]
source = iPhone4sの画面画像
output = 出力結果(json)
template_lock = ロック状態のテンプレート画像
template_unlock = アンロック状態のテンプレート画像

[settings]
threshold = テンプレートマッチの適合度(0.99くらいでOK)
mag_size = 利用しているleafee magの個数
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
            "state": "unlocked"
        }
    ]
}
```