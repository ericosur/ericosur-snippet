README
======

## invoke

* use ```make clean``` to remove all intermediate files
* use ```make``` to run all stuff

## file list

* Makefile to control the sample flow

* [mk_table.py](./mk_table.py) is a script to use "StorePrime" to load prime numbers from table and write it to xlsx file. It uses upper one level modules (StorePrime)

* [ggmail.py](./ggmail.py) it could send file via gmail.
> NOTICE:
For ggmail.py, it need auth key for gmail usage. It MUST NOT be included in the git repository. The config file is $HOME/Private/mktable_ggmail.json.
