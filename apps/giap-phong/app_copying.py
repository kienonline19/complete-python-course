import servicemanager
import socket
import sys
import win32event
import win32service
import win32serviceutil
import shutil
import os
import time
from glob import glob


class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "GiapPhongService"
    _svc_display_name_ = "Giap Phong Service"
    _svc_description_ = "My service description"

    def __init__(self, args):

        self.params = {
            "src": "D:/data",
            "out1": "D:/data1",
            "out2": "D:/data2",
            "extension": ".dat",
            "pattern1": "E1-2F-S10-NXT",
            "pattern2": "E1-2F-S05-NXT",
            "separator": "/"
        }

        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def get_files(self, my_path):

        separator = self.params["separator"]

        return (
            y.replace('\\', separator)
            for x in os.walk(my_path)
            for y in glob(os.path.join(x[0], '*{}'.format(self.params["extension"])))
        )

    def main(self):
        data_folder = self.params["src"]
        dst1 = self.params["out1"]
        dst2 = self.params["out2"]
        pattern1 = self.params["pattern1"]
        pattern2 = self.params["pattern2"]
        separator = self.params["separator"]

        result = self.get_files(data_folder)
        if not os.path.exists(dst1):
            os.makedirs(dst1)

        if not os.path.exists(dst2):
            os.makedirs(dst2)

        for file_name in result:
            fname = file_name.split(separator)[-1]

            if pattern1 in fname:
                shutil.copy(file_name, os.path.join(dst1, fname))
                os.remove(file_name)
            elif pattern2 in fname:
                shutil.copy(file_name, os.path.join(dst2, fname))
                os.remove(file_name)

    def SvcDoRun(self):
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            while True:
                self.main()
                time.sleep(5 * 60)
        rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MyService)
