原本的 system.img 可以使用

$ sudo mount -t ext4 -o loop system.img /mnt/system

loop 進自己的桌面系統, 但是在 chagall codebase 裡頭，blake 更改了
ext4_utils.c
write_ext4_image()
pad_output_file() 這行呼叫裡刪去。（註一）

導致我們產出使用 make_ext4fs 的 image 無法被 ubuntu 所 mount。（註二）

解決的方法是把少掉的 padding 使用 mypad.pl 補回來。（註三）



註一：請看 ext4_utils.c-git.diff

註二：google原先的可以，我們的不行
mount：錯誤檔案系統類型、不當的選項、不當的超區塊於 /dev/loop1,
      缺少編碼頁或輔助程式，或其他錯誤
       在某些狀況下，syslog 中可以找到有用的資訊 - 嘗試
      dmesg | tail 之類命令
[110264.017053] EXT4-fs (loop1): bad geometry: block count 131072 exceeds size of device (130713 blocks)

註三：雖然可以 mount 但是 dmesg 還是有錯誤警告：
[108944.561417] EXT4-fs (loop1): mounted filesystem with ordered data mode. Opts: (null)

註四：make_ext4fs-google 是原本 AOSP 版本的 make_ext4fs，產出的image可以用mount。製
作的指令可以參考 callmkext4.sh
