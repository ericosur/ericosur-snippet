<?php
/**
 The MIT License

 Copyright (c) 2007 <Tsung-Hao>

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
 * function English2ArabicNumeral($english_number_string)
 * English numeral words convert to arabic numeral.
 *
 * @author: Tsung <tsunghao@gmail.com> http://plog.longwin.com.tw
 * @date: 2007/11/25
 * @version: v1.00
 * @desc: http://plog.longwin.com.tw/programming/2007/11/25/php_english_arabic_numeral_convert_2007
 *
 * @param english number string
 * @return arabic numeral
 */
function English2ArabicNumeral($english)
{
    if (empty($english)) {
        return;
    }

    $english_list = array('negative', 'zero',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
            'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
            'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
            'hundred', 'thousand', 'million', 'billion');

    $number_list = array(-1, 0,
            11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 30, 40, 50, 60, 70, 80, 90,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            100, 1000, 1000000, 1000000000);

    $sum = 0; // 算總數
    $sum_array = array();
    $negative = 1; // 正負數(最後要乘上此值)

    // remove '-' & more space ( - => remove, more space => a space)
    $english = str_replace('-', ' ', $english);
    $english = preg_replace('/ +/', ' ', $english);

    // english numeral word replace to arabic numeral
    $number = str_replace($english_list, $number_list, $english);

    // split to array by space
    $num_array = split(' ', $number);

    // 遇到連續 %100 == 0 的狀況, 需特殊處理.
    $double_multiply = false;
    for ($i = 0, $j = 0, $c = count($num_array); $i < $c; $i++) {
        // remove last 's' or 'AND' or any non-numeral something.
        $num_array[$i] = intval($num_array[$i]);

        // if value == null, continue.
        if ('' == $num_array[$i]) {
            $j++;
            continue;
        }

        if (0 > $num_array[$i]) {
            $negative = -1;
            $double_multiply = false;
        } else if (0 === $num_array[$i]) { // zero
            // special case: english zero is 0, so ... if zero, return 0
            $double_multiply = false;
            return 0;
        } else if (100 > $num_array[$i]) {
            if (isset($sum_array[$j])) {
                $sum_array[$j] += $num_array[$i];
            } else {
                $sum_array[$j] = $num_array[$i];
            }

            $double_multiply = false;
        } else if (0 == $num_array[$i] % 100) {
            // 若上一次也是 %100 == 0, 那就需要多 做一次乘法
            if ($double_multiply) {
                $j--;
            }

            if (isset($sum_array[$j])) {
                $sum_array[$j] *= $num_array[$i];
            } else {
                $sum_array[$j] = $num_array[$i];
            }
            $j++;

            $double_multiply = true;
        } else {
            // none, 不應該會跑來這邊.
        }
    }

    foreach ($sum_array as $key => $num) {
        $sum += $num;
    }

    return $sum * $negative;
}

/* Test */
//$english = 'negative seven hundred twenty nine'; // -729
//$english = 'six'; // 6
//$english = 'one million one hundred one'; // 1000101
//$english = 'sixty four thousand'; // 64000
//$english = 'one hundred thousand'; // 100000
/*
$english = 'one hundred thousand and thirty four hundred'; // 103400
echo English2ArabicNumeral($english) . "\n";
*/
?>
