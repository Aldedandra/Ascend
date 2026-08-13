"""Module 2, Lesson 1: Linux & the DevOps Engineer."""

LESSON = {'id': '2-1',
 'title': 'Linux & the DevOps Engineer',
 'summary': 'Build a practical mental model of a Linux system: kernel, distribution, shell, terminal, '
            'filesystem, processes, services, and logs. Connect those pieces to the cloud, containers, '
            'CI/CD, and everyday DevOps troubleshooting.',
 'duration_minutes': 55,
 'xp': 60,
 'audio_script': 'Welcome to Module 2 of Ascend: Linux and the Command Line.\n'
                 '\n'
                 'In Module 0, you learned to approach systems with evidence before action. In Module 1, Git '
                 'gave you a structured way to preserve evidence about change. Now we are going to learn the '
                 'operating environment where a huge amount of DevOps work actually happens.\n'
                 '\n'
                 'Linux.\n'
                 '\n'
                 'The goal of this module is not to turn you into someone who can recite hundreds of '
                 'commands from memory. The goal is to make Linux feel understandable. When you connect to '
                 'an unfamiliar server, enter a container, inspect a CI runner, or troubleshoot a service, '
                 'you should be able to orient yourself, gather evidence, make a controlled change, and '
                 'verify the result.\n'
                 '\n'
                 'Start with an important distinction. Linux technically refers to the kernel.\n'
                 '\n'
                 'The kernel is the core software layer that manages resources such as CPU time, memory, '
                 'storage devices, networking, and processes. Applications do not normally manipulate '
                 'hardware directly. They request services from the operating system, and the kernel '
                 'coordinates access to the underlying resources.\n'
                 '\n'
                 'But when people say, quote, a Linux server, end quote, they usually mean a complete '
                 'operating system built around the Linux kernel.\n'
                 '\n'
                 'That complete system is commonly delivered as a Linux distribution, or distro.\n'
                 '\n'
                 'Ubuntu, Debian, Red Hat Enterprise Linux, Rocky Linux, AlmaLinux, Amazon Linux, and Alpine '
                 'Linux are all examples of distributions. A distribution combines the Linux kernel with '
                 'system utilities, libraries, package-management tools, a shell, configuration conventions, '
                 'and other software needed to make the system usable.\n'
                 '\n'
                 'You do not need to memorize every distribution. The fundamentals transfer. Files are still '
                 'files. Processes still have process identifiers. Users and groups still matter. '
                 'Permissions still control access. Services still need to start, stop, and report status. '
                 'Logs still provide evidence. The exact commands or package manager may differ, but the '
                 'mental model remains useful.\n'
                 '\n'
                 'Next, separate the terminal from the shell.\n'
                 '\n'
                 'A terminal is the interface where you type commands and see output. On your Mac, Terminal '
                 'dot app is a terminal application. A shell is the program interpreting the commands you '
                 'type. Bash, Z shell, and Fish are examples of shells.\n'
                 '\n'
                 'Think of the flow as you, then terminal, then shell, then operating system.\n'
                 '\n'
                 'If you type pwd, the shell interprets the command. The system runs the appropriate '
                 'operation. The result is printed back through the terminal.\n'
                 '\n'
                 'This distinction matters because you may use a different terminal application without '
                 'changing your shell, or change shells without changing the operating system.\n'
                 '\n'
                 'Now consider the filesystem.\n'
                 '\n'
                 'Linux organizes files and directories in one hierarchy beginning at forward slash, called '
                 'the root directory. Under root are directories with conventional purposes. Slash etc '
                 'commonly contains configuration. Slash home contains user home directories. Slash var '
                 'contains changing data such as logs. Slash tmp is used for temporary files. Slash usr '
                 'contains many installed programs and shared resources. Slash opt is often used for '
                 'optional application software.\n'
                 '\n'
                 'You do not need to memorize the entire filesystem hierarchy today. In the next lesson, you '
                 'will learn how to navigate it deliberately. For now, remember that configuration, '
                 'application data, executables, logs, and user files have locations, and finding the right '
                 'location is often the beginning of troubleshooting.\n'
                 '\n'
                 'Running programs become processes.\n'
                 '\n'
                 'Linux gives each process a process identifier, or PID. A server may have processes for '
                 'SSH, a web server, a database, a Python application, monitoring agents, and many other '
                 'tasks at the same time.\n'
                 '\n'
                 'A process consumes resources. It can use CPU, memory, open files, and network connections. '
                 'When someone says, quote, the server is slow, end quote, you should immediately hear a '
                 'question rather than a diagnosis. Which process is consuming resources? Is memory '
                 'exhausted? Is disk space full? Is the application blocked waiting on something? Evidence '
                 'comes before action.\n'
                 '\n'
                 'Some long-running programs are managed as services.\n'
                 '\n'
                 'On many modern Linux systems, systemd manages services. A command such as systemctl status '
                 'nginx can tell you whether the nginx service is active, inactive, failed, or in another '
                 'state.\n'
                 '\n'
                 'But status is only part of the story.\n'
                 '\n'
                 'If a service failed, you need to know why.\n'
                 '\n'
                 'That is where logs become critical.\n'
                 '\n'
                 'Logs may reveal a permission error, an invalid configuration, a missing file, a failed '
                 'network connection, a full disk, or another cause. On a system using systemd, journalctl '
                 'can show journal entries, including logs associated with a specific service.\n'
                 '\n'
                 'Notice the investigation pattern.\n'
                 '\n'
                 'First, observe the symptom.\n'
                 '\n'
                 'Second, inspect service status.\n'
                 '\n'
                 'Third, inspect logs.\n'
                 '\n'
                 'Fourth, inspect related files, processes, permissions, resources, or network state.\n'
                 '\n'
                 'Fifth, form a hypothesis.\n'
                 '\n'
                 'Sixth, make the smallest reasonable change.\n'
                 '\n'
                 'Seventh, verify that the service and the user-facing system are healthy.\n'
                 '\n'
                 'That is Evidence Before Action expressed through Linux.\n'
                 '\n'
                 'Now connect Linux to DevOps.\n'
                 '\n'
                 'Imagine a cloud virtual machine in AWS. You may launch Ubuntu or Amazon Linux, connect '
                 'with SSH, and receive a command prompt with no graphical desktop. You are expected to '
                 'navigate the filesystem, inspect configuration, view logs, manage services, and understand '
                 'processes through the command line.\n'
                 '\n'
                 'Docker makes Linux knowledge even more useful.\n'
                 '\n'
                 'When you run docker compose exec backend sh, you enter the shell environment inside a '
                 'container. That container may be based on Alpine, Debian, Ubuntu, or another Linux '
                 'userspace. Commands such as ls, cd, cat, env, ps, and grep suddenly become your tools for '
                 'answering questions about what is happening inside the container.\n'
                 '\n'
                 'CI and CD systems often run jobs on Linux runners. Your pipeline script may execute shell '
                 'commands, create files, install packages, read environment variables, and return exit '
                 'codes. If you understand the shell and Linux behavior, pipeline failures become easier to '
                 'interpret.\n'
                 '\n'
                 'Kubernetes adds another layer, but Linux is still underneath much of the system. '
                 'Kubernetes nodes commonly run Linux. Containers execute processes. Filesystems, '
                 'networking, permissions, logs, signals, and resource limits continue to matter.\n'
                 '\n'
                 'This is why Linux belongs early in your Ascend path. It is not a side topic. It is part of '
                 'the vocabulary shared by many later tools.\n'
                 '\n'
                 'There is also a useful shift in how to think about commands.\n'
                 '\n'
                 'Do not treat a command as magic syntax.\n'
                 '\n'
                 'Treat it as a question you are asking the system.\n'
                 '\n'
                 'Who am I? Run whoami.\n'
                 '\n'
                 'What machine is this? Run hostname.\n'
                 '\n'
                 'Where am I in the filesystem? Run pwd.\n'
                 '\n'
                 'What is here? Run ls.\n'
                 '\n'
                 'What shell am I using? Inspect the SHELL environment variable.\n'
                 '\n'
                 'What operating system and kernel information can I see? Run uname dash a.\n'
                 '\n'
                 'What processes can I see? Run ps.\n'
                 '\n'
                 'Each command gives you evidence about one part of the environment.\n'
                 '\n'
                 'On your Mac, many of these commands work because macOS is Unix-like. The output will not '
                 'be identical to Linux, and some command options differ, but your Mac terminal is a useful '
                 'place to practice shell fundamentals before we work inside Linux environments directly.\n'
                 '\n'
                 'You have already touched some of this without calling it Linux training.\n'
                 '\n'
                 'When you have entered a Docker container to inspect files or verify a build, you were '
                 'already operating in a command-line environment. When you used shell commands to inspect '
                 'the Ascend or Forge project, you were already building habits that transfer directly to '
                 'Linux.\n'
                 '\n'
                 'Now we are going to make the mental model explicit.\n'
                 '\n'
                 "For this lesson's lab, you will profile the system you are currently using. You will "
                 'identify your user, hostname, current directory, shell, visible processes, and operating '
                 'system information. The objective is not to produce impressive output. The objective is to '
                 'practice orientation.\n'
                 '\n'
                 'Imagine being dropped into an unfamiliar machine during an incident. Before changing '
                 'anything, you should know where you are, who you are, and what kind of environment you are '
                 'operating in.\n'
                 '\n'
                 'That is the first Linux habit I want you to develop.\n'
                 '\n'
                 'Orient before acting.\n'
                 '\n'
                 'Here is the takeaway for Lesson 2.1.\n'
                 '\n'
                 'Linux is more than a list of commands. It is an operating environment made of '
                 'understandable pieces.\n'
                 '\n'
                 'The kernel manages resources. A distribution packages the kernel with a usable operating '
                 'system. The terminal gives you an interface. The shell interprets commands. The filesystem '
                 'organizes data and configuration. Processes represent running programs. Services manage '
                 'persistent functionality. Logs preserve evidence about system behavior.\n'
                 '\n'
                 'DevOps tools do not replace those concepts. They build on them.\n'
                 '\n'
                 'In the next lesson, we will enter the filesystem and learn how to navigate an unfamiliar '
                 'machine confidently using paths, directories, hidden files, and search tools.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain the difference between the Linux kernel and a Linux distribution.',
                'Distinguish a terminal from a shell and describe how commands reach the operating system.',
                'Identify the roles of the filesystem, processes, services, and logs in a Linux system.',
                'Explain why Linux knowledge transfers to cloud servers, Docker containers, CI/CD runners, '
                'and Kubernetes.',
                'Use low-risk commands to orient yourself before changing an unfamiliar system.'],
 'content': [{'heading': 'Linux is the operating environment behind modern infrastructure',
              'body': 'Linux appears throughout DevOps: cloud virtual machines, container hosts, CI/CD '
                      'runners, Kubernetes nodes, web servers, databases, and observability systems. '
                      'Learning Linux gives you a common mental model that transfers across many later '
                      'Ascend modules.'},
             {'heading': 'Linux technically means the kernel',
              'body': 'The Linux kernel is the core layer that manages CPU scheduling, memory, devices, '
                      'filesystems, networking, and processes. In everyday conversation, “Linux” often '
                      'refers to a complete operating system built around that kernel.'},
             {'heading': 'A distribution packages a usable Linux system',
              'body': 'Ubuntu, Debian, RHEL, Rocky Linux, Amazon Linux, and Alpine are Linux distributions. '
                      'A distro combines the kernel with utilities, libraries, package management, '
                      'configuration conventions, shells, and other software. Fundamentals transfer even '
                      'when tooling differs.'},
             {'heading': 'Terminal and shell are different layers',
              'body': 'The terminal is the interface where you type and view output. The shell interprets '
                      'your commands. Bash and zsh are shells. You can change terminal applications without '
                      'changing shells, and you can change shells without changing the operating system.'},
             {'heading': 'The filesystem gives the system structure',
              'body': 'Linux uses one directory hierarchy beginning at /. Common locations include /etc for '
                      'configuration, /home for user home directories, /var for changing system data such as '
                      'logs, /tmp for temporary files, /usr for many programs and shared resources, and /opt '
                      'for optional software.'},
             {'heading': 'Processes are running programs',
              'body': 'A running program becomes a process with a process identifier, or PID. Processes '
                      'consume resources such as CPU, memory, open files, and network connections. Process '
                      'evidence helps turn vague symptoms such as “the server is slow” into specific '
                      'investigation questions.'},
             {'heading': 'Services provide persistent functionality',
              'body': 'Long-running programs such as web servers, SSH daemons, databases, and application '
                      'backends are often managed as services. On many Linux distributions, systemd and '
                      'systemctl are used to start, stop, restart, enable, and inspect those services.'},
             {'heading': 'Logs turn system behavior into evidence',
              'body': 'A failed service is a symptom. Logs help explain the cause. Linux logs may expose '
                      'invalid configuration, permission errors, authentication failures, missing files, '
                      'full disks, application exceptions, or failed network connections. The journalctl '
                      'command is especially important on systemd-based systems.'},
             {'heading': 'Commands are questions, not magic spells',
              'body': 'whoami asks which user you are. hostname asks which machine you are on. pwd asks '
                      'where you are. ls asks what is present. ps asks about processes. Thinking in '
                      'questions makes the command line easier to reason about and encourages observation '
                      'before action.'},
             {'heading': 'Linux connects directly to Docker and cloud work',
              'body': 'Entering a container with docker compose exec ... sh places you in a Linux-style '
                      'shell environment. Connecting to an AWS Linux VM with SSH does the same at the host '
                      'level. Later CI/CD and Kubernetes work will repeatedly reuse filesystem, process, '
                      'permission, shell, logging, and networking concepts.'}],
 'diagram': {'title': 'A practical Linux mental model',
             'description': 'Think in layers. Each layer answers different troubleshooting questions.',
             'nodes': [{'label': 'You', 'detail': 'Decide what evidence you need and type a command.'},
                       {'label': 'Terminal', 'detail': 'Displays your session, input, and command output.'},
                       {'label': 'Shell',
                        'detail': 'Interprets commands, variables, redirection, and scripts.'},
                       {'label': 'Linux userspace',
                        'detail': 'Utilities, services, libraries, processes, and configuration.'},
                       {'label': 'Kernel',
                        'detail': 'Manages CPU, memory, storage, devices, networking, and process '
                                  'execution.'},
                       {'label': 'Hardware / virtual hardware',
                        'detail': 'The physical or virtual resources underneath the operating system.'}],
             'caption': 'When troubleshooting, identify which layer your evidence describes instead of '
                        'treating the server as one black box.'},
 'engineer_perspective': {'title': 'Orient before you operate',
                          'body': 'During an incident, an unfamiliar prompt can create pressure to act '
                                  'quickly. Strong operators first establish context: which host, which '
                                  'user, which directory, which service, and which environment. A correct '
                                  'command on the wrong host can be more dangerous than no command at all.'},
 'try_it_yourself': {'title': 'Ask your machine six questions',
                     'intro': 'Open Terminal on your Mac. These commands are observational and give you a '
                              'first system profile.',
                     'steps': ['Run whoami. Record the user returned by the system.',
                               'Run hostname. Record the machine name.',
                               'Run pwd. Explain what the returned path represents.',
                               'Run ls. Identify at least three files or directories in the current '
                               'location.',
                               'Run echo $SHELL. Record the shell path and identify the shell name.',
                               'Run uname -a and ps. Do not decode every field yet; identify what kind of '
                               'information each command provides.'],
                     'takeaway': 'Before you change a system, establish who you are, where you are, and what '
                                 'environment you are operating.'},
 'lab': {'title': 'Create a command-line system profile',
         'instructions': ['Create a Journal entry titled “Lesson 2.1 — System Profile.”',
                          'Before running commands, write down what you believe your current username, '
                          'hostname, shell, and starting directory will be. Mark these as assumptions.',
                          'Run whoami, hostname, pwd, and echo $SHELL. Record the exact outputs and compare '
                          'them with your assumptions.',
                          'Run ls and then ls -la. Record at least two differences between the outputs. You '
                          'do not need to understand every permission field yet.',
                          'Run uname -a. Identify the operating system/kernel family information you '
                          'recognize and list anything you do not yet understand.',
                          'Run ps. Choose one visible process and record its PID and command name if shown.',
                          'Write a short paragraph explaining the difference between a terminal and a shell.',
                          'Draw a simple chain: You → Terminal → Shell → Operating System → Hardware. Under '
                          'each item, write one sentence describing its role.',
                          'Write three examples of where Linux is likely to appear in a future DevOps '
                          'workflow.',
                          'Finish with one operational rule: explain why identifying the host and user '
                          'should happen before making changes on an unfamiliar system.']},
 'quiz': [{'question': 'What does Linux technically refer to?',
           'choices': ['The Linux kernel',
                       'The Bash shell',
                       'Any command-line interface',
                       'The Ubuntu package manager'],
           'correct': 0},
          {'question': 'Which item is a Linux distribution?',
           'choices': ['systemd', 'Ubuntu', 'bash', 'SSH'],
           'correct': 1},
          {'question': 'What is the primary role of a shell?',
           'choices': ['Physically store files',
                       'Interpret commands and shell syntax',
                       'Replace the kernel',
                       'Provide cloud billing'],
           'correct': 1},
          {'question': 'Which statement best describes a terminal?',
           'choices': ['It is always the Linux kernel',
                       'It is the interface used to interact with a command-line session',
                       'It is a package manager',
                       'It is a filesystem permission'],
           'correct': 1},
          {'question': 'What is a PID?',
           'choices': ['A Process ID',
                       'A Package Installation Directory',
                       'A Permission Index Definition',
                       'A Private Internet Domain'],
           'correct': 0},
          {'question': 'Which directory commonly contains system configuration?',
           'choices': ['/etc', '/home', '/tmp', '/devops'],
           'correct': 0},
          {'question': 'Why are logs useful when a service fails?',
           'choices': ['They guarantee the service will restart',
                       'They can provide evidence about the cause of the failure',
                       'They replace backups',
                       'They automatically repair configuration'],
           'correct': 1},
          {'question': 'Where might you encounter Linux in DevOps?',
           'choices': ['Cloud VMs only',
                       'Docker containers only',
                       'CI/CD runners only',
                       'Cloud VMs, containers, runners, and Kubernetes nodes'],
           'correct': 3},
          {'question': 'Which command is most directly asking “who am I operating as?”',
           'choices': ['pwd', 'whoami', 'hostname', 'uname -a'],
           'correct': 1},
          {'question': 'What best applies Evidence Before Action to Linux?',
           'choices': ['Restart first and read logs later',
                       'Identify the host, state, and evidence before making a change',
                       'Always become root before investigating',
                       'Delete configuration and recreate it'],
           'correct': 1}],
 'reflection': 'Imagine you SSH into a Linux server during an outage and immediately receive a shell prompt. '
               'Before changing anything, what five pieces of context would you want to establish, and why?'}
