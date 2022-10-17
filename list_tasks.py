import jpype
import mpxj

jpype.startJVM()
from net.sf.mpxj.reader import UniversalProjectReader
project = UniversalProjectReader().read('example.mpp')

print("Tasks")
for task in project.getTasks():
	print(task.getID().toString() + "\t" + task.getName())

jpype.shutdownJVM()