#!/bin/bash

function is_ssh() {
    # provide a function to tell if this script is running in ssh connection
    # not local machine
    # you will be taken from remote if "ssh localhost"
    if [[ -n "$SSH_CLIENT" ]] || [[ -n "$SSH_CONNECTION" ]]; then
        return 0 # true from remote
    else
        return 1 # false from local machine
    fi
}

function is_wsl() {
    # Check if the script is running in WSL (Windows Subsystem for Linux)
    if grep -qEi "(Microsoft|WSL)" /proc/version &>/dev/null; then
        return 0  # True, running in WSL
    else
        return 1  # False, not running in WSL
    fi
}

function is_cygwin() {
    # Check if the script is running in Cygwin
    if [[ "$(uname -s)" == *"CYGWIN"* ]]; then
        return 0  # True, running in Cygwin
    else
        return 1  # False, not running in Cygwin
    fi
}

function is_docker() {
    if [ -f /.dockerenv ] ; then
        return 0  # running in docker
    else
        return 1  # not in docker
    fi
}

# exmaple to use these functions
if is_ssh ; then
    echo "This script is running remotely via SSH."
    # You can also extract details:
    echo "SSH Client: $SSH_CLIENT"
    echo "SSH Connection: $SSH_CONNECTION"
else
    echo "This script is running on the local machine."
fi
