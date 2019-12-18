# quickcode


###### tags: ```boshiamy``` ```input``` ```ime``` ```quick```


## description

[eat.pl](./eat.pl) helps to reformat quick 2-keystoke boshiamy table into
a compact form.

The following tables are copied from [boshiamy.com][1]

  * 由__標準字根__產生的兩碼字：共計124個
    * [t1.txt](./t1.txt)
  * 由__簡速字根__產生的兩碼字：共計76個
    * [t2.txt](./t2.txt)
  * 由__頭碼__與__尾碼__所產生的兩碼字：共計324個
    * [t3.txt](./t3.txt)
  * 只看得懂其中的一個碼，但另一碼就看不出來的兩碼字：共計82個
    * [t7.txt](./t7.txt)

以上共606字

- [txt2csv.py](./txt2csv.py) reads __t?.txt__ and output them into __t?.csv__
- [it.py](./it.py) reads __t?.csv__ and __[table.txt][2]__ to show difference those
  combination (70 radicals) which does not exist in t[1,2,3,7].txt.



[1]: https://boshiamy.com/tutorial_advance.php?page=2
[2]: https://github.com/ericosur/charencoding/blob/master/ime/little_prince/table.txt
