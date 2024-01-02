import jpype
import mpxj

jpype.startJVM()

from net.sf.mpxj.reader import UniversalProjectReader
from net.sf.mpxj.writer import ProjectWriterUtility

def convert(input_file, output_file):
	reader = UniversalProjectReader()
	project_file = reader.read(input_file);
	writer = ProjectWriterUtility.getProjectWriter(output_file)
	writer.write(project_file, output_file)

jpype.shutdownJVM()
