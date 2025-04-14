# This code illustrates how to read and write
# a schedule file using MPXJ's readers and writers directly.

import jpype
import mpxj
import tempfile

jpype.startJVM()

# Read a sample file
from org.mpxj.reader import UniversalProjectReader
project = UniversalProjectReader().read('example.mpp')

# Create a temporary file name
tempFile = tempfile.NamedTemporaryFile(suffix='.xml').name
print(tempFile)

# Write as MSPDI to the temporary file
from org.mpxj.mspdi import MSPDIWriter
writer = MSPDIWriter()
writer.write(project, tempFile)

jpype.shutdownJVM()