"""Module 2, Lesson 5: Processes, Jobs & System Resources."""

LESSON = {'id': '2-5',
 'title': 'Processes, Jobs & System Resources',
 'summary': 'Investigate what is running and what resources it consumes. Learn PIDs, ps, top, jobs, signals, '
            'CPU, memory, disk, and a disciplined approach to the vague report: “the server is slow.”',
 'duration_minutes': 65,
 'xp': 70,
 'audio_script': 'Welcome to Lesson 2.5: Processes, Jobs, and System Resources.\n'
                 '\n'
                 'A user reports, quote, the server is slow.\n'
                 '\n'
                 'What do you do?\n'
                 '\n'
                 'Not restart it.\n'
                 '\n'
                 'Not kill the first process with a high number next to it.\n'
                 '\n'
                 'You turn the symptom into questions.\n'
                 '\n'
                 'What is running? Which processes are consuming CPU or memory? Is the machine short on '
                 'memory? Is disk space exhausted? Is the problem system-wide or isolated to one '
                 'application? Did something change recently?\n'
                 '\n'
                 'Linux gives you evidence for each question.\n'
                 '\n'
                 'Start with processes.\n'
                 '\n'
                 'A process is an executing instance of a program. Linux assigns each process a PID, or '
                 'process identifier. Processes also have a parent process identifier, or PPID, an owner, a '
                 'state, resource usage, and a command.\n'
                 '\n'
                 'One program can create many processes. A web server may have a master process plus '
                 'workers. A Python application may spawn child processes. A shell launches processes for '
                 'commands you run.\n'
                 '\n'
                 'The ps command takes a snapshot of process information.\n'
                 '\n'
                 'Plain ps usually shows processes associated with your current terminal session.\n'
                 '\n'
                 'ps aux is a common broader view on Linux and many Unix-like systems. It can show user, '
                 'PID, CPU percentage, memory percentage, and command information.\n'
                 '\n'
                 'ps dash ef is another common full-format view.\n'
                 '\n'
                 'Exact columns and options vary somewhat across Unix implementations, so focus on the '
                 'questions the tool can answer.\n'
                 '\n'
                 'Which process is this?\n'
                 '\n'
                 'Who owns it?\n'
                 '\n'
                 'How much CPU or memory is it using?\n'
                 '\n'
                 'What command started it?\n'
                 '\n'
                 'What is its parent?\n'
                 '\n'
                 'For a live view, top continuously refreshes process and system information. On many '
                 'systems you may also encounter htop, an interactive alternative that is often easier to '
                 'read, but it may not be installed.\n'
                 '\n'
                 'A high CPU process is not automatically broken.\n'
                 '\n'
                 'If a build is compiling code, high CPU may be expected. If a database is handling a large '
                 'query, usage may spike. Context matters.\n'
                 '\n'
                 'Similarly, a large memory number is not automatically a leak. Linux deliberately uses '
                 'memory for caches. You need to understand whether the system is actually under memory '
                 'pressure.\n'
                 '\n'
                 'The free dash h command on Linux summarizes memory in human-readable units. Pay attention '
                 'to available memory rather than assuming every used byte is unavailable.\n'
                 '\n'
                 'Your Mac has different memory tools, so some of this lab is best practiced in a Linux '
                 'container or VM when available.\n'
                 '\n'
                 'Now disk.\n'
                 '\n'
                 'df dash h reports filesystem space usage in human-readable units.\n'
                 '\n'
                 'If the root filesystem is one hundred percent full, services may fail to write logs, '
                 'databases may stop accepting writes, package operations may fail, and applications can '
                 'behave unpredictably.\n'
                 '\n'
                 'du estimates space used by files and directories. df asks about filesystem capacity. du '
                 'helps answer where file space is being consumed.\n'
                 '\n'
                 'Those are related but different questions.\n'
                 '\n'
                 'Disk inodes can also be exhausted even when byte capacity remains. df dash i can report '
                 'inode usage on many Linux systems. You do not need to become a filesystem expert today, '
                 'but know that, quote, disk full, end quote, can mean more than bytes.\n'
                 '\n'
                 'Now return to process control.\n'
                 '\n'
                 'Your shell can run jobs in the foreground or background.\n'
                 '\n'
                 'A foreground command occupies the terminal until it finishes, stops, or is interrupted.\n'
                 '\n'
                 'Appending an ampersand can start a command as a background job in many shells.\n'
                 '\n'
                 'jobs lists jobs managed by the current shell.\n'
                 '\n'
                 'fg brings a job to the foreground.\n'
                 '\n'
                 'bg resumes a stopped job in the background.\n'
                 '\n'
                 "These shell jobs are not the same thing as all system processes. They are the shell's view "
                 'of commands associated with your session.\n'
                 '\n'
                 'You can often interrupt a foreground command with Control C.\n'
                 '\n'
                 'What actually happens is a signal.\n'
                 '\n'
                 'Signals are a mechanism for notifying processes of events.\n'
                 '\n'
                 'SIGTERM asks a process to terminate gracefully. It gives the application an opportunity to '
                 'clean up.\n'
                 '\n'
                 'SIGKILL forces termination at the kernel level. The process cannot catch or ignore it.\n'
                 '\n'
                 'That distinction matters.\n'
                 '\n'
                 'kill PID normally sends SIGTERM by default.\n'
                 '\n'
                 'kill dash nine PID sends SIGKILL.\n'
                 '\n'
                 'Do not jump directly to kill dash nine because a process is inconvenient. A forceful kill '
                 'can prevent cleanup, interrupt writes, or hide evidence.\n'
                 '\n'
                 'Try graceful termination first when appropriate. Escalate only when the process will not '
                 'respond and you understand the consequences.\n'
                 '\n'
                 'Signals also include SIGHUP, SIGINT, SIGSTOP, SIGCONT, and others. You will learn them as '
                 'needed. The core lesson is that, quote, kill, end quote, is really a signal-sending tool.\n'
                 '\n'
                 'Now think about process state.\n'
                 '\n'
                 'Processes can be running, sleeping, stopped, waiting, or zombie, among other states.\n'
                 '\n'
                 'A sleeping process is not necessarily unhealthy. Most services spend plenty of time '
                 'waiting for work.\n'
                 '\n'
                 'A zombie is a process that has finished execution but whose parent has not yet collected '
                 'its exit status. One zombie is not necessarily a crisis, but persistent growth can '
                 'indicate a parent-process problem.\n'
                 '\n'
                 'Again, interpret evidence in context.\n'
                 '\n'
                 'What about load average?\n'
                 '\n'
                 'Commands such as uptime and top can show load averages over approximately one, five, and '
                 'fifteen minutes.\n'
                 '\n'
                 'Load is not simply CPU percentage. On Linux it represents runnable tasks and tasks in '
                 'certain uninterruptible waits. The number becomes meaningful relative to the machine and '
                 'workload.\n'
                 '\n'
                 'A load of four on a system with many CPU cores may be fine. A sustained load of four on a '
                 'single-core machine deserves investigation.\n'
                 '\n'
                 'Do not memorize a universal, quote, bad load number.\n'
                 '\n'
                 'Correlate.\n'
                 '\n'
                 'CPU evidence.\n'
                 '\n'
                 'Memory evidence.\n'
                 '\n'
                 'Disk evidence.\n'
                 '\n'
                 'Process evidence.\n'
                 '\n'
                 'Application logs.\n'
                 '\n'
                 'Recent changes.\n'
                 '\n'
                 "Now imagine Ascend's API appears slow.\n"
                 '\n'
                 'You check service status and it is active.\n'
                 '\n'
                 'You inspect processes and see the API process.\n'
                 '\n'
                 'CPU is normal.\n'
                 '\n'
                 'Memory is not exhausted.\n'
                 '\n'
                 'Then df dash h shows the filesystem containing the database volume is nearly full.\n'
                 '\n'
                 'That changes your hypothesis.\n'
                 '\n'
                 'Or perhaps disk is fine, but one process is consuming a full CPU core after a deployment.\n'
                 '\n'
                 'Now you inspect that process, logs, and recent change history.\n'
                 '\n'
                 'This is systems thinking. A symptom at the application layer can originate from a resource '
                 'below it.\n'
                 '\n'
                 'There is also process priority, represented by nice values. Linux can influence CPU '
                 'scheduling priority with nice and renice. Lower nice values generally mean higher '
                 'scheduling priority. We will not manipulate production priority in this lesson; simply '
                 'recognize the concept when you see NI in process tools.\n'
                 '\n'
                 'For the lab, you will create a harmless background sleep process, find its PID, inspect '
                 'it, view shell jobs, and terminate it gracefully. You will also collect system-resource '
                 'evidence.\n'
                 '\n'
                 'Do not kill processes you did not start for the lab.\n'
                 '\n'
                 'That is an important operational rule.\n'
                 '\n'
                 'Here is the takeaway.\n'
                 '\n'
                 'Processes are running programs with identity and resource state.\n'
                 '\n'
                 'ps gives you a snapshot.\n'
                 '\n'
                 'top gives you a live view.\n'
                 '\n'
                 'jobs describes work associated with your shell.\n'
                 '\n'
                 'Signals let you communicate with processes.\n'
                 '\n'
                 'SIGTERM is a graceful request. SIGKILL is forceful.\n'
                 '\n'
                 'free helps inspect memory on Linux.\n'
                 '\n'
                 'df asks how full filesystems are.\n'
                 '\n'
                 'du helps locate file usage.\n'
                 '\n'
                 'uptime provides load context.\n'
                 '\n'
                 'And, quote, the server is slow, end quote, is not a diagnosis.\n'
                 '\n'
                 'It is the beginning of an evidence-gathering investigation.\n'
                 '\n'
                 'Next we will combine these skills with services and logs and build a repeatable Linux '
                 'troubleshooting workflow.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain processes, PIDs, parent processes, process ownership, and common process states.',
                'Use ps and top to inspect process identity and resource consumption.',
                'Distinguish shell jobs from system processes and use foreground/background job controls.',
                'Explain signals and choose graceful SIGTERM before forceful SIGKILL when appropriate.',
                'Gather CPU, memory, disk, and load evidence before diagnosing a performance problem.'],
 'content': [{'heading': 'A process is a running program',
              'body': 'Linux assigns each process a PID and tracks attributes such as owner, parent, state, '
                      'command, CPU use, and memory use. One application can consist of multiple related '
                      'processes.'},
             {'heading': 'ps gives you a process snapshot',
              'body': 'ps shows process information at a point in time. Common broader views include ps aux '
                      'and ps -ef. Read the columns as evidence: identity, PID, resource usage, state, and '
                      'command.'},
             {'heading': 'top gives you a live view',
              'body': 'top refreshes system and process information continuously. htop is a friendlier '
                      'optional alternative on many systems. High usage is not automatically a fault; '
                      'correlate it with workload, logs, and system pressure.'},
             {'heading': 'Jobs belong to your shell session',
              'body': "Foreground and background jobs are shell concepts. jobs lists the current shell's "
                      'jobs; fg and bg control them. A shell job is still backed by one or more processes, '
                      'but jobs is not a list of every process on the machine.'},
             {'heading': 'Signals are process communication',
              'body': 'kill sends signals. SIGTERM requests graceful termination and is the normal default. '
                      'SIGKILL forces termination and prevents application cleanup. Escalate deliberately '
                      'rather than reflexively using kill -9.'},
             {'heading': "Memory 'used' does not mean 'unavailable'",
              'body': 'Linux uses spare memory for useful caching. free -h helps distinguish total, used, '
                      'and available memory. Diagnose memory pressure from multiple indicators rather than '
                      'reacting to one large used-memory number.'},
             {'heading': 'df and du answer different disk questions',
              'body': 'df -h reports filesystem capacity and free space. du estimates usage attributable to '
                      'files/directories. Use df to identify a full filesystem and du to investigate where '
                      'space is being consumed.'},
             {'heading': 'Load average needs context',
              'body': 'uptime and top expose load averages over roughly 1, 5, and 15 minutes. Interpret load '
                      'relative to CPU capacity, workload, and waits. There is no universal load number that '
                      'proves a system is unhealthy.'},
             {'heading': 'Process state is evidence, not a verdict',
              'body': 'Processes may be running, sleeping, stopped, waiting, or zombie. Sleeping is normal '
                      'for many services. Persistent zombie growth may point to a parent-process issue, but '
                      'the state must be interpreted in context.'},
             {'heading': 'Performance diagnosis requires correlation',
              'body': 'A slow application can originate in CPU contention, memory pressure, full storage, '
                      'blocking I/O, a dependency, or application behavior. Gather system and application '
                      'evidence before choosing an action.'}],
 'diagram': {'title': 'From vague symptom to resource evidence',
             'description': 'Break “the server is slow” into measurable questions.',
             'nodes': [{'label': 'Symptom',
                        'detail': 'Users report latency, timeouts, or sluggish behavior.'},
                       {'label': 'Processes',
                        'detail': 'Which processes are running and what are they consuming?'},
                       {'label': 'Memory', 'detail': 'Is the system actually under memory pressure?'},
                       {'label': 'Storage',
                        'detail': 'Are filesystems full or is a directory consuming unexpected space?'},
                       {'label': 'Load / CPU',
                        'detail': 'Is runnable work exceeding available capacity or is one process unusually '
                                  'busy?'},
                       {'label': 'Correlate',
                        'detail': 'Compare resource evidence with logs, service state, workload, and recent '
                                  'changes.'}],
             'caption': 'No single number is the diagnosis. Correlation turns metrics into an explanation.'},
 'engineer_perspective': {'title': 'Do not kill what you have not identified',
                          'body': 'Process-control commands can terminate production work instantly. Before '
                                  'sending a signal, verify the PID, owner, command, role, and expected '
                                  'consequence. Prefer a graceful signal when termination is actually '
                                  'necessary, then verify the system afterward.'},
 'try_it_yourself': {'title': 'Create, inspect, and terminate your own process',
                     'intro': 'Only signal the harmless process you create in this exercise.',
                     'steps': ['Run sleep 300 & to create a background job.',
                               'Run jobs and record the shell job number and status.',
                               'Run ps and locate the sleep process. Record its PID.',
                               'Run ps -p PID -o pid,ppid,user,state,command using your actual PID.',
                               'Run kill PID to send the default SIGTERM.',
                               'Run jobs and ps again to verify the process is gone.'],
                     'takeaway': 'Identify first, signal second, verify third.'},
 'lab': {'title': 'Investigate a simulated slow-server report',
         'instructions': ['Create a Journal entry titled “Lesson 2.5 — Resource Investigation.”',
                          'Record the hypothesis “the server is slow” and explain why it is too vague to act '
                          'on.',
                          'Run ps and then a broader process view available on your environment, such as ps '
                          'aux. Identify your shell process and at least two other processes.',
                          'Start sleep 300 &. Use jobs and ps to prove that a shell job and a process are '
                          'two views of the same work.',
                          'Inspect the sleep PID with a targeted ps command. Record PID, PPID, user, state, '
                          'and command where available.',
                          'Run uptime and record the load averages. Do not label them good or bad without '
                          'context; write what additional context you would need.',
                          'On Linux, run free -h and df -h. If you are on macOS, note that free is not a '
                          'standard macOS command and perform the Linux-specific portion later inside a '
                          'Linux container or VM.',
                          "Use du -sh ~/ascend-linux-lab to estimate the practice directory's disk usage. "
                          'Explain how this differs from df.',
                          'Terminate only your sleep process with normal kill, verify it exited, and explain '
                          'why kill -9 was unnecessary.',
                          'Write an investigation order for a slow Ascend API: include process, CPU/load, '
                          'memory, disk, logs, and recent-change evidence before any restart.']},
 'quiz': [{'question': 'What is a PID?',
           'choices': ['A process identifier',
                       'A permission mode',
                       'A filesystem capacity value',
                       'A Linux group'],
           'correct': 0},
          {'question': 'What is the main difference between ps and top?',
           'choices': ['ps is a snapshot; top provides a refreshing live view',
                       'ps changes permissions; top changes owners',
                       'top only works on files',
                       'There is no difference'],
           'correct': 0},
          {'question': 'What does jobs primarily show?',
           'choices': ['Jobs associated with the current shell',
                       'Every process on every server',
                       'Only systemd services',
                       'Disk partitions'],
           'correct': 0},
          {'question': 'What signal does kill PID normally send by default?',
           'choices': ['SIGTERM', 'SIGKILL', 'SIGSTOP only', 'No signal'],
           'correct': 0},
          {'question': 'Why prefer SIGTERM before SIGKILL when appropriate?',
           'choices': ['It gives the process an opportunity to shut down cleanly',
                       'SIGKILL is slower',
                       'SIGTERM always fixes the root cause',
                       'SIGKILL requires no PID'],
           'correct': 0},
          {'question': 'What does df -h primarily help answer?',
           'choices': ['How full are mounted filesystems?',
                       'Which user owns a file?',
                       'What shell am I using?',
                       'Which lines contain ERROR?'],
           'correct': 0},
          {'question': 'What does du help estimate?',
           'choices': ['Space used by files/directories',
                       'Network latency',
                       'User permissions',
                       'Service startup order'],
           'correct': 0},
          {'question': 'Why is high CPU usage not automatically a fault?',
           'choices': ['The workload may legitimately require CPU',
                       'Linux ignores CPU usage',
                       'CPU cannot affect performance',
                       'Only root processes use CPU'],
           'correct': 0},
          {'question': 'How should load average be interpreted?',
           'choices': ['Relative to system capacity, workload, waits, and other evidence',
                       'Any value over 1 is always broken',
                       'Any value under 100 is always healthy',
                       'As disk usage only'],
           'correct': 0},
          {'question': 'Before terminating a process, what should you verify?',
           'choices': ['PID, owner, command/role, and expected impact',
                       'Only that kill -9 is available',
                       'That it uses any memory',
                       'That you are root'],
           'correct': 0}],
 'reflection': 'A teammate says, “CPU is high, so we should restart the server.” How would you turn that '
               'statement into an evidence-based investigation before deciding whether any restart or '
               'process termination is justified?'}
