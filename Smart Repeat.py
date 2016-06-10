## -----------------------------------------------------------------------------
## Author : yongchan jeon (Kris) poucotm@gmail.com
## File   : Smart Repeat.py
## Create : 2016-06-10 23:12:21
## Editor : sublime text3, tab size (3)
## -----------------------------------------------------------------------------

import sublime, sublime_plugin
import os, time
import re

############################################################################
# for settings

ST3 = int(sublime.version()) >= 3000

# def plugin_loaded():
# 	global sr_settings
# 	sr_settings = sublime.load_settings('Smart Repeat.sublime-settings')
# 	sr_settings.clear_on_change('reload')
# 	sr_settings.add_on_change('reload', plugin_loaded)

# def plugin_unloaded():
	# print ("unloaded : Verilog Gadget.py")

# def get_settings():
# 	if ST3:
# 		return sr_settings
# 	else:
# 		return sublime.load_settings('Smart Repeat.sublime-settings')

############################################################################
# SmartRepeatCommand

class SmartRepeatCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		selr = self.view.sel()[0]
		self.text = self.view.substr(selr)
		self.view.window().show_input_panel("type range [from]~[to],[↓step],[→step]", "", self.on_done, None, None)

	def on_done(self, user_input):
		frm_err   = False
		_range    = re.compile(r"[-+]?\d+").findall(user_input)
		_step     = re.compile(r"(?<=,)\s*[-\d]+").findall(user_input)
		range_len = 0
		try:
			if len(_range) >= 2:
				sta_n = int(_range[0])
				end_n = int(_range[1])
				if sta_n <= end_n:
					end_n = end_n + 1
					rsp_n = 1
					csp_n = 0
				else:
					end_n = end_n - 1
					rsp_n = -1
					csp_n = 0
				if len(_step) > 0:
					rsp_n = int(_step[0])
					if len(_step) > 1:
						csp_n = int(_step[1])
			else:
				frm_err = True
			range_len = len(range(sta_n, end_n, rsp_n))
		except:
			frm_err = True

		if range_len < 1 or frm_err:
			sublime.status_message("Smart Repeat : Range format error (" + user_input + ")")
			return

		try:
			tup_l = re.compile(r"(?<!{)\s*{\s*(?!{)").findall(self.text)
			tup_n = len(tup_l)
			repeat_str = ""
			for i in range(sta_n, end_n, rsp_n):
				prm_l = []
				for j in range(tup_n):
					prm_l.append(i + j *csp_n)
				repeat_str = repeat_str + '\n' + self.text.format(*prm_l)
		except:
			sublime.status_message("Smart Repeat : Range format error " + + self.text)
			return

		self.view.run_command("smart_repeat_insert", {"args":{'text': repeat_str}})

############################################################################
# SmartRepeatInsertCommand

class SmartRepeatInsertCommand(sublime_plugin.TextCommand):

	def run(self, edit, args):
		text = args['text']
		selr = self.view.sel()[0]
		self.view.insert(edit, selr.end(), text)
