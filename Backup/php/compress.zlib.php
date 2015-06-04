#!/usr/bin/php

<?php

$url = 'http://ericosur.googlepages.com/gb2312_widechar.txt.gz';
// 若是遠端網址, http 不可省略
$file = 'compress.zlib://' . $url;

$fh = fopen($file, 'rb');

$data = '';
$cnt = 0;
while (!feof($fh)) {
	++ $cnt;
    $data .= fgets($fh, 128);
    if ($cnt > 2)  {
    	break;
    }
}

echo $data; // 這樣子就會將 filename 的內容印出來.
fclose($fh);

?>
