import jpype
import mpxj

jpype.startJVM()
from org.mpxj.sample import MpxjConvert
MpxjConvert().process('example.mpp', 'example.mpx')
jpype.shutdownJVM()