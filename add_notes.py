# This code illustrates reading a schedule, adding notes to
# the tasks it contains, then rewriting the schedule.

import jpype
import mpxj
import tempfile

jpype.startJVM()

# Read a sample file
from net.sf.mpxj.reader import UniversalProjectReader
project = UniversalProjectReader().read('example.mpp')

# Update the tasks with notes
for task in project.getTasks():
	notes = "This task's ID is " + str(task.getID()) + " and it's name is " + str(task.getName())
	task.setNotes(notes)

# Create a temporary file name
tempFile = tempfile.NamedTemporaryFile(suffix='.xml').name
print("Writing new file to", tempFile)

# Write as MSPDI to the temporary file
from net.sf.mpxj.mspdi import MSPDIWriter
writer = MSPDIWriter()
writer.write(project, tempFile)

jpype.shutdownJVM()