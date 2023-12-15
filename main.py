from selenium import webdriver
import os
import subprocess
import psutil

def open_browser_with_urls(websites: []) -> None:
	# This is for Firefox
	webBrowser = webdriver.Firefox()
 
	if len(websites) == 0:
		webBrowser.get("https://www.google.com")
		return

	for i in range(0, len(websites)):
		if i == 0:
			webBrowser.get(websites[i])
		else:
			webBrowser.execute_script("window.open('about:blank', 'newtab');")
			webBrowser.switch_to.window("newtab")
			webBrowser.get(websites[i])
 
def main():
  # List of urls to open
	websites = ["https://www.youtube.com/watch?v=9QQL3oBpoh4", "https://www.google.com", "https://mail.google.com/mail/u/0/#inbox"]  
	open_browser_with_urls(websites)
 
main()