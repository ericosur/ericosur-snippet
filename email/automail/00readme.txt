00readme.txt	本說明檔
1.txt			除錯訊息檔 #1
2.txt			除錯訊息檔 #2
automail.log	運行時間的紀錄檔
automailer.pl	寄信的 perl script
mail.conf		寄件人與寄件server的設定檔，目前設定用 dailybuild 寄信
mailbody.txt	信件的內容檔，檔案的第一行會被視作標題
				(目前預設把內容視為 big5 編碼，並轉為 utf-8，所以餵 utf-8 內容反而會變亂碼)
recp.conf		收件人清單 (一行一個人，可用 # 作註解)要記得改
rr.bat			偷懶用的批次檔，命令參數都寫好了，定時跑這支
