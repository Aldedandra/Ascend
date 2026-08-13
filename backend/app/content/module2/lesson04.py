"""Module 2, Lesson 4: Users, Groups & Permissions."""

LESSON = {'id': '2-4',
 'title': 'Users, Groups & Permissions',
 'summary': 'Understand Linux identity and access: users, groups, ownership, rwx permissions, chmod, chown, '
            'sudo, root, and least privilege. Learn to diagnose permission failures instead of bypassing '
            'them.',
 'duration_minutes': 65,
 'xp': 70,
 'audio_script': 'Welcome to Lesson 2.4: Users, Groups, and Permissions.\n'
                 '\n'
                 'You can now navigate a Linux filesystem and use the shell to inspect text. The next '
                 'question is one you will encounter constantly in real systems: who is allowed to do what?\n'
                 '\n'
                 'Linux is a multi-user operating system. Even a server with only one human administrator '
                 'usually has many identities. Your login account is one identity. A web server may run as '
                 'another. A database may run as another. Automation can use service accounts. Containers '
                 'can run processes as specific users. Files and processes have ownership, and permissions '
                 'determine which identities can access them.\n'
                 '\n'
                 'This is not administrative trivia. It is part of application reliability and security.\n'
                 '\n'
                 'Start with users.\n'
                 '\n'
                 'Every Linux user has a numeric user identifier, or UID. Usernames are the human-friendly '
                 'labels mapped to those identifiers. The root user conventionally has UID zero and has '
                 'extremely broad authority.\n'
                 '\n'
                 'Run id and Linux can show your UID, primary group, and additional group memberships. Run '
                 'whoami when you only need the current username.\n'
                 '\n'
                 'Groups let administrators grant access to sets of users. A user has a primary group and '
                 'may belong to supplementary groups. Instead of granting ten people separate access to the '
                 'same resource, you can often grant a group access and manage membership.\n'
                 '\n'
                 'Now connect identity to files.\n'
                 '\n'
                 'A typical long listing from ls dash l begins with a string such as dash r w dash r dash '
                 'dash r dash dash.\n'
                 '\n'
                 'The first character describes the file type. A dash commonly means a regular file. A d '
                 'means directory. An l commonly means symbolic link.\n'
                 '\n'
                 'The next nine characters are three permission sets.\n'
                 '\n'
                 'The first three apply to the owner.\n'
                 '\n'
                 'The next three apply to the group.\n'
                 '\n'
                 'The final three apply to everyone else, commonly called other.\n'
                 '\n'
                 'Each set uses r, w, and x.\n'
                 '\n'
                 'For a regular file, r means read its contents. w means modify it. x means execute it as a '
                 'program or script.\n'
                 '\n'
                 'Directories are slightly different. Read lets you list directory entries. Write lets you '
                 'create, remove, or rename entries, subject to other rules. Execute on a directory means '
                 'you can traverse it and access entries when you know their names.\n'
                 '\n'
                 'That directory execute bit surprises many beginners. A directory can be readable but still '
                 'unusable for normal traversal if execute permission is missing.\n'
                 '\n'
                 'Now consider ownership.\n'
                 '\n'
                 'ls dash l also shows the owning user and group.\n'
                 '\n'
                 'A configuration file might be owned by root and a service group. An application directory '
                 'might be owned by a deployment account. A log file might be writable only by the service '
                 'that produces it.\n'
                 '\n'
                 'If your application reports permission denied, do not immediately make everything '
                 'writable.\n'
                 '\n'
                 'First ask: which identity is performing the operation? Who owns the target? What are the '
                 'owner, group, and other permissions? Is a parent directory blocking traversal? Is the '
                 'application supposed to have this access at all?\n'
                 '\n'
                 'That is Evidence Before Action applied to permissions.\n'
                 '\n'
                 'chmod changes permission bits.\n'
                 '\n'
                 'Symbolic mode expresses intent directly. For example, chmod u plus x script dot sh adds '
                 'execute permission for the owner. chmod g minus w file removes group write permission.\n'
                 '\n'
                 'You will also see numeric, or octal, modes.\n'
                 '\n'
                 'Read is four. Write is two. Execute is one. Add the values for each permission set.\n'
                 '\n'
                 'Seven means read, write, execute.\n'
                 '\n'
                 'Six means read and write.\n'
                 '\n'
                 'Five means read and execute.\n'
                 '\n'
                 'Four means read only.\n'
                 '\n'
                 'So seven five five means owner read-write-execute, group read-execute, and other '
                 'read-execute.\n'
                 '\n'
                 'Six four zero means owner read-write, group read-only, and no permissions for other.\n'
                 '\n'
                 'Do not treat numeric modes as magic. Translate them back into the access they represent.\n'
                 '\n'
                 'chown changes ownership. For example, chown user colon group file changes both owner and '
                 'group, assuming you have authority to do so.\n'
                 '\n'
                 'chgrp changes the group owner.\n'
                 '\n'
                 'These are consequential operations. Changing ownership recursively across the wrong '
                 'directory can break applications or weaken security. Verify your path and understand why '
                 'the ownership should change.\n'
                 '\n'
                 'Now we need to talk about root and sudo.\n'
                 '\n'
                 'Root is the superuser. It can bypass many normal permission checks and make system-wide '
                 'changes.\n'
                 '\n'
                 'sudo allows an authorized user to execute a command with elevated privileges, often as '
                 'root.\n'
                 '\n'
                 'The important habit is not, quote, use sudo whenever permission denied appears, end '
                 'quote.\n'
                 '\n'
                 'Permission denied is evidence.\n'
                 '\n'
                 'It may mean you need elevation. It may also mean you are operating on the wrong file, '
                 'using the wrong account, or attempting something the application should never be allowed '
                 'to do.\n'
                 '\n'
                 'Blindly adding sudo can turn a safe failure into a damaging success.\n'
                 '\n'
                 'This is why least privilege matters.\n'
                 '\n'
                 'Least privilege means an identity should have only the access required to perform its '
                 'job.\n'
                 '\n'
                 'A web application that only needs to read configuration and write to one data directory '
                 'should not run as root merely because that makes permissions easier.\n'
                 '\n'
                 'A CI runner should not receive broad production credentials if it only needs access to one '
                 'deployment target.\n'
                 '\n'
                 'A human engineer should elevate only for operations that require it.\n'
                 '\n'
                 'Security and reliability often point in the same direction here. Smaller permissions '
                 'reduce the blast radius of mistakes and compromise.\n'
                 '\n'
                 'There is another concept called umask. When programs create files and directories, default '
                 'permissions are influenced by the process umask. You do not need to master the calculation '
                 'today, but know that new files do not simply receive every possible permission. Defaults '
                 'are intentionally restricted.\n'
                 '\n'
                 'Special permission bits such as setuid, setgid, and the sticky bit also exist. You may '
                 'encounter them later. For now, recognize that the basic owner-group-other model is the '
                 'foundation.\n'
                 '\n'
                 "Let's turn this into a troubleshooting scenario.\n"
                 '\n'
                 'Suppose the Ascend service starts as user ascend. It needs to read slash etc slash ascend '
                 'slash app dot env and write uploaded files under slash var slash lib slash ascend slash '
                 'uploads.\n'
                 '\n'
                 'The service fails with permission denied.\n'
                 '\n'
                 'A weak response is chmod seven seven seven on everything.\n'
                 '\n'
                 'That gives every user read, write, and execute access and hides the actual design '
                 'problem.\n'
                 '\n'
                 'A stronger investigation asks which exact path failed, which user the service runs as, who '
                 'owns the path, what the permissions are on the file and its parent directories, and what '
                 'access the service genuinely needs.\n'
                 '\n'
                 'Maybe the upload directory is accidentally owned by root after a manual deployment. The '
                 'smallest safe fix might be restoring the intended owner or group, not opening access to '
                 'everyone.\n'
                 '\n'
                 'Then you verify.\n'
                 '\n'
                 'Can the intended service identity perform the required operation? Can identities that '
                 'should not have access still not perform it? Does the service recover?\n'
                 '\n'
                 'That is permissions engineering.\n'
                 '\n'
                 'For the lab, you will stay inside a safe directory in your home folder. You will inspect '
                 'ownership, create files, modify permissions, translate symbolic and numeric modes, and '
                 'intentionally trigger a permission failure without changing system files.\n'
                 '\n'
                 'Do not use sudo for the lab. If an exercise seems to require it, stop and inspect the '
                 'path. The lab is designed to work as your normal user.\n'
                 '\n'
                 'Here is the takeaway.\n'
                 '\n'
                 'Users establish identity. Groups make shared access manageable. Ownership associates '
                 'resources with identities. Permission bits express read, write, and execute access for '
                 'owner, group, and other. chmod changes permissions. chown changes ownership. sudo provides '
                 'controlled elevation. Root is powerful. Least privilege limits blast radius.\n'
                 '\n'
                 'And permission denied is not an instruction to bypass security. It is evidence to '
                 'investigate.\n'
                 '\n'
                 'In the next lesson, we will move from who can access resources to what is actually '
                 'running: processes, jobs, signals, CPU, memory, disk, and system resource evidence.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain Linux users, UIDs, primary/supplementary groups, and the special role of root.',
                'Read owner/group/other rwx permissions from ls -l output for files and directories.',
                'Use chmod safely in symbolic and numeric modes and explain the access a mode grants.',
                'Explain ownership, chown, sudo, and why permission denied should be investigated before '
                'elevation.',
                'Apply least privilege when reasoning about application and human access.'],
 'content': [{'heading': 'Linux access begins with identity',
              'body': 'Users have numeric UIDs and belong to groups. The id command shows identity and group '
                      'membership. Root conventionally has UID 0 and broad authority, while applications '
                      'commonly run under dedicated non-root identities.'},
             {'heading': 'Ownership and permissions work together',
              'body': 'Files and directories have an owning user and group. The rwx bits then describe '
                      'access for owner, group, and other. Diagnose access by identifying the acting user, '
                      'ownership, permissions, and parent-directory access.'},
             {'heading': 'rwx means different things for files and directories',
              'body': 'For files, read views content, write modifies content, and execute permits execution. '
                      'For directories, read lists entries, write changes entries, and execute permits '
                      'traversal/access. Directory execute permission is essential to reach content below '
                      'it.'},
             {'heading': 'Read ls -l as structured evidence',
              'body': 'The first character identifies entry type; the next nine characters are owner, group, '
                      'and other permission triplets. The listing also shows owner and group names. Do not '
                      'change permissions until you can explain the current state.'},
             {'heading': 'chmod changes permissions',
              'body': 'Symbolic modes such as u+x or g-w express a targeted change. Numeric modes use r=4, '
                      'w=2, x=1 for each owner/group/other position. 755 means rwx for owner and r-x for '
                      'group and other; 640 means rw- for owner, r-- for group, and --- for other.'},
             {'heading': 'chown changes ownership',
              'body': "chown can change a file's owner and group; chgrp changes group ownership. Recursive "
                      'ownership changes are consequential, so prove the target path and intended ownership '
                      'before applying them.'},
             {'heading': 'sudo is elevation, not a permission-error button',
              'body': 'sudo lets authorized users run commands with elevated privileges. A permission '
                      'failure may be an intentional protection or evidence of a wrong path/account. '
                      'Investigate first; elevate only when the operation truly requires it.'},
             {'heading': 'Least privilege reduces blast radius',
              'body': 'Users and services should receive only the access required for their job. Running '
                      'applications as root or granting world-writable permissions may hide design problems '
                      'while increasing security and reliability risk.'},
             {'heading': 'Default permissions are influenced by umask',
              'body': 'A process umask restricts default permissions on newly created files and directories. '
                      'You do not need to master its arithmetic yet, but recognize that creation defaults '
                      'are part of the access model.'},
             {'heading': 'Verify both success and boundaries',
              'body': 'After a permission fix, verify the intended identity can perform the required '
                      'operation and that unintended identities have not gained unnecessary access. A fix is '
                      'not complete merely because the original error disappeared.'}],
 'diagram': {'title': 'How Linux decides basic file access',
             'description': 'Start with the process identity, then evaluate ownership and the matching '
                            'permission set.',
             'nodes': [{'label': 'Process identity', 'detail': 'Which UID and groups is the process using?'},
                       {'label': 'Target path',
                        'detail': 'Which file or directory is the process trying to access?'},
                       {'label': 'Owner / group',
                        'detail': 'Who owns the resource and which group is assigned?'},
                       {'label': 'rwx bits',
                        'detail': 'Which owner, group, or other permission set applies?'},
                       {'label': 'Allow or deny',
                        'detail': 'The operation succeeds or Linux returns an access error.'}],
             'caption': 'Permission denied is a result to explain. Do not skip the identity and ownership '
                        'questions by reflexively adding sudo.'},
 'engineer_perspective': {'title': 'Make the permission model match the application design',
                          'body': 'A reliable permission fix expresses intended access. If a service should '
                                  'write one data directory, give its identity the appropriate access there. '
                                  'Do not solve a narrow requirement by running the entire service as root '
                                  'or making the whole tree world-writable.'},
 'try_it_yourself': {'title': 'Decode permissions before changing them',
                     'intro': 'Use only a safe directory under your home folder; no sudo is needed.',
                     'steps': ['Create ~/ascend-linux-lab/permissions and cd into it.',
                               'Create deploy.sh and app.conf with touch, then run ls -l.',
                               'Run chmod u+x deploy.sh and inspect the exact permission change with ls -l.',
                               'Run chmod 640 app.conf. Translate 640 into owner, group, and other '
                               'permissions before checking ls -l.',
                               'Run id and identify your UID, primary group, and any supplementary groups.',
                               'Run chmod u-w app.conf and attempt to append text to it. Observe the '
                               'failure, then restore owner write permission with chmod u+w app.conf.'],
                     'takeaway': 'Treat the permission string as evidence you can decode, not as an obstacle '
                                 'to bypass.'},
 'lab': {'title': 'Diagnose a permission problem safely',
         'instructions': ['Create a Journal entry titled “Lesson 2.4 — Permission Investigation.”',
                          'Create ~/ascend-linux-lab/permissions/service-data and a file named '
                          'application.conf inside it.',
                          'Run id and ls -ld on the directory plus ls -l on the file. Record user, group, '
                          'ownership, and permissions.',
                          'Set application.conf to mode 640. Translate every digit and permission triplet in '
                          'your journal.',
                          'Add owner execute permission to a separate script file using symbolic chmod. '
                          'Explain why execute makes sense for the script but not for ordinary '
                          'configuration.',
                          'Remove owner write permission from application.conf, attempt to append a test '
                          'line, and capture the permission-denied evidence. Do not use sudo.',
                          'Use ls -l to form a hypothesis, restore only owner write permission, retry the '
                          'append, and verify success.',
                          'Run umask and record the value. Create a new file and directory and inspect their '
                          'initial permissions. Note the observed relationship without changing your system '
                          'umask.',
                          'Write what chmod 777 would grant and explain why it would be an inappropriate '
                          'default response to an application permission error.',
                          'Write a hypothetical Ascend service scenario identifying the service user, a '
                          'read-only configuration path, a writable data path, and the least access each '
                          'should require.']},
 'quiz': [{'question': 'What does UID identify?',
           'choices': ['A Linux user',
                       'A directory permission only',
                       'A network interface',
                       'A package repository'],
           'correct': 0},
          {'question': 'In -rwxr-x---, which triplet applies to the owning group?',
           'choices': ['rwx', 'r-x', '---', 'The leading dash'],
           'correct': 1},
          {'question': 'What does execute permission on a directory primarily allow?',
           'choices': ['Traversal/access through the directory',
                       'Automatic file deletion',
                       'Changing the owner',
                       'Reading every file regardless of its permissions'],
           'correct': 0},
          {'question': 'What permissions does numeric mode 640 represent?',
           'choices': ['Owner rw-, group r--, other ---',
                       'Owner rwx, group r--, other ---',
                       'Owner r--, group rw-, other ---',
                       'Everyone rw-'],
           'correct': 0},
          {'question': 'Which command changes permission bits?',
           'choices': ['chmod', 'pwd', 'grep', 'ps'],
           'correct': 0},
          {'question': 'What does chown change?',
           'choices': ['Ownership', 'Current directory', 'Process priority only', 'Shell history'],
           'correct': 0},
          {'question': 'What is the best first response to an unexpected permission denied error?',
           'choices': ['Run the same command with sudo immediately',
                       'Inspect the acting identity, path, ownership, and permissions',
                       'Set the target to 777',
                       'Log in as root permanently'],
           'correct': 1},
          {'question': 'Why is running an application as root usually undesirable?',
           'choices': ['It increases the blast radius of mistakes or compromise',
                       'Root cannot read files',
                       'Root cannot bind network ports',
                       'Linux has no root account'],
           'correct': 0},
          {'question': 'What principle says an identity should have only the access it needs?',
           'choices': ['Least privilege', 'Eventual consistency', 'Horizontal scaling', 'Immutability'],
           'correct': 0},
          {'question': 'After changing permissions, what should you verify?',
           'choices': ['Only that the original error disappeared',
                       'That intended access works and unnecessary access was not granted',
                       'That every user can write the file',
                       'That sudo is installed'],
           'correct': 1}],
 'reflection': 'Why is `sudo` a poor default response to `Permission denied`? Describe the evidence you '
               'would gather before deciding whether elevation, ownership, or permission changes are '
               'actually appropriate.'}
