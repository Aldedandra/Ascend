"""Module 2, Lesson 3: Files, Text & the Power of the Shell."""

LESSON = {'id': '2-3',
 'title': 'Files, Text & the Power of the Shell',
 'summary': 'Learn to inspect and transform text with cat, less, head, tail, grep, pipes, redirection, '
            'wildcards, and environment variables. Build command pipelines that answer focused '
            'troubleshooting questions.',
 'duration_minutes': 65,
 'xp': 70,
 'audio_script': 'Welcome to Lesson 2.3: Files, Text, and the Power of the Shell.\n'
                 '\n'
                 'So far, you can identify the pieces of a Linux system and navigate its filesystem. Now we '
                 'reach one of the most important reasons command-line environments are so powerful: text.\n'
                 '\n'
                 'Linux tools are often designed to do one focused job well, read text or structured '
                 'streams, and pass results to another tool.\n'
                 '\n'
                 'Instead of opening a giant log file and scrolling manually, you can ask focused '
                 'questions.\n'
                 '\n'
                 'Show me the newest twenty lines.\n'
                 '\n'
                 'Show me only lines containing ERROR.\n'
                 '\n'
                 'Show me those errors from the last output and count them.\n'
                 '\n'
                 'Save the filtered results into a new file.\n'
                 '\n'
                 'That composability is one of the core ideas of the shell.\n'
                 '\n'
                 'Begin with reading files.\n'
                 '\n'
                 'cat prints file content to standard output. It is useful for short files.\n'
                 '\n'
                 'If a configuration file contains twenty lines, cat may be perfect.\n'
                 '\n'
                 'If a log contains fifty thousand lines, cat is usually a poor choice because the terminal '
                 'fills with output.\n'
                 '\n'
                 'For larger files, less gives you an interactive pager. You can move through content, '
                 'search, and quit without dumping the entire file onto the screen at once.\n'
                 '\n'
                 'head shows the beginning of input. By default it commonly shows ten lines.\n'
                 '\n'
                 'tail shows the end.\n'
                 '\n'
                 'tail is especially valuable for logs because recent events are often at the bottom.\n'
                 '\n'
                 'Tail dash f follows a file as new lines are appended. That lets you watch activity while '
                 'reproducing a problem.\n'
                 '\n'
                 'This creates a powerful troubleshooting pattern.\n'
                 '\n'
                 'Start following a log.\n'
                 '\n'
                 'Reproduce the failing request.\n'
                 '\n'
                 'Watch what new evidence appears.\n'
                 '\n'
                 'Now add grep.\n'
                 '\n'
                 'grep searches text for matching patterns.\n'
                 '\n'
                 'If an application log contains thousands of lines, grep ERROR app dot log can return only '
                 'lines containing ERROR.\n'
                 '\n'
                 'Grep dash i performs case-insensitive matching.\n'
                 '\n'
                 'Grep dash n includes line numbers.\n'
                 '\n'
                 'Grep dash r can search recursively through directories, although you should aim it '
                 'carefully because broad recursive searches can produce enormous output.\n'
                 '\n'
                 'The key idea is not grep syntax. The key idea is filtering.\n'
                 '\n'
                 'You start with a large body of evidence and reduce it to the subset relevant to your '
                 'question.\n'
                 '\n'
                 'The shell becomes much more powerful when you use a pipe.\n'
                 '\n'
                 'The pipe character takes standard output from the command on the left and provides it as '
                 'standard input to the command on the right.\n'
                 '\n'
                 'For example, ps aux pipe grep python.\n'
                 '\n'
                 'Conceptually, ps aux produces process information. The pipe passes that stream to grep. '
                 'Grep keeps only lines containing python.\n'
                 '\n'
                 'The result is not a special built-in DevOps command. It is two smaller tools composed into '
                 'a focused question.\n'
                 '\n'
                 'You can keep composing.\n'
                 '\n'
                 'journalctl dash u ascend dash api pipe grep ERROR.\n'
                 '\n'
                 'One tool produces service journal entries. Another filters them.\n'
                 '\n'
                 'Later you may add tail, sort, uniq, awk, sed, or other tools. Do not rush into memorizing '
                 'all of them. First understand the pipeline model.\n'
                 '\n'
                 'Output from one program becomes input to another.\n'
                 '\n'
                 'Linux commands commonly work with three standard streams.\n'
                 '\n'
                 'Standard input, or stdin.\n'
                 '\n'
                 'Standard output, or stdout.\n'
                 '\n'
                 'Standard error, or stderr.\n'
                 '\n'
                 'Stdout is normal command output.\n'
                 '\n'
                 'Stderr is intended for errors or diagnostic messages.\n'
                 '\n'
                 'This distinction becomes important because the shell lets you redirect streams.\n'
                 '\n'
                 'The greater-than operator redirects standard output into a file.\n'
                 '\n'
                 'echo healthy greater-than status dot txt writes the output into status dot txt, replacing '
                 'the file if it already exists.\n'
                 '\n'
                 'Two greater-than characters append instead of replacing.\n'
                 '\n'
                 'echo another line greater-than greater-than status dot txt adds content to the end.\n'
                 '\n'
                 'This is a place where caution matters.\n'
                 '\n'
                 'A single greater-than can overwrite a file.\n'
                 '\n'
                 'Before redirecting into an important path, verify the target.\n'
                 '\n'
                 'Again, Evidence Before Action.\n'
                 '\n'
                 'The less-than operator can provide a file as standard input to a command, although many '
                 'utilities can also accept filenames directly.\n'
                 '\n'
                 'You will also encounter redirection for stderr, such as two greater-than, and combinations '
                 'that merge or separate output streams. We will not make that the focus yet, but recognize '
                 'that normal output and error output are different channels.\n'
                 '\n'
                 "Now let's look at wildcards.\n"
                 '\n'
                 'The shell can expand patterns before a command runs.\n'
                 '\n'
                 'An asterisk can match multiple characters.\n'
                 '\n'
                 'For example, ls star dot log may expand to all matching dot log files in the current '
                 'directory.\n'
                 '\n'
                 'A question mark can match a single character.\n'
                 '\n'
                 'This is called globbing.\n'
                 '\n'
                 'It is convenient, but it can also make commands act on more files than you intended.\n'
                 '\n'
                 'Before using a wildcard with a consequential operation, preview what it matches with a '
                 'harmless command such as printf or ls.\n'
                 '\n'
                 'This is the shell version of inspecting your target set.\n'
                 '\n'
                 'Another core concept is the environment.\n'
                 '\n'
                 'A process can receive environment variables: key-value settings available to that '
                 'process.\n'
                 '\n'
                 'You have already used one when you ran echo dollar SHELL.\n'
                 '\n'
                 'PATH is another extremely important environment variable.\n'
                 '\n'
                 'PATH contains directories the shell searches when you type a command without an explicit '
                 'path.\n'
                 '\n'
                 'When you type python or git, the shell searches PATH to locate an executable with that '
                 'name.\n'
                 '\n'
                 'The command which can often tell you which executable would be selected, although command '
                 'dash v is more portable in shell scripts.\n'
                 '\n'
                 'Environment variables are everywhere in DevOps.\n'
                 '\n'
                 'Applications use them for configuration.\n'
                 '\n'
                 'CI/CD systems inject variables into jobs.\n'
                 '\n'
                 'Containers receive environment variables.\n'
                 '\n'
                 'Cloud credentials may be exposed through environment variables or credential providers.\n'
                 '\n'
                 'Secrets can also appear in environment variables, which means you should never dump '
                 'environment data carelessly into logs or public output.\n'
                 '\n'
                 'The env command displays environment variables. Useful, yes. Safe to paste publicly, not '
                 'automatically.\n'
                 '\n'
                 'Now connect these tools into troubleshooting.\n'
                 '\n'
                 "Imagine Ascend's API is returning errors.\n"
                 '\n'
                 'You find a log file.\n'
                 '\n'
                 'First you might run tail dash fifty app dot log.\n'
                 '\n'
                 'That answers: what happened recently?\n'
                 '\n'
                 'Then grep ERROR app dot log.\n'
                 '\n'
                 'That answers: which lines explicitly contain ERROR?\n'
                 '\n'
                 'Then grep dash i timeout app dot log.\n'
                 '\n'
                 'That asks a narrower hypothesis.\n'
                 '\n'
                 'Perhaps you pipe results into tail to view only the latest matching entries.\n'
                 '\n'
                 'Each command should correspond to a question.\n'
                 '\n'
                 'Do not build a six-command pipeline simply because it looks impressive. Start with the '
                 'smallest command that provides useful evidence. Add filters only when you need them.\n'
                 '\n'
                 'This keeps your investigation understandable.\n'
                 '\n'
                 'Pipes also encourage non-destructive exploration.\n'
                 '\n'
                 'If you can answer a question by reading and filtering existing output, you often do not '
                 'need to modify the system at all.\n'
                 '\n'
                 'That is excellent incident behavior.\n'
                 '\n'
                 "Now let's discuss file creation and copying briefly.\n"
                 '\n'
                 'touch can create an empty file or update timestamps.\n'
                 '\n'
                 'cp copies files.\n'
                 '\n'
                 'mv moves or renames them.\n'
                 '\n'
                 'mkdir creates directories.\n'
                 '\n'
                 'These commands are simple, but the paths matter.\n'
                 '\n'
                 'cp source destination.\n'
                 '\n'
                 'mv source destination.\n'
                 '\n'
                 'Always inspect the destination and understand whether an existing file may be replaced.\n'
                 '\n'
                 'We are intentionally delaying destructive removal commands until you have stronger path '
                 'and permission habits.\n'
                 '\n'
                 'One more useful idea: exit status.\n'
                 '\n'
                 'Commands return a numeric exit status to the shell.\n'
                 '\n'
                 'By convention, zero indicates success and non-zero indicates some form of failure or '
                 'special condition.\n'
                 '\n'
                 'The shell variable question mark contains the exit status of the most recent command.\n'
                 '\n'
                 'Run a successful command, then echo dollar question mark.\n'
                 '\n'
                 'You will usually see zero.\n'
                 '\n'
                 'Run a command that fails, such as trying to list a path that does not exist, then inspect '
                 'the value again.\n'
                 '\n'
                 'Exit codes become extremely important in automation and CI/CD. A pipeline step often '
                 "determines success or failure based on the command's exit code, not on whether the output "
                 'looked convincing to a human.\n'
                 '\n'
                 'This gives us another evidence channel.\n'
                 '\n'
                 'Text output tells you something.\n'
                 '\n'
                 'Error output tells you something.\n'
                 '\n'
                 'Exit status tells automation whether the command reported success.\n'
                 '\n'
                 "For this lesson's lab, you are going to create a fake application log and investigate it "
                 'entirely through the command line.\n'
                 '\n'
                 'You will inspect the beginning and end, filter errors, combine commands with pipes, '
                 'redirect selected evidence into a report file, use a wildcard safely, inspect an '
                 'environment variable, and compare successful and failed exit codes.\n'
                 '\n'
                 'The goal is not syntax gymnastics.\n'
                 '\n'
                 'The goal is to experience the shell as a composable evidence system.\n'
                 '\n'
                 'Here is the takeaway.\n'
                 '\n'
                 'cat reads short files.\n'
                 '\n'
                 'less lets you inspect large files interactively.\n'
                 '\n'
                 'head and tail show boundaries.\n'
                 '\n'
                 'grep filters.\n'
                 '\n'
                 'Pipes connect tools.\n'
                 '\n'
                 'Redirection controls where output goes.\n'
                 '\n'
                 'Wildcards let the shell expand sets of paths.\n'
                 '\n'
                 'Environment variables supply process configuration.\n'
                 '\n'
                 'Exit codes communicate success or failure to automation.\n'
                 '\n'
                 'Put those concepts together and the command line becomes more than navigation. It becomes '
                 'a way to build precise questions about a running system.\n'
                 '\n'
                 'In the next lesson, we will tackle users, groups, ownership, permissions, sudo, and least '
                 'privilege.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Choose appropriate tools to read short files, large files, beginnings, endings, and '
                'live-appended logs.',
                'Use grep to filter text and pipes to compose multiple commands into a focused '
                'investigation.',
                'Explain stdin, stdout, stderr, output redirection, and the difference between overwrite and '
                'append.',
                'Use shell wildcards carefully and preview the target set before consequential operations.',
                'Explain environment variables, PATH, and command exit status in the context of DevOps '
                'automation.'],
 'content': [{'heading': 'Choose the reader that fits the evidence',
              'body': 'cat is convenient for short files. less is better for long interactive reading. head '
                      'shows the beginning. tail shows the end. tail -f follows a file as new lines arrive, '
                      'which is especially useful while reproducing an application problem.'},
             {'heading': 'grep turns a large stream into a focused question',
              'body': 'grep filters lines matching a pattern. Options such as -i for case-insensitive '
                      'matching and -n for line numbers make it more useful. Filtering is a troubleshooting '
                      'skill: start broad enough to gather evidence, then narrow deliberately.'},
             {'heading': 'Pipes compose small tools',
              'body': 'The | operator sends stdout from the command on the left into stdin for the command '
                      'on the right. A pipeline such as ps aux | grep python is powerful because each '
                      'command does one understandable job.'},
             {'heading': 'Standard streams separate input, output, and errors',
              'body': 'Commands commonly receive stdin and produce stdout plus stderr. The separation '
                      'matters for scripts, logging, pipelines, and redirection because normal results and '
                      'diagnostic failures can be handled differently.'},
             {'heading': '> overwrites; >> appends',
              'body': 'Output redirection can save command results into files. A single > replaces the '
                      'destination content, while >> appends. Because overwriting is consequential, verify '
                      'the destination before redirecting important output.'},
             {'heading': 'Wildcards are expanded by the shell',
              'body': 'Patterns such as *.log can expand into multiple filenames before the command runs. '
                      'This is convenient but can widen the scope of an operation. Preview wildcard matches '
                      'with a read-only command before using them with copy, move, or removal operations.'},
             {'heading': 'Environment variables configure processes',
              'body': 'Variables such as SHELL and PATH are part of a process environment. Applications, '
                      'containers, and CI/CD jobs frequently receive configuration through environment '
                      'variables. Treat environment output carefully because secrets may be present.'},
             {'heading': "PATH answers 'where does this command come from?'",
              'body': 'When you type a command without an explicit path, the shell searches directories '
                      'listed in PATH. Tools such as command -v git or which git can help identify the '
                      'executable that would run.'},
             {'heading': 'Exit status is evidence for automation',
              'body': 'Commands report an exit code. Zero conventionally means success; non-zero represents '
                      'failure or another condition. The shell exposes the previous exit code through $?. '
                      'CI/CD systems rely heavily on exit status to decide whether a step passed.'},
             {'heading': 'Readable pipelines beat clever pipelines',
              'body': 'A long one-liner is not automatically better engineering. Start with a simple '
                      'command, inspect its evidence, then add filters only when they answer a real '
                      'question. A pipeline you understand is easier to debug and safer to reuse.'}],
 'diagram': {'title': 'The shell as an evidence pipeline',
             'description': 'Standard output from one command can become standard input for the next.',
             'nodes': [{'label': 'Source command',
                        'detail': 'Produces text or structured output, such as ps, cat, or journalctl.'},
                       {'label': 'Pipe |',
                        'detail': "Connects the left command's stdout to the right command's stdin."},
                       {'label': 'Filter',
                        'detail': 'grep or another tool narrows or transforms the stream.'},
                       {'label': 'Second filter',
                        'detail': 'Optional additional processing answers a more specific question.'},
                       {'label': 'Terminal or file',
                        'detail': 'View the evidence directly or redirect it into a report.'}],
             'caption': 'Build pipelines one understandable step at a time. Each stage should have a '
                        'reason.'},
 'engineer_perspective': {'title': 'Filter evidence without destroying it',
                          'body': 'During an incident, read-only text processing is extremely powerful. You '
                                  'can inspect logs, processes, configuration, and command output without '
                                  'changing the system. This reduces risk while still letting you test '
                                  'hypotheses quickly.'},
 'try_it_yourself': {'title': 'Build a small troubleshooting pipeline',
                     'intro': 'Use the safe practice directory from Lesson 2.2, or create it if needed.',
                     'steps': ['Create ~/ascend-linux-lab/logs/app.log with several lines using printf, '
                               'including at least two INFO lines, two ERROR lines, and one WARNING line.',
                               'Run cat on the file. Then run head and tail. Explain what each command '
                               'emphasizes.',
                               "Run grep 'ERROR' ~/ascend-linux-lab/logs/app.log.",
                               "Run grep -n 'ERROR' ~/ascend-linux-lab/logs/app.log and explain the added "
                               'evidence.',
                               "Run cat ~/ascend-linux-lab/logs/app.log | grep 'ERROR'. Compare the result "
                               'with grep reading the file directly.',
                               'Redirect the matching lines into ~/ascend-linux-lab/logs/error-report.txt '
                               'using >, then inspect the report with cat.'],
                     'takeaway': 'The shell becomes powerful when small tools can be combined into precise, '
                                 'low-risk questions.'},
 'lab': {'title': 'Investigate a simulated application log',
         'instructions': ['Create a Journal entry titled “Lesson 2.3 — Shell Evidence Pipeline.”',
                          'Ensure ~/ascend-linux-lab/logs exists. Create app.log with at least twelve '
                          'timestamped lines containing a mixture of INFO, WARNING, and ERROR messages. '
                          'Include at least one message containing the word timeout.',
                          'Run head -5 on the log and record what question that answers. Run tail -5 and '
                          'explain how the question changes.',
                          "Run grep -n 'ERROR' against the log. Record the number and line positions of "
                          'matching entries.',
                          "Run grep -i 'timeout' against the log. Explain why -i can matter with "
                          'human-generated or inconsistent log text.',
                          "Pipe grep 'ERROR' output into tail -2. Explain the role of each command in the "
                          'pipeline.',
                          'Redirect all ERROR lines to error-report.txt with >. Inspect the file. Then '
                          "append the line 'Investigation complete' using >> and verify the existing report "
                          'was preserved.',
                          'Create two extra files named api-1.log and api-2.log. Run ls '
                          '~/ascend-linux-lab/logs/*.log and list exactly which paths the wildcard matched '
                          'before doing anything else with the pattern.',
                          'Run echo $PATH and then command -v git. Explain how PATH relates to the returned '
                          'Git executable.',
                          'Run ls ~/ascend-linux-lab/logs/app.log followed immediately by echo $?. Record '
                          'the value. Then run ls ~/ascend-linux-lab/logs/does-not-exist and echo $? again. '
                          'Explain the difference.',
                          'Finish with a three-stage troubleshooting pipeline of your own design. Write the '
                          'question it answers first, then the command, then explain each stage.']},
 'quiz': [{'question': 'Which command is usually best for interactively reading a very large text file?',
           'choices': ['less', 'mkdir', 'pwd', 'hostname'],
           'correct': 0},
          {'question': 'Why is tail useful for logs?',
           'choices': ['It shows the newest lines at the end of a file',
                       'It changes file ownership',
                       'It searches every directory',
                       'It installs a log service'],
           'correct': 0},
          {'question': 'What does grep primarily do?',
           'choices': ['Filter text for matching patterns',
                       'Change directories',
                       'Manage Linux users',
                       'Restart services'],
           'correct': 0},
          {'question': 'What does the pipe operator | do?',
           'choices': ['Deletes the left command',
                       'Sends stdout from one command into stdin of another',
                       'Runs commands only as root',
                       'Creates a hidden file'],
           'correct': 1},
          {'question': 'What is stdout?',
           'choices': ['The normal output stream of a command',
                       "The root user's password",
                       'A Linux distribution',
                       'A filesystem mount'],
           'correct': 0},
          {'question': 'What is the key difference between > and >>?',
           'choices': ['> overwrites while >> appends',
                       '> appends while >> overwrites',
                       'Both always delete the destination',
                       'They are identical'],
           'correct': 0},
          {'question': 'Why preview a wildcard such as *.log before a consequential operation?',
           'choices': ['To confirm exactly which paths the shell will expand it to',
                       'To make the kernel faster',
                       'To disable permissions',
                       'To convert files into logs'],
           'correct': 0},
          {'question': 'What is PATH?',
           'choices': ['An environment variable containing directories searched for commands',
                       'The root directory itself',
                       'A log severity',
                       'A process signal'],
           'correct': 0},
          {'question': 'What does an exit status of 0 conventionally indicate?',
           'choices': ['The command reported success',
                       'The command definitely made no changes',
                       'The command ran as root',
                       'The system has zero processes'],
           'correct': 0},
          {'question': 'Which approach best follows Evidence Before Action?',
           'choices': ['Build the longest possible one-liner immediately',
                       'Start with a simple read-only query and add filters as needed',
                       'Redirect output over an important file to test the command',
                       'Dump every environment variable into a public ticket'],
           'correct': 1}],
 'reflection': 'Think of a troubleshooting question you have encountered in Ascend, Forge, or another '
               'system. How could breaking that question into a source command plus one or more filters make '
               'the investigation clearer?'}
