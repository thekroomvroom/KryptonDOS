# List of all Executable Commands of KryptonDOS v0.0.1a

# Basic Commands
 - krver - Displays the Version of KryptonDOS and its Distribution
 - clear - Clears the Screen of all Commands and Output (Both 'clear' and 'cls' are interchangeable and share the same purpose)
 - cls - Similar to 'clear', clears the screen of all Commands and Output (Both 'clear' and 'cls' are interchangeable and share the same purpose)
 - dir - Lists Files and Directories in the user's current directory location
 - cd - Changes Directory Location
 - help - Lists available executable commands

# Complex Objective Commands
Groups:
 - sys (Commands for modifying and inspecting system-based values)
 - dir (Commands for modifying and inspecting Directories and Files)
 - cd
 - dsk (Commands for modifying and inspecting External and Internal Storage Devices)

Expandable Commands for 'sys' (e.g., sys.info):
 - ver (Similar to 'krver', Displays the Version of KryptonDOS and its Distribution)
 - info (Displays the Version of KryptonDOS, its Distribution, and Hardware Specifications)
 - shutdown "{desired time}" [s/min/h/d] (Powers Off the Host)
 - restart "{desired time}" [s/min/h/d] (Reboots the Host)
 - help (Lists available executable expandable commands for 'sys')

Expandable Commands for 'dir' (e.g., dir.era):
 - wai (Displays your current directory location)
 - era "{target file/directory}" .{file extension (if it's a file)} (Destroys selected file or directory (Add a '"YES"' to the back of the command to bypass confirmation). e.g., dir.era "Personal Files" OR dir.era "image" .png "YES")
 - new "{desired directory name}" (Creates a new Directory (THIS DOES NOT APPLY TO FILES!!!). e.g., dir.new "Work Documents")
 - fnew "{desired file name}" .{file extension} (Creates a new File in the user's current Directory Location. e.g., dir.fnew "list" .txt)
 - move "{file/directory location}" >> "{desired file/directory location}" (Moves file or directory's location. e.g., dir.move "D:\Recorded Tracks\soundtrack.wav" >> "E:\Uploads\" OR dir.move "D:\Backups\My iPhone\Photos\" << "E:\Captures\IMG_1876.jpg")
 - dupe "{file/directory location}" >> "{desired file/directory location}" (Copies file or directory and pastes it to desired directory location)
 - list *.{file extension} (OR) "{file name}" .{file extension} (Locate specific files. e.g., dir.list *.mp4 OR dir.list "bangle" .cad)
 - nick "{target file/directory}" .{file extension (if it's a file)} >> "desired label" (Renames targeted file or directory. e.g., dir.nick "Documents" >> "Classified Documents" OR dir.nick "video" .mov >> "my blog")
 - info "{target file}" .{file extension} (Displays metadata on the targeted file)
 - help (Lists available executable expandable commands for 'dir')

Expandable Commands for 'cd':
 - .. (Moves back a directory. e.g., cd ?)
 - ? (Similar to 'dir.wai', Displays your current directory location. e.g., cd ?)
 - help (Lists available executable expandable commands for 'cd')

Expandable Commands for 'dsk':
 - list (List all Storage Devices mounted to the Host (add a '"EXTERNAL"' to the back of the command to list only External Storage Devices mounted onto the Host or '"INTERNAL"' to the back of the command to list only Internal Storage Devices mounted onto the Host))
 - eye {target disk number} (Select your targeted Storage Device. e.g., dsk.eye 1)
 - era (Destroys all existing Data, and Partitions to the selected storage device(Add '"YES"' to the back of the command to bypass confirmation). e.g., dsk.era)
 - format {desired format} [quick/full](Formats targeted Storage Device to your desired format)
 - create partition [primary/secondary] == {desired data amount} [tb/gb/mb/kb/b] nick="{Desired nickname (Optional)}"
 - list partition (List all existing partitions on the Selected Storage Device)
 - eye partition {partition number} (Select your target partition)
 - era partition (Destroys all existing Data stored in the Selected Storage Device (Add '"YES"' to the back of the command to bypass confirmation))
 - format partition {desired format} [quick/full] (Formats Selected Partition to Desired Format)
 - partition shrink >> {new data amount} [tb/gb/mb/kb/b] (Shrinks Partition to Desired Amount)
 - partition expand >> {new data amount} [tb/gb/mb/kb/b] (Expands Selected Partition to Desired Amount
 - partition nick >> "{desired name}" (Renames Selected Partition to desired amount)
 - partition merge {second target partition number} (Merges Selected Partition with Second Target Partition)
 - eject (Make Selceted Storage Device Safe to Dismount from Host)
 - nick >> "{desired name}" (Rename Selected Storage Device)
 - help (List available executable expandabe commands for 'dsk')

# Commands for Moving System from Bootable Installation Drive to Internal Drive
 - cuhtransfer - Formats Target Internal Drive and Transfers System from Bootable Installation Drive to Target Internal Drive
