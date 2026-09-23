# Agent Instructions

This document provides project-specific guidelines and environment setup instructions for AI coding agents working in this workspace.

## Environment Setup & Python Version

1. Before running Python code or scripts, check whether this workspace has a
   `.venv` directory. If it does, activate it and verify the interpreter:
   ```bash
   source .venv/bin/activate
   python --version
   ```
   Use Python 3.14.x for this project. Do not rely on the system Python when a
   suitable virtual environment is available.
2. If `.venv` is absent, suggest that the user create a workspace-local
   environment. Offer either `uv` (a separate tool from `pip-tools`) or the
   traditional `venv`/`pip` approach:
   ```bash
   uv venv --python 3.14 .venv
   uv pip install --python .venv/bin/python -r requirements.txt
   ```
   or:
   ```bash
   python3.14 -m venv .venv
   .venv/bin/python -m pip install -r requirements.txt
   ```
   Do not install packages or create the environment merely to inspect the
   workspace; suggest setup to the user when it is needed.

## Managing Third-Party Python Modules

1. Use `pip-sync` to keep the same Python modules between machines when
   dependency synchronization is needed and the tool is available.
2. Use `pip-compile --upgrade` if the user needs to upgrade some modules.
3. If the user says the environment is limited and cannot download third-party
   Python modules, prefer standard-library solutions wherever practical. Do
   not attempt downloads or installations. If a required feature cannot be
   provided with the standard library or already-installed modules, explain
   that limitation to the user.
