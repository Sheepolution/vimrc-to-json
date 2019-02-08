import os
import re

# Get the path of this file.
path = os.path.dirname(os.path.realpath(__file__)).replace("\\","/") + "/"

file = open(path + ".vimrc", "r", encoding='utf-8')
lines = file.read().split("\n")
file.close()

maptypes = {
	"nmap":"normalModeKeyBindings",
	"vmap":"visualModeKeyBindings",
	"imap":"insertModeKeyBindings",
	"nnoremap":"normalModeKeyBindingsNonRecursive",
	"vnoremap":"visualModeKeyBindingsNonRecursive",
	"inoremap":"insertModeKeyBindingsNonRecursive"
}

maplists = {
	"nmap":[],
	"vmap":[],
	"imap":[],
	"nnoremap":[],
	"vnoremap":[],
	"inoremap":[]
}

new_file = "{\n"

# Get all the mappings and place them in the correct category.
for item in lines:
	matches = re.match("(^.*map)\s([\S]+)\s+([\S]+)$", item)
	if matches:
		maptype = matches.group(1)
		before = matches.group(2)
		after = matches.group(3)
		if maptype in maplists:
			maplists[maptype].append({"before" : before, "after" : after})

# Parses abc to ["a", "b", "c"] and :wq<CR> to [":wq"]
def mapToJSONList(mapstring, command):
	map_json = "["
	if command:
		map_json += '"' + re.match("(:\w+)", mapstring).group(1) + '"]'
		return map_json
	else:
		parts = re.findall("(<[^>]+>|.)", mapstring)
		for part in parts:

			if part == '"':
				part = '\\"'

			map_json += '"' + part + '", '

	# Remove the last ', '
	return map_json[:-2] + "]"

# Turn all the mappings into JSON format
for maptype in maplists:
	maplist = maplists[maptype]

	if len(maplist) > 0:
		new_file += '"vim.' + maptypes[maptype] + '": [\n'

		for item in maplist:
			new_file += '{\n"before": '
			new_file += mapToJSONList(item["before"], False)
			
			# Check if it's a command
			after = item["after"]
			command = False
			if after.startswith(":") and len(after) > 1:
				new_file += ',\n"commands": '
				command = True
			else:
				new_file += ',\n"after": '
			new_file += mapToJSONList(item["after"], command)
			new_file += '\n},\n'

		# Remove the last ',\n'
		new_file = new_file[:-2]
		new_file += "\n],\n"

# Remove the last '],\n'
new_file = new_file[:-2] + "\n}"

# Write the JSON to settings.json in the same directory.
file = open(path + "settings.json", "w")
file.write(new_file)
file.close()