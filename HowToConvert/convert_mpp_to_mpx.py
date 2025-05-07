import jpype
import mpxj

jpype.startJVM()

from org.mpxj.mpp import MPPReader
from org.mpxj.mpx import MPXWriter

def convert(input_file, output_file):
	reader = MPPReader()
	project_file = reader.read(input_file)
	writer = MPXWriter()
	writer.write(project_file, output_file)

jpype.shutdownJVM()
