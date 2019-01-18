#!/usr/bin/env python3
#coding:UTF-8

import os
import sys
import schedule
import time
import pygame.mixer

# 読み込みファイル名
ExtendHeaterFileName = './extend_heater.txt'

# 赤外線送信
def send(code):
	os.system('/usr/local/bin/bto_advanced_USBIR_cmd -d ' + code)

# 延長コードの送信
def job():
	f = open(ExtendHeaterFileName, 'r')
	code = f.read()
	send(code);
	print("sended extend heater code.")

# 繰り返しテスト
def registerTest():
	# 10秒毎に送信
	schedule.every(10).seconds.do(job)

# 繰り返しタイムテーブルの登録
def registerTimeTable():
	schedule.every().day.at("00:00").do(job)
	schedule.every().day.at("02:00").do(job)
	schedule.every().day.at("04:00").do(job)
	schedule.every().day.at("06:00").do(job)
	schedule.every().day.at("08:00").do(job)
	schedule.every().day.at("10:00").do(job)
	schedule.every().day.at("12:00").do(job)
	schedule.every().day.at("14:00").do(job)
	schedule.every().day.at("16:00").do(job)
	schedule.every().day.at("18:00").do(job)
	schedule.every().day.at("20:00").do(job)
	schedule.every().day.at("22:00").do(job)

if __name__ == '__main__':
	
	# 初回起動時、音声を鳴らす
	pygame.mixer.init()
	pygame.mixer.music.load("./sound/se.mp3")
	pygame.mixer.music.play()
	
	job() # 初回起動時
	#registerTest() # テスト 10秒毎処理 (テストOK)
	registerTimeTable() # 2時間置き、既定時刻に処理
	while True:
		schedule.run_pending()
		time.sleep(1)
