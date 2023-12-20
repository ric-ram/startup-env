from selenium import webdriver
import os
import subprocess
import psutil


class Control:
    def __init__(self, browser=None, websites=[], apps=[]):
        self.__default_browser = "chrome"
        self.__default_webdriver = self.__get_webdriver(self.__default_browser)
        self.__active_browser = browser.lower()
        self.__active_webdriver = None
        self.__websites = websites
        self.__apps = apps

    def set_default_browser(self, browser):
        self.__default_browser = browser.lower()
        self.__default_webdriver = self.__get_webdriver(self.__default_browser)

    def get_default_browser(self):
        return self.__default_browser

    def set_active_browser(self, active_browser):
        self.__active_browser = active_browser

    def get_active_browser(self):
        return self.__active_browser

    def set_websites(self, websites):
        self.__websites = websites

    def get_websites(self):
        return self.__websites

    def set_apps(self, apps):
        self.__apps = apps

    def get_apps(self):
        return self.__apps

    def __get_webdriver(self, browser):
        if browser == "chrome":
            return webdriver.Chrome()
        elif browser == "firefox":
            return webdriver.Firefox()
        elif browser == "edge":
            return webdriver.Edge()
        else:
            print(f"The browser is not supported, using default browser {
                  self.__default_browser}")
            return self.__default_webdriver

    def open_browser_with_urls(self) -> None:
        if self.__active_browser is None:
            print(f"No browser provided. Using default browser {
                  self.__default_browser}")
            self.__active_webdriver = self.__default_webdriver
        else:
            self.__active_webdriver = self.__get_webdriver(
                self.__active_browser)

        if len(self.__websites) == 0:
            self.__active_webdriver.get("https://www.google.com")
            return
        for i in range(0, len(self.__websites)):
            if i == 0:
                self.__active_webdriver.get(self.__websites[i])
            else:
                self.__active_webdriver.execute_script(
                    "window.open('about:blank', 'newtab');")
                self.__active_webdriver.switch_to.window("newtab")
                self.__active_webdriver.get(self.__websites[i])

    def __open_app(self, app_name: str, folder_path=None) -> None:
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

    def open_apps(self):
        if len(self.__apps) == 0:
            return "No apps to open"

        for app in self.__apps:
            self.__open_app(app.app_name, app.folder_path)


class App:
    def __init__(self, app_name, folder_path=None):
        self.app_name = app_name
        self.folder_path = folder_path

    def __str__(self):
        return f"The app {self.app_name} location is: {self.folder_path}"

    def change_folder_path(self, new_folder_path):
        self.folder_path = new_folder_path
