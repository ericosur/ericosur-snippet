<?php
/**
 * Morse code encode/decode
 *
 * Powerby: Mgccl's
 * Doc: http://en.wikipedia.org/wiki/Morse_code
 * Source code: http://mgccl.com/2007/01/24/morse-code-in-php/
 */
function morse_encode($string)
{
    $strlength = strlen($string);
    $string = strtoupper($string);
    $i = 0;
    $search = array(
            ' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
            '4', '5', '6', '7', '8', '9', '.', ',', '?', '\'',
            '!', '/', '(', ')', '&', ':', ';', '=', '-', '_',
            '"', '$', '@'
            );

    $replace = array(
            '    ','¡P* ', '*¡P¡P¡P ', '*¡P*¡P ', '*¡P¡P ', '¡P ', '¡P¡P*¡P ', '**¡P ', '¡P¡P¡P¡P ', '¡P¡P ', '¡P*** ',
            '*¡P* ', '¡P*¡P¡P ', '** ', '*¡P ', '*** ', '¡P**¡P ', '**¡P* ', '¡P*¡P ', '¡P¡P¡P ', '* ',
            '¡P¡P* ', '¡P¡P¡P* ', '¡P** ', '*¡P¡P* ', '*¡P** ', '**¡P¡P ', '***** ', '¡P**** ', '¡P¡P*** ', '¡P¡P¡P** ',
            '¡P¡P¡P¡P* ', '¡P¡P¡P¡P¡P ', '*¡P¡P¡P¡P ', '**¡P¡P¡P ', '***¡P¡P ', '****¡P ', '¡P*¡P*¡P* ', '**¡P¡P** ', '¡P¡P**¡P¡P ', '¡P****¡P ',
            '*¡P*¡P** ', '*¡P¡P*¡P ', '*¡P**¡P ', '*¡P**¡P* ', '¡P*¡P¡P¡P* ', '***¡P¡P¡P ', '*¡P*¡P*¡P ', '*¡P¡P¡P* ', '*¡P¡P¡P¡P* ', '¡P¡P** ¡P* ', '¡P*¡P¡P*¡P ', '¡P¡P¡P*¡P¡P* ', '¡P**¡P*¡P '
            );

    $string = str_replace($search, $replace, $string);
    $string = str_replace('*', '-', $string);
    $string = str_replace('¡P', '.', $string);

    return $string;
}

function morse_decode($string)
{
    $string .= ' ';
    $array['0'] = '----- ';
    $array['1'] = '.---- ';
    $array['2'] = '..--- ';
    $array['3'] = '...-- ';
    $array['-'] = '-....- ';
    $array['4'] = '....- ';
    $array['5'] = '..... ';
    $array['6'] = '-.... ';
    $array['7'] = '--... ';
    $array['8'] = '---.. ';
    $array['\''] = '.----. ';
    $array['9'] = '----. ';
    $array['B'] = '-... ';
    $array[';'] = '-.-.-. ';
    $array['@'] = '.--.-. ';
    $array['C'] = '-.-. ';
    $array['"'] = '.-..-. ';
    $array['/'] = '-..-. ';
    $array['F'] = '..-. ';
    $array['('] = '-.--. ';
    $array['P'] = '.--. ';
    $array['G'] = '--. ';
    $array['H'] = '.... ';
    $array['J'] = '.--- ';
    $array[')'] = '-.--.- ';
    $array['Q'] = '--.- ';
    $array['.'] = '.-.-.- ';
    $array['K'] = '-.- ';
    $array['L'] = '.-.. ';
    $array['?'] = '..--.. ';
    $array['Z'] = '--.. ';
    $array['D'] = '-.. ';
    $array[':'] = '---... ';
    $array['S'] = '... ';
    $array['I'] = '.. ';
    $array['O'] = '--- ';
    $array['!'] = '-.-.-- ';
    $array['Y'] = '-.-- ';
    $array[','] = '--..-- ';
    $array['&'] = '. ... ';
    $array['_'] = '..-- .- ';
    $array['M'] = '-- ';
    $array['&'] = '.-...- ';
    $array['R'] = '.-. ';
    $array['N'] = '-. ';
    $array['='] = '-...- ';
    $array['V'] = '...- ';
    $array['$'] = '...-..- ';
    $array['X'] = '-..- ';
    $array['U'] = '..- ';
    $array['A'] = '.- ';
    $array['T'] = '- ';
    $array['W'] = '.-- ';
    $array[')'] = '-.--.- ';
    $array['E'] = '. ';
    $array['    '] = ' ';

    foreach ($array as $key => $var) {
        $string = str_replace($var, $key, $string);
    }

    return $string;
}

 // Test
 echo morse_encode('this is a book'); // - .... .. ...    .. ...  .-  -... --- --- -.-
 echo "\n";
 echo morse_decode(morse_encode('this is a book')); // THIS   IS  A   BOOK
?>
