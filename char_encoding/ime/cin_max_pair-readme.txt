cin_max_pair.pl 是由 countcin_range.pl 改良而來，原先 countcin_range.pl
的功能是計算 cin 檔內可打出的中文字數，以及中文字在 unicode 內的哪個區域。
例如：cjk unified、extension A/B 以及其他...

cin_max_pair.pl 主要去紀錄一個字的所有字根，以及一個字根相關聯的所有文字。

以下是輸出的結果節錄，tab 資料檔使用 liupat.cin，liu6.0 + 補破網 1.3，
再用 uni2txt 把這個對應表轉為文字檔，手工加上 cin 需要的一些欄位。

IME	cjk	extA	extB	misc	total
liupat.cin	18600	0	0	8	18608
--------------------------------------------------------------------------------
艷	14	fcv,fddc,fddl,fdnc,fdnl,ffec,ffel,fifc,fifl,fnc,fncl,iffc,iffl,rorl
麵	14	gcth,gcto,gcty,gpth,gpto,gpty,hg,lcth,lcto,lcty,lpth,lpto,lpty,toh
麶	13	bplu,gcl,gclu,gcwu,gpl,gplu,gpwu,lcl,lclu,lcwu,lpl,lplu,lpwu
麯	12	gcf,gcro,gcrr,gpf,gpro,gprr,lcf,lcro,lcrr,lpf,lpro,lprr
豔	12	fdc,fdyf,ffec,ffef,fifc,fiff,fnc,fncr,iffc,ifff,rorc,rorf
縣	11	mba,mbes,mbps,mes,mess,mls,mlss,ms,msa,msps,mua

[deleted]

--------------------------------------------------------------------------------
yneu	14	殼,穀,轂,嗀,彀,榖,瞉,縠,觳,豰,鷇,嗀,瑴,糓
ufe	11	盂,魨,鮸,鯞,鱮,鯣,鰀,鯂,鮧,鰑,鲀
lok	10	研,哀,袞,磺,斫,碪,硏,碱,碊,厛
ewn	10	建,錄,辿,迍,逿,汖,隶,逷,录,逎

[deleted]

2008/09/25
