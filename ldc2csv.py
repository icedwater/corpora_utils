#! /usr/bin/env python3

"""
Convert the text transcript from the LDC text format into a CSV.
"""
import sys

filename = sys.argv[1]
csvfilename = filename.replace("txt", "csv")

# create CSV file first
csvfile = open(csvfilename, 'w')
csvfile.write('"ID","Start","End","Speaker","Text","Semantic","Dialogue","Emotional"\n')

with open(filename, 'r') as hub5file:
    for line in hub5file:
        if line[0] == '#':
            try:
                key, val = line.split(':')
            except ValueError as v:
                print(">>> {}\n>>> Not assigning key/val from this: {}\n".format(str(v), line))
                key = ''
                val = ''
            if key == "#Language":
                pass
            elif key == "#File id":
                file_id = val.strip()
        elif line.strip() == '':
            pass
        else:
            try:
                # split line by colon, columns before and rest after
                meta, text = line.split(':')
                time_start, time_end, speaker = meta.split(' ')
                output_line = '{},{},{},{},"{}","{}","{}","{}"\n'.format(file_id, time_start, time_end, speaker, text.strip(), text.strip(), text.strip(), text.strip())
            except ValueError as v:
                print(">>> {}\n>>> Please check: {}\n".format(str(v), meta))
                output_line = '{},{},"{}","{}","{}","{}"\n'.format(file_id, meta, text.strip(), text.strip(), text.strip(), text.strip())
                
            csvfile.write(output_line)

csvfile.close()
