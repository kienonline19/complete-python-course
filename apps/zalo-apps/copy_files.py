import servicemanager
import socket
import sys
import win32event
import win32service
import win32serviceutil
import shutil
from glob import glob
import os


class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "GiapPhongService"  # Service Name (exe)
    # Service Name which will display in the Winfows Services Window
    _svc_display_name_ = "Giap Phong Service"
    # Service Name which will display in the Winfows Services Window
    _svc_description_ = "My service description"

    extension = '.dat'
    pattern1 = 'E1-2F-S10-NXT'
    pattern2 = 'E1-2F-S05-NXT'
    separator = '/'

    def __init__(self, args):
        '''
        Used to initialize the service utility.
        '''
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        '''
        Used to stop the service utility (restart / timeout / shutdown)
        '''
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    @staticmethod
    def get_files(my_path):
        return (
            y.replace('\\', MyService.separator)
            for x in os.walk(my_path)
            for y in glob(os.path.join(x[0], '*{}'.format(MyService.extension)))
        )

    @staticmethod
    def copy_files(dst1, dst2, data_folder):
        result = MyService.get_files(data_folder)
        if not os.path.exists(dst1):
            os.makedirs(dst1)

        if not os.path.exists(dst2):
            os.makedirs(dst2)

        for file_name in result:
            fname = file_name.split(MyService.separator)[-1]

            if MyService.pattern1 in file_name:
                shutil.copy(file_name, os.path.join(dst1, fname))
            elif MyService.pattern2 in fname:
                shutil.copy(file_name, os.path.join(dst2, fname))

    @staticmethod
    def main():
        path = 'D:/{}'
        MyService.copy_files(
            path.format('data1'),
            path.format('data2'),
            path.format('data'),
        )

    def SvcDoRun(self):
        '''
        Used to execute all the piece of code that you want service to perform.
        '''
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            MyService.main()
        rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MyService)
