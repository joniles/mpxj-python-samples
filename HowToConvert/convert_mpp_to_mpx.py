import jpype
import mpxj

jpype.startJVM()

from net.sf.mpxj.mpp import MPPReader
from net.sf.mpxj.mpx import MPXWriter

def convert(input_file, output_file):
	reader = MPPReader()
	project_file = reader.read(input_file)
	writer = MPXWriter()
	writer.write(project_file, output_file)

jpype.shutdownJVM()
