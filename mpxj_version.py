import jpype
import mpxj

jpype.startJVM()

from org.mpxj import MPXJ

print("MPXJ Version: " + str(MPXJ.VERSION))

jpype.shutdownJVM()