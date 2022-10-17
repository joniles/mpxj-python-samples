import jpype
import mpxj

# Unless you happen to need to configure Log4j yourself
# you can silence the annoying warning messaging it produces like this:
jpype.startJVM("-Dlog4j2.loggerContextFactory=org.apache.logging.log4j.simple.SimpleLoggerContextFactory")
from net.sf.mpxj.sample import MpxjConvert
MpxjConvert().process('example.mpp', 'example.mpx')
jpype.shutdownJVM()