# sublime-stylus-supremacy

__Sublime text plugin to format stylus `.styl` files__

Sublime Text plugin for [Stylus Supremacy](https://github.com/ThisIsManta/stylus-supremacy)

**You need to have [Node.js](http://nodejs.org) installed.**  
Make sure it's in your $PATH by running `node -v` in your command-line.

> Note: On OS X it's expected that Node resides in the /usr/local/bin/ folder, which it does when installed with the default installer. If this is not the case, symlink your Node binary to this location:  
`ln -s /full/path/to/your/node /usr/local/bin/node`

## Usage 

Press ctrl + shift + p and choose `Stylus Supremacy: Format code` to format your file or selected stylus code.

### Keyboard shortcut

You can also set up a keyboard shortcut to run the command by opening up *Preferences > Key Bindings - User* and adding your shortcut with the `stylus_supremacy` command.

Example:

```json
[
	{ "keys": ["ctrl+alt+f"], "command": "stylus_supremacy" }
]
```



You also can use it with `Chain of Command` plugin if you need to bind multiple formatters to one shortcut:

```json
[
	{
		"keys": ["ctrl+alt+f"],
		"command": "chain",
		"args": {
			"commands": [
				["js_prettier"],
				["stylus_supremacy"]
			]
		}
	}
]
```

## Kudos
This plugin is based on the excellent [Autoprefixer plugin](https://github.com/sindresorhus/sublime-autoprefixer) by Sindre Sorhus.

Also based on [Sublime Stylefmt plugin](https://github.com/dmnsgn/sublime-stylefmt) by Damien Seguin.