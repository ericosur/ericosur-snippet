# README

> [!NOTE]
> What kinds of words qualify as idioms is a subject of debate. Here, we're simply using an idiom table from the Ministry of Education.
> 什麼樣的詞才能當作成語有爭議，這裡只是使用一個來自教育部的成語表格來使用

- table from: https://language.moe.gov.tw/001/Upload/Files/site_content/M0001/respub/dict_idiomsdict_download.html

After cleanup, the result table is ```idiom_list.py```. Refer to ```pickme.py``` for usage.


## files

- idiom_list.py
	- a python syntax dict for all idioms
- numer4_idioms.py
	- idioms that has
		- only 4 han characters
		- with numbers or quantity characters

## sort

TODO: sort the idiom_list by ㄅㄆㄇㄈ.

- 拼音排序：以「拼音」為基礎的 Unicode 排序。
- 部首筆畫排序：以標準康熙為排列順序，先以部首，然後是筆畫數做整理。
- 筆畫排序：以筆畫為基礎的 Unicode 排序。
- 注音排序：以注音（ㄅㄆㄇㄈ）語音符號為基礎的繁體中文排序。
