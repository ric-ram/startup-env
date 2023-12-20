from selenium import webdriver
import os
import subprocess
import psutil


class Control:
    def __init__(self):
        self.__browsers = []
        self.__websites = []
        self.__apps = {}

    def set_browsers(self, browsers):
        self.__browsers = browsers

    def get_browsers(self):
        return self.__browsers

    def set_websites(self, websites):
        self.__websites = websites

    def get_websites(self):
        return self.__websites

    def set_apps(self, apps):
        self.__apps = apps

    def get_apps(self):
        return self.__apps

    def open_browser_with_urls(self) -> None:
        webBrowser = webdriver.Firefox()

        if len(self.__websites) == 0:
            webBrowser.get("https://www.google.com")
            return
        for i in range(0, len(self.__websites)):
            if i == 0:
                webBrowser.get(self.__websites[i])
            else:
                webBrowser.execute_script(
                    "window.open('about:blank', 'newtab');")
                webBrowser.switch_to.window("newtab")
                webBrowser.get(self.__websites[i])

    def open_apps(self, app_name: str, folder_path=None) -> None:
        app_active = [process.name() for process in psutil.process_iter()
                      if app_name in process.name()]

        if not app_active:  # check if app is running at start
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
