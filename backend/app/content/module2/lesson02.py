"""Module 2, Lesson 2: Navigating the Linux Filesystem."""

LESSON = {'id': '2-2',
 'title': 'Navigating the Linux Filesystem',
 'summary': 'Learn to orient yourself anywhere in a Linux filesystem using paths, pwd, ls, cd, hidden files, '
            'file metadata, and find. Build the habit of proving where you are before acting.',
 'duration_minutes': 60,
 'xp': 65,
 'audio_script': 'Welcome to Lesson 2.2: Navigating the Linux Filesystem.\n'
                 '\n'
                 'In the last lesson, you built a mental model of a Linux system. Now we are going to focus '
                 'on one of its most important structures: the filesystem.\n'
                 '\n'
                 'A Linux filesystem is not just a place where documents live. Application code, '
                 'configuration, logs, credentials, executables, service definitions, temporary files, '
                 'mounted storage, and user data all have locations.\n'
                 '\n'
                 'During troubleshooting, location matters.\n'
                 '\n'
                 'If you edit the wrong configuration file, nothing may happen. If you delete a file in the '
                 'wrong directory, you may damage the system. If you inspect logs from the wrong service or '
                 'environment, you may build a completely incorrect hypothesis.\n'
                 '\n'
                 'So the first filesystem habit is simple.\n'
                 '\n'
                 'Always know where you are.\n'
                 '\n'
                 'The command pwd means print working directory.\n'
                 '\n'
                 'If pwd returns slash home slash bryant, your current working directory is that directory.\n'
                 '\n'
                 'A path tells Linux where something is located.\n'
                 '\n'
                 'There are two major forms you need to understand: absolute paths and relative paths.\n'
                 '\n'
                 'An absolute path begins at the filesystem root, forward slash.\n'
                 '\n'
                 'Slash var slash log slash nginx is absolute. It identifies the same location regardless of '
                 'your current working directory, assuming that path exists.\n'
                 '\n'
                 'A relative path is interpreted from your current working directory.\n'
                 '\n'
                 'If you are currently in slash var and type cd log, the shell resolves log relative to '
                 'slash var and moves you to slash var slash log.\n'
                 '\n'
                 'This distinction sounds simple, but it explains a huge amount of shell behavior.\n'
                 '\n'
                 'The dot character can refer to the current directory.\n'
                 '\n'
                 'Two dots refer to the parent directory.\n'
                 '\n'
                 'If you are in slash home slash bryant slash projects and run cd dot dot, you move to slash '
                 'home slash bryant.\n'
                 '\n'
                 "The tilde character commonly expands to your current user's home directory.\n"
                 '\n'
                 'So cd tilde is a convenient way to return home.\n'
                 '\n'
                 'Next is ls, which lists directory contents.\n'
                 '\n'
                 'Plain ls gives you a quick view.\n'
                 '\n'
                 'But Linux often hides files whose names begin with a dot. Files such as dot bashrc, dot '
                 'profile, dot ssh, and dot env may contain important configuration.\n'
                 '\n'
                 'The dash a option tells ls to include hidden entries.\n'
                 '\n'
                 'The dash l option gives a long listing with metadata.\n'
                 '\n'
                 'Combined, ls dash la is one of the most useful orientation commands you can learn.\n'
                 '\n'
                 'A long listing may show permissions, link count, owner, group, size, modification time, '
                 'and file name.\n'
                 '\n'
                 'You do not need to decode the permissions yet. We will do that in Lesson 2.4. For now, '
                 'notice that ls can provide much more than names.\n'
                 '\n'
                 'Navigation is handled with cd, change directory.\n'
                 '\n'
                 "cd followed by a directory path moves your shell's working directory.\n"
                 '\n'
                 'One strong habit is to combine cd with pwd and ls.\n'
                 '\n'
                 'Move somewhere.\n'
                 '\n'
                 'Prove where you arrived.\n'
                 '\n'
                 'Inspect what is present.\n'
                 '\n'
                 'That pattern sounds almost too simple to matter, but it prevents mistakes.\n'
                 '\n'
                 'Suppose you believe you are in slash etc slash nginx and intend to inspect nginx dot conf. '
                 'If you are actually in a copied project directory under your home folder, the same '
                 'filename could exist there. Reading the wrong file wastes time. Editing the wrong file can '
                 'be worse.\n'
                 '\n'
                 'Do not trust your memory of where the shell is.\n'
                 '\n'
                 'Ask the system.\n'
                 '\n'
                 'Linux also has conventional top-level directories.\n'
                 '\n'
                 'Slash etc commonly stores system and application configuration.\n'
                 '\n'
                 'Slash var stores changing data. Slash var slash log is a common log location.\n'
                 '\n'
                 "Slash home contains regular users' home directories.\n"
                 '\n'
                 "Slash root is normally the root user's home directory. It is not the same thing as forward "
                 'slash, the root of the filesystem.\n'
                 '\n'
                 'Slash tmp is used for temporary data and may be cleaned automatically.\n'
                 '\n'
                 'Slash usr contains many user-space programs, libraries, and shared resources.\n'
                 '\n'
                 'Slash bin and slash sbin historically contain important commands, although modern '
                 'distributions may link these into slash usr.\n'
                 '\n'
                 'Slash opt is often used for optional or third-party application software.\n'
                 '\n'
                 'Slash proc is unusual. It is a virtual filesystem exposing information about processes and '
                 'the kernel. Many entries are generated dynamically rather than stored like normal disk '
                 'files.\n'
                 '\n'
                 'Slash dev exposes device files.\n'
                 '\n'
                 'You do not need to memorize a filesystem standard. What matters is knowing enough '
                 'conventions to make good first guesses, then verifying those guesses with the system.\n'
                 '\n'
                 "Now let's talk about file names and spaces.\n"
                 '\n'
                 'The shell separates arguments on whitespace unless you quote or escape it.\n'
                 '\n'
                 'A directory named Project Files cannot always be referenced by typing cd Project Files, '
                 'because the shell may interpret that as two separate arguments.\n'
                 '\n'
                 'You could write cd quote Project Files quote, or escape the space.\n'
                 '\n'
                 'Quoting becomes increasingly important as we work with scripts and variables later.\n'
                 '\n'
                 'Tab completion is another essential habit.\n'
                 '\n'
                 'Instead of typing long file and directory names from memory, type part of the name and '
                 'press Tab. The shell can often complete it or show possible matches.\n'
                 '\n'
                 'This improves speed, but more importantly, it reduces typing errors.\n'
                 '\n'
                 'Linux paths are also case-sensitive on typical Linux filesystems.\n'
                 '\n'
                 'File dot TXT, file dot txt, and FILE dot txt may be three different names.\n'
                 '\n'
                 'That can surprise people coming from environments where filename case is less strict.\n'
                 '\n'
                 'Now imagine that you know a file exists somewhere, but you do not know where.\n'
                 '\n'
                 'This is where find becomes useful.\n'
                 '\n'
                 'A command such as find slash etc dash name quote nginx dot conf quote asks the system to '
                 'search under slash etc for a matching name.\n'
                 '\n'
                 'You can also search your current directory with find dot.\n'
                 '\n'
                 'Find can become extremely powerful, but start with a simple model: search beneath a path '
                 'using criteria.\n'
                 '\n'
                 'Be aware that searching large parts of the filesystem may produce permission denied '
                 'messages when your user cannot inspect certain directories. Those messages are evidence '
                 'about your access level, not necessarily a sign that find itself failed.\n'
                 '\n'
                 'Another useful command is file.\n'
                 '\n'
                 'The file command examines content or metadata clues and reports what kind of file '
                 'something appears to be. A filename extension is only part of the story on Linux. A file '
                 'can be executable without ending in dot exe, and configuration files may have no extension '
                 'at all.\n'
                 '\n'
                 'There is also realpath on many Linux systems, which resolves a path into an absolute '
                 'canonical path. You will not need it constantly, but it reinforces the idea that relative '
                 'references can be resolved into a specific location.\n'
                 '\n'
                 'Symlinks, or symbolic links, are another filesystem concept you will encounter.\n'
                 '\n'
                 'A symlink is a filesystem entry that points to another path. It behaves somewhat like a '
                 'reference or shortcut. Commands and configuration may use symlinks to expose one path '
                 'while the real data exists elsewhere.\n'
                 '\n'
                 'When a path seems confusing, ls dash l can reveal a link and show its target.\n'
                 '\n'
                 'Mounts add another layer. Linux can attach filesystems at directories within the '
                 'hierarchy. A separate disk, network filesystem, or container volume may appear as an '
                 'ordinary directory even though its storage comes from somewhere else.\n'
                 '\n'
                 'This is why the Linux filesystem is best understood as one navigable tree, not a '
                 'collection of drive letters.\n'
                 '\n'
                 'Now connect this to DevOps.\n'
                 '\n'
                 'A web application might live under slash opt slash ascend.\n'
                 '\n'
                 'Its environment file might live under slash etc slash ascend.\n'
                 '\n'
                 'Its logs might appear in slash var slash log slash ascend or in the systemd journal.\n'
                 '\n'
                 'Uploaded data might live on a mounted volume.\n'
                 '\n'
                 'A container may use slash app as its working directory.\n'
                 '\n'
                 'A CI job may start in a checked-out repository path created by the runner.\n'
                 '\n'
                 'The paths differ, but your investigation behavior remains the same.\n'
                 '\n'
                 'pwd.\n'
                 '\n'
                 'ls dash la.\n'
                 '\n'
                 'inspect the path.\n'
                 '\n'
                 'move deliberately.\n'
                 '\n'
                 'verify.\n'
                 '\n'
                 'One final safety idea.\n'
                 '\n'
                 'Many Linux commands interpret relative paths based on your current directory. Destructive '
                 'commands do too.\n'
                 '\n'
                 'A command such as rm dash r is not something we need for this lesson, but understand the '
                 'principle: if an operation removes or overwrites files, being wrong about your current '
                 'directory can be catastrophic.\n'
                 '\n'
                 'That is why navigation is operational safety, not beginner trivia.\n'
                 '\n'
                 "For this lesson's lab, you are going to create a small practice filesystem under your home "
                 'directory. You will move through it using both absolute and relative paths, inspect hidden '
                 'files, use parent-directory references, and search for a specific file.\n'
                 '\n'
                 'You will not need sudo. You will not modify system directories.\n'
                 '\n'
                 'The goal is to become comfortable moving through a filesystem while continuously proving '
                 'your location.\n'
                 '\n'
                 'Here is the takeaway.\n'
                 '\n'
                 'A path is evidence.\n'
                 '\n'
                 'pwd tells you where your shell is.\n'
                 '\n'
                 'ls tells you what is there.\n'
                 '\n'
                 'cd moves you deliberately.\n'
                 '\n'
                 'Absolute and relative paths describe location from different reference points.\n'
                 '\n'
                 'Hidden files, symlinks, mounts, and conventional directories all become easier to '
                 'understand when you stop treating the filesystem as a mystery and start asking precise '
                 'location questions.\n'
                 '\n'
                 'In the next lesson, we will stay in the shell but shift from navigation to working with '
                 'file content: reading text, searching it, combining commands with pipes, and redirecting '
                 'output.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Distinguish absolute paths from relative paths and predict how the shell resolves each.',
                'Use pwd, ls, ls -la, and cd to navigate an unfamiliar filesystem safely.',
                'Explain the purpose of common Linux directories such as /etc, /home, /var, /tmp, /usr, and '
                '/opt.',
                'Recognize hidden files, symbolic links, case sensitivity, and home/parent-directory '
                'shorthand.',
                'Use find to locate files without relying on a graphical file browser.'],
 'content': [{'heading': 'Your working directory is operational context',
              'body': 'pwd prints the current working directory. Because many commands interpret relative '
                      'paths from that location, proving where you are before reading, editing, copying, or '
                      'removing files is a safety habit.'},
             {'heading': 'Absolute paths start at /',
              'body': 'An absolute path identifies a location beginning at the filesystem root, such as '
                      '/var/log/nginx. Its meaning does not depend on your current working directory.'},
             {'heading': 'Relative paths start from where you are',
              'body': 'A relative path is resolved from the current working directory. If you are in /var '
                      'and run cd log, the shell moves to /var/log. Use . for the current directory, .. for '
                      "the parent, and ~ for the current user's home directory."},
             {'heading': 'ls is more than a filename list',
              'body': 'ls provides a quick view. ls -a includes hidden dotfiles. ls -l provides metadata '
                      'such as permissions, ownership, size, and timestamps. ls -la combines both views and '
                      'is a strong orientation command.'},
             {'heading': 'Linux paths are normally case-sensitive',
              'body': 'On typical Linux filesystems, App.conf and app.conf can be different files. Treat '
                      'exact spelling and capitalization as part of the path.'},
             {'heading': 'Common directories give you useful first guesses',
              'body': '/etc commonly contains configuration, /home user directories, /var changing data such '
                      'as logs, /tmp temporary files, /usr many programs and shared resources, /opt optional '
                      'software, /proc kernel/process information, and /dev device files. Verify rather than '
                      'assuming.'},
             {'heading': 'Hidden files often matter',
              'body': 'Names beginning with a dot are normally hidden from plain ls output. Shell '
                      'configuration, SSH configuration, environment files, and application metadata are '
                      'frequently stored in dotfiles or dot-directories.'},
             {'heading': 'Symbolic links point somewhere else',
              'body': 'A symlink is a filesystem entry referring to another path. ls -l can reveal the '
                      'relationship. Symlinks help explain why an apparent path may lead to content stored '
                      'elsewhere.'},
             {'heading': 'find searches beneath a path',
              'body': 'find starts from a location and evaluates entries beneath it. For example, find . '
                      "-name '*.log' searches below the current directory for matching names. "
                      'Permission-denied output may simply mean your current user cannot inspect part of the '
                      'tree.'},
             {'heading': 'Tab completion improves both speed and accuracy',
              'body': 'Type part of a path and press Tab to ask the shell to complete it when possible. '
                      'Completion reduces typo-driven failures and helps you discover valid names without '
                      'memorizing them.'}],
 'diagram': {'title': 'One filesystem tree',
             'description': 'Linux organizes locations beneath a single root instead of presenting separate '
                            'drive letters.',
             'nodes': [{'label': '/', 'detail': 'Root of the filesystem hierarchy.'},
                       {'label': '/etc', 'detail': 'Common home for system and application configuration.'},
                       {'label': '/home', 'detail': 'Home directories for regular users.'},
                       {'label': '/var', 'detail': 'Changing system/application data, often including logs.'},
                       {'label': '/usr',
                        'detail': 'Many installed programs, libraries, and shared resources.'},
                       {'label': '/opt',
                        'detail': 'Common location for optional or third-party application software.'}],
             'caption': 'Directory conventions are clues, not guarantees. Use them to form a hypothesis, '
                        'then inspect the actual system.'},
 'engineer_perspective': {'title': 'The wrong directory can make a correct command dangerous',
                          'body': 'Filesystem mistakes are often context mistakes. A relative command may be '
                                  'perfectly valid yet operate on the wrong files because the engineer '
                                  'assumed the current directory. pwd and ls are cheap evidence. Use them '
                                  'generously before consequential operations.'},
 'try_it_yourself': {'title': 'Navigate without Finder',
                     'intro': 'Work from Terminal and deliberately alternate between absolute and relative '
                              'paths.',
                     'steps': ['Run cd ~ and then pwd. Confirm you are in your home directory.',
                               'Run ls and then ls -la. Identify at least one hidden entry that plain ls did '
                               'not show.',
                               'If ~/Projects exists, run cd ~/Projects and confirm the location with pwd.',
                               'Move into the Ascend directory using a relative path. Run pwd again.',
                               'Run cd .. and explain where you expect to land before checking with pwd.',
                               "Use find ~/Projects/Ascend -name 'modules.py' to locate the Ascend module "
                               'catalog.'],
                     'takeaway': 'Navigation should be a cycle: move, prove location, inspect.'},
 'lab': {'title': 'Build and investigate a practice filesystem',
         'instructions': ['Create a Journal entry titled “Lesson 2.2 — Filesystem Investigation.”',
                          'From your home directory, create a safe practice tree with: mkdir -p '
                          '~/ascend-linux-lab/config ~/ascend-linux-lab/logs/archive ~/ascend-linux-lab/app.',
                          'Run cd ~/ascend-linux-lab and pwd. Record the absolute path.',
                          'Run ls and ls -la. Compare the outputs.',
                          'Create a hidden file with touch .lesson2-hidden and a normal file with touch '
                          'config/ascend.conf. Run ls and ls -la again and record what changed.',
                          'Move to logs/archive using a relative path. Then use cd ../.. to return to the '
                          'lab root. Predict each destination before running pwd.',
                          "From the lab root, run find . -name 'ascend.conf'. Record the returned relative "
                          'path.',
                          "Run find ~/ascend-linux-lab -name 'ascend.conf'. Explain how the result differs "
                          'from the previous command and why.',
                          'Run ls -ld config logs app. Explain the difference between listing a directory '
                          'itself with -d and listing its contents.',
                          'Finish by drawing the practice directory tree and labeling one absolute path and '
                          'two relative paths that refer to locations inside it.']},
 'quiz': [{'question': 'What does pwd show?',
           'choices': ['The current working directory',
                       'All running processes',
                       'Your password',
                       'The Linux distribution only'],
           'correct': 0},
          {'question': 'Which path is absolute?',
           'choices': ['logs/app.log', '../logs', '/var/log/app.log', './config'],
           'correct': 2},
          {'question': 'What does .. normally refer to in a path?',
           'choices': ['The root directory', 'The parent directory', 'The home directory', 'A hidden file'],
           'correct': 1},
          {'question': 'What does ~ commonly represent in the shell?',
           'choices': ["The current user's home directory",
                       'The kernel',
                       'The previous command',
                       'The system log directory'],
           'correct': 0},
          {'question': 'Why use ls -a?',
           'choices': ['To include hidden dotfiles',
                       'To start all services',
                       'To show only directories',
                       'To change ownership'],
           'correct': 0},
          {'question': 'Which directory commonly contains configuration?',
           'choices': ['/etc', '/tmp', '/proc', '/home only'],
           'correct': 0},
          {'question': 'What is a symbolic link?',
           'choices': ['A path reference to another filesystem location',
                       'A process identifier',
                       'A type of Linux user',
                       'A network port'],
           'correct': 0},
          {'question': 'Why can filename capitalization matter on Linux?',
           'choices': ['Linux normally treats paths as case-sensitive',
                       'The shell converts every name to uppercase',
                       'Only root can use lowercase names',
                       'It matters only inside Docker'],
           'correct': 0},
          {'question': 'What is the basic purpose of find?',
           'choices': ['Search beneath a path using criteria',
                       'Edit file permissions',
                       'Restart the kernel',
                       'Display network routes only'],
           'correct': 0},
          {'question': 'What is the safest habit before running a path-sensitive destructive command?',
           'choices': ['Assume your shell is still in the same directory',
                       'Run pwd and inspect the target location',
                       'Become root first',
                       'Disable hidden files'],
           'correct': 1}],
 'reflection': 'Why can filesystem navigation be considered an operational safety skill rather than merely a '
               'beginner command-line skill? Give one example where being wrong about your current directory '
               'could mislead or harm an investigation.'}
