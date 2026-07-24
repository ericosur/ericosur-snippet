# Ruff Linting Report

This file lists all the linting issues found by `ruff check` in this workspace.

## Summary Statistics

```text
361	EXE001 	[ ] shebang-not-executable
218	I001   	[*] unsorted-imports
155	UP039  	[*] unnecessary-class-parentheses
 40	UP010  	[-] unnecessary-future-import
 19	RUF012 	[ ] mutable-class-default
 18	FURB129	[*] readlines-in-for
 18	UP007  	[*] non-pep604-annotation-union
 16	RET501 	[*] unnecessary-return-none
 16	RUF100 	[*] unused-noqa
 16	SIM103 	[ ] needless-bool
 15	DTZ011 	[ ] call-date-today
 13	DTZ005 	[ ] call-datetime-now-without-tzinfo
 13	UP035  	[-] deprecated-import
 12	UP006  	[*] non-pep585-annotation
 11	SIM102 	[ ] collapsible-if
  8	DTZ001 	[ ] call-datetime-without-tzinfo
  8	SIM113 	[ ] enumerate-for-loop
  8	UP045  	[*] non-pep604-annotation-optional
  7	DTZ002 	[ ] call-datetime-today
  7	TRY004 	[ ] type-check-without-type-error
  6	UP024  	[*] os-error-alias
  5	PERF402	[ ] manual-list-copy
  4	DTZ006 	[ ] call-datetime-fromtimestamp
  3	RUF013 	[ ] implicit-optional
  3	RUF059 	[ ] unused-unpacked-variable
  2	BLE001 	[ ] blind-except
  2	FURB122	[*] for-loop-writes
  2	PERF102	[ ] incorrect-dict-iterator
  2	PIE808 	[*] unnecessary-range-start
  2	SIM115 	[ ] open-file-with-context-handler
  2	SIM118 	[ ] in-dict-keys
  2	UP018  	[*] native-literals
  2	UP025  	[*] unicode-kind-prefix
  1	C408   	[ ] unnecessary-collection-call
  1	C414   	[ ] unnecessary-double-cast-or-process
  1	DTZ007 	[ ] call-datetime-strptime-without-zone
  1	FURB157	[*] verbose-decimal-constructor
  1	FURB167	[*] regex-flag-alias
  1	PLR1711	[*] useless-return
  1	PLR2044	[*] empty-comment
  1	RUF022 	[*] unsorted-dunder-all
  1	RUF046 	[ ] unnecessary-cast-to-int
  1	SIM117 	[ ] multiple-with-statements
  1	UP012  	[*] unnecessary-encode-utf8
  1	YTT201 	[ ] sys-version-info0-eq3
  1	YTT203 	[ ] sys-version-info1-cmp-int
  1	YTT204 	[ ] sys-version-info-minor-cmp-int
Found 1030 errors.
[*] 524 fixable with the `--fix` option (37 hidden fixes can be enabled with the `--unsafe-fixes` option).
```

## Detailed Issues

```text
aaa.py:
  1:1 EXE001 Shebang is present but file is not executable

abc101.py:
   1:1 EXE001 Shebang is present but file is not executable
  16:1 I001 [*] Import block is un-sorted or un-formatted

access_file.py:
   1:1  EXE001 Shebang is present but file is not executable
  21:14 SIM115 Use a context manager for opening files
  22:12 UP024 [*] Replace aliased errors with `OSError`

alpha/alphabravo.py:
   1:1  EXE001 Shebang is present but file is not executable
  15:1  I001 [*] Import block is un-sorted or un-formatted
  17:24 UP039 [*] Unnecessary parentheses after class definition

alpha/the_typer.py:
   1:1 EXE001 Shebang is present but file is not executable
   9:1 I001 [*] Import block is un-sorted or un-formatted
  16:1 I001 [*] Import block is un-sorted or un-formatted

args.py:
  1:1 EXE001 Shebang is present but file is not executable

argv_env.py:
  1:1 EXE001 Shebang is present but file is not executable

arrow-to-right.py:
  1:1 EXE001 Shebang is present but file is not executable

b2a.py:
  1:1 EXE001 Shebang is present but file is not executable

b64/ai64.py:
   1:1 EXE001 Shebang is present but file is not executable
  22:1 I001 [*] Import block is un-sorted or un-formatted
  40:5 SIM103 Return the condition directly

b64/b6485.py:
   1:1  EXE001 Shebang is present but file is not executable
  14:1  I001 [*] Import block is un-sorted or un-formatted
  31:1  I001 [*] Import block is un-sorted or un-formatted
  35:12 YTT201 `sys.version_info[0] == 3` referenced (python4), use `>=`
  35:39 YTT203 `sys.version_info[1]` compared to integer (python4), compare `sys.version_info` to tuple

b64/butil.py:
  1:1 EXE001 Shebang is present but file is not executable
  8:1 I001 [*] Import block is un-sorted or un-formatted

b64/demo_baseconv.py:
   1:1 EXE001 Shebang is present but file is not executable
  16:1 I001 [*] Import block is un-sorted or un-formatted

b64/do_digest.py:
   1:1 EXE001 Shebang is present but file is not executable
  10:1 I001 [*] Import block is un-sorted or un-formatted
  25:1 RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  32:1 I001 [*] Import block is un-sorted or un-formatted

b64/mknn64.py:
   7:1  I001 [*] Import block is un-sorted or un-formatted
  23:5  RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  35:18 UP039 [*] Unnecessary parentheses after class definition
  73:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly
  75:17 SIM113 Use `enumerate()` for index variable `cnt` in `for` loop

b64/topt.py:
  1:1 EXE001 Shebang is present but file is not executable
  7:1 I001 [*] Import block is un-sorted or un-formatted

basic/aio.py:
   1:1 EXE001 Shebang is present but file is not executable
   7:1 I001 [*] Import block is un-sorted or un-formatted
  89:5 RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  89:5 PLR1711 [*] Useless `return` statement at end of function

basic/base58_demo.py:
  1:1 EXE001 Shebang is present but file is not executable

basic/bsc.py:
   1:1 EXE001 Shebang is present but file is not executable
  13:1 I001 [*] Import block is un-sorted or un-formatted

basic/byte_to_str.py:
   1:1 EXE001 Shebang is present but file is not executable
  31:5 RET501 [*] Do not explicitly `return None` in function if it is the only possible return value

basic/check_path_with_space.py:
  1:1 EXE001 Shebang is present but file is not executable
  7:1 I001 [*] Import block is un-sorted or un-formatted

basic/clsmethod.py:
  1:1  EXE001 Shebang is present but file is not executable
  8:13 UP039 [*] Unnecessary parentheses after class definition

basic/const.py:
   1:1  EXE001 Shebang is present but file is not executable
  13:1  I001 [*] Import block is un-sorted or un-formatted
  20:13 UP039 [*] Unnecessary parentheses after class definition

basic/count-by-letter.py:
  1:1 EXE001 Shebang is present but file is not executable

basic/dataclass.py:
  6:1 I001 [*] Import block is un-sorted or un-formatted

basic/date_toml.py:
  1:1 EXE001 Shebang is present but file is not executable

basic/dict_keys.py:
  1:1 EXE001 Shebang is present but file is not executable

basic/dict_test.py:
   1:1 EXE001 Shebang is present but file is not executable
  11:5 I001 [*] Import block is un-sorted or un-formatted

basic/getmac.py:
   1:1 EXE001 Shebang is present but file is not executable
   7:1 I001 [*] Import block is un-sorted or un-formatted
  12:5 I001 [*] Import block is un-sorted or un-formatted
  30:5 I001 [*] Import block is un-sorted or un-formatted

basic/ifc.py:
   1:1 EXE001 Shebang is present but file is not executable
   7:1 I001 [*] Import block is un-sorted or un-formatted
  12:5 I001 [*] Import block is un-sorted or un-formatted
  32:5 I001 [*] Import block is un-sorted or un-formatted

basic/ipaddr.py:
  1:1 EXE001 Shebang is present but file is not executable
  7:1 I001 [*] Import block is un-sorted or un-formatted

basic/list2bytes.py:
  1:1 EXE001 Shebang is present but file is not executable
  9:1 I001 [*] Import block is un-sorted or un-formatted

basic/load_toml.py:
   1:1  EXE001 Shebang is present but file is not executable
  11:1  I001 [*] Import block is un-sorted or un-formatted
  27:15 UP039 [*] Unnecessary parentheses after class definition

basic/lvwords.py:
  1:1 EXE001 Shebang is present but file is not executable
  6:1 I001 [*] Import block is un-sorted or un-formatted

basic/match.py:
  1:1 EXE001 Shebang is present but file is not executable
  8:1 I001 [*] Import block is un-sorted or un-formatted

basic/match_case.py:
  1:1 EXE001 Shebang is present but file is not executable

basic/mcsample.py:
  1:1 EXE001 Shebang is present but file is not executable
  9:1 I001 [*] Import block is un-sorted or un-formatted

basic/multiline_string.py:
  1:1 EXE001 Shebang is present but file is not executable

basic/mycls.py:
  1:1 EXE001 Shebang is present but file is not executable

basic/ordereddict.py:
  1:1 EXE001 Shebang is present but file is not executable

basic/os_path_join.py:
  1:1 EXE001 Shebang is present but file is not executable

basic/read_os_release.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  I001 [*] Import block is un-sorted or un-formatted
  10:1  UP035 `typing.Dict` is deprecated, use `dict` instead
  18:16 UP039 [*] Unnecessary parentheses after class definition
  24:34 UP007 [*] Use `X | Y` for type annotations
  24:40 UP006 [*] Use `dict` instead of `Dict` for type annotation
  32:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly
  42:28 UP007 [*] Use `X | Y` for type annotations
  46:49 UP007 [*] Use `X | Y` for type annotations
  50:33 UP007 [*] Use `X | Y` for type annotations
  54:33 UP007 [*] Use `X | Y` for type annotations
  58:43 UP007 [*] Use `X | Y` for type annotations
  69:36 UP007 [*] Use `X | Y` for type annotations
  79:24 UP007 [*] Use `X | Y` for type annotations

basic/readtoml.py:
  8:1 I001 [*] Import block is un-sorted or un-formatted

basic/sort_dict_by_value.py:
  1:1 EXE001 Shebang is present but file is not executable
  8:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

basic/sorted_try.py:
  1:1 EXE001 Shebang is present but file is not executable

basic/static_var.py:
   1:1  EXE001 Shebang is present but file is not executable
   8:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  11:14 UP039 [*] Unnecessary parentheses after class definition

basic/static_var2.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:10 UP039 [*] Unnecessary parentheses after class definition

basic/strjoin.py:
  1:1 EXE001 Shebang is present but file is not executable

basic/sum.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:1  I001 [*] Import block is un-sorted or un-formatted
  15:15 UP039 [*] Unnecessary parentheses after class definition
  34:33 UP007 [*] Use `X | Y` for type annotations

basic/the9801.py:
   1:1  EXE001 Shebang is present but file is not executable
   6:1  I001 [*] Import block is un-sorted or un-formatted
  18:5  RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  22:15 UP039 [*] Unnecessary parentheses after class definition
  68:13 SIM118 Use `key in dict` instead of `key in dict.keys()`

basic/trytoml.py:
   1:1  EXE001 Shebang is present but file is not executable
  30:15 UP039 [*] Unnecessary parentheses after class definition

basic/wmic.py:
   1:1 EXE001 Shebang is present but file is not executable
  16:1 I001 [*] Import block is un-sorted or un-formatted
  27:5 I001 [*] Import block is un-sorted or un-formatted

basic/xxhash_example.py:
  1:1 EXE001 Shebang is present but file is not executable

bisect_demo.py:
  1:1 EXE001 Shebang is present but file is not executable

bpmf/bp.py:
   1:1  EXE001 Shebang is present but file is not executable
  13:15 UP039 [*] Unnecessary parentheses after class definition
  29:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly

bpmf/the_opencc_demo.py:
   1:1  EXE001 Shebang is present but file is not executable
  16:11 UP039 [*] Unnecessary parentheses after class definition

brent_factor.py:
  1:1 EXE001 Shebang is present but file is not executable

calcpi.py:
   1:1  EXE001 Shebang is present but file is not executable
  22:13 UP039 [*] Unnecessary parentheses after class definition

celsius.py:
  1:1 EXE001 Shebang is present but file is not executable
  7:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

change_subject.py:
   1:1  EXE001 Shebang is present but file is not executable
  14:1  I001 [*] Import block is un-sorted or un-formatted
  25:17 UP039 [*] Unnecessary parentheses after class definition

cntchr.py:
   1:1  EXE001 Shebang is present but file is not executable
   5:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  13:10 C414 Unnecessary `list()` call within `sorted()`

collatz_conj.py:
   1:1  EXE001 Shebang is present but file is not executable
  16:14 UP039 [*] Unnecessary parentheses after class definition

crypto/aes-siv.py:
   1:1  EXE001 Shebang is present but file is not executable
  34:1  I001 [*] Import block is un-sorted or un-formatted
  38:5  RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  42:11 UP039 [*] Unnecessary parentheses after class definition

crypto/chataes.py:
   1:1  EXE001 Shebang is present but file is not executable
  12:1  I001 [*] Import block is un-sorted or un-formatted
  35:5  RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  39:11 UP039 [*] Unnecessary parentheses after class definition

crypto/cryptohash.py:
  1:1 EXE001 Shebang is present but file is not executable

crypto/decpu.py:
   1:1  EXE001 Shebang is present but file is not executable
  11:1  I001 [*] Import block is un-sorted or un-formatted
  17:11 UP039 [*] Unnecessary parentheses after class definition

crypto/exchange/keyiv.py:
   1:1 EXE001 Shebang is present but file is not executable
   7:1 I001 [*] Import block is un-sorted or un-formatted
  26:5 RET501 [*] Do not explicitly `return None` in function if it is the only possible return value

crypto/exchange/t0.py:
    1:1  EXE001 Shebang is present but file is not executable
    7:1  I001 [*] Import block is un-sorted or un-formatted
   25:1  I001 [*] Import block is un-sorted or un-formatted
   97:15 UP039 [*] Unnecessary parentheses after class definition
  147:13 FURB122 [*] Use of `f.write` in a for loop
  176:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly

crypto/fernet.py:
  1:1 EXE001 Shebang is present but file is not executable

crypto/kid_rsa/decrypt_sta.py:
  8:1 I001 [*] Import block is un-sorted or un-formatted

crypto/kid_rsa/encrypt_sta.py:
  8:1 I001 [*] Import block is un-sorted or un-formatted

crypto/kid_rsa/fulltest.py:
  8:1 I001 [*] Import block is un-sorted or un-formatted

crypto/kid_rsa/genkey_sta.py:
  8:1 I001 [*] Import block is un-sorted or un-formatted

crypto/kid_rsa/sta_prompt.py:
  1:1 EXE001 Shebang is present but file is not executable

crypto/passutil.py:
    1:1  EXE001 Shebang is present but file is not executable
   12:1  I001 [*] Import block is un-sorted or un-formatted
   17:1  UP035 `typing.Dict` is deprecated, use `dict` instead
   17:1  UP035 `typing.Tuple` is deprecated, use `tuple` instead
   30:5  RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
   32:15 UP039 [*] Unnecessary parentheses after class definition
   79:23 UP006 [*] Use `dict` instead of `Dict` for type annotation
  109:32 UP006 [*] Use `tuple` instead of `Tuple` for type annotation
  131:11 UP039 [*] Unnecessary parentheses after class definition

crypto/run_vector.py:
  30:1 I001 [*] Import block is un-sorted or un-formatted

crypto/scrypt_demo.py:
   1:1  EXE001 Shebang is present but file is not executable
  14:1  I001 [*] Import block is un-sorted or un-formatted
  36:5  RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  40:5  I001 [*] Import block is un-sorted or un-formatted
  45:17 UP039 [*] Unnecessary parentheses after class definition

cython/t/setup.py:
  1:1 I001 [*] Import block is un-sorted or un-formatted

datetime/TianGanDiZhi/cli_tester.py:
   1:1 EXE001 Shebang is present but file is not executable
  10:1 I001 [*] Import block is un-sorted or un-formatted
  27:1 RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  32:1 I001 [*] Import block is un-sorted or un-formatted

datetime/TianGanDiZhi/ganzhi.py:
   1:1 EXE001 Shebang is present but file is not executable
  15:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

datetime/TianGanDiZhi/gngan_yaljux.py:
   1:1  EXE001 Shebang is present but file is not executable
  18:1  I001 [*] Import block is un-sorted or un-formatted
  19:1  UP035 [*] Import from `collections.abc` instead: `Callable`
  25:1  I001 [*] Import block is un-sorted or un-formatted
  28:5  I001 [*] Import block is un-sorted or un-formatted
  41:12 DTZ002 `datetime.datetime.today()` used
  43:13 UP039 [*] Unnecessary parentheses after class definition
  50:15 RUF012 Mutable default value for class attribute

datetime/TianGanDiZhi/typer_gng.py:
   1:1  EXE001 Shebang is present but file is not executable
  12:1  I001 [*] Import block is un-sorted or un-formatted
  14:1  UP035 [*] Import from `typing` instead: `Annotated`
  21:1  I001 [*] Import block is un-sorted or un-formatted
  24:1  I001 [*] Import block is un-sorted or un-formatted
  25:1  RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  30:1  I001 [*] Import block is un-sorted or un-formatted
  33:11 UP039 [*] Unnecessary parentheses after class definition
  38:38 UP007 [*] Use `X | Y` for type annotations

datetime/be_prepared.py:
   9:1  I001 [*] Import block is un-sorted or un-formatted
  13:12 DTZ011 `datetime.date.today()` used
  47:9  PERF402 Use `list` or `list.copy` to create a copy of a list

datetime/between.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  17:17 DTZ005 `datetime.datetime.now()` called without a `tz` argument
  21:16 DTZ005 `datetime.datetime.now()` called without a `tz` argument
  24:23 DTZ005 `datetime.datetime.now()` called without a `tz` argument

datetime/black_friday.py:
    1:1  EXE001 Shebang is present but file is not executable
    9:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
    9:1  I001 [*] Import block is un-sorted or un-formatted
   12:1  UP035 [*] Import from `collections.abc` instead: `Callable`
   20:5  I001 [*] Import block is un-sorted or un-formatted
   30:5  I001 [*] Import block is un-sorted or un-formatted
   65:15 UP039 [*] Unnecessary parentheses after class definition
  155:27 UP045 [*] Use `X | None` for type annotations

datetime/calc-workdays.py:
   1:1 EXE001 Shebang is present but file is not executable
  13:5 I001 [*] Import block is un-sorted or un-formatted
  23:5 I001 [*] Import block is un-sorted or un-formatted

datetime/calendar_demo.py:
   1:1  EXE001 Shebang is present but file is not executable
  13:10 DTZ011 `datetime.date.today()` used

datetime/clockemoji.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  I001 [*] Import block is un-sorted or un-formatted
  12:1  I001 [*] Import block is un-sorted or un-formatted
  14:16 UP039 [*] Unnecessary parentheses after class definition
  16:14 RUF012 Mutable default value for class attribute
  74:15 DTZ005 `datetime.datetime.now()` called without a `tz` argument

datetime/count_month.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  26:13 DTZ001 `datetime.datetime()` called without a `tzinfo` argument

datetime/date_palidrome.py:
   1:1 EXE001 Shebang is present but file is not executable
   7:1 I001 [*] Import block is un-sorted or un-formatted
  17:9 TRY004 Prefer `TypeError` exception for invalid type

datetime/date_typer.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:1  I001 [*] Import block is un-sorted or un-formatted
  22:1  RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  27:1  I001 [*] Import block is un-sorted or un-formatted
  55:9  UP007 [*] Use `X | Y` for type annotations
  59:23 UP007 [*] Use `X | Y` for type annotations

datetime/datedelta.py:
   1:1  EXE001 Shebang is present but file is not executable
  14:13 DTZ001 `datetime.datetime()` called without a `tzinfo` argument
  16:13 DTZ002 `datetime.datetime.today()` used

datetime/dbetw.py:
   1:1  EXE001 Shebang is present but file is not executable
   5:1  I001 [*] Import block is un-sorted or un-formatted
   9:1  I001 [*] Import block is un-sorted or un-formatted
  11:15 UP039 [*] Unnecessary parentheses after class definition
  47:34 DTZ011 `datetime.date.today()` used
  54:13 DTZ011 `datetime.date.today()` used
  63:13 DTZ011 `datetime.date.today()` used

datetime/delta_seconds.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
   7:1  I001 [*] Import block is un-sorted or un-formatted
  17:15 UP039 [*] Unnecessary parentheses after class definition
  20:16 DTZ001 `datetime.datetime()` called without a `tzinfo` argument
  42:40 DTZ005 `datetime.datetime.now()` called without a `tz` argument
  52:36 DTZ005 `datetime.datetime.now()` called without a `tz` argument

datetime/dooms/dooms_day.py:
   1:1  EXE001 Shebang is present but file is not executable
  25:15 UP039 [*] Unnecessary parentheses after class definition

datetime/dooms/dooms_day_test.py:
   1:1  EXE001 Shebang is present but file is not executable
  20:19 UP039 [*] Unnecessary parentheses after class definition

datetime/dooms/doomsday.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  I001 [*] Import block is un-sorted or un-formatted
  15:5  I001 [*] Import block is un-sorted or un-formatted
  43:14 DTZ011 `datetime.date.today()` used
  72:18 DTZ011 `datetime.date.today()` used

datetime/dooms/dow_caller.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:1  I001 [*] Import block is un-sorted or un-formatted
  33:10 DTZ011 `datetime.date.today()` used

datetime/dooms/easydoom.py:
   1:1  EXE001 Shebang is present but file is not executable
  43:1  I001 [*] Import block is un-sorted or un-formatted
  46:5  I001 [*] Import block is un-sorted or un-formatted
  62:19 UP039 [*] Unnecessary parentheses after class definition
  64:14 RUF012 Mutable default value for class attribute
  69:22 DTZ011 `datetime.date.today()` used

datetime/easter_date.py:
    1:1  EXE001 Shebang is present but file is not executable
   11:1  I001 [*] Import block is un-sorted or un-formatted
   21:5  I001 [*] Import block is un-sorted or un-formatted
   31:5  I001 [*] Import block is un-sorted or un-formatted
   37:1  RUF100 [*] Unused `noqa` directive (non-enabled: `E741`)
   58:15 UP039 [*] Unnecessary parentheses after class definition
  123:32 UP045 [*] Use `X | None` for type annotations

datetime/ep.py:
   1:1  EXE001 Shebang is present but file is not executable
  44:1  UP035 `typing.Tuple` is deprecated, use `tuple` instead
  48:1  I001 [*] Import block is un-sorted or un-formatted
  56:53 UP006 [*] Use `tuple` instead of `Tuple` for type annotation

datetime/july1st.py:
  1:1 EXE001 Shebang is present but file is not executable

datetime/list_old_folder.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
   7:1  I001 [*] Import block is un-sorted or un-formatted
  16:1  I001 [*] Import block is un-sorted or un-formatted
  18:18 UP039 [*] Unnecessary parentheses after class definition
  65:62 DTZ006 `datetime.datetime.fromtimestamp()` called without a `tz` argument
  76:61 DTZ006 `datetime.datetime.fromtimestamp()` called without a `tz` argument

datetime/list_possible_workday.py:
    1:1  EXE001 Shebang is present but file is not executable
   29:1  I001 [*] Import block is un-sorted or un-formatted
   33:1  UP035 [*] Import from `collections.abc` instead: `Callable`
   65:12 DTZ005 `datetime.datetime.now()` called without a `tz` argument
   71:21 UP039 [*] Unnecessary parentheses after class definition
  125:25 DTZ007 Naive datetime constructed using `datetime.datetime.strptime()` without %z
  155:15 DTZ005 `datetime.datetime.now()` called without a `tz` argument
  197:14 DTZ002 `datetime.datetime.today()` used
  209:31 UP045 [*] Use `X | None` for type annotations
  217:29 UP007 [*] Use `X | Y` for type annotations
  221:38 UP045 [*] Use `X | None` for type annotations
  255:25 DTZ011 `datetime.date.today()` used
  257:35 DTZ001 `datetime.datetime()` called without a `tzinfo` argument
  261:35 DTZ001 `datetime.datetime()` called without a `tzinfo` argument

datetime/lunar_date.py:
   1:1 EXE001 Shebang is present but file is not executable
  15:1 I001 [*] Import block is un-sorted or un-formatted
  29:5 I001 [*] Import block is un-sorted or un-formatted

datetime/new_date.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  I001 [*] Import block is un-sorted or un-formatted
  37:13 DTZ002 `datetime.datetime.today()` used
  55:13 UP007 [*] Use `X | Y` for type annotations

datetime/ngorgo.py:
    1:1  EXE001 Shebang is present but file is not executable
   14:1  I001 [*] Import block is un-sorted or un-formatted
   25:15 UP039 [*] Unnecessary parentheses after class definition
   29:14 RUF012 Mutable default value for class attribute
   31:16 RUF012 Mutable default value for class attribute
   63:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly
  138:33 DTZ011 `datetime.date.today()` used

datetime/nothing.py:
  1:1 EXE001 Shebang is present but file is not executable
  9:5 RET501 [*] Do not explicitly `return None` in function if it is the only possible return value

datetime/perfect_square_date.py:
   1:1  EXE001 Shebang is present but file is not executable
  12:1  I001 [*] Import block is un-sorted or un-formatted
  15:1  I001 [*] Import block is un-sorted or un-formatted
  21:15 UP039 [*] Unnecessary parentheses after class definition

datetime/ratio_month.py:
   1:1  EXE001 Shebang is present but file is not executable
  49:16 UP039 [*] Unnecessary parentheses after class definition
  55:26 DTZ011 `datetime.date.today()` used

datetime/sickutil.py:
   1:1  EXE001 Shebang is present but file is not executable
  11:1  I001 [*] Import block is un-sorted or un-formatted
  45:9  TRY004 Prefer `TypeError` exception for invalid type
  74:9  TRY004 Prefer `TypeError` exception for invalid type
  99:10 DTZ006 `datetime.datetime.fromtimestamp()` called without a `tz` argument

datetime/test_translate_weekday.py:
  1:1 EXE001 Shebang is present but file is not executable

datetime/wtfstamp.py:
    1:1  EXE001 Shebang is present but file is not executable
   21:1  I001 [*] Import block is un-sorted or un-formatted
   25:5  I001 [*] Import block is un-sorted or un-formatted
   30:1  I001 [*] Import block is un-sorted or un-formatted
   37:15 UP039 [*] Unnecessary parentheses after class definition
   45:15 DTZ001 `datetime.datetime()` called without a `tzinfo` argument
   47:15 DTZ001 `datetime.datetime()` called without a `tzinfo` argument
  142:27 DTZ001 `datetime.datetime()` called without a `tzinfo` argument

datetime/yesterday.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  10:1  I001 [*] Import block is un-sorted or un-formatted
  23:13 DTZ006 `datetime.datetime.fromtimestamp()` called without a `tz` argument

demo_pushover/base_pushover.py:
   1:1  EXE001 Shebang is present but file is not executable
  17:1  I001 [*] Import block is un-sorted or un-formatted
  34:37 DTZ005 `datetime.datetime.now()` called without a `tz` argument

demo_pushover/p2over.py:
  10:1 I001 [*] Import block is un-sorted or un-formatted

demo_pushover/p3over.py:
  10:1  I001 [*] Import block is un-sorted or un-formatted
  60:14 DTZ002 `datetime.datetime.today()` used

demo_pushover/pushover.py:
  22:1  RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  36:13 UP039 [*] Unnecessary parentheses after class definition
  44:50 DTZ005 `datetime.datetime.now()` called without a `tz` argument

demo_pushover/request-soundlist.py:
  12:1 I001 [*] Import block is un-sorted or un-formatted
  18:1 RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  22:1 I001 [*] Import block is un-sorted or un-formatted

demo_pushover/yagmail_send_pushover.py:
   1:1 EXE001 Shebang is present but file is not executable
  13:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  34:1 RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  38:1 I001 [*] Import block is un-sorted or un-formatted

dice.py:
  11:1  I001 [*] Import block is un-sorted or un-formatted
  36:15 UP039 [*] Unnecessary parentheses after class definition

easy_sieve.py:
   1:1  EXE001 Shebang is present but file is not executable
  14:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  27:12 UP039 [*] Unnecessary parentheses after class definition

easydump.py:
   1:1  EXE001 Shebang is present but file is not executable
  11:15 UP039 [*] Unnecessary parentheses after class definition

emoji/food/clean_from.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  I001 [*] Import block is un-sorted or un-formatted
   9:14 UP039 [*] Unnecessary parentheses after class definition
  19:9  SIM117 Use a single `with` statement with multiple contexts instead of nested `with` statements
  21:27 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly

emoji/food/lookup.py:
   1:1  EXE001 Shebang is present but file is not executable
  14:1  I001 [*] Import block is un-sorted or un-formatted
  25:18 UP039 [*] Unnecessary parentheses after class definition
  31:13 RUF012 Mutable default value for class attribute

emoji/logd.py:
  6:1 I001 [*] Import block is un-sorted or un-formatted

emoji/mytofrom.py:
   1:1 EXE001 Shebang is present but file is not executable
   7:1 I001 [*] Import block is un-sorted or un-formatted
  49:9 TRY004 Prefer `TypeError` exception for invalid type

emoji/parse_enxml.py:
    1:1  EXE001 Shebang is present but file is not executable
   10:1  I001 [*] Import block is un-sorted or un-formatted
   24:13 DTZ002 `datetime.datetime.today()` used
   46:15 UP039 [*] Unnecessary parentheses after class definition
   65:9  SIM103 Return the condition `"skin_tone" in k` directly
  119:13 UP018 [*] Unnecessary `str` call (rewrite as a literal)

emoji/pickup.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:1  I001 [*] Import block is un-sorted or un-formatted
  12:1  I001 [*] Import block is un-sorted or un-formatted
  51:18 UP039 [*] Unnecessary parentheses after class definition

emoji/read_enxml.py:
   1:1  EXE001 Shebang is present but file is not executable
  25:15 UP039 [*] Unnecessary parentheses after class definition
  28:13 RUF012 Mutable default value for class attribute
  64:13 UP018 [*] Unnecessary `str` call (rewrite as a literal)
  94:13 DTZ011 `datetime.date.today()` used

emoji/surgg.py:
  1:1 EXE001 Shebang is present but file is not executable

emoji/test_emoji.py:
   1:1  EXE001 Shebang is present but file is not executable
  14:15 UP039 [*] Unnecessary parentheses after class definition

emoji/test_loge.py:
  5:1 I001 [*] Import block is un-sorted or un-formatted

emoji/u8u16.py:
   1:1 EXE001 Shebang is present but file is not executable
  10:1 I001 [*] Import block is un-sorted or un-formatted

euc_dist.py:
  1:1 EXE001 Shebang is present but file is not executable
  5:1 I001 [*] Import block is un-sorted or un-formatted

exiftool/exif.py:
  24:15 UP039 [*] Unnecessary parentheses after class definition
  26:15 RUF012 Mutable default value for class attribute

exiftool/get-date.py:
  16:9 SIM113 Use `enumerate()` for index variable `cnt` in `for` loop

extfactor.py:
   1:1  EXE001 Shebang is present but file is not executable
   8:1  I001 [*] Import block is un-sorted or un-formatted
  41:15 UP039 [*] Unnecessary parentheses after class definition

factorint.py:
  1:1 EXE001 Shebang is present but file is not executable

factorint_sta.py:
  1:1 EXE001 Shebang is present but file is not executable

fastapi/api1st.py:
    1:1  EXE001 Shebang is present but file is not executable
   16:1  I001 [*] Import block is un-sorted or un-formatted
   18:1  UP035 `typing.List` is deprecated, use `list` instead
   25:1  RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
   28:1  I001 [*] Import block is un-sorted or un-formatted
   30:1  I001 [*] Import block is un-sorted or un-formatted
   34:1  I001 [*] Import block is un-sorted or un-formatted
   59:12 UP045 [*] Use `X | None` for type annotations
   60:13 UP045 [*] Use `X | None` for type annotations
   61:14 UP045 [*] Use `X | None` for type annotations
  145:14 UP006 [*] Use `list` instead of `List` for type annotation
  172:33 RUF013 PEP 484 prohibits implicit `Optional`
  172:51 RUF013 PEP 484 prohibits implicit `Optional`
  172:69 RUF013 PEP 484 prohibits implicit `Optional`
  172:82 UP006 [*] Use `list` instead of `List` for type annotation
  185:9  PERF402 Use `list` or `list.copy` to create a copy of a list
  204:34 UP007 [*] Use `X | Y` for type annotations

fastapi/trylog.py:
  1:1 EXE001 Shebang is present but file is not executable
  7:1 I001 [*] Import block is un-sorted or un-formatted

fbkey.py:
  31:50 FURB167 [*] Use of regular expression alias `re.M`

fetch_currency.py:
  7:1 UP010 Unnecessary `__future__` import `print_function` for target Python version
  7:1 I001 [*] Import block is un-sorted or un-formatted

fft/dft1.py:
  41:5 RUF059 Unpacked variable `fig` is never used

fft/dft2.py:
  37:5 RUF059 Unpacked variable `fig` is never used

fft/hann.py:
  7:1 I001 [*] Import block is un-sorted or un-formatted

fft/night.py:
  63:5 RUF059 Unpacked variable `f` is never used

fib/calc_factorial.py:
   7:1  I001 [*] Import block is un-sorted or un-formatted
  13:20 UP039 [*] Unnecessary parentheses after class definition

fib/factorial-redis.py:
   1:1  EXE001 Shebang is present but file is not executable
  23:1  RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  29:21 UP039 [*] Unnecessary parentheses after class definition

fib/fib-redis.py:
   1:1  EXE001 Shebang is present but file is not executable
  24:1  RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  30:15 UP039 [*] Unnecessary parentheses after class definition

fib/fib.py:
   1:1  EXE001 Shebang is present but file is not executable
  14:1  I001 [*] Import block is un-sorted or un-formatted
  33:10 DTZ002 `datetime.datetime.today()` used

fib/fib_store.py:
  30:5  RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  38:14 UP039 [*] Unnecessary parentheses after class definition
  89:16 UP024 [*] Replace aliased errors with `OSError`

fib/listp.py:
   1:1  EXE001 Shebang is present but file is not executable
  37:12 UP024 [*] Replace aliased errors with `OSError`

fib/loadp.py:
   1:1  EXE001 Shebang is present but file is not executable
  22:17 SIM113 Use `enumerate()` for index variable `cnt` in `for` loop
  26:12 UP024 [*] Replace aliased errors with `OSError`

fib/stirling.py:
  1:1 EXE001 Shebang is present but file is not executable

fisher_yates_shuffle.py:
   1:1  EXE001 Shebang is present but file is not executable
  24:23 PIE808 [*] Unnecessary `start` argument in `range`

foobar.py:
   1:1 EXE001 Shebang is present but file is not executable
   7:1 I001 [*] Import block is un-sorted or un-formatted
  13:5 I001 [*] Import block is un-sorted or un-formatted

for_loop_else.py:
  7:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

get_word_freq.py:
  5:1 I001 [*] Import block is un-sorted or un-formatted

guess_filetype.py:
  1:1 EXE001 Shebang is present but file is not executable
  7:1 I001 [*] Import block is un-sorted or un-formatted

hash_factory.py:
   1:1  EXE001 Shebang is present but file is not executable
  35:11 UP012 [*] Unnecessary call to `encode` as UTF-8

hashids/demo_hashid.py:
  1:1 EXE001 Shebang is present but file is not executable

hello_world.py:
  1:1 EXE001 Shebang is present but file is not executable
  7:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  7:1 I001 [*] Import block is un-sorted or un-formatted

image/blobid.py:
   1:1  EXE001 Shebang is present but file is not executable
  11:1  I001 [*] Import block is un-sorted or un-formatted
  34:15 UP039 [*] Unnecessary parentheses after class definition
  36:13 RUF012 Mutable default value for class attribute

image/get_home.py:
  6:1 I001 [*] Import block is un-sorted or un-formatted

image/imamp.py:
   1:1  EXE001 Shebang is present but file is not executable
  20:15 UP039 [*] Unnecessary parentheses after class definition

image/iterfiles.py:
   1:1  EXE001 Shebang is present but file is not executable
   8:1  I001 [*] Import block is un-sorted or un-formatted
  17:1  RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  21:1  I001 [*] Import block is un-sorted or un-formatted
  24:15 UP039 [*] Unnecessary parentheses after class definition
  42:13 SIM102 Use a single `if` statement instead of nested `if` statements

image/rainbow.py:
  1:1 EXE001 Shebang is present but file is not executable

image/readimzip.py:
   1:1  EXE001 Shebang is present but file is not executable
  15:15 UP039 [*] Unnecessary parentheses after class definition

image/readpbf.py:
    1:1  EXE001 Shebang is present but file is not executable
   81:15 UP039 [*] Unnecessary parentheses after class definition
  103:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly

image/side-by-side.py:
   1:1  EXE001 Shebang is present but file is not executable
  20:1  I001 [*] Import block is un-sorted or un-formatted
  27:15 UP039 [*] Unnecessary parentheses after class definition

image/top-down.py:
   1:1  EXE001 Shebang is present but file is not executable
  20:1  I001 [*] Import block is un-sorted or un-formatted
  28:15 UP039 [*] Unnecessary parentheses after class definition

innprod.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:15 UP039 [*] Unnecessary parentheses after class definition
  13:13 RUF012 Mutable default value for class attribute
  19:11 RUF012 Mutable default value for class attribute
  23:11 RUF012 Mutable default value for class attribute
  27:12 RUF012 Mutable default value for class attribute

kana/iroha.py:
  38:1 I001 [*] Import block is un-sorted or un-formatted

kana/kana.py:
   1:1  EXE001 Shebang is present but file is not executable
  29:15 UP039 [*] Unnecessary parentheses after class definition
  33:14 RUF012 Mutable default value for class attribute
  43:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly

kana/kanji/kjutil.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  I001 [*] Import block is un-sorted or un-formatted
  20:5  RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  28:13 DTZ011 `datetime.date.today()` used

kana/kanji/loadyaml.py:
  5:1 I001 [*] Import block is un-sorted or un-formatted

kana/kanji/roast.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:1  I001 [*] Import block is un-sorted or un-formatted
  16:15 UP039 [*] Unnecessary parentheses after class definition
  33:13 PERF402 Use `list` or `list.copy` to create a copy of a list
  42:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly
  63:20 PERF102 When using only the values of a dict use the `values()` method
  66:13 SIM113 Use `enumerate()` for index variable `cnt` in `for` loop

look_factor_1k.py:
  1:1 EXE001 Shebang is present but file is not executable

loop.py:
  1:1 EXE001 Shebang is present but file is not executable

mistune-demo.py:
  1:1 EXE001 Shebang is present but file is not executable

mk-embed-script.py:
  1:1 EXE001 Shebang is present but file is not executable

montyhall.py:
   1:1  EXE001 Shebang is present but file is not executable
  33:1  I001 [*] Import block is un-sorted or un-formatted
  36:5  I001 [*] Import block is un-sorted or un-formatted
  51:16 UP039 [*] Unnecessary parentheses after class definition

myip.py:
   8:1  I001 [*] Import block is un-sorted or un-formatted
  16:5  I001 [*] Import block is un-sorted or un-formatted
  33:11 UP039 [*] Unnecessary parentheses after class definition
  62:33 UP007 [*] Use `X | Y` for type annotations
  77:30 UP007 [*] Use `X | Y` for type annotations

myutil/__head.py:
  1:1 EXE001 Shebang is present but file is not executable

myutil/__init__.py:
  14:1  I001 [*] Import block is un-sorted or un-formatted
  34:5  RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  40:11 RUF022 [*] `__all__` is not sorted

myutil/__myutil.py:
  1:1 EXE001 Shebang is present but file is not executable
  5:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  5:1 I001 [*] Import block is un-sorted or un-formatted

myutil/commonutil.py:
  1:1 EXE001 Shebang is present but file is not executable

myutil/debug_verbose.py:
   1:1  EXE001 Shebang is present but file is not executable
  25:14 UP039 [*] Unnecessary parentheses after class definition
  63:16 UP039 [*] Unnecessary parentheses after class definition

myutil/hashutil.py:
   1:1 EXE001 Shebang is present but file is not executable
  16:1 I001 [*] Import block is un-sorted or un-formatted

myutil/jsonutil.py:
  1:1 EXE001 Shebang is present but file is not executable
  9:1 I001 [*] Import block is un-sorted or un-formatted

myutil/mydateutil.py:
  1:1 EXE001 Shebang is present but file is not executable

myutil/pathutil.py:
  1:1 EXE001 Shebang is present but file is not executable
  8:1 I001 [*] Import block is un-sorted or un-formatted

myutil/queryutil.py:
  1:1 EXE001 Shebang is present but file is not executable
  6:1 I001 [*] Import block is un-sorted or un-formatted

myutil/run_cmd.py:
  1:1 EXE001 Shebang is present but file is not executable
  8:1 I001 [*] Import block is un-sorted or un-formatted

myutil/thedatetime.py:
   1:1  EXE001 Shebang is present but file is not executable
  32:11 DTZ005 `datetime.datetime.now()` called without a `tz` argument
  40:14 UP039 [*] Unnecessary parentheses after class definition
  52:13 DTZ005 `datetime.datetime.now()` called without a `tz` argument

myutil/versionutil.py:
   1:1  EXE001 Shebang is present but file is not executable
  38:40 YTT204 `sys.version_info.minor` compared to integer (python4), compare `sys.version_info` to tuple

np_genrandom_std.py:
   1:1  EXE001 Shebang is present but file is not executable
  24:1  I001 [*] Import block is un-sorted or un-formatted
  57:24 UP039 [*] Unnecessary parentheses after class definition

numpy/arr.py:
  7:1 I001 [*] Import block is un-sorted or un-formatted

numpy/ndist.py:
   1:1  EXE001 Shebang is present but file is not executable
  15:1  I001 [*] Import block is un-sorted or un-formatted
  25:1  I001 [*] Import block is un-sorted or un-formatted
  33:21 UP039 [*] Unnecessary parentheses after class definition

numpy/normal_dist.py:
   1:1  EXE001 Shebang is present but file is not executable
  14:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  14:1  I001 [*] Import block is un-sorted or un-formatted
  26:21 UP039 [*] Unnecessary parentheses after class definition
  77:17 UP039 [*] Unnecessary parentheses after class definition

numpy/np_pmt.py:
   1:1 EXE001 Shebang is present but file is not executable
   9:1 I001 [*] Import block is un-sorted or un-formatted
  22:1 I001 [*] Import block is un-sorted or un-formatted

numpy/pmt_json.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:1  I001 [*] Import block is un-sorted or un-formatted
  23:1  I001 [*] Import block is un-sorted or un-formatted
  39:66 FURB157 [*] Verbose expression in `Decimal` constructor

numpy/sum_timeit.py:
   1:1 EXE001 Shebang is present but file is not executable
   9:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  26:9 PERF402 Use `list` or `list.copy` to create a copy of a list

numpy/timeit_sum.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  14:14 UP039 [*] Unnecessary parentheses after class definition

numpy/vald_gauss.py:
   9:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  16:23 UP039 [*] Unnecessary parentheses after class definition

odd_square_mod_eight.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/a24bcde.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:15 UP039 [*] Unnecessary parentheses after class definition
  41:9  SIM103 Return the condition `n % 24 == 0` directly

omc/ab2468cd.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/ab9.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/abc_ab.py:
   1:1  EXE001 Shebang is present but file is not executable
  21:15 UP039 [*] Unnecessary parentheses after class definition
  43:9  SIM103 Return the condition directly

omc/abcd.py:
  1:1  EXE001 Shebang is present but file is not executable
  9:15 UP039 [*] Unnecessary parentheses after class definition

omc/ar105.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/bbbb.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/bead106.py:
   1:1  EXE001 Shebang is present but file is not executable
  11:15 UP039 [*] Unnecessary parentheses after class definition
  21:9  SIM103 Return the condition `p + q + r <= self.TOTAL` directly

omc/card100.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/coin47.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/coins4.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/d240318-q16.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:1  I001 [*] Import block is un-sorted or un-formatted
  12:15 UP039 [*] Unnecessary parentheses after class definition

omc/d240318-q17.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/d240318-q20.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/d240319-q25.py:
   1:1 EXE001 Shebang is present but file is not executable
  27:9 SIM102 Use a single `if` statement instead of nested `if` statements

omc/d240319-q26.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/d240319-q27.py:
   1:1 EXE001 Shebang is present but file is not executable
  10:1 I001 [*] Import block is un-sorted or un-formatted

omc/defdef.py:
   1:1  EXE001 Shebang is present but file is not executable
  13:15 UP039 [*] Unnecessary parentheses after class definition
  34:9  SIM103 Return the condition `p * p == q` directly

omc/digit21.py:
   1:1 EXE001 Shebang is present but file is not executable
  12:5 SIM102 Use a single `if` statement instead of nested `if` statements

omc/div7.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/eleven.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/eqmod.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/find1115.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/five-eight-thirteen.py:
  1:1  EXE001 Shebang is present but file is not executable
  9:15 UP039 [*] Unnecessary parentheses after class definition

omc/fivesix.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/fseats.py:
   1:1  EXE001 Shebang is present but file is not executable
  11:15 UP039 [*] Unnecessary parentheses after class definition

omc/howmany0.py:
  1:1  EXE001 Shebang is present but file is not executable
  7:15 UP039 [*] Unnecessary parentheses after class definition

omc/howmany7.py:
  1:1  EXE001 Shebang is present but file is not executable
  7:15 UP039 [*] Unnecessary parentheses after class definition

omc/lcm-gcd.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/leog.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/locks/lock5.py:
  1:1  EXE001 Shebang is present but file is not executable
  9:15 UP039 [*] Unnecessary parentheses after class definition

omc/mcn.py:
   1:1 EXE001 Shebang is present but file is not executable
   8:1 I001 [*] Import block is un-sorted or un-formatted
  19:5 SIM103 Return the condition `target - s == 0` directly
  40:9 SIM102 Use a single `if` statement instead of nested `if` statements

omc/mk_remainer.py:
   1:1  EXE001 Shebang is present but file is not executable
  13:15 UP039 [*] Unnecessary parentheses after class definition

omc/mutual.py:
  1:1 EXE001 Shebang is present but file is not executable
  7:1 I001 [*] Import block is un-sorted or un-formatted

omc/nineteen.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/not4sum.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/numbercards.py:
   1:1  EXE001 Shebang is present but file is not executable
  12:15 UP039 [*] Unnecessary parentheses after class definition
  22:9  SIM103 Return the condition `not (a == b or b == c or c == a)` directly
  29:9  SIM103 Return the condition directly
  36:9  SIM103 Return the condition `total == self.target` directly
  57:13 SIM102 Use a single `if` statement instead of nested `if` statements

omc/omc21p26q9.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/one.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/one23.py:
   1:1 EXE001 Shebang is present but file is not executable
  10:5 SIM103 Return the condition `n % 1000 == t` directly

omc/one2nine.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/onethird.py:
   1:1 EXE001 Shebang is present but file is not executable
  14:5 SIM103 Return the condition `1000 <= n <= 9999` directly
  20:5 SIM103 Return the condition `10000 <= n <= 99999` directly

omc/over2015_2022.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/p14x5.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/p20-q22.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/p25-q14.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:15 UP039 [*] Unnecessary parentheses after class definition
  12:14 RUF012 Mutable default value for class attribute
  79:20 PERF102 When using only the values of a dict use the `values()` method

omc/p38-q22.py:
   1:1 EXE001 Shebang is present but file is not executable
  11:1 I001 [*] Import block is un-sorted or un-formatted

omc/p38-q23.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/p41-q15.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:15 UP039 [*] Unnecessary parentheses after class definition
  37:9  SIM103 Return the condition `bool(sum(ds) == 21 and ds[1] - ds[2] == 1)` directly

omc/p43-q15.py:
  1:1  EXE001 Shebang is present but file is not executable
  9:15 UP039 [*] Unnecessary parentheses after class definition

omc/p43-q4.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:14 UP039 [*] Unnecessary parentheses after class definition

omc/p68-q12.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/pen_p61.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:15 UP039 [*] Unnecessary parentheses after class definition
  28:21 SIM102 Use a single `if` statement instead of nested `if` statements

omc/perfect_shuffle.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/pr7.py:
   1:1  EXE001 Shebang is present but file is not executable
  48:15 UP039 [*] Unnecessary parentheses after class definition

omc/prime4.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/q27-add-digits.py:
  1:1  EXE001 Shebang is present but file is not executable
  9:15 UP039 [*] Unnecessary parentheses after class definition

omc/q29-3digits.py:
   1:1  EXE001 Shebang is present but file is not executable
  11:15 UP039 [*] Unnecessary parentheses after class definition

omc/q30/y24p40q30.py:
   1:1  EXE001 Shebang is present but file is not executable
  14:15 UP039 [*] Unnecessary parentheses after class definition

omc/qq13.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/qq15.py:
   1:1  EXE001 Shebang is present but file is not executable
  31:13 SIM102 Use a single `if` statement instead of nested `if` statements

omc/qq4.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/remainer.py:
   1:1  EXE001 Shebang is present but file is not executable
  13:15 UP039 [*] Unnecessary parentheses after class definition

omc/resd_2018.py:
   1:1  EXE001 Shebang is present but file is not executable
  11:15 UP039 [*] Unnecessary parentheses after class definition

omc/resident5.py:
   1:1  EXE001 Shebang is present but file is not executable
  20:15 UP039 [*] Unnecessary parentheses after class definition

omc/run500.py:
   1:1  EXE001 Shebang is present but file is not executable
  13:13 UP039 [*] Unnecessary parentheses after class definition

omc/same3num.py:
  1:1  EXE001 Shebang is present but file is not executable
  7:15 UP039 [*] Unnecessary parentheses after class definition

omc/sendmoremoney.py:
   1:1  EXE001 Shebang is present but file is not executable
  13:15 UP039 [*] Unnecessary parentheses after class definition
  32:9  RUF100 [*] Unused `noqa` directive (non-enabled: `E741`)
  41:9  SIM103 Return the condition `send + more == money` directly

omc/seqodds.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:15 UP039 [*] Unnecessary parentheses after class definition

omc/ser1357.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/ser19_99.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/ser25.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/serial5-37-71.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:15 UP039 [*] Unnecessary parentheses after class definition
  11:12 RUF012 Mutable default value for class attribute

omc/seveN.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/six_multiple/sixes.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:1  I001 [*] Import block is un-sorted or un-formatted
  11:15 UP039 [*] Unnecessary parentheses after class definition

omc/sixty_prime_sum.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:15 UP039 [*] Unnecessary parentheses after class definition
  10:14 RUF012 Mutable default value for class attribute

omc/small60.py:
  1:1  EXE001 Shebang is present but file is not executable
  8:15 UP039 [*] Unnecessary parentheses after class definition

omc/spend_money.py:
   1:1  EXE001 Shebang is present but file is not executable
  23:17 UP039 [*] Unnecessary parentheses after class definition
  62:17 PERF402 Use `list` or `list.copy` to create a copy of a list

omc/sum-vs-avg.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/sumx.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/test7.py:
   1:1  EXE001 Shebang is present but file is not executable
  54:20 PIE808 [*] Unnecessary `start` argument in `range`

omc/threex3coins.py:
   1:1  EXE001 Shebang is present but file is not executable
  13:15 UP039 [*] Unnecessary parentheses after class definition
  15:13 RUF012 Mutable default value for class attribute
  16:14 RUF012 Mutable default value for class attribute

omc/time4.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/utils.py:
   1:1 EXE001 Shebang is present but file is not executable
  20:9 TRY004 Prefer `TypeError` exception for invalid type

omc/work_n_rest.py:
   1:1  EXE001 Shebang is present but file is not executable
  11:15 UP039 [*] Unnecessary parentheses after class definition

omc/y24p25q3.py:
  1:1 EXE001 Shebang is present but file is not executable
  8:1 I001 [*] Import block is un-sorted or un-formatted

omc/y24p26q5.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/y24p28q13.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/y24p28q14.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/y24p28q15.py:
   1:1 EXE001 Shebang is present but file is not executable
  11:5 SIM102 Use a single `if` statement instead of nested `if` statements

omc/y24p29q21-palindrome.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/y24p29q23.py:
   1:1 EXE001 Shebang is present but file is not executable
  10:5 SIM103 Return the condition `bool('4' in ss and n % 4 != 0)` directly

omc/y24p29q24.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/y24p32q30.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:1  I001 [*] Import block is un-sorted or un-formatted
  15:15 UP039 [*] Unnecessary parentheses after class definition

omc/y24p36q15.py:
   1:1 EXE001 Shebang is present but file is not executable
  23:5 SIM102 Use a single `if` statement instead of nested `if` statements

omc/y24p36q16.py:
  1:1 EXE001 Shebang is present but file is not executable

omc/y24p37q18.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:1  I001 [*] Import block is un-sorted or un-formatted
  11:15 UP039 [*] Unnecessary parentheses after class definition

omc/y24p39q26.py:
   1:1  EXE001 Shebang is present but file is not executable
  37:15 UP039 [*] Unnecessary parentheses after class definition

omc/youngage.py:
  1:1  EXE001 Shebang is present but file is not executable
  8:15 UP039 [*] Unnecessary parentheses after class definition

pandas/boxplot_by_years.py:
   1:1  EXE001 Shebang is present but file is not executable
  13:1  I001 [*] Import block is un-sorted or un-formatted
  24:15 UP039 [*] Unnecessary parentheses after class definition

pandas/check_csv.py:
   7:1  I001 [*] Import block is un-sorted or un-formatted
  17:15 UP039 [*] Unnecessary parentheses after class definition
  57:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly

pandas/cmaps-lightness.py:
  1:1 EXE001 Shebang is present but file is not executable

pandas/cmaps_data.py:
  1:1 PLR2044 [*] Line with empty comment

pandas/commune_all.py:
   1:1  EXE001 Shebang is present but file is not executable
   3:1  I001 [*] Import block is un-sorted or un-formatted
  17:15 UP039 [*] Unnecessary parentheses after class definition

pandas/dataframe.py:
  8:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

pandas/driving_data.py:
   33:1  I001 [*] Import block is un-sorted or un-formatted
   41:5  I001 [*] Import block is un-sorted or un-formatted
   51:18 UP039 [*] Unnecessary parentheses after class definition
  301:33 DTZ011 `datetime.date.today()` used
  303:21 RUF046 Value being cast to `int` is already an integer

pandas/eggs.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  20:15 UP039 [*] Unnecessary parentheses after class definition

pandas/heatmap_example.py:
  1:1 EXE001 Shebang is present but file is not executable

pandas/hello_pd.py:
  5:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

pandas/matplotlib-cmaps.py:
  1:1 EXE001 Shebang is present but file is not executable

pandas/perfect_square.py:
  5:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

pandas/showutil.py:
    1:1 EXE001 Shebang is present but file is not executable
    6:5 I001 [*] Import block is un-sorted or un-formatted
   12:1 I001 [*] Import block is un-sorted or un-formatted
  133:9 FURB122 [*] Use of `f.write` in a for loop

pandas/strutil.py:
   1:1 EXE001 Shebang is present but file is not executable
   5:1 I001 [*] Import block is un-sorted or un-formatted
  18:9 TRY004 Prefer `TypeError` exception for invalid type

pandas/tpd.py:
  5:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

pandas/working_days.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:1  I001 [*] Import block is un-sorted or un-formatted
  20:5  I001 [*] Import block is un-sorted or un-formatted
  28:22 UP039 [*] Unnecessary parentheses after class definition

percent_dec.py:
  1:1 EXE001 Shebang is present but file is not executable
  7:1 I001 [*] Import block is un-sorted or un-formatted

percent_enc.py:
  1:1 EXE001 Shebang is present but file is not executable
  7:1 I001 [*] Import block is un-sorted or un-formatted

percent_encdec.py:
  1:1 EXE001 Shebang is present but file is not executable

periodic/brief.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  I001 [*] Import block is un-sorted or un-formatted
  18:5  I001 [*] Import block is un-sorted or un-formatted
  23:18 UP039 [*] Unnecessary parentheses after class definition

periodic/query-elements.py:
  1:1 EXE001 Shebang is present but file is not executable
  8:1 I001 [*] Import block is un-sorted or un-formatted

platfrom.py:
  5:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

play_miranda.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  I001 [*] Import block is un-sorted or un-formatted
  12:1  UP035 `typing.List` is deprecated, use `list` instead
  18:14 UP039 [*] Unnecessary parentheses after class definition
  47:53 UP006 [*] Use `list` instead of `List` for type annotation

productroot.py:
  1:1 EXE001 Shebang is present but file is not executable

pythag.py:
   1:1  EXE001 Shebang is present but file is not executable
  12:15 UP039 [*] Unnecessary parentheses after class definition

qr/common.py:
  1:1 EXE001 Shebang is present but file is not executable

qr/segno_demo.py:
  1:1 EXE001 Shebang is present but file is not executable
  8:1 I001 [*] Import block is un-sorted or un-formatted

qr/tp.py:
   1:1  EXE001 Shebang is present but file is not executable
  19:18 UP039 [*] Unnecessary parentheses after class definition

quotation_mark/read_twopp.py:
  8:19 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly

random/five_char_verbs.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:1  I001 [*] Import block is un-sorted or un-formatted
  13:15 UP039 [*] Unnecessary parentheses after class definition

random/ran.py:
  1:1 EXE001 Shebang is present but file is not executable
  5:1 I001 [*] Import block is un-sorted or un-formatted

random/random_string.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:1  I001 [*] Import block is un-sorted or un-formatted
  31:15 UP039 [*] Unnecessary parentheses after class definition
  65:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly

random/ranit.py:
  1:1 EXE001 Shebang is present but file is not executable

random/ranstr.py:
  1:1 EXE001 Shebang is present but file is not executable

random/unique_namer_demo.py:
  1:1 EXE001 Shebang is present but file is not executable

random/verbs_random.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  I001 [*] Import block is un-sorted or un-formatted
  12:5  I001 [*] Import block is un-sorted or un-formatted
  21:15 UP039 [*] Unnecessary parentheses after class definition
  44:20 BLE001 Do not catch blind exception: `Exception`
  64:20 BLE001 Do not catch blind exception: `Exception`

rdf/filesum.py:
  1:1 EXE001 Shebang is present but file is not executable

rdf/rdf_parse.py:
  25:1 I001 [*] Import block is un-sorted or un-formatted

rdf/this_is_bad.py:
  1:1 EXE001 Shebang is present but file is not executable
  3:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

read_ten_lines.py:
   1:1  EXE001 Shebang is present but file is not executable
  15:19 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly
  16:13 SIM113 Use `enumerate()` for index variable `cnt` in `for` loop

recip.py:
  1:1 EXE001 Shebang is present but file is not executable

remainder.py:
   1:1  EXE001 Shebang is present but file is not executable
  19:15 UP039 [*] Unnecessary parentheses after class definition

repeating_decimal.py:
  1:1 EXE001 Shebang is present but file is not executable

reth.py:
   1:1  EXE001 Shebang is present but file is not executable
  11:1  I001 [*] Import block is un-sorted or un-formatted
  15:1  UP035 `typing.List` is deprecated, use `list` instead
  22:15 UP039 [*] Unnecessary parentheses after class definition
  38:28 UP006 [*] Use `list` instead of `List` for type annotation
  63:32 UP006 [*] Use `list` instead of `List` for type annotation

reurl.py:
  20:16 UP039 [*] Unnecessary parentheses after class definition
  51:19 SIM115 Use a context manager for opening files

rich/sp.py:
  1:1 EXE001 Shebang is present but file is not executable
  8:1 I001 [*] Import block is un-sorted or un-formatted

rpc/concat.py:
   1:1 EXE001 Shebang is present but file is not executable
  12:1 RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  16:1 I001 [*] Import block is un-sorted or un-formatted

rpc/dogapi.py:
  1:1 EXE001 Shebang is present but file is not executable

rpc/fetch_currency_rate.py:
   1:1 EXE001 Shebang is present but file is not executable
  12:9 SIM118 Use `key in dict` instead of `key in dict.keys()`

rpc/fetch_pi.py:
  1:1 EXE001 Shebang is present but file is not executable

rpc/firstai.py:
   1:1  EXE001 Shebang is present but file is not executable
   8:1  I001 [*] Import block is un-sorted or un-formatted
  16:1  I001 [*] Import block is un-sorted or un-formatted
  18:15 UP039 [*] Unnecessary parentheses after class definition
  52:19 DTZ005 `datetime.datetime.now()` called without a `tz` argument

rpc/get_loc.py:
  1:1 EXE001 Shebang is present but file is not executable

rpc/getapikey.py:
   1:1 EXE001 Shebang is present but file is not executable
  12:1 I001 [*] Import block is un-sorted or un-formatted

rpc/getimgur.py:
  1:1 EXE001 Shebang is present but file is not executable

rpc/ghibli_api.py:
   1:1  EXE001 Shebang is present but file is not executable
  18:13 UP039 [*] Unnecessary parentheses after class definition

rpc/goodinfo_qrcode.py:
  1:1 EXE001 Shebang is present but file is not executable

rpc/httpbin.py:
   1:1  EXE001 Shebang is present but file is not executable
  13:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  51:18 UP039 [*] Unnecessary parentheses after class definition

rpc/query_water.py:
   1:1 EXE001 Shebang is present but file is not executable
  12:1 I001 [*] Import block is un-sorted or un-formatted

rpc/req_guassian.py:
  15:1  I001 [*] Import block is un-sorted or un-formatted
  25:22 UP039 [*] Unnecessary parentheses after class definition

rpc/req_random_int.py:
  1:1 EXE001 Shebang is present but file is not executable
  6:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

rpc/rgen.py:
  1:1 EXE001 Shebang is present but file is not executable

rpc/send-attached.py:
  15:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  40:15 UP039 [*] Unnecessary parentheses after class definition
  78:9  SIM102 Use a single `if` statement instead of nested `if` statements

rpc/testqr.py:
   8:1  I001 [*] Import block is un-sorted or un-formatted
  35:22 UP039 [*] Unnecessary parentheses after class definition

rpc/validate_gaussian.py:
  10:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  17:23 UP039 [*] Unnecessary parentheses after class definition
  37:16 UP024 [*] Replace aliased errors with `OSError`
  50:16 UP024 [*] Replace aliased errors with `OSError`

run_gcd.py:
   1:1 EXE001 Shebang is present but file is not executable
  13:1 I001 [*] Import block is un-sorted or un-formatted

run_test3.py:
  1:1 EXE001 Shebang is present but file is not executable
  5:1 I001 [*] Import block is un-sorted or un-formatted

sdir.py:
  1:1 EXE001 Shebang is present but file is not executable

show_arrows.py:
  1:1 EXE001 Shebang is present but file is not executable
  7:1 I001 [*] Import block is un-sorted or un-formatted

show_keyring.py:
  1:1 EXE001 Shebang is present but file is not executable
  9:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

showmsg.py:
  1:1 EXE001 Shebang is present but file is not executable

shuf.py:
  1:1 EXE001 Shebang is present but file is not executable

singleton.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  10:16 UP039 [*] Unnecessary parentheses after class definition

slow.py:
  1:1 EXE001 Shebang is present but file is not executable

spath.py:
   1:1  EXE001 Shebang is present but file is not executable
  16:1  I001 [*] Import block is un-sorted or un-formatted
  66:5  RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  68:17 UP039 [*] Unnecessary parentheses after class definition

sphere.py:
  1:1 EXE001 Shebang is present but file is not executable

sql/getloc.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  I001 [*] Import block is un-sorted or un-formatted
  18:5  RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  20:15 UP039 [*] Unnecessary parentheses after class definition

sumconti.py:
  1:1 EXE001 Shebang is present but file is not executable

syspath.py:
   1:1 EXE001 Shebang is present but file is not executable
  14:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  14:1 I001 [*] Import block is un-sorted or un-formatted

ten_digits.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:15 UP039 [*] Unnecessary parentheses after class definition
  77:13 SIM113 Use `enumerate()` for index variable `cnt` in `for` loop

termux/blnotify.py:
   1:1  EXE001 Shebang is present but file is not executable
  53:15 UP039 [*] Unnecessary parentheses after class definition

test_redirect.py:
  1:1 EXE001 Shebang is present but file is not executable

test_uniform.py:
  1:1 EXE001 Shebang is present but file is not executable

the_gcd.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  UP035 `typing.List` is deprecated, use `list` instead
  21:16 UP006 [*] Use `list` instead of `List` for type annotation

the_tips.py:
   1:1  EXE001 Shebang is present but file is not executable
  13:10 UP039 [*] Unnecessary parentheses after class definition

tm4.py:
  11:15 UP039 [*] Unnecessary parentheses after class definition

triangle.py:
    1:1  EXE001 Shebang is present but file is not executable
   36:13 UP039 [*] Unnecessary parentheses after class definition
   81:13 SIM113 Use `enumerate()` for index variable `cnt` in `for` loop
  122:13 SIM102 Use a single `if` statement instead of nested `if` statements

tstp.py:
  1:1  EXE001 Shebang is present but file is not executable
  8:15 UP039 [*] Unnecessary parentheses after class definition

turtule.py:
  1:1 EXE001 Shebang is present but file is not executable

typer_example.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:1  I001 [*] Import block is un-sorted or un-formatted
  11:1  UP035 `typing.List` is deprecated, use `list` instead
  16:5  I001 [*] Import block is un-sorted or un-formatted
  24:5  RET501 [*] Do not explicitly `return None` in function if it is the only possible return value
  26:11 UP039 [*] Unnecessary parentheses after class definition
  60:35 UP006 [*] Use `list` instead of `List` for type annotation
  81:38 UP045 [*] Use `X | None` for type annotations
  81:47 UP006 [*] Use `list` instead of `List` for type annotation

unicode/apple_logo.py:
  1:1 EXE001 Shebang is present but file is not executable
  8:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
  8:1 I001 [*] Import block is un-sorted or un-formatted

unicode/show_emojis.py:
   1:1  EXE001 Shebang is present but file is not executable
  10:1  I001 [*] Import block is un-sorted or un-formatted
  16:15 UP039 [*] Unnecessary parentheses after class definition
  28:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly
  54:13 SIM113 Use `enumerate()` for index variable `cnt` in `for` loop

unicode/showutf38.py:
  1:1 EXE001 Shebang is present but file is not executable
  7:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

unicode/showutf8.py:
   1:1  EXE001 Shebang is present but file is not executable
   9:1  UP010 [*] Unnecessary `__future__` import `print_function` for target Python version
   9:1  I001 [*] Import block is un-sorted or un-formatted
  27:9  UP025 [*] Remove unicode literals from strings
  27:19 UP025 [*] Remove unicode literals from strings

unicode/unicode_data.py:
  1:1 EXE001 Shebang is present but file is not executable

unihan/num_variants.py:
   1:1  EXE001 Shebang is present but file is not executable
  15:19 UP039 [*] Unnecessary parentheses after class definition
  48:25 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly

unihan/suzhou_numerals.py:
   1:1 EXE001 Shebang is present but file is not executable
  11:1 I001 [*] Import block is un-sorted or un-formatted
  45:9 TRY004 Prefer `TypeError` exception for invalid type

utext.py:
  1:1 EXE001 Shebang is present but file is not executable

utf8_demo.py:
  1:1 EXE001 Shebang is present but file is not executable

util/collect_import.py:
   1:1  EXE001 Shebang is present but file is not executable
   5:1  I001 [*] Import block is un-sorted or un-formatted
  10:1  RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  31:15 UP039 [*] Unnecessary parentheses after class definition
  43:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly
  58:29 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly

util/mkrep.py:
   1:1  EXE001 Shebang is present but file is not executable
   7:1  I001 [*] Import block is un-sorted or un-formatted
  14:1  RUF100 [*] Unused `noqa` directive (non-enabled: `E402`)
  24:15 UP039 [*] Unnecessary parentheses after class definition
  40:23 FURB129 [*] Instead of calling `readlines()`, iterate over file object directly

uuid_demo.py:
  1:1 EXE001 Shebang is present but file is not executable
  8:1 I001 [*] Import block is un-sorted or un-formatted

vampire_number.py:
  1:1 EXE001 Shebang is present but file is not executable
  9:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

write_bin3.py:
   1:1 EXE001 Shebang is present but file is not executable
  15:1 UP010 [*] Unnecessary `__future__` import `print_function` for target Python version

write_bin4.py:
   1:1  EXE001 Shebang is present but file is not executable
  20:15 UP039 [*] Unnecessary parentheses after class definition

xlsxwriter/chart.py:
  1:1 EXE001 Shebang is present but file is not executable

xlsxwriter/go.py:
  11:15 UP039 [*] Unnecessary parentheses after class definition
  35:24 C408 Unnecessary `tuple()` call (rewrite as a literal)

xlsxwriter/w2.py:
  1:1 EXE001 Shebang is present but file is not executable

yaml/ly.py:
   5:1  I001 [*] Import block is un-sorted or un-formatted
  20:30 UP007 [*] Use `X | Y` for type annotations

Found 1030 errors.
[*] 524 fixable with the `--fix` option (37 hidden fixes can be enabled with the `--unsafe-fixes` option).
```
