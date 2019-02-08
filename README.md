# .vimrc to JSON

A Python script that converts a `.vimrc` into a `settings.json` for [VSCodeVim](https://github.com/VSCodeVim/Vim).

## How to use

1. Install [Python 3.x](https://www.python.org/downloads/)

2. Download [vimrc-to-json.py](vimrc-to-json.py)

3. Put your `.vimrc` and `vimrc-to-json.py` in the same directory

4. Run `vimrc-to-json.py`. It outputs a `settings.json` for VSCodeVim.

## Example

`.vim`
```vim
nmap nt gg
nnoremap + <C-a>
vnoremap Y :w<CR>
```

`settings.json`
```json
{
	"vim.normalModeKeyBindings": [
		{
			"before": ["n", "t"],
			"after": ["g", "g"]
		}
	],
	"vim.normalModeKeyBindingsNonRecursive": [
		{
			"before": ["+"],
			"after": ["<C-a>"]
		}
	],
	"vim.visualModeKeyBindingsNonRecursive": [
		{
			"before": ["Y"],
			"commands": [":w"]
		}
	]
}
```

## License

This tool is free software; you can redistribute it and/or modify it under the terms of the MIT license. See [LICENSE](LICENSE) for details.