# Make the AI Judge Laugh

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)

Entry for the make.fun competition **Make the AI Judge Laugh**
(`u-rama-melon-make-the-ai-judge-laugh-302d0825`): a single one-line joke
about office life, written by `main.py` to `/output/entry.txt`.

## How it works

`main.py` writes one joke line (1-200 characters, single line, no trailing
newline) to the output directory named by `MAKEFUN_OUTPUT_DIR`
(default `/output`), and leaves the file world-readable (mode 0644).

## Run

```sh
python3 main.py
```
