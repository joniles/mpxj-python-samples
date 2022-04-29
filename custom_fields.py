import jpype
import mpxj

jpype.startJVM()

from net.sf.mpxj.reader import UniversalProjectReader
from net.sf.mpxj import FieldTypeClass
from net.sf.mpxj import TaskField

project = UniversalProjectReader().read(
    'some-file-with-custom-fields.mpp')

# Just to get started, let's see what tasks we have
print("Tasks")
tasks = project.getTasks()

for task in tasks:
    print(task.getID().toString() + "\t" +
          task.getName())
print()

# OK, so what custom field so we have?
print("Custom Fields")
for field in project.getCustomFields():
    print(field.getFieldType().getFieldTypeClass().toString() + "\t" +
          field.getFieldType().toString() + "\t" +
          field.getAlias())
print()

# Ah! We have custom field definitions here for different entity types
# (tasks, resources etc). Let's filter that list down to just task custom
# fields and print those.
task_custom_fields = list(filter(lambda field: field.getFieldType(
).getFieldTypeClass() == FieldTypeClass.TASK, project.getCustomFields()))

print("Task Custom Fields")
for field in task_custom_fields:
    print(field.getFieldType().getFieldTypeClass().toString() + "\t" +
          field.getFieldType().toString() + "\t" + field.getAlias())

# Let's build a report showing the ID, Name and any custom fields for each task.
# First we'll build a list of column headings and a list of field types
column_names = ['ID', 'Name']
column_types = [TaskField.ID, TaskField.NAME]
for field in task_custom_fields:
    column_names.append(str(field.getAlias()))
    column_types.append(field.getFieldType())

# Now we can print the column headings, then iterate through the tasks
# and retrieve the values using the field types.
print('\t'.join(column_names))
for task in tasks:
    column_values = map(lambda type: str(
        task.getCachedValue(type)), column_types)
    print(task.getID().toString() + "\t" +
          task.getName() + "\t" +
          '\t'.join(column_values))

jpype.shutdownJVM()
