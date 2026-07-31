# 🌌 KryptonDOS

## What is KryptonDOS?

KryptonDOS is a Command Line Interface (CLI) Shell written primarily on Python 3 programing language and the C Plus Plus programming language for its launcher. KryptonDOS is designed to run on top of primarily on POSIX-Compliant Shells and Windows Command Prompt or PowerShell — Certain Functions on Windows NT-Based Systems are not fully supported thus far. Its current purpose is to explore Shell Design and Command Parsing.

The KryptonDOS Project is inspired by Microsoft Disk Operating System (MS-DOS) and the FreeDOS Project. It aims to recreate the classic command-line computing experience while introducing a more organized and intuitive command structure. The project also serves as a platform for exploring cross-platform shell development and modern systems programming concepts.

> #### Tired of Reading?
> Click [here](#how-to-get-started) to get started.

> [!Warning]
> Certain functions and commands have not be implemented yet. It is advisable to use this software at your own risk.

## Technologies used

### Python 3 🐍

Python 3 is the primary programming language used to implement the KryptonDOS shell, its built-in commands, and bundled applications.

### C++ (programming language) ⚙️

C++ is used to develop the KryptonDOS shell launcher. The launcher provides a native executable that improves startup convenience and offers the experience of launching an application rather than executing a Python script directly.

### JavaScript Object Notation (JSON) 🗂️

JSON is used to store system metadata and configuration instead of hardcoding values into the shell. This approach simplifies configuration management and allows command scripts to retrieve system information consistently.

### Batch Scripting and Shell Scripting 📜

Batch scripts and POSIX shell scripts automate the process of compiling the KryptonDOS shell launcher. Batch scripts also serve as a temporary launcher on Windows while native support for Windows NT-based systems is under development.

## How to get started

go to projects and download the installer and run it.
<!-- ### Windows 🪟

- Ensure that **Python 3.13** and the **PsUtil** python library is installed. If it is already not installed, open Command Prompt or PowerShell and run `winget install Python.Python3.13` for Python 3.13 and `pip install psutil` for psutil.
- Execute the `kry.cmd` batch file. Do not move the batch file to a different directory, as it must remain in its original location to function correctly.

> [!NOTE]
> The KryptonDOS `.exe` launcher is not currently supported on Windows NT-based operating systems. Support for these systems is planned and will be available in a future release.

### macOS 🍎

- Ensure that **Xcode Command Line Tools** and **Clang** are installed. Xcode can be installed from the official Mac App Store. To install the Xcode Command Line Tools, run `xcode-select --install` in the Terminal.
- Ensure that **Python 3** and the **psutil** Python library are installed. Python can be downloaded from the official Python website. To install the psutil library, run `pip3 install psutil` in the Terminal.
- Compile `./dos/kry.c` manually using Clang, or execute the automated build script `kry.sh`. Before running the script, ensure it has executable permissions by executing `chmod +x /path/to/kry.sh` in the Terminal.

### Linux🐧

- Ensure that **GCC** or **Clang** is installed. GCC is strongly recommended if you intend to use the automated build script.
- Ensure that **Python 3** and the **psutil** Python library are installed. Python can be installed either through your distribution's package manager or downloaded from the official Python website. To install the psutil library, run `pip3 install psutil` in the Terminal.
- Compile `./dos/kry.c` manually either using Clang or GCC, or execute the automated build script `kry.sh`. Before running the script, ensure it has executable permissions by executing `chmod +x /path/to/kry.sh` in the Terminal. -->

## Known Issues ⚠️

- Certain commands documented in `manual.md` are not yet implemented and may not function as expected.

## Future Development Plans

> [!NOTE]
> The following roadmap represents the planned direction of KryptonDOS. Features, milestones, and release targets are subject to change and are not guaranteed.

### v0.0.3b

- Official support for Windows NT-based operating systems.
- Full implementation of all documented commands.

### Long-Term Goals

- Code Rewritten in C and C++
- Support for Microsoft Disk Operating System (MS-DOS) applications.
- Evolve KryptonDOS from a Python-based command-line shell into a lightweight bare-metal operating system with a native C/Rust kernel.
