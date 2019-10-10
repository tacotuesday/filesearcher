import os, csv

filelist = []
ignore_directories = 'data/mb/washer', 'data/sb', 'spec', 'tools', 'build-scripts'
show_results = 'all' #use 'all' to see all results or specify a number

for dirpath, dirnames, filenames in os.walk('.'):
  for filename in [x for x in filenames if x.endswith('.lua')]:
    filepath = os.path.join(dirpath, filename)
    filepath = filepath[2:]
    filelist.append(filepath)
filtered_filelist = [y for y in filelist if not y.startswith(ignore_directories)]

with open('listtest.csv', mode='w') as listDude:
  listWriter=csv.writer(listDude, delimiter=',')
  for filepath in filtered_filelist:
    count = 0
    for searchfile in filtered_filelist:
      with open(searchfile) as myfile:
        if filepath in myfile.read():
          count = count + 1
    if show_results == 'all':
      # print 'Total usage for', filepath, count
      row = [filepath, count]
      listWriter.writerow(row)
    else:
      if count == show_results:
        print 'Total usage for', filepath, count
