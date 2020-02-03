import sublime
import sublime_plugin
import json
from os.path import dirname, realpath, join, splitext, basename

try:
	# Python 2
	from node_bridge import node_bridge
except:
	from .node_bridge import node_bridge

def get_setting(view, key):
	settings = view.settings().get('Stylus Supremacy')
	if settings is None:
		settings = sublime.load_settings('Stylus Supremacy.sublime-settings')
	return settings.get(key)

BIN_PATH = join(sublime.packages_path(), dirname(realpath(__file__)), 'stylussupremacy.js')

class StylusSupremacyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if not self.is_stylus():
			# print("File's type isn't stylus one, ignoring format.")
			return

		if not self.has_selection():
			region = sublime.Region(0, self.view.size())
			originalBuffer = self.view.substr(region)
			fixed = self.fix(originalBuffer)
			if fixed:
				self.view.replace(edit, region, fixed)
			return

		for region in self.view.sel():
			if region.empty():
				continue
			originalBuffer = self.view.substr(region)
			fixed = self.fix(originalBuffer)
			if fixed:
				self.view.replace(edit, region, fixed)

	def is_stylus(self):
		return self.view.settings().get('syntax').endswith("Stylus.tmLanguage")

	def fix(self, data):
		try:
			return node_bridge(data, BIN_PATH, [json.dumps({
				'insertColons': get_setting(self.view, 'insertColons'),
				'insertSemicolons': get_setting(self.view, 'insertSemicolons'),
				'insertBraces': get_setting(self.view, 'insertBraces'),
				'insertNewLineAroundImports': get_setting(self.view, 'insertNewLineAroundImports'),
				'insertNewLineAroundBlocks': get_setting(self.view, 'insertNewLineAroundBlocks'),
				'insertNewLineAroundProperties': get_setting(self.view, 'insertNewLineAroundProperties'),
				'insertNewLineAroundOthers': get_setting(self.view, 'insertNewLineAroundOthers'),
				'preserveNewLinesBetweenPropertyValues': get_setting(self.view, 'preserveNewLinesBetweenPropertyValues'),
				'insertSpaceBeforeComment': get_setting(self.view, 'insertSpaceBeforeComment'),
				'insertSpaceAfterComment': get_setting(self.view, 'insertSpaceAfterComment'),
				'insertSpaceAfterComma': get_setting(self.view, 'insertSpaceAfterComma'),
				'insertSpaceInsideParenthesis': get_setting(self.view, 'insertSpaceInsideParenthesis'),
				'insertParenthesisAfterNegation': get_setting(self.view, 'insertParenthesisAfterNegation'),
				'insertParenthesisAroundIfCondition': get_setting(self.view, 'insertParenthesisAroundIfCondition'),
				'insertNewLineBeforeElse': get_setting(self.view, 'insertNewLineBeforeElse'),
				'insertLeadingZeroBeforeFraction': get_setting(self.view, 'insertLeadingZeroBeforeFraction'),
				'selectorSeparator': get_setting(self.view, 'selectorSeparator'),
				'tabStopChar': get_setting(self.view, 'tabStopChar'),
				'newLineChar': get_setting(self.view, 'newLineChar'),
				'quoteChar': get_setting(self.view, 'quoteChar'),
				'sortProperties': get_setting(self.view, 'sortProperties'),
				'alwaysUseImport': get_setting(self.view, 'alwaysUseImport'),
				'alwaysUseNot': get_setting(self.view, 'alwaysUseNot'),
				'alwaysUseAtBlock': get_setting(self.view, 'alwaysUseAtBlock'),
				'alwaysUseExtends': get_setting(self.view, 'alwaysUseExtends'),
				'alwaysUseNoneOverZero': get_setting(self.view, 'alwaysUseNoneOverZero'),
				'alwaysUseZeroWithoutUnit': get_setting(self.view, 'alwaysUseZeroWithoutUnit'),
				'reduceMarginAndPaddingValues': get_setting(self.view, 'reduceMarginAndPaddingValues'),
				'ignoreFiles': get_setting(self.view, 'ignoreFiles'),
			})])
		except Exception as e:
			sublime.error_message('Stylus Supremacy\n%s' % e)

	def has_selection(self):
		for sel in self.view.sel():
			start, end = sel
			if start != end:
				return True
		return False
