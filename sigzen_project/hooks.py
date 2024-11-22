app_name = "sigzen_project"
app_title = "sigzen_project"
app_publisher = "Aerele Technologies"
app_description = "Builded frontend app for frontend builder"
app_email = "support@aerele.in"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sigzen_project/css/sigzen_project.css"
# app_include_js = "/assets/sigzen_project/js/sigzen_project.js"

# include js, css files in header of web template
# web_include_css = "/assets/sigzen_project/css/sigzen_project.css"
# web_include_js = "/assets/sigzen_project/js/sigzen_project.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sigzen_project/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sigzen_project/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sigzen_project.utils.jinja_methods",
# 	"filters": "sigzen_project.utils.jinja_filters"
# }
after_migrate = "sigzen_project.after_migrate.AfterMigrate"

# Installation
# ------------

# before_install = "sigzen_project.install.before_install"
# after_install = "sigzen_project.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sigzen_project.uninstall.before_uninstall"
# after_uninstall = "sigzen_project.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sigzen_project.utils.before_app_install"
# after_app_install = "sigzen_project.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sigzen_project.utils.before_app_uninstall"
# after_app_uninstall = "sigzen_project.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sigzen_project.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sigzen_project.tasks.all"
# 	],
# 	"daily": [
# 		"sigzen_project.tasks.daily"
# 	],
# 	"hourly": [
# 		"sigzen_project.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sigzen_project.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sigzen_project.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sigzen_project.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sigzen_project.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sigzen_project.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sigzen_project.utils.before_request"]
# after_request = ["sigzen_project.utils.after_request"]

# Job Events
# ----------
# before_job = ["sigzen_project.utils.before_job"]
# after_job = ["sigzen_project.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sigzen_project.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

website_route_rules = [{'from_route': '/frontend/<path:app_path>', 'to_route': 'frontend'},]