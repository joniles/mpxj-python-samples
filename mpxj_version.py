import jpype
import mpxj

jpype.startJVM()

from net.sf.mpxj import MPXJ

print("MPXJ Version: " + str(MPXJ.VERSION))

jpype.shutdownJVM()