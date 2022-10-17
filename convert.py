import jpype
import mpxj

jpype.startJVM()
from net.sf.mpxj.sample import MpxjConvert
MpxjConvert().process('example.mpp', 'example.mpx')
jpype.shutdownJVM()