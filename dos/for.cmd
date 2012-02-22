@echo off
: FOR /F "tokens=*" %%a in (input.txt) do @echo %%a

rem 對一組檔案中的每個檔案執行指定的命令。
rem
rem FOR %variable IN (set) DO 命令 [command-parameters]
rem
rem   %variable 指定一個可以取代的參數。
rem   (set)      指定由一或多個檔案組成的檔案組。您可使用通配字元。
rem   command    指定命令來執行每一個檔案。
rem  command-parameters
rem              為所指定的命令指定變數或參數。
rem
rem 如果要在批次程式中使用 FOR 命令，請指定 %%variable，而不要指定
rem %variable。  變數名稱有大小寫的區分，所以 %i 不同於 %I。
rem
rem 如果您啟用擴充命令，則額外支援下列的 FOR 命令
rem 格式:
rem
rem FOR /D %variable IN (set) DO command  [command-parameters]
rem
rem     如果 set 中包含萬用字元，則指定與目錄
rem     名稱相符，而不是與檔案名稱相符。
rem
rem FOR /R [[drive:]path] %variable IN (set) DO command  [command-parameters]
rem
rem     在樹狀目錄中切換 [drive:]路徑，並於樹狀目錄的每一個目錄下執行
rem     FOR 陳述式。如果未在 /R 之後指定目錄規格，則採用目前的目錄。
rem     如果 set 只是單一句點 (.) 字元，則它只會列舉樹狀目錄結構。
rem

for /l %%a in (1,3,99) do @echo %%a

rem FOR /L %variable IN (start,step,end) DO command [command-parameters]
rem
rem     set 是從開頭到結尾一次跳一步的連續數字。所以 (1,1,5) 會產生
rem     連續值 (1 2 3 4 5) 而 (5,-1,1) 會產生連續值 (5 4 3 2 1)
rem
rem FOR /F ["options"] %variable IN (file-set) DO command [command-parameters]
rem FOR /F ["options"] %variable IN ("string") DO command [command-parameters]
rem FOR /F ["options"] %variable IN ('command') DO command [command-parameters]
rem
rem     或，如果使用 usebackq 選項:
rem
rem FOR /F ["options"] %variable IN (file-set) DO command [command-parameters]
rem FOR /F ["options"] %variable IN ('string') DO command [command-parameters]
rem FOR /F ["options"] %variable IN (`command`) DO command [command-parameters]
rem
rem     filenameset 可以是一個以上的檔案名稱。每個檔案都已開啟，
rem     讀取及處理過，才繼續進行下個檔案名稱組。處理檔案讀取的一致
rem     性，將它分成獨立的文字行，然後將每一行分析成零或更多的字串。
rem     用已找到的字串值為變數值，來呼叫 For 迴圈的內容。預設狀態，
rem     /F 傳出每個檔案的每一行中，以空格分隔的第一個字串。空白行
rem     會被略過。您可以指定 "options" 參數來覆寫預設的分析行為。
rem     這是有引號的字串，包含一個以上的關鍵字，來指定不同的分析
rem     選項。關鍵字是:
rem
rem         eol=c           - 指定一個行尾註解字元
rem                           (只有一個)
rem         skip=n          - 指定在檔案開頭要掠過的
rem                           行數。
rem         delims=xxx      - 指定分隔符號的集合。  這會取代
rem                           預設的空白與定位字元的分隔符號集合。
rem         tokens=x,y,m-n  - 指定每一行的哪些文字串應該被
rem                           傳到 for 的內部以用來進行每一個重複操作。
rem                           這會導致額外的變數名稱被配置。
rem                           m-n 格式代表一個範圍，
rem                           指定了第 m 個到第 n 個字串項。
rem                           如果在 tokens= 字串的最後一個字元是
rem                           星號，則會配置一個額外的變數
rem                           來接收最後一個字串項被分析後
rem                           的其他文字。
rem         usebackq        - 指定新語義開始作用。
rem                           其中反括號的字串會被當作命令來執行，
rem                           而單引號字串是純文字字串。
rem                           此外還允許使用雙引號來
rem                           引用在 filenameset 內
rem                           的檔名。
rem
rem     以下是一個範例:
rem
rem FOR /F "eol=; tokens=2,3* delims=, " %i in (myfile.txt) do @echo %i %j %k
rem
rem     這會分析 myfile.txt 檔案中的每一行，它不會去管以分號開頭的行數
rem     ，直接將第 2 個及第 3 個語法從每一行傳到 for 主體，而其語法是
rem     用逗號和/或空格分開的。請注意，for 主體陳述式參照 %i 以取得第
rem     二個語法，參照 %j 以取得第三個語法，使用 %k 取得第三個語法之
rem     後的剩餘字串。因為檔案名稱含有空格，您必須用雙引號來括住檔案名
rem     稱。要這樣使用雙引號，您必須使用 usebackq 參數。否則雙引號會被
rem     解譯成用來定義一般文字。
rem
rem     使用 %i 明白地在 for 陳述式中宣告，並透過 tokens= option 使用
rem     %j 作暗式性的宣告。您可以藉由 tokens= line 來指定最多 26 個語
rem     法，前提是它宣告的變數不能高於字母 'z' 或 'Z'。請記住，FOR 變
rem     數是單一字元的，同時在任一時間內，您不能同時使用超過 52 個 FOR
rem     變數。
rem
rem     您也可以使用 FOR /F 命令在立即字串中分析邏輯，方法是將括弧之間的
rem     filenameset 變成一個引號字串。它會被視為從檔案輸入的單行，並加
rem     以分析。
rem
rem     最後，您可以使用 FOR /F 命令來分析一個命令的輸出。方法是將括弧
rem     內的 filenameset 變成單引號字串。它將被視為一個命令列，這個命令
rem     行將會傳到子 CMD.EXE，而輸出將會被擷取到記憶體中，當成檔案來分
rem     析。所以下列的範例:
rem
rem         FOR /F "delims==" %i IN ('set') DO @echo %i
rem
rem     將列舉目前環境中的環境變數名稱。
rem
rem 此外，已經加強了 FOR 變數參考的取代功能。
rem 您現在可以選用下列的語法:
rem
rem     %~I         - 展開 %I 且移除包圍的引號 (")
rem     %~fI        - 展開 %I 為一個完全符合的路徑名稱
rem     %~dI        - 只展開 %I 為磁碟機代號
rem     %~pI        - 只展開 %I 為路徑
rem     %~nI        - 只展開 %I 為檔名
rem     %~xI        - 只展開 %I 為副檔名
rem     %~sI        - 展開的路徑只包含短檔名
rem     %~aI        - 展開 %I 為檔案的檔案屬性
rem     %~tI        - 展開 %I 為檔案的日期/時間
rem     %~zI        - 展開 %I 檔案的長度
rem     %~$PATH:I   - 搜尋所有列在 PATH 環境變數內的目錄
rem                    且展開 %I 為
rem                    第一個找到的完全符合檔名。
rem                    如果沒有定義環境變數名稱
rem                    或是搜尋找不到檔案，
rem                    則這個修飾元會展開為
rem                    空字串。
rem
rem 修飾元可以合併使用以獲得綜合的結果:
rem
rem     %~dpI       - 只展開 %I 為磁碟機代號與路徑
rem     %~nxI       - 只展開 %I 為檔名與副檔名
rem     %~fsI       - 只展開 %I 為含短檔名的完全路徑
rem     %~dp$PATH:i - 為 %I 搜尋所有列在 PATH 環境變數內的目錄
rem                    且展開第一個找到的項目為磁碟機代號及
rem                    路徑。
rem     %~ftzaI     - 展開 %I 為像 DIR 一樣的輸出行
rem
rem 在上面的範例中 %I 和 PATH 能用其他的合法值取代。%~ 語法是由合法的
rem FOR 變數名稱來終止。如果選用像 %I 的大寫名稱可以增加可讀性而且避免
rem 和修飾元的混淆，因為這些並不區分大小寫。
