
from ClockFile import ClockFile
from StatusFile import StatusFile
from TcpFile import TcpFile
from CurlFile import CurlFile
from DSKMapFile import DSKMapFile


class SpecialFiles(object):

    def __init__(self, tipi_io):
        self.tipi_io = tipi_io
        self.specreg = {
            TcpFile.filename(): TcpFile(self.tipi_io),
            ClockFile.filename(): ClockFile(self.tipi_io),
            StatusFile.filename(): StatusFile(self.tipi_io),
            DSKMapFile.filename(): DSKMapFile(self.tipi_io),
            CurlFile.filename(): CurlFile(self.tipi_io)
        }

    def handle(self, pab, devname):
        for prefix in self.specreg.keys():
            if devname.startswith(prefix):
                handler = self.specreg.get(prefix, None)
                handler.handle(pab, devname)
                return True
        return False
