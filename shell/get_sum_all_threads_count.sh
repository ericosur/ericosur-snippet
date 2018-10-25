#!/bin/bash

# reference:
# https://askubuntu.com/questions/88972/how-to-get-from-terminal-total-number-of-threads-per-process-and-total-for-al
#

ps h -eo nlwp | awk '{ num_threads += $1 } END { print num_threads }'


