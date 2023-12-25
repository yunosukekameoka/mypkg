# robosys2023_ros2_ws
このリポジトリは2023年4sのロボットシステム学の授業の課題で作成したROS 2のパッケージです。

[![test](https://github.com/yunosukekameoka/robosys2023_ros2_ws/actions/workflows/test.yml/badge.svg)](https://github.com/yunosukekameoka/robosys2023_ros2_ws/actions/workflows/test.yml)

## 機能
* talkerとlistenerの二つのノードがあり、機能はそれぞれ次のようになる。
###talker
* "talker"ノードは0.5秒定期に整数値を0から1ずつ増加させながら"countup"トピックにパブリッシュする
###listener
* "listener"ノードは"countup"というトピックから整数メッセージを受信し、その内容をログに表示する

## インストール
* ROS 2をダウンロードがされていない場合は以下を入力し実行して下さい。

Ubuntuのターミナルに以下を入力してください。
```
$ git clone https://github.com/yunosukekameoka/robosys2023_ros2_ws.git
```

## 実行例
* talker
```
$ ros2 run mypkg talker
(何も表示されない)
```
別端末でros2を使ってサブスクライブする
```
$ ros2 topic echo /countup
data: 0
---
data: 1
---
data: 2
---
・・・
```

* listener
  * listenerのみで実行した場合
```
$ ros2 run mypkg listener
(何も表示されない)
```
  * talkerを実行した状態で別端末でlistenerを実行した場合
```
端末１$ ros2 run mypkg talker　
端末２$ ros2 run mypkg listener
[INFO] [1703493670.563216112] [listener]: Listen: 9
[INFO] [1703493671.052137853] [listener]: Listen: 10
[INFO] [1703493671.552634157] [listener]: Listen: 11
[INFO] [1703493672.051993306] [listener]: Listen: 12
・・・
```

* ２つを同じ端末上で実行
```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/"youer_name"/.ros/log/
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [26658]
[INFO] [listener-2]: process started with pid [26660]
[listener-2] [INFO] [1703494426.636467029] [listener]: Listen: 0
[listener-2] [INFO] [1703494427.130861401] [listener]: Listen: 1
・・・　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
```

## 必要なソフトウェア
* ROS 2
* Python
  * テスト済み: 3.7～3.10

## テスト環境
* Ubuntu 20.04.6 LTS


## 著作権、ライセンス

  * このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
  * このパッケージのコードは，下記のスライド群（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
      * [ryuichiueda/my_slides robosys_2022/lesson4.html#/20](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson4.html#/20)
 
  * © 2023 Yunosuke Kameoka




