#!/usr/bin/php
<?php
/**
 The MIT License

 Copyright (c) 2008 <Tsung-Hao>

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
 *
 * @author: Tsung <tsunghao@gmail.com> http://plog.longwin.com.tw
 * @date: 2008/08/20
 * @version: v1.00
 * @desc: http://plog.longwin.com.tw/programming/2008/08/20/php-timezone-conver-date-time-2008
 */

/**
 * 看加洲現在時間幾點
 */
// Create two timezone objects, one for Taipei (Taiwan) and one for
// Tokyo (Japan)
$dateTimeZoneTaipei = new DateTimeZone('Asia/Taipei'); // $dateTimeZoneTaipei = timezone_open('Asia/Taipei');
$dateTimeZoneUS = new DateTimeZone('America/Los_Angeles'); // $dateTimeZoneUS = timezone_open('America/Los_Angeles');

// Create two DateTime objects that will contain the same Unix timestamp, but
// have different timezones attached to them.
$dateTimeTaipei = new DateTime('now', $dateTimeZoneTaipei);
$dateTimeUS = new DateTime('now', $dateTimeZoneUS);

// Calculate the GMT offset for the date/time contained in the $dateTimeTaipei
// object, but using the timezone rules as defined for Tokyo
// ($dateTimeZoneJapan).
$timeOffset = $dateTimeZoneUS->getOffset($dateTimeTaipei);
$timeOffset = 8 - ($timeOffset / 60 / 60);

echo 'Now Time(Taiwan): ';
$hour = 60 * 60;
echo date('Y-m-d H:i:s', time());
echo "\n";

echo 'LA Time: ';
$x = time() - $hour * $timeOffset;
echo date('Y-m-d H:i:s', $x);
echo "\n";

exit;
?>
