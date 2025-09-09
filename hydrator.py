import rumps
import os

class HydrationReminderApp(rumps.App):
    def __init__(self):
        super().__init__("💧 Hydration")

        self.timer = rumps.Timer(self.show_alert, 10 * 60)
        self.timer.start()
        self.first_run = True
        self.is_running = False

        # Menu options
        self.menu = ["30 min", "1 hour"]

    @rumps.clicked("30 min")
    def set_30min(self, _):
        self.timer.stop()
        self.timer.interval = 30 * 60
        self.first_run = True
        self.timer.start()
        self.show_confirmation("Timer set for 30 minutes")
        

    @rumps.clicked("1 hour")
    def set_1hour(self, _):
        self.timer.stop()
        self.timer.interval = 60 * 60
        self.first_run = True
        self.timer.start()
        self.show_confirmation("Timer set for 1 hour")
        
    def show_confirmation(self, message):
        command = f'''osascript -e 'display dialog "{message}" with title "Hydration" buttons {{"OK"}} default button "OK"' '''
        os.system(command)



    def show_alert(self, sender):
        if self.first_run:
            self.first_run = False
            return
        message = "Time to Hydrate!"
        title = "Hydration App"
        command = f'''
        osascript -e 'display dialog "{message}" with title "{title}" buttons {{"OK"}} default button "OK"'
        '''
        os.system(command)

if __name__ == "__main__":
    HydrationReminderApp().run()
