import pprint
import xml.dom.minidom
dom = xml.dom.minidom.parse("conf.xml")
import shutil

dom.normalize()

#У нас 2 тега с именем file соответственно берем первый и второй

node1=dom.getElementsByTagName("file")[0]
node2=dom.getElementsByTagName("file")[1]

# В тегах 3 атрибута sourse_path, destination_path, file_name следовательно возьмем их все
sourse_path1=node1.getAttribute("source_path")
sourse_path2=node2.getAttribute("source_path")

destination_path1=node1.getAttribute("destination_path")
destination_path2=node2.getAttribute("destination_path")

file_name1=node1.getAttribute("file_name")
file_name2=node2.getAttribute("file_name")
# с помощью copy 2 скопируем 
shutil.copy2(sourse_path1+file_name1, destination_path1)
shutil.copy2(sourse_path2+file_name2, destination_path2)


