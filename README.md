USB赤外線リモコンアドバンス コロナVXシリーズ 自動延長ツール
====

## 概要

USB赤外線リモコンアドバンスを使用した  
コロナVXシリーズ(石油ファンヒーター)の自動延長ツールです。

いちいち手動で延長する手間を省くことができますが、  
部屋を離れるときや寝るときは危険なので停止してください。  
（このツールの利用で起きたことについて筆者は責任を取れません）

対応OS : Linux  
Raspberry Pi（ラズベリーパイ）で動きます。

## 使い方

インストール後、pythonスクリプトを実行、または自動設定している場合はそのままで動作します。

0:00から22:00まで2時間置きに延長コマンドが送信されます。

## インストール

1. Linuxのコマンドラインツールをインストールします  
https://github.com/nakamichi3011/bto_ir_advanced_cmd

pythonのScheduleライブラリを使用しています。  
インストールしていない人はこれもインストールします。

2. このプロジェクトのファイルを適当な場所に置きます

3. pythonスクリプトを実行します

## 自動起動する手順

・init.dをお使いの方  
init_dに自動登録用のスクリプトを置きました。  
自身の環境のinit.dに置いて再起動し動くか確認してみてください。

・systemdをお使いの方  
system_dにスクリプトを用意しましたが、未確認です。  

## 改造方法

while_extend_heater.pyが本体のファイルです。  
extend_heater.txtが延長コマンドです。  
コマンドファイルを何かしらのオリジナルコマンドを登録して、  
それをpythonスクリプト上で呼び出すように変更すると、  
他のコマンドがスケジュール実行されます。

## ライセンス

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## 開発元

[nakamichi3011](https://github.com/nakamichi3011)
