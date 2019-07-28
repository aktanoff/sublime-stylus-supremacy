import sublime
import sublime_plugin
from os.path import dirname, realpath, join, splitext, basename

try:
	# Python 2
	from node_bridge import node_bridge
except:
	from .node_bridge import node_bridge


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
			return node_bridge(data, BIN_PATH)
		except Exception as e:
			sublime.error_message('Stylus Supremacy\n%s' % e)

	def has_selection(self):
		for sel in self.view.sel():
			start, end = sel
			if start != end:
				return True
		return False
