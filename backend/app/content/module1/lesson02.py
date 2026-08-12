"""Module 1, Lesson 2: Understanding a Git Repository."""

LESSON = {'id': '1-2',
 'title': 'Understanding a Git Repository',
 'summary': 'Turn the Git mental model into observable states. Create a safe repository, inspect .git, and watch '
            'files move from untracked to staged to committed while learning what status and diff actually prove.',
 'duration_minutes': 60,
 'xp': 65,
 'audio_script': 'Welcome back to Module 1 of Ascend: Git and Collaborative Source Control.\n'
                 '\n'
                 'In Lesson 1.1, you learned why version control exists. Git preserves evidence about change, and '
                 'you built a mental model separating the working tree, staging area, local repository history, and '
                 'remote repository.\n'
                 '\n'
                 'Now we are going to make that model concrete.\n'
                 '\n'
                 'By the end of this lesson, you should be able to look at a directory and reason about whether Git '
                 'is tracking it, identify the state of individual files, and deliberately move a change from '
                 'untracked or modified, to staged, to committed.\n'
                 '\n'
                 'What makes a directory a Git repository?\n'
                 '\n'
                 'A normal directory is just a directory. It can contain source code, documentation, images, '
                 'configuration files, or anything else. Git does not automatically track a folder simply because it '
                 'contains code.\n'
                 '\n'
                 'One way to create a Git repository is with git init. When you run git init inside a directory, Git '
                 'initializes repository metadata, normally in a hidden dot-git directory. That directory contains '
                 'the internal information Git needs to represent history, references, configuration, objects, and '
                 'other repository state.\n'
                 '\n'
                 'You normally do not edit dot-git by hand. Think of your visible project files as the workspace you '
                 "operate on and dot-git as Git's internal recordkeeping system.\n"
                 '\n'
                 'On macOS and Linux, names beginning with a period are normally hidden from a basic directory '
                 'listing. The command ls dash a includes hidden entries. In a repository root, that can reveal '
                 'dot-git.\n'
                 '\n'
                 'But remember Evidence Before Action. Seeing dot-git is useful evidence, but you generally interact '
                 "with repository state through Git commands rather than modifying Git's internal files.\n"
                 '\n'
                 'Now let us talk about how Git sees project files.\n'
                 '\n'
                 'A file can be untracked. Untracked means the file exists in the working tree, but Git is not '
                 'currently including it in tracked history or staging. If you create notes dot txt inside a '
                 'repository, git status may list it under untracked files.\n'
                 '\n'
                 'That does not mean Git cannot see the file. Git status is telling you that Git sees it and knows '
                 'it is not yet tracked.\n'
                 '\n'
                 'A tracked file is a file Git already knows as part of repository history or staging. Tracked files '
                 'can still have different states.\n'
                 '\n'
                 'A tracked file can be unchanged. Its working-tree content matches the recorded state.\n'
                 '\n'
                 'It can be modified. You changed the working copy after the last recorded or staged state.\n'
                 '\n'
                 'It can be staged. The current change has been selected for inclusion in the next commit.\n'
                 '\n'
                 'After a commit, that staged snapshot becomes part of local repository history.\n'
                 '\n'
                 'Imagine a brand-new file named deployment-notes dot M D.\n'
                 '\n'
                 'You create it. It is untracked.\n'
                 '\n'
                 'You run git add deployment-notes dot M D. Its current content becomes staged.\n'
                 '\n'
                 'You run git commit with a meaningful message. The staged snapshot becomes part of local history.\n'
                 '\n'
                 'Then you edit deployment-notes dot M D again. The file is still tracked, but the new working-tree '
                 'change is modified and unstaged. You can stage that new change and commit another snapshot.\n'
                 '\n'
                 'State describes the relationship between versions of content at a particular moment.\n'
                 '\n'
                 'This is why git status is so valuable.\n'
                 '\n'
                 'Let us create a safe practice repository. You do not need to experiment with risky commands inside '
                 'Ascend itself to learn Git. Instead, create a temporary directory specifically for practice.\n'
                 '\n'
                 'Make a directory named ascend-git-lab somewhere outside the Ascend project. Change into it and run '
                 'git init. Then run git status.\n'
                 '\n'
                 'Before creating any files, read what Git tells you. Depending on your Git version and '
                 'configuration, the initial branch name may be main, master, or another configured default. Do not '
                 'assume. Observe it.\n'
                 '\n'
                 'Now create a file called README dot M D. Run git status again.\n'
                 '\n'
                 'Before the file existed, the working tree had no README. Now README exists, but Git has no '
                 'committed history containing it. Git reports it as untracked.\n'
                 '\n'
                 'Next run git add README dot M D. Then run git status again. README has moved from untracked to '
                 'staged.\n'
                 '\n'
                 'Nothing has been pushed anywhere. No remote is required. You have simply prepared the current '
                 'content of README for the next commit.\n'
                 '\n'
                 'Before committing, run git diff. You may be surprised that plain git diff shows nothing for the '
                 'staged README.\n'
                 '\n'
                 'That is useful evidence.\n'
                 '\n'
                 'Plain git diff normally shows unstaged working-tree changes relative to the staging area, which is '
                 'also called the index. To inspect staged content, run git diff dash dash staged.\n'
                 '\n'
                 'This distinction matters. If git diff is empty, that does not necessarily mean there are no '
                 'changes. Some changes may already be staged.\n'
                 '\n'
                 'Good troubleshooting rarely relies on one command in isolation.\n'
                 '\n'
                 'Now create the commit with git commit dash m and a useful message such as add initial README.\n'
                 '\n'
                 'If Git says your user name or email is not configured, read the message before changing '
                 'configuration. Git needs author identity information for the commit, and the appropriate identity '
                 'or configuration scope may matter.\n'
                 '\n'
                 'After the commit succeeds, run git status again. If nothing else has changed, Git should report a '
                 'clean working tree.\n'
                 '\n'
                 'Then run git log dash dash oneline. You should see the commit you just created.\n'
                 '\n'
                 'This is a complete local Git lifecycle: create content, observe it as untracked, stage it, inspect '
                 'the staged change, commit it, and verify the resulting history.\n'
                 '\n'
                 'Now edit README again. Add another line, perhaps, This repository is for Ascend Git practice.\n'
                 '\n'
                 'Run git status. The file is no longer untracked because Git already tracks README. Instead, it is '
                 'modified.\n'
                 '\n'
                 'Run git diff. This time plain git diff should show the new unstaged change.\n'
                 '\n'
                 'Stage it with git add README dot M D. Run git status. Then run git diff again. The plain diff may '
                 'once again be empty because the working tree now matches the staged version.\n'
                 '\n'
                 'Run git diff dash dash staged. There is the change.\n'
                 '\n'
                 'This exercise teaches an important lesson: Git commands answer specific questions. Empty output '
                 'can be misinterpreted if you do not know what boundary the command is inspecting.\n'
                 '\n'
                 'Engineering evidence must be understood in context.\n'
                 '\n'
                 'Now we need to discuss git add a little more carefully.\n'
                 '\n'
                 'You will often see git add dot. The dot commonly means the current directory and its descendants, '
                 'so this can stage many changes at once.\n'
                 '\n'
                 'Sometimes that is exactly what you intend. But using git add dot as an automatic reflex can hide '
                 'mistakes. You may stage a debug file, generated output, temporary note, secret, or unrelated '
                 'change without noticing.\n'
                 '\n'
                 'A safer learning habit is to stage intentionally by path, then inspect git status and git diff '
                 'dash dash staged.\n'
                 '\n'
                 'As you become more experienced, you can use broader staging operations when appropriate because '
                 'you understand their scope, not because they are the only command you memorized.\n'
                 '\n'
                 'What about files you never want Git to track?\n'
                 '\n'
                 'Repositories often contain generated files, local configuration, caches, dependency directories, '
                 'build output, operating-system metadata, or secrets that should not enter version control.\n'
                 '\n'
                 'Git uses a file named dot-gitignore to describe patterns that should normally be ignored when Git '
                 'considers untracked files.\n'
                 '\n'
                 'A JavaScript project commonly ignores node_modules because dependencies can be restored from '
                 'package metadata and node_modules can be enormous. Python projects often ignore pycache '
                 'directories and virtual environments. Build systems may ignore generated dist directories.\n'
                 '\n'
                 'But dot-gitignore is not a security system.\n'
                 '\n'
                 'If a secret has already been committed, adding its filename to dot-gitignore does not erase it '
                 'from existing Git history. And if you place a password or API token into a file that is not '
                 'ignored, Git may stage and commit it if you tell Git to do so.\n'
                 '\n'
                 'There is another subtle point: dot-gitignore primarily affects untracked files. If Git already '
                 'tracks a file, adding that filename to dot-gitignore does not automatically make Git forget it.\n'
                 '\n'
                 'Ignored and untracked are not synonyms. An ignored file is normally excluded by an ignore rule. An '
                 'untracked file is visible to Git as a file that is not currently tracked.\n'
                 '\n'
                 'Now return to commits.\n'
                 '\n'
                 'A commit records the staged snapshot, not every unsaved thought in your editor and not '
                 'automatically every changed file in the repository.\n'
                 '\n'
                 'That means you can have a successful commit while other working-tree changes remain.\n'
                 '\n'
                 'After every commit, git status is a useful verification step. If you expected a clean working tree '
                 'but Git reports modified files, ask why.\n'
                 '\n'
                 'Maybe those changes were intentionally excluded. Maybe you forgot to stage something. Maybe a tool '
                 'changed a generated file during the commit process.\n'
                 '\n'
                 'Do not assume the commit captured everything you meant to preserve. Verify.\n'
                 '\n'
                 'This leads to a strong local workflow.\n'
                 '\n'
                 'First, observe with git status.\n'
                 '\n'
                 'Second, inspect unstaged changes with git diff.\n'
                 '\n'
                 'Third, stage deliberately with git add and specific paths when practical.\n'
                 '\n'
                 'Fourth, inspect the proposed commit with git diff dash dash staged.\n'
                 '\n'
                 'Fifth, commit with a message that explains the purpose.\n'
                 '\n'
                 'Sixth, inspect history with git log.\n'
                 '\n'
                 'Seventh, verify again with git status.\n'
                 '\n'
                 'This loop turns Git from a mysterious set of commands into a state machine you can observe.\n'
                 '\n'
                 'Connect this directly to Ascend.\n'
                 '\n'
                 'When we changed the narrator display name to Archer, the file changed in the working tree. Before '
                 "committing, git diff could show the exact text change. git add selected that file's current change "
                 'for the next commit. git diff dash dash staged could verify the proposed commit. git commit '
                 'preserved that staged snapshot in local history. git push, if performed afterward, could publish '
                 'the local commit to the remote.\n'
                 '\n'
                 'At every step, the state was different.\n'
                 '\n'
                 'Once you can name those states, Git becomes dramatically easier.\n'
                 '\n'
                 'Your lab for this lesson will deliberately create those transitions in a disposable repository. '
                 'You will predict the result of git status before each operation, run the command, and compare your '
                 'prediction with the evidence.\n'
                 '\n'
                 'If your prediction is wrong, that is not failure. That mismatch is where learning happens.\n'
                 '\n'
                 "Do not rush through the lab just to reach a clean status. The goal is to see Git's model.\n"
                 '\n'
                 'Here is the takeaway for Lesson 1.2.\n'
                 '\n'
                 'A Git repository is not merely a folder with code. It is a working tree connected to repository '
                 'metadata and history.\n'
                 '\n'
                 'Files move through meaningful states: untracked, tracked and unchanged, modified, staged, '
                 'committed, and sometimes ignored.\n'
                 '\n'
                 'git status tells you how Git currently sees the repository. git diff and git diff dash dash staged '
                 'inspect different boundaries between states. git add selects content. git commit records the '
                 'staged snapshot.\n'
                 '\n'
                 'When you understand those relationships, later topics such as branches, remotes, conflicts, '
                 'merges, and recovery become much less intimidating.\n'
                 '\n'
                 'Do not memorize Git as a spellbook.\n'
                 '\n'
                 'Observe the state. Predict the next state. Make one deliberate change. Verify the result.\n'
                 '\n'
                 'That is how engineers learn Git.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain what makes a directory a Git repository and the role of the hidden .git directory.',
                'Distinguish untracked, tracked, unchanged, modified, staged, committed, and ignored file states.',
                'Use git status, git diff, git diff --staged, and git log to gather evidence about repository state.',
                'Stage and commit changes deliberately instead of treating git add . as an automatic reflex.',
                'Explain what .gitignore does, what it does not do, and why verification after a commit matters.'],
 'content': [{'heading': 'What makes a directory a repository?',
              'body': 'Source code can exist in an ordinary directory without Git. A Git repository has Git metadata '
                      'associated with it. Running git init creates that repository metadata locally, normally in a '
                      'hidden .git directory at the repository root.'},
             {'heading': 'The hidden .git directory',
              'body': ".git contains Git's internal repository data: objects, references, configuration, and other "
                      'metadata used to represent history and state. You normally interact with it through Git '
                      'commands rather than editing its contents by hand.'},
             {'heading': 'Untracked does not mean invisible',
              'body': "An untracked file exists in the working tree but is not currently part of Git's tracked "
                      'history or staging state. git status can report an untracked file precisely because Git sees '
                      'the file and knows it is not yet tracked.'},
             {'heading': 'Tracked files can have different states',
              'body': 'A tracked file may match the recorded state, contain an unstaged modification, or have '
                      'changes staged for the next commit. State describes the relationship between versions of '
                      'content at the moment you inspect the repository.'},
             {'heading': 'Watch a new file move through Git',
              'body': 'Create README.md in a new practice repository and it begins as untracked. git add README.md '
                      'stages its current content. git commit records that staged snapshot. Editing README.md '
                      'afterward makes the already-tracked file modified again.'},
             {'heading': 'git status is your state report',
              'body': 'git status reports the current branch and important working-tree and staging information '
                      'without changing repository state. Run it repeatedly while learning so you can connect each '
                      'action with the state transition it causes.'},
             {'heading': 'Plain diff and staged diff answer different questions',
              'body': 'git diff normally shows unstaged working-tree changes relative to the staging area. git diff '
                      '--staged shows changes currently prepared for the next commit. An empty plain diff does not '
                      'prove the repository has no changes; changes may already be staged.'},
             {'heading': 'Stage deliberately',
              'body': 'git add selects content for the next commit. git add . can be useful, but it may stage more '
                      'than you intended. While building good habits, prefer deliberate paths and inspect git status '
                      'plus git diff --staged before committing.'},
             {'heading': 'What .gitignore does',
              'body': '.gitignore defines patterns Git should normally ignore when considering untracked files. '
                      'Common examples include dependency directories, caches, generated output, and local '
                      'environment files.'},
             {'heading': 'What .gitignore does not do',
              'body': '.gitignore is not a security boundary and does not erase committed history. Adding an '
                      'already-tracked file to .gitignore does not automatically stop Git from tracking it. Secrets '
                      'require deliberate handling.'},
             {'heading': 'A commit records the staged snapshot',
              'body': 'git commit records what is staged. Other unstaged or untracked work can remain after a '
                      'successful commit. A successful commit therefore does not prove every intended change was '
                      'included.'},
             {'heading': 'Verify after committing',
              'body': 'Run git status after a commit. If you expected a clean working tree but see changes, '
                      'investigate. Verification catches forgotten files, intentionally excluded work, generated '
                      'changes, and incorrect assumptions.'},
             {'heading': 'Repository state as a state machine',
              'body': 'Think in transitions: create file → untracked; git add → staged; git commit → committed; edit '
                      'tracked file → modified; git add again → staged modification. Predicting and observing these '
                      'transitions is more durable than memorizing isolated commands.'},
             {'heading': 'Connect the model to Ascend',
              'body': 'A change such as renaming the narrator to Archer begins in the working tree. Diff shows the '
                      'exact edit, add selects it, staged diff verifies the proposed commit, commit records it '
                      'locally, and push can later publish that commit to a remote.'},
             {'heading': "Alex's Engineering Notes",
              'body': 'A clean git diff can be misleading if you forget about the staging area. Pair git status with '
                      'the appropriate diff. Resist destructive commands while learning; this lesson can be '
                      'completed entirely with a disposable repository and non-destructive inspection.'},
             {'heading': 'Takeaway',
              'body': 'Git becomes predictable when you treat it as observable state. Know what state a file is in, '
                      'understand which boundary a command inspects or changes, and verify the result before moving '
                      'on.'}],
 'diagram': {'title': 'The lifecycle of a file in a local repository',
             'description': 'A file can move through several observable states as you create, stage, commit, and '
                            'edit it.',
             'nodes': [{'label': 'Untracked', 'detail': 'The file exists, but Git is not tracking it yet.'},
                       {'label': 'Staged', 'detail': 'git add selects the current content for the next commit.'},
                       {'label': 'Committed', 'detail': 'git commit records the staged snapshot in local history.'},
                       {'label': 'Modified',
                        'detail': 'A tracked file has new working-tree changes after the recorded state.'},
                       {'label': 'Staged again', 'detail': 'The new modification is selected for another commit.'}],
             'caption': 'File state is relational, not permanent. The same tracked file can move between unchanged, '
                        'modified, staged, and committed states many times.'},
 'engineer_perspective': {'title': 'Empty output is evidence only when you know the question',
                          'body': 'If git diff prints nothing, a beginner may conclude there are no changes. But '
                                  'staged changes are inspected with git diff --staged. Operational troubleshooting '
                                  'works the same way: understand what a tool measures before drawing a conclusion.'},
 'try_it_yourself': {'title': 'Create a disposable repository and watch its state',
                     'intro': 'Use a new practice directory rather than experimenting inside Ascend. Predict git '
                              'status before every state-changing command.',
                     'steps': ['Create ~/Projects/ascend-git-lab, change into it, and run git init.',
                               'Run git status and record the initial branch name instead of assuming what it will '
                               'be.',
                               'Run ls -la and identify the hidden .git directory. Do not edit anything inside it.',
                               'Create README.md with one line of text, predict its state, then run git status.',
                               'Run git add README.md. Predict the new state, verify with git status, then compare '
                               'git diff with git diff --staged.',
                               'Commit the staged README with a useful message. If Git requests identity '
                               'configuration, read the message before deciding what configuration is appropriate.',
                               'Run git status and git log --oneline. Explain what each command proves.',
                               'Edit README.md again, then repeat status → diff → add → staged diff to observe the '
                               'difference between a new untracked file and a modified tracked file.'],
                     'takeaway': 'The commands matter, but the real skill is predicting and verifying repository '
                                 'state before and after each operation.'},
 'lab': {'title': 'Git State Transition Lab',
         'instructions': ['Create a Journal entry titled “Lesson 1.2 — Git State Transition Lab.”',
                          'Use a disposable practice repository, not the Ascend repository, for the state-changing '
                          'portion of this lab.',
                          'Before running git init, explain whether the directory is currently a Git repository and '
                          'what evidence would prove your answer.',
                          'Run git init, ls -la, and git status. Record the evidence that the directory is now a '
                          'repository.',
                          'Create README.md. Predict whether it will be untracked, modified, staged, or committed, '
                          'then verify with git status.',
                          'Stage README.md. Run git status, git diff, and git diff --staged. Explain why the two '
                          'diff commands may produce different results.',
                          'Commit README.md and verify the result with git status and git log --oneline.',
                          'Modify README.md. Predict and verify its new state. Stage it and verify again.',
                          'Create local-debug.log. Add *.log to .gitignore, then use git status to determine whether '
                          'the debug file is being ignored.',
                          'Explain why adding a filename to .gitignore after it has already been committed is a '
                          'different situation.',
                          'Write the lifecycle you observed using arrows, beginning with an ordinary directory and '
                          'ending with a modified tracked file prepared for a second commit.',
                          'Finish with a five-sentence explanation of why a clean git diff alone is insufficient '
                          'evidence that a repository has no pending changes.']},
 'quiz': [{'question': 'What normally makes an ordinary project directory a local Git repository?',
           'choices': ['It contains source code',
                       'It has Git repository metadata such as a .git directory',
                       'It has been uploaded to GitHub',
                       'Its files use the .git extension'],
           'correct': 1},
          {'question': "A newly created README.md appears under 'Untracked files' in git status. What does that "
                       'mean?',
           'choices': ['Git cannot see the file',
                       'The file is already committed',
                       'The file exists but is not currently tracked',
                       'The file has been pushed but not pulled'],
           'correct': 2},
          {'question': 'After running git add README.md, what has happened?',
           'choices': ['The current README content has been staged for the next commit',
                       'README has been pushed to the remote',
                       'The repository has been deleted',
                       'README can no longer be edited'],
           'correct': 0},
          {'question': 'Why might git diff show no output even though git status reports staged changes?',
           'choices': ['git diff is broken',
                       'Plain git diff normally inspects unstaged changes, while staged changes can be inspected '
                       'with git diff --staged',
                       'Staged files are automatically pushed',
                       'Git hides all staged changes permanently'],
           'correct': 1},
          {'question': 'You commit README.md and then edit it again. How should Git generally describe the new '
                       'working-tree change?',
           'choices': ['Untracked', 'Modified', 'Remote only', 'Ignored automatically'],
           'correct': 1},
          {'question': 'What is a good reason not to use git add . blindly?',
           'choices': ['The command never works',
                       'It always deletes ignored files',
                       'It can stage unrelated or unintended changes within its scope',
                       'It automatically creates a remote'],
           'correct': 2},
          {'question': 'What is .gitignore primarily used for?',
           'choices': ['Encrypting repository secrets',
                       'Defining patterns for files Git should normally ignore as untracked content',
                       'Deleting previous commits',
                       'Choosing the current branch'],
           'correct': 1},
          {'question': 'You accidentally committed a secret and then add its filename to .gitignore. Which statement '
                       'is correct?',
           'choices': ['The secret is automatically erased from all previous history',
                       '.gitignore encrypts the old commit',
                       'The ignore rule does not remove the already committed secret from history',
                       'Git immediately deletes the remote repository'],
           'correct': 2},
          {'question': 'What does a successful git commit guarantee?',
           'choices': ['Every changed file in the working tree was included',
                       'The staged snapshot was recorded in local history',
                       'The commit was pushed to every remote',
                       'The working tree must now be clean'],
           'correct': 1},
          {'question': 'Which workflow best reflects Evidence Before Action?',
           'choices': ['git add . → commit immediately → inspect later',
                       'status → inspect diff → stage deliberately → inspect staged diff → commit → verify status',
                       'reset --hard whenever status looks unfamiliar',
                       'delete .git and start over whenever a file is modified'],
           'correct': 1}],
 'reflection': 'Which Git state was least intuitive before this lesson: untracked, modified, staged, committed, or '
               'ignored? Explain how repeatedly predicting git status changed your mental model. Then describe one '
               'situation where checking both git status and the correct form of git diff could prevent a mistake.'}
