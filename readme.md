[![PyPI](https://img.shields.io/pypi/v/mcget.svg)](https://pypi.org/project/mcget)

"mcget" is a simple tool to download and update the Minecraft server or/and 
launcher.

## Features

* Install or update the Minecraft server (`server.jar`) in any directory.
* Install or update the Minecraft Java launcher (`launcher.jar`) in any
  directory (This launcher variant was chosen because it works on every OS and
  only requires Java installed).
* Downloads files only if outdated or not installed. 
* Uses the SHA1 hash provided by Mojang API to check download integrity and
  check if a file needs to be updated.
* Performs the operation on server and launcher in parallel to improve update
  performance.

## Installation

"mcget" can be installed using pip and require Python >= 3.6:

```bash
pip3 install mcget
```

## Usage

"mcget" is a simple command line utility that support following arguments:

* `--launcher` or `-l`: If specified, install or update the launcher.
* `--server` or `-s`: If specified, Install or update the server.
* `--out_dir` or `-o`: Output directory. Default to current directory if not 
  specified.
* `--quiet` or `-q`: If specified, hide outputs.
* `--version`: If specified, return "mcget" version and exit.

### Examples
 
Installing (or updating) the launcher and the server in a the `/opt/minecraft`
directory:
```bash
mcget --launcher --server --out_dir=/opt/minecraft

# Or with a shorter syntax:
mcget -lso /opt/minecraft
```

Installing (or updating) the server only in the current directory:
```bash
mcget --server

# Or with a shorter syntax:
mcget -s
```
