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
   
     
def open_apps(app_name: str, folder_path=None) -> None:
	app_active = [process.name() for process in psutil.process_iter() if app_name in process.name()]
 
	if not app_active: # check if app is running at start
		print("starting app: ", app_name)
  
		current_dir = os.getcwd()
		if folder_path is not None:
			os.chdir(folder_path)
   
		if os.path.exists(f'{app_name}.exe'):
			subprocess.Popen(app_name)
		else:
			print("File does not exist")
   
		os.chdir(current_dir)
	else:	
		print("App is already open")
 
def main():
  # List of urls to open
	websites = ["https://www.youtube.com/watch?v=9QQL3oBpoh4", "https://www.google.com", "https://mail.google.com/mail/u/0/#inbox"]  
	open_browser_with_urls(websites)
 
	open_apps("firefox")
 
main()