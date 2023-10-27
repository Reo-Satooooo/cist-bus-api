# 公立千歳科学技術大学シャトルバス時刻表API

## 概要
公立千歳科学技術大学のシャトルバスの時刻表を取得するAPIです。  
[公立千歳科学技術大学HP](https://www.chitose.ac.jp/access/)のシャトルバス時刻表をスクレイピングしています。

## 使い方
プロジェクトをクローンし、python3.7以上で実行してください。
```
cd bus-api
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
uvicorn main:app --reload
```
仮想環境でPythonパッケージを簡易する場合は以下の記事を参考にしてください。
[Pythonの開発環境の3つの観点をおさえよう](https://zenn.dev/os1ma/articles/935f6e653f1052)

### バス停の一覧を取得する
```
GET /json
```
#### レスポンス例
```
{
  "sheet": {
    "created at": "2023-10-27 00:10",
    "timetable": {
      "outbound": [
        {
          "chitose": "7:48",
          "minami_chitose": "-",
          "lab": "8:03",
          "main": "8:06",
          "remark": "0b00100"
        },
        {
          "chitose": "-",
          "minami_chitose": "7:55",
          "lab": "8:03",
          "main": "8:06",
          "remark": "0b00010"
        },
        {
          "chitose": "7:58",
          "minami_chitose": "8:08",
          "lab": "8:16",
          "main": "8:19",
          "remark": "0b00000"
        }
    ],
      "inbound": [
        {
          "main": "10:45",
          "lab": "10:48",
          "minami_chitose": "10:56",
          "chitose": "11:06",
          "remark": "0b00000"
        },
        {
          "main": "11:25",
          "lab": "11:28",
          "minami_chitose": "11:36",
          "chitose": "11:46",
          "remark": "0b00000"
        },
        {
          "main": "12:22",
          "lab": "12:25",
          "minami_chitose": "12:33",
          "chitose": "12:43",
          "remark": "0b00000"
        }
      ]
    }
  }
}
```
#### 詳細
- "created at": 時刻表をスクレイピングした日時。"YYYY-MM-DD HH:MM"の形式で表現されます。
- "timetable": 時刻表のデータです。
- "outbound": 往路の時刻表。
- "inbound": 復路の時刻表。
- "chitose": 千歳駅に発着する時刻。発着しない場合は"-"が入ります。
- "minami_chitose": 南千歳駅に発着する時刻。発着しない場合は"-"が入ります。
- "lab": 研究棟に発着する時刻。発着しない場合は"-"が入ります。
- "main": 本部棟に発着する時刻。発着しない場合は"-"が入ります。
- "remark": 備考を参照してください。

#### 備考
"remark"は、バス停の発着状況を表す数字です。
第1bit -> 復路のバス乗り場。0なら1番乗り場、1なら2番乗り場。
第2bit -> 1なら千歳駅に発着しない
第3bit -> 1なら南千歳駅に発着しない
第4bit -> 1なら研究棟に発着しない
第5bit -> 1なら本部棟に発着しない