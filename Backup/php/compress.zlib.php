#!/usr/bin/php

<?php

$url = 'http://ericosur.googlepages.com/gb2312_widechar.txt.gz';
// �Y�O���ݺ��}, http ���i�ٲ�
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

echo $data; // �o�ˤl�N�|�N filename �����e�L�X��.
fclose($fh);

?>
