import os, csv

filelist = []
ignore_directories = 'data/mb/mb-chad', 'data/sb', 'data/spec', 'data/builder'
show_results = 'all' # Use 'all' to see all results or specify a number

# Crawl directories to create a master file list.
for dirpath, dirnames, filenames in os.walk('.'):
  for fn in [x for x in filenames if x.endswith('.lua')]:
    filepath = os.path.join(dirpath, fn)
    filepath = filepath[2:]
    filelist.append(filepath)

# Filter the file list by removing files from ignored directories.
filtered_filelist = [y for y in filelist if not y.startswith(ignore_directories)]

# Create a CSV with the filenames and import counts
with open('hitlist.csv', mode='w') as cleaner:
  listWriter=csv.writer(cleaner, delimiter=',')
  for filepath in filtered_filelist:
    count = 0
    for searchfile in filtered_filelist:
      with open(searchfile) as myfile:
        if filepath in myfile.read():
          count = count + 1
    if show_results == 'all':
      # Uncomment the line below to echo program output to stdout.
      # print('Total usage for', filepath, count)
      row = [filepath, count]
      listWriter.writerow(row)
    else:
      if count == show_results:
        # TODO: Create this feature.
        print('Total usage for', filepath, count)
