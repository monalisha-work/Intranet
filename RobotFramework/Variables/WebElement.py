class WebElement():
	def create_ff_profile(self, path):
		from selenium import webdriver
		fp = webdriver.FirefoxProfile()
		fp.set_preference("browser.download.folderList", 2);
		fp.set_preference("browser.download.manager.showWhenStarting", False);
		fp.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf");
		fp.set_preference("pdfjs.disabled", True);
		fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf; application/zip; application/octet-stream; application/csv");
		fp.set_preference("browser.download.manager.alertOnEXEOpen", False);
		fp.set_preference("browser.download.dir", path)
		fp.update_preferences()
		return fp.path