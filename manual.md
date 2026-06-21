# List of all Executable Commands of KryptonDOS v0.0.1a

## Basic Commands ⚙️
 - clear - Clears the Screen of all Commands and Output (Both 'clear' and 'cls' are interchangeable and share the same purpose)
 - cls - Similar to 'clear', clears the screen of all Commands and Output (Both 'clear' and 'cls' are interchangeable and share the same purpose)
 - dir - Lists Files and Directories in the user's current directory location
 - cd - Changes Directory Location
 - help - Lists available executable commands
 - time - displays time
 - logout - signs out of the current logged-in user

## Complex Objective Commands ⚙ 
### Groups:
 - sys (Commands for modifying and inspecting system-based values)
 - dir (Commands for modifying and inspecting Directories and Files)
 - cd
 - dsk (Commands for modifying and inspecting External and Internal Storage Devices)
 - time (Commands for time-related actions)
 - usr (Commands for user related actions)

#### **Expandable Commands for 'sys' (e.g., sys.info)**:
 - abt (Similar to 'krver', Displays the Version of KryptonDOS and its Distribution)
 - shutdown "{desired time}" [s/min/h/d] (Powers Off the Host)
 - restart "{desired time}" [s/min/h/d] (Reboots the Host)
 - help (Lists available executable expandable commands for 'sys')
 - newusr (creates a new user)
 - yap (like echoes)

#### **Expandable Commands for 'dir' (e.g., dir.era)**:
 - wai (Displays your current directory location)
 - era "{target file/directory}" (Destroys selected file or directory)
 - new "{desired directory name}" (Creates a new Directory (THIS DOES NOT APPLY TO FILES!!!)(Add "HIDDEN" to the back of the command to make the directory a Hidden Directory). e.g., dir.new "Work Documents")
 - fnew "{desired file name}" .{file extension} (Creates a new File in the user's current Directory Location (Add "HIDDEN" to the back of the command to make the file a Hidden File). e.g., dir.fnew "list" .txt)
 - move "{file/directory location}" >> "{desired file/directory location}" (Moves file or directory's location. e.g., dir.move "D:\Recorded Tracks\soundtrack.wav" >> "E:\Uploads\" OR dir.move "D:\Backups\My iPhone\Photos\" << "E:\Captures\IMG_1876.jpg")
 - dupe "{file/directory location}" >> "{desired file/directory location}" (Copies file or directory and pastes it to desired directory location)
 - list *.{file extension} (OR) "{file name}" .{file extension} (Locate specific files. e.g., dir.list *.mp4 OR dir.list "bangle" .cad)
 - "HIDDEN" (Lists all Files and Directories that are Hidden. e.g., dir "HIDDEN")
 - nick "{target file/directory}" .{file extension (if it's a file)} >> "desired label" (Renames targeted file or directory. e.g., dir.nick "Documents" >> "Classified Documents" OR dir.nick "video" .mov >> "my blog")
 - info "{target file}" .{file extension} (Displays metadata on the targeted file)
 - hide "{target file/directory}" .{file extension (if target is a file)}(Makes selected file/directory a Hidden File/Directory. e.g., dir.hide "README" .md OR dir.hide "D:\Hiddens")
 - help (Lists available executable expandable commands for 'dir')

#### **Expandable Commands for 'cd'**:
 - .. (Moves back a directory, e.g., cd ..)

#### **Expandable Commands for 'dsk'**:
 - list (List all Storage Devices mounted to the Host (add a '"EXTERNAL"' to the back of the command to list only External Storage Devices mounted onto the Host or '"INTERNAL"' to the back of the command to list only Internal Storage Devices mounted onto the Host))
 - eye {target disk number} (Select your targeted Storage Device, e.g., dsk.eye 1)
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
 - eject (Make Selected Storage Device Safe to Dismount from Host)
 - nick >> "{desired name}" (Rename Selected Storage Device)
 - help (List available executable expandable commands for 'dsk')

#### **Expandable Commands for 'time'**:
 - format24 (Display time in 24 hours)
 - format12 (Display time in 12 hours)
 - change timezone (changes timezone)
 - change format mm = 1 dd = 2 yyyy = 3 (Changes date format, e.g., you want to change date format into YYYY/MM/DD, use it like `time.change format mm = 2, dd = 3, yyyy = 1`)
