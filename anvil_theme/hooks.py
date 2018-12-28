# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "anvil_theme"
app_title = "Anvil Theme"
app_publisher = "zaqout"
app_description = "Anvil Theme"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "zaqoutabed@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/anvil_theme/css/anvil_theme.css"
# app_include_js = "/assets/anvil_theme/js/anvil_theme.js"

# include js, css files in header of web template
# web_include_css = "/assets/anvil_theme/css/anvil_theme.css"
# web_include_js = "/assets/anvil_theme/js/anvil_theme.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "home"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "anvil_theme.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "anvil_theme.install.before_install"
# after_install = "anvil_theme.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "anvil_theme.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"anvil_theme.tasks.all"
# 	],
# 	"daily": [
# 		"anvil_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"anvil_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"anvil_theme.tasks.weekly"
# 	]
# 	"monthly": [
# 		"anvil_theme.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "anvil_theme.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "anvil_theme.event.get_events"
# }

