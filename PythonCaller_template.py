import traceback
from locale import getdefaultlocale
from fmeobjects import *


class MyClassNamePleaseChange(object):

    def __init__(self):
        self.feature_count = 0
        self.log = FMELogFile()
        try:
            self.locale_encoding = getdefaultlocale()[1]
        except:
            self.locale_encoding = "cp1252"

    def log2FME(self, message, severity=FME_INFORM):
        """
        Sends message to the FME log file and console window.
        Severity must be one of FME_INFORM, FME_WARN, FME_ERROR,
        FME_FATAL, FME_STATISTIC, or FME_STATUSREPORT.
        """
        if isinstance(message, unicode):
            # Unicode messages needs transforming to client locale
            message = message.encode(self.locale_encoding)
        self.log.logMessageString(message, severity)

    def input(self, feature):
        """Called once for each feature."""
        try:
            self.feature_count += 1

            # ###########################
            #   Your code goes here...
            # ###########################

            self.pyoutput(feature)

        except:
            self.log2FME('='*78, FME_ERROR)
            self.log2FME("PythonCaller(%s) exception at feature number %d:" %
                         (self.__class__.__name__, self.feature_count),
                         FME_ERROR)
            self.log2FME('-'*78, FME_ERROR)
            for line in traceback.format_exc().splitlines():
                self.log2FME(line, FME_ERROR)
            self.log2FME('='*78, FME_ERROR)
            if feature:
                self.log.logFeature(feature, FME_ERROR)
            raise FMEException("An error occurred in PythonCaller '%s'. " +
                               "See log for details." %
                               self.__class__.__name__)

    def close(self):
        """Called once after the last feature has been processed."""
        self.log2FME("PythonCaller(%s): %d feature(s) processed" %
                     (self.__class__.__name__, self.feature_count),
                     FME_STATISTIC)