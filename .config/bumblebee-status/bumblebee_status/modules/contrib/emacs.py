
# pylint: disable=C0111,R0903

"""Shows Linux kernel version information

contributed by `pierre87 <https://github.com/pierre87>`_ - many thanks!
"""

import psutil
import core.module
import core.widget

def is_process_running(process_name):
    # Iterate over all running process
    for proc in psutil.process_iter():
        try:
            if proc.name() == process_name:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

class Module(core.module.Module):
    def __init__(self, config, theme):
        super().__init__(config, theme, core.widget.Widget(self.is_running))
        self.__is_running = ""
        self.__app_name = "emacs"
        self.__brightness = "n/a"

    def is_running(self, widget):
        return self.__is_running

    def update(self):
        if is_process_running(self.__app_name):
            self.__is_running = self.__app_name + ":on"
        else:
            self.__is_running = self.__app_name + ":off"

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
