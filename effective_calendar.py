# This code illustrates how to display details of
# teh effective calendar for each task

import jpype
import mpxj

jpype.startJVM()

# Read a sample file
from net.sf.mpxj.reader import UniversalProjectReader
project = UniversalProjectReader().read('example.mpp')

# Display details of the effective calendar for each task
for task in project.getTasks():	
	print("Task: " + str(task.getID()) + "\t" + str(task.getName()))
	effective_calendar = task.getEffectiveCalendar()
	print("Effective calendar: " + str(effective_calendar.getUniqueID()) + "\t" + str(effective_calendar.getName()))
	print()

jpype.shutdownJVM()
