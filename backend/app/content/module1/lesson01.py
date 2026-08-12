"""Module 1, Lesson 1: Why Version Control Exists."""

LESSON = {'id': '1-1',
 'title': 'Why Version Control Exists',
 'summary': 'Build a practical mental model of Git as an evidence system for change. Learn how repositories, working '
            'trees, staging, commits, diffs, and remotes fit together before memorizing workflows.',
 'duration_minutes': 55,
 'xp': 60,
 'audio_script': 'Welcome to Module 1 of Ascend: Git and Collaborative Source Control.\n'
                 '\n'
                 'In Module 0, you learned that strong engineering begins with evidence, systems thinking, '
                 'controlled change, verification, and feedback. Git is where those ideas become part of your '
                 'everyday development workflow.\n'
                 '\n'
                 'Before Git, imagine working on Ascend with no version control at all. You have a folder containing '
                 'code that works. You want to change the lesson player, so you make a copy called Ascend backup. '
                 'Later you make another copy called Ascend backup new. Then Ascend final. Then Ascend final two. A '
                 'week later, one version contains the audio fix, another contains the navigation fix, and a third '
                 'contains a content change you still need. You remember that one folder worked yesterday, but you '
                 'cannot prove exactly what changed between yesterday and today.\n'
                 '\n'
                 'That is not just inconvenient. It is a loss of engineering evidence.\n'
                 '\n'
                 'Version control exists to preserve the history of change in a structured, inspectable way.\n'
                 '\n'
                 'Git lets you ask questions that ordinary folders cannot answer well. What changed? Who changed it? '
                 'When did it change? Why was the change made? Which version was known to work? Can I compare the '
                 'current state with that version? Can I safely experiment without destroying the stable line of '
                 'work? Can two people contribute without emailing project folders back and forth?\n'
                 '\n'
                 'Git does not eliminate mistakes. It makes change observable, reviewable, and recoverable.\n'
                 '\n'
                 'That is why Git belongs near the beginning of a DevOps curriculum. Nearly every later skill in '
                 'Ascend will interact with version-controlled files. Dockerfiles live in repositories. CI/CD '
                 'pipelines are triggered by repository changes. Terraform configuration is version controlled. '
                 'Kubernetes manifests are version controlled. Application source code, scripts, documentation, and '
                 'deployment configuration are all commonly managed through Git.\n'
                 '\n'
                 'To use Git well, begin with one distinction: Git is not GitHub, and Git is not GitLab.\n'
                 '\n'
                 'Git is the version control system. It can run locally on your Mac with no internet connection and '
                 'no account on a hosting service. A Git repository can exist entirely on your computer.\n'
                 '\n'
                 'GitHub and GitLab are platforms that can host Git repositories and add collaboration features such '
                 'as pull or merge requests, issue tracking, permissions, automation, and web interfaces. You can '
                 'use Git without GitHub. You can use Git without GitLab. When you run a command such as git status '
                 'or git commit, Git is doing local work. When you push to a remote repository, Git communicates '
                 'with a server such as GitHub or GitLab.\n'
                 '\n'
                 'That local-versus-remote distinction will matter throughout this module.\n'
                 '\n'
                 'Now let us define a repository.\n'
                 '\n'
                 'A Git repository is a project whose history Git tracks. When a normal directory becomes a Git '
                 'repository, Git stores its internal history and metadata in a hidden dot-git directory. You '
                 'normally do not edit that directory by hand. Instead, Git commands read and update it for you.\n'
                 '\n'
                 'The files you can see and edit are often called the working tree or working directory. This is '
                 'your current checkout of the project.\n'
                 '\n'
                 'Suppose you open AscendAudioPlayer dot J S X and change the displayed narrator from Ascend '
                 'Narrator A to Archer. The file in your working tree is now different from the version recorded by '
                 'the most recent commit. Git can detect that difference.\n'
                 '\n'
                 'This gives us one of the most useful commands you will ever learn: git status.\n'
                 '\n'
                 'Git status does not change your project. It reports state. It tells you which branch you are on, '
                 'which files are modified, which changes are staged, and which files Git is not yet tracking.\n'
                 '\n'
                 'Notice how well that fits Evidence Before Action.\n'
                 '\n'
                 'Before committing, pulling, switching branches, or trying to recover from a mistake, git status is '
                 'often one of the safest first observations you can make.\n'
                 '\n'
                 'The next concept is the staging area.\n'
                 '\n'
                 'A common beginner model says that Git simply saves your project whenever you commit. That is '
                 'incomplete. Git gives you an intermediate step where you choose what should belong to the next '
                 'commit.\n'
                 '\n'
                 "Imagine that while working on Ascend you change three files. One change fixes Archer's display "
                 'name. Another contains unfinished experiments. A third is an accidental debug edit. You may want '
                 'the Archer change in the next commit without including the other two.\n'
                 '\n'
                 'The staging area lets you prepare that exact set of changes.\n'
                 '\n'
                 'When you run git add on a file, you are not uploading it to GitHub and you are not permanently '
                 'saving a commit. You are telling Git, in effect, include the current version of this change in the '
                 'next snapshot I create.\n'
                 '\n'
                 "Then git commit records the staged snapshot in the repository's history.\n"
                 '\n'
                 'A commit is more than a save button. It is a named point in the history of the project. Each '
                 'commit has a unique identifier, author information, a timestamp, a message, and a relationship to '
                 'earlier commits. Git uses these relationships to form a history of how the project evolved.\n'
                 '\n'
                 'Good commits create useful evidence.\n'
                 '\n'
                 'Consider two commit messages.\n'
                 '\n'
                 'The first says, quote, stuff, end quote.\n'
                 '\n'
                 'The second says, quote, integrate Archer Gold Master narration for Module 0, end quote.\n'
                 '\n'
                 'Months later, the second message tells you something meaningful. Combined with the actual diff, it '
                 'helps explain why the repository changed.\n'
                 '\n'
                 'A diff is the difference between versions of files. Git can show lines that were added, removed, '
                 'or modified. This is powerful because engineering work is often easier to understand as a change '
                 'than as an entire file.\n'
                 '\n'
                 'You have already experienced this in our Ascend and Forge workflow. Replacing an entire project '
                 'folder creates a huge surface area. A focused replacement file is easier to inspect. A small '
                 'commit is easier to understand. If something breaks, a narrow change is easier to investigate and '
                 'reverse.\n'
                 '\n'
                 'This is one reason small, purposeful commits are a DevOps habit rather than merely a Git '
                 'preference.\n'
                 '\n'
                 'Now let us look at a simple local workflow.\n'
                 '\n'
                 'First, git status. Observe the repository.\n'
                 '\n'
                 'Second, make a focused change.\n'
                 '\n'
                 'Third, git diff. Inspect what changed before deciding to preserve it.\n'
                 '\n'
                 'Fourth, git add followed by the path you intend to stage.\n'
                 '\n'
                 'Fifth, git diff dash dash staged. Inspect what the next commit will contain.\n'
                 '\n'
                 'Sixth, git commit dash m followed by a useful message.\n'
                 '\n'
                 'Seventh, git status again. Verify the repository is in the state you expect.\n'
                 '\n'
                 'The commands are easy to memorize. The engineering behavior behind them matters more: observe, '
                 'change deliberately, inspect, stage intentionally, verify, record.\n'
                 '\n'
                 'There is another distinction we need before moving on: commit is not push.\n'
                 '\n'
                 'A commit is created in your local Git repository. If your Mac is offline, you can still create '
                 'commits.\n'
                 '\n'
                 'Push sends local commits to a configured remote repository.\n'
                 '\n'
                 'That explains a question that often appears when working across machines: if you create several '
                 'commits locally and have not pushed them yet, another machine cannot pull those commits from the '
                 'remote because the remote does not have them. Once you push the branch, the remote receives those '
                 'commits. Another machine can then fetch or pull them.\n'
                 '\n'
                 'Think of it as three locations: your working tree, your local repository history, and the remote '
                 'repository.\n'
                 '\n'
                 'A file can be changed in the working tree but not committed. A commit can exist locally but not be '
                 'pushed. A commit can exist on the remote while another computer has not fetched it yet.\n'
                 '\n'
                 'When you understand those locations, many Git mysteries stop being mysterious.\n'
                 '\n'
                 'This also explains why git status is local evidence. It tells you about the repository and working '
                 'tree on the machine where you run it. It does not automatically prove what is on another '
                 'computer.\n'
                 '\n'
                 'Later in this module, we will go much deeper into branches, remotes, pull and fetch, merge '
                 'conflicts, tags, recovery, and collaborative review. For now, the goal is to build the mental '
                 'model that makes those features understandable.\n'
                 '\n'
                 'Let us also address a fear that many people have when learning Git: the command line can make Git '
                 'look dangerous.\n'
                 '\n'
                 'Some Git commands can absolutely discard work if used carelessly. But the answer is not to avoid '
                 'Git or memorize recovery commands without understanding them. The answer is to inspect state '
                 'before acting and choose the least destructive operation that accomplishes your goal.\n'
                 '\n'
                 'If you are uncertain, stop and gather evidence.\n'
                 '\n'
                 'Run git status. Read the output.\n'
                 '\n'
                 'Run git diff. See what is actually different.\n'
                 '\n'
                 'Run git log with a small number of entries. Inspect recent history.\n'
                 '\n'
                 'Ask whether the change is committed, staged, unstaged, untracked, local, or remote.\n'
                 '\n'
                 'Those words describe different states. Recovery becomes much safer when you identify the state '
                 'first.\n'
                 '\n'
                 'This is the Git version of Evidence Before Action.\n'
                 '\n'
                 'There is one final idea I want you to carry into every lesson in this module: history is part of '
                 'the product.\n'
                 '\n'
                 'The current code tells you what the system is now. Git history can tell you how it became that '
                 'way.\n'
                 '\n'
                 'When an application suddenly fails after a deployment, the difference between the known-good '
                 'commit and the deployed commit may be some of your strongest evidence. When a configuration value '
                 'changes unexpectedly, Git history may show when and why. When two engineers disagree about what a '
                 'file used to contain, the repository can provide an inspectable record instead of relying on '
                 'memory.\n'
                 '\n'
                 'Version control turns change into data.\n'
                 '\n'
                 'That matters to DevOps because DevOps is full of change. New application versions, infrastructure '
                 'changes, configuration changes, pipeline changes, dependency updates, security patches, and '
                 'documentation updates all need to move safely through systems.\n'
                 '\n'
                 'Git gives those changes identity and history.\n'
                 '\n'
                 "For this lesson's lab, you are going to inspect a real Git repository without making any "
                 'destructive changes. You will identify the working tree, current branch, recent commits, remote '
                 'configuration, and any current modifications. Then you will explain the difference between what '
                 'exists in your files, what exists in local history, and what exists on the remote.\n'
                 '\n'
                 'Do not rush to run commands just because they are listed. Read the output. Ask what each command '
                 'proves.\n'
                 '\n'
                 'Here is the takeaway for Lesson 1.1.\n'
                 '\n'
                 'Git is not primarily a place to store code. Git is a system for preserving evidence about change.\n'
                 '\n'
                 'A strong Git workflow lets you answer what changed, why it changed, which state is trusted, and '
                 'how to move forward without losing the ability to understand or recover.\n'
                 '\n'
                 'In the next lesson, we will build on this mental model by creating and inspecting repositories '
                 'more deliberately and learning how Git sees files as untracked, modified, staged, and committed.\n'
                 '\n'
                 'For now, remember the workflow: observe, change, inspect, stage, verify, commit.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain why version control is an engineering control rather than simply a backup system.',
                'Distinguish Git from repository-hosting platforms such as GitHub and GitLab.',
                'Describe the working tree, staging area, local commit history, and remote repository in plain '
                'language.',
                'Use read-only Git commands to gather evidence about the current state and recent history of a '
                'repository.',
                'Explain the difference between committing and pushing, and why small focused commits improve '
                'troubleshooting and recovery.'],
 'content': [{'heading': 'Why version control exists',
              'body': 'Software changes constantly. Without structured history, teams fall back to copied folders, '
                      "filenames such as 'final-v2', memory, and guesswork. Git records change as inspectable "
                      'history so an engineer can determine what changed, when it changed, why it changed, and which '
                      'earlier state was known to work.'},
             {'heading': 'Git is not GitHub or GitLab',
              'body': 'Git is the distributed version control system running on your computer. GitHub and GitLab are '
                      'services that can host Git repositories and add collaboration, permissions, reviews, '
                      'automation, and web interfaces. Commands such as git status, git diff, and git commit work '
                      'locally. Network access becomes relevant when you communicate with a remote.'},
             {'heading': 'The repository and working tree',
              'body': "A Git repository contains both the files you work with and Git's history. Your visible "
                      'checkout is the working tree. When you edit a tracked file, Git can compare the working copy '
                      'with the recorded version and report the difference.'},
             {'heading': 'Status before action',
              'body': 'git status is one of the safest first commands in Git. It reports the current branch and '
                      'identifies staged, unstaged, and untracked changes. It changes nothing. Before pulling, '
                      'committing, switching branches, or attempting recovery, use status to establish what is '
                      'true.'},
             {'heading': 'A change is not automatically a commit',
              'body': 'Editing a file changes the working tree. Git does not automatically place that change into '
                      'history. This separation is intentional: it gives you time to inspect and decide what belongs '
                      'in the next recorded snapshot.'},
             {'heading': 'The staging area',
              'body': 'The staging area lets you construct the next commit deliberately. git add stages selected '
                      'content; it does not push anything to a server. This matters when several files are modified '
                      'but only one focused change is ready to preserve.'},
             {'heading': 'Commits are evidence',
              'body': 'A commit records a snapshot plus metadata and a relationship to earlier history. Useful '
                      'commit messages explain the purpose of the change. Small, focused commits make reviews, '
                      'troubleshooting, rollback decisions, and future investigation easier.'},
             {'heading': 'Inspect the diff',
              'body': 'git diff shows how files differ from a recorded or staged state. Instead of rereading an '
                      'entire file, you can inspect the exact lines that changed. git diff --staged is especially '
                      'valuable immediately before committing because it shows the content you are preparing to '
                      'record.'},
             {'heading': 'Commit is not push',
              'body': 'A commit exists in your local repository. A push transfers local commits to a configured '
                      'remote. You can make several commits while offline; another computer cannot pull those '
                      'commits until they have been pushed somewhere that computer can reach.'},
             {'heading': 'Three useful locations',
              'body': 'Think about Git state in three broad locations: files in your working tree, commits in your '
                      'local repository, and commits available from a remote repository. A change can exist in one '
                      'location without yet existing in the others.'},
             {'heading': 'Small changes reduce risk',
              'body': 'Focused changes are easier to understand and reverse. This is the same reason replacing one '
                      'Ascend lesson file is safer than replacing an entire project folder. Git works best when the '
                      'history tells a sequence of understandable engineering decisions.'},
             {'heading': 'Evidence Before Action applies to Git',
              'body': 'When Git feels confusing, avoid reaching immediately for destructive commands. Determine '
                      'whether the work is untracked, modified, staged, committed, pushed, or only present on '
                      'another branch or remote. Recovery is safer after the state is known.'},
             {'heading': 'History is operational evidence',
              'body': 'DevOps systems change through application commits, Dockerfiles, pipeline definitions, '
                      'infrastructure code, configuration, and documentation. Comparing a failing deployment with a '
                      'known-good commit can turn repository history into incident evidence.'},
             {'heading': 'A deliberate local loop',
              'body': 'A strong beginner workflow is: git status → make a focused change → git diff → git add → git '
                      'diff --staged → git commit → git status. The value is not the command sequence alone; it is '
                      'the habit of observing, inspecting, recording, and verifying.'},
             {'heading': "Alex's Engineering Notes",
              'body': 'Do not use git add . as a reflex until you know what it will stage. Do not use force, reset '
                      '--hard, clean, or checkout-based discard operations just because a search result says they '
                      'fix something. First identify the state you are trying to change.'},
             {'heading': 'Takeaway',
              'body': 'Git is a system for preserving evidence about change. The goal is not to memorize commands; '
                      'it is to make change observable, intentional, reviewable, and recoverable.'}],
 'diagram': {'title': 'From edit to shared history',
             'description': 'A change moves through distinct states. Knowing the current state tells you which Git '
                            'operation is appropriate.',
             'nodes': [{'label': 'Working tree', 'detail': 'You edit files in the current checkout.'},
                       {'label': 'Staging area', 'detail': 'git add selects content for the next commit.'},
                       {'label': 'Local history', 'detail': 'git commit records the staged snapshot.'},
                       {'label': 'Remote repository', 'detail': 'git push publishes local commits to a remote.'},
                       {'label': 'Another machine', 'detail': 'fetch or pull can obtain remote commits later.'}],
             'caption': 'Editing, staging, committing, and pushing are separate operations. Treating them as '
                        'separate states makes Git much easier to reason about.'},
 'engineer_perspective': {'title': 'A clean history makes incidents easier',
                          'body': 'Imagine a deployment begins failing after five unrelated changes are bundled into '
                                  'one giant commit. Investigation must untangle all five at once. If each '
                                  'purposeful change has its own commit, the team can compare, test, review, or '
                                  'revert with much greater confidence. Repository hygiene becomes operational '
                                  'reliability.'},
 'try_it_yourself': {'title': 'Read a repository before changing it',
                     'intro': 'Use the Ascend repository for this exercise. Every command below is observational; '
                              'none should modify tracked files or repository history.',
                     'steps': ['From ~/Projects/Ascend, run git status. Identify the current branch and whether the '
                               'working tree contains staged, unstaged, or untracked changes.',
                               'Run git log --oneline -5. Read the five commit messages and identify which one most '
                               'clearly communicates intent.',
                               'Run git remote -v. Identify the name of the remote and whether fetch and push point '
                               'to the same destination.',
                               'Run git diff. If output appears, identify one changed file and explain what the diff '
                               'proves. If no output appears, explain what that does and does not prove.',
                               'Run git diff --staged. Compare its meaning with plain git diff.',
                               'Write one sentence for each state: working-tree change, staged change, local commit, '
                               'remote commit.'],
                     'takeaway': 'You can learn a great deal about a repository without changing it. '
                                 'Observation-first Git is safer Git.'},
 'lab': {'title': 'Build an evidence report for a real Git repository',
         'instructions': ['Create a Journal entry titled “Lesson 1.1 — Ascend Git Evidence Report.”',
                          'Before running any command, write what you currently believe the active branch is and '
                          'whether your latest work has been committed and pushed. Mark these as assumptions.',
                          'In ~/Projects/Ascend, run git status and record the branch plus every staged, modified, '
                          'or untracked file category that appears.',
                          'Run git log --oneline -10 and record the newest three commit identifiers and messages. '
                          'Explain what this proves about local history.',
                          'Run git remote -v and record the configured remote name. Explain why the presence of a '
                          'remote does not prove your newest local commit has been pushed.',
                          'Run git diff and git diff --staged. Record whether each command produced output and '
                          'explain the state represented by each result.',
                          'Draw a four-box model labeled Working Tree → Staging Area → Local Repository → Remote '
                          'Repository. Under each box, write the Git operation that moves work to the next box.',
                          'Choose one recent Ascend commit and explain why its message is or is not useful '
                          'engineering evidence.',
                          'Write a safe pre-commit checklist containing at least five steps. It must include git '
                          'status, inspecting the diff, and verifying staged content.',
                          "Finish with a short explanation of why 'I saved the file', 'I committed it', and 'I "
                          "pushed it' describe three different facts."]},
 'quiz': [{'question': 'What is Git?',
           'choices': ['A cloud hosting website that requires internet access',
                       'A distributed version control system that can operate locally',
                       'A replacement for the Linux filesystem',
                       'A CI/CD pipeline product only'],
           'correct': 1},
          {'question': 'You edited AscendAudioPlayer.jsx but have not run git add. Where does that change exist?',
           'choices': ['Only in the working tree',
                       'In the remote repository',
                       'In a new commit',
                       'In the staging area automatically'],
           'correct': 0},
          {'question': 'What does git add primarily do?',
           'choices': ['Uploads a file to GitHub or GitLab',
                       'Deletes the previous file version',
                       'Stages selected content for the next commit',
                       'Creates and pushes a commit'],
           'correct': 2},
          {'question': 'Why run git diff --staged before committing?',
           'choices': ['To see what the next commit is currently prepared to contain',
                       'To download remote changes',
                       'To restart Git',
                       'To delete unstaged files'],
           'correct': 0},
          {'question': 'You created three local commits but have not pushed. Can another computer pull those commits '
                       'from the remote?',
           'choices': ['Yes, commits automatically appear on every computer',
                       'No, the remote does not have those commits until they are pushed',
                       'Yes, but only if git status is clean',
                       'No, because Git supports only one computer'],
           'correct': 1},
          {'question': 'Which command is the best low-risk first observation when you are unsure about repository '
                       'state?',
           'choices': ['git status', 'git reset --hard', 'git clean -fd', 'git push --force'],
           'correct': 0},
          {'question': 'Why are small focused commits useful in DevOps work?',
           'choices': ['They make repository files smaller on disk',
                       'They remove the need for testing',
                       'They make changes easier to understand, review, troubleshoot, and reverse',
                       'They guarantee deployments cannot fail'],
           'correct': 2},
          {'question': 'Which statement about GitHub and GitLab is most accurate?',
           'choices': ['They are alternative names for the Git command-line program',
                       'Git cannot work without one of them',
                       'They can host Git repositories and provide collaboration features around Git',
                       'They are required to create a local commit'],
           'correct': 2},
          {'question': 'A clean git status proves which fact?',
           'choices': ['Production is healthy',
                       'Every local commit has definitely been pushed',
                       'The checked-out working tree has no reported staged or unstaged changes',
                       'No other branch contains newer work'],
           'correct': 2},
          {'question': 'What is the central lesson of Evidence Before Action when applied to Git?',
           'choices': ['Use destructive recovery commands quickly',
                       'Identify whether work is untracked, modified, staged, committed, or remote before choosing '
                       'an action',
                       'Always stage every changed file together',
                       'Never use the command line'],
           'correct': 1}],
 'reflection': 'Think about a time you copied a project folder, worried about losing a working version, or wondered '
               'whether commits had reached another machine. How would the working tree → staging area → local '
               'history → remote model have made that situation clearer? Describe one Git habit you want to make '
               'automatic before Lesson 1.2.'}
