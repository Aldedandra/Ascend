"""Module 1, Lesson 6: Remotes, Fetch, Pull & Push."""

LESSON = {'id': '1-6',
 'title': 'Remotes, Fetch, Pull & Push',
 'summary': 'Connect local Git history to remote repositories and learn the distinct roles of origin, '
            'remote-tracking branches, fetch, pull, push, clone, and upstream tracking.',
 'duration_minutes': 65,
 'xp': 70,
 'audio_script': 'Welcome back to Module 1 of Ascend: Git and Collaborative Source Control.\n'
                 '\n'
                 'Up to this point, most of our Git work has happened inside one repository on one machine. You have '
                 'created commits, branches, and merges. Now we are going to connect that local history to another '
                 'repository.\n'
                 '\n'
                 'That brings us to remotes.\n'
                 '\n'
                 'A remote is a named reference to another Git repository.\n'
                 '\n'
                 'That other repository may live on GitHub, GitLab, a company Git server, another machine, or even '
                 'another directory on your own computer.\n'
                 '\n'
                 'The important idea is that Git is distributed.\n'
                 '\n'
                 'Your local repository is not merely a thin client connected to a central database. It contains its '
                 'own Git history. You can create commits locally without being connected to GitHub or GitLab.\n'
                 '\n'
                 'This leads to one of the most important distinctions in everyday Git work.\n'
                 '\n'
                 'Commit does not mean push.\n'
                 '\n'
                 'When you run git commit, you record a commit in your local repository.\n'
                 '\n'
                 'When you run git push, you communicate appropriate local history to a remote repository.\n'
                 '\n'
                 'Those are separate actions.\n'
                 '\n'
                 'Imagine you make three commits on your Mac while working on Ascend.\n'
                 '\n'
                 'Commit one adds a lesson.\n'
                 '\n'
                 'Commit two fixes its registration.\n'
                 '\n'
                 'Commit three adjusts the audio player.\n'
                 '\n'
                 'If you have not pushed, those commits can exist only in your local repository.\n'
                 '\n'
                 'When you later push the branch, Git can send the commits the remote does not already have.\n'
                 '\n'
                 'You do not need to push after every single commit.\n'
                 '\n'
                 'Likewise, another machine does not need to pull each commit one at a time. If several commits are '
                 'available upstream, synchronization can bring the branch forward through that history.\n'
                 '\n'
                 'Now let us discuss remote names.\n'
                 '\n'
                 'When you clone a repository, Git commonly creates a remote named origin.\n'
                 '\n'
                 'Origin is a convention, not a magical server.\n'
                 '\n'
                 'It is simply a name stored in your local repository that maps to a remote location.\n'
                 '\n'
                 'Run git remote dash v to inspect configured remotes and their fetch and push locations.\n'
                 '\n'
                 'Before pushing somewhere important, this is valuable evidence.\n'
                 '\n'
                 'Do not assume origin points where you think it does.\n'
                 '\n'
                 'Inspect it.\n'
                 '\n'
                 'A repository can have more than one remote. For example, an open-source workflow might use origin '
                 'for your fork and upstream for the original project.\n'
                 '\n'
                 'The names are chosen by humans. The important thing is knowing what each name references.\n'
                 '\n'
                 'Now we need to distinguish local branches from remote-tracking branches.\n'
                 '\n'
                 'Suppose your local branch is main.\n'
                 '\n'
                 'After communicating with origin, you may also see a reference named origin slash main.\n'
                 '\n'
                 'Origin slash main is not the remote server itself, and it is not exactly the same thing as your '
                 'local main branch.\n'
                 '\n'
                 "It is a local reference that records Git's knowledge of the main branch from the remote named "
                 'origin as of your most recent relevant communication.\n'
                 '\n'
                 'This mental model helps explain fetch.\n'
                 '\n'
                 'git fetch contacts the remote and updates your local knowledge of remote references and objects '
                 'without automatically merging those changes into your currently checked-out branch.\n'
                 '\n'
                 'That makes fetch an excellent evidence-gathering command.\n'
                 '\n'
                 "Suppose your local main is at commit C, but a teammate has pushed commit D to origin's main "
                 'branch.\n'
                 '\n'
                 'Before fetching, your local repository may not know about D.\n'
                 '\n'
                 'Run git fetch origin.\n'
                 '\n'
                 'Git retrieves the new information.\n'
                 '\n'
                 'Your local main can remain at C while origin slash main moves to D.\n'
                 '\n'
                 'Now you can inspect the difference before integrating it.\n'
                 '\n'
                 'That separation is powerful.\n'
                 '\n'
                 'Fetching answers: what changed on the remote?\n'
                 '\n'
                 'It does not automatically answer: should I integrate it into my current branch right now?\n'
                 '\n'
                 'You can inspect git status, git log, or a diff between references and make a deliberate decision.\n'
                 '\n'
                 'Now let us talk about git pull.\n'
                 '\n'
                 'At a high level, git pull combines fetching with an integration step.\n'
                 '\n'
                 'The exact integration behavior can depend on configuration and options. A pull may merge fetched '
                 'changes, or in some workflows it may rebase them.\n'
                 '\n'
                 'For now, the important lesson is that pull does more than fetch.\n'
                 '\n'
                 'Fetch updates your knowledge.\n'
                 '\n'
                 'Pull fetches and then attempts to integrate according to the configured or requested behavior.\n'
                 '\n'
                 'This is why git pull can sometimes produce a merge conflict.\n'
                 '\n'
                 'The conflict is not because downloading failed. The fetch portion may have succeeded. The conflict '
                 'can occur during integration of remote history with your local history.\n'
                 '\n'
                 'If you want to inspect before integrating, fetch gives you that pause.\n'
                 '\n'
                 'Now let us discuss push.\n'
                 '\n'
                 'git push sends local commits and updates a branch on a remote when the remote accepts the update.\n'
                 '\n'
                 'A common command is git push origin main.\n'
                 '\n'
                 'In plain language: take the appropriate history from my local main branch and update main on the '
                 'remote named origin.\n'
                 '\n'
                 'But Git will not always accept the push.\n'
                 '\n'
                 'Suppose someone else pushed new commits to the remote main after your last synchronization.\n'
                 '\n'
                 "Your local main no longer contains the remote's latest history.\n"
                 '\n'
                 'A normal push may be rejected as non-fast-forward.\n'
                 '\n'
                 'That rejection protects remote history.\n'
                 '\n'
                 'Do not respond by immediately force-pushing.\n'
                 '\n'
                 'First gather evidence.\n'
                 '\n'
                 'Run git status.\n'
                 '\n'
                 'Fetch from the remote.\n'
                 '\n'
                 'Inspect how the histories differ.\n'
                 '\n'
                 "Then integrate appropriately for your team's workflow.\n"
                 '\n'
                 'After your branch contains the required remote history and the result is verified, a normal push '
                 'may succeed.\n'
                 '\n'
                 'A rejected push is often Git telling you that your model of the shared history is stale.\n'
                 '\n'
                 'That is useful information.\n'
                 '\n'
                 'Now consider upstream tracking.\n'
                 '\n'
                 'A local branch can be configured to track a remote branch.\n'
                 '\n'
                 'For example, local main may track origin slash main.\n'
                 '\n'
                 'When tracking is configured, git status can tell you whether your branch is ahead of, behind, or '
                 'has diverged from its upstream.\n'
                 '\n'
                 'This language is extremely useful.\n'
                 '\n'
                 'Ahead means your local branch contains commits the tracked remote reference does not.\n'
                 '\n'
                 'Behind means the remote-tracking reference contains commits your local branch does not.\n'
                 '\n'
                 'Diverged means both sides contain unique commits.\n'
                 '\n'
                 'Remember that this comparison depends on your local knowledge. If you have not fetched recently, '
                 'your view of the remote can be stale.\n'
                 '\n'
                 'Again: evidence has a timestamp.\n'
                 '\n'
                 'Now let us connect this to cloning.\n'
                 '\n'
                 'git clone creates a new local repository based on an existing repository and normally configures a '
                 'remote named origin.\n'
                 '\n'
                 "It also checks out an initial branch according to the repository's configuration.\n"
                 '\n'
                 'A clone is not merely a folder download.\n'
                 '\n'
                 'You receive Git objects and history so the new local repository can participate in distributed '
                 'version control.\n'
                 '\n'
                 'This is why you can inspect old commits locally after cloning.\n'
                 '\n'
                 'Now imagine your Mac and your home server.\n'
                 '\n'
                 'You work on Ascend on the Mac and create several commits.\n'
                 '\n'
                 'Those commits are local until you push them to the shared remote.\n'
                 '\n'
                 'On the home server, a pull can then retrieve and integrate the remote history.\n'
                 '\n'
                 'If three new commits were pushed, the home server does not require three separate pull commands. '
                 'Git works with the branch history and can bring the local branch forward across those commits as '
                 'appropriate.\n'
                 '\n'
                 'This is the practical answer to a common question: commits accumulate locally, pushes publish '
                 'history, and pulls synchronize another repository with remote history.\n'
                 '\n'
                 'Now let us make the workflow safe enough to practice without touching a real hosting service.\n'
                 '\n'
                 'Your lab will use a bare repository.\n'
                 '\n'
                 "A bare Git repository has Git's repository data but no normal checked-out working tree.\n"
                 '\n'
                 'Bare repositories are commonly suitable as shared repositories because users do not directly edit '
                 'working files inside them.\n'
                 '\n'
                 'You will create a bare repository in a temporary practice directory and use it as a fake remote.\n'
                 '\n'
                 'Then you will create a working repository, make a commit, add the bare repository as origin, and '
                 'push main.\n'
                 '\n'
                 'Next, you will clone that bare repository into a second working directory.\n'
                 '\n'
                 'Now you have a miniature distributed system on one computer.\n'
                 '\n'
                 'Repository A can represent your Mac.\n'
                 '\n'
                 'The bare repository can represent GitHub or GitLab.\n'
                 '\n'
                 'Repository B can represent another developer or your home server.\n'
                 '\n'
                 'You will create and push commits from Repository A.\n'
                 '\n'
                 'Then you will fetch from Repository B and inspect origin slash main before integrating.\n'
                 '\n'
                 'This will let you see the difference between fetch and pull rather than memorizing definitions.\n'
                 '\n'
                 'You will also create a situation where Repository B is behind.\n'
                 '\n'
                 'Then you will synchronize it.\n'
                 '\n'
                 'If time permits, you can create independent commits in both working repositories and observe what '
                 'happens when one tries to push after the remote has advanced.\n'
                 '\n'
                 'The goal is not to manufacture disaster.\n'
                 '\n'
                 'The goal is to see Git protect shared history.\n'
                 '\n'
                 'Now we need to discuss force push.\n'
                 '\n'
                 'You will encounter git push dash dash force in tutorials and troubleshooting posts.\n'
                 '\n'
                 'Do not treat it as a standard solution to a rejected push.\n'
                 '\n'
                 "Force pushing can rewrite a remote branch in ways that discard or hide other people's reachable "
                 'history from that branch.\n'
                 '\n'
                 'There are legitimate workflows that rewrite history, and later we can discuss safer variants such '
                 'as force with lease.\n'
                 '\n'
                 'But your current default should be simple.\n'
                 '\n'
                 'If a normal push is rejected, stop and inspect why.\n'
                 '\n'
                 'Do not overpower the safety mechanism before you understand what it is protecting.\n'
                 '\n'
                 'This principle applies broadly in engineering.\n'
                 '\n'
                 'A guardrail is evidence.\n'
                 '\n'
                 'Understand it before bypassing it.\n'
                 '\n'
                 'Now let us look at a practical pre-push routine.\n'
                 '\n'
                 'Run git status.\n'
                 '\n'
                 'Confirm the current branch.\n'
                 '\n'
                 'Inspect recent commits with git log dash dash oneline.\n'
                 '\n'
                 'Run git remote dash v if there is any uncertainty about the destination.\n'
                 '\n'
                 'Fetch when shared history may have changed.\n'
                 '\n'
                 'Understand whether you are ahead, behind, or diverged.\n'
                 '\n'
                 'Run relevant tests.\n'
                 '\n'
                 'Then push intentionally.\n'
                 '\n'
                 'After pushing, inspect the result.\n'
                 '\n'
                 'Git often reports the remote and branch update directly.\n'
                 '\n'
                 'You can also fetch or inspect status as appropriate to verify your local understanding.\n'
                 '\n'
                 'This may sound slower than simply typing git push.\n'
                 '\n'
                 'In practice, the habit becomes fast, and it prevents expensive mistakes.\n'
                 '\n'
                 'Now let us connect remotes to branches.\n'
                 '\n'
                 'A local feature branch does not automatically exist on a remote merely because it exists locally.\n'
                 '\n'
                 'The first push may establish the remote branch and its upstream relationship.\n'
                 '\n'
                 'A common pattern is git push dash u origin feature-name.\n'
                 '\n'
                 'The dash u option is shorthand for setting the upstream relationship.\n'
                 '\n'
                 'After that, Git may be able to infer the remote destination for simpler push and pull commands, '
                 'depending on configuration.\n'
                 '\n'
                 'Again, do not memorize flags without understanding the relationship.\n'
                 '\n'
                 'Local branch.\n'
                 '\n'
                 'Remote name.\n'
                 '\n'
                 'Remote branch.\n'
                 '\n'
                 'Tracking relationship.\n'
                 '\n'
                 'Those are separate concepts.\n'
                 '\n'
                 'Now consider remote deletion or renaming.\n'
                 '\n'
                 'Remote branches can disappear or change, and your local remote-tracking references may become '
                 'stale until Git updates them.\n'
                 '\n'
                 'Git provides options such as pruning to clean up remote-tracking references that no longer exist '
                 'remotely.\n'
                 '\n'
                 'We do not need to make cleanup the focus today.\n'
                 '\n'
                 'The larger lesson is that origin slash branch represents local knowledge of remote state, not a '
                 'live magical connection.\n'
                 '\n'
                 'Your repository learns through communication.\n'
                 '\n'
                 'Now let us connect this to DevOps.\n'
                 '\n'
                 'Remote repositories are often more than storage.\n'
                 '\n'
                 'A push may trigger CI.\n'
                 '\n'
                 'A pull or merge request may start tests.\n'
                 '\n'
                 'Branch protections may require approvals.\n'
                 '\n'
                 'A tag may trigger a release pipeline.\n'
                 '\n'
                 'A commit reaching main may begin deployment.\n'
                 '\n'
                 'The Git event becomes an input to automation.\n'
                 '\n'
                 'This is why Git discipline matters beyond developers.\n'
                 '\n'
                 'The shape of commits, branches, and remote updates can influence build systems, deployment '
                 'systems, audit trails, and incident response.\n'
                 '\n'
                 'Version control becomes part of the delivery platform.\n'
                 '\n'
                 'Here is the takeaway for Lesson 1.6.\n'
                 '\n'
                 'Your local repository owns its own history.\n'
                 '\n'
                 'A commit records history locally.\n'
                 '\n'
                 'A remote is another repository referenced by a name such as origin.\n'
                 '\n'
                 'Fetch updates your local knowledge of remote history without automatically integrating it into '
                 'your current branch.\n'
                 '\n'
                 'Pull fetches and then integrates according to the chosen behavior.\n'
                 '\n'
                 'Push sends appropriate local history to a remote.\n'
                 '\n'
                 "Remote-tracking references such as origin slash main represent your local repository's knowledge "
                 'of remote branches.\n'
                 '\n'
                 'And when a push is rejected, do not immediately force it.\n'
                 '\n'
                 'Inspect the histories and understand what Git is protecting.\n'
                 '\n'
                 'Commit locally.\n'
                 '\n'
                 'Inspect deliberately.\n'
                 '\n'
                 'Synchronize intentionally.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain why committing and pushing are separate operations in distributed Git.',
                'Inspect configured remotes and explain the conventional role of origin.',
                'Distinguish a local branch such as main from a remote-tracking reference such as origin/main.',
                'Explain and practice the different effects of git fetch, git pull, and git push.',
                'Recognize ahead, behind, and diverged states and respond safely to a rejected push.'],
 'content': [{'heading': 'Git is distributed',
              'body': 'A local Git repository contains its own history. You can create commits without a network '
                      'connection or a hosting service. Remote synchronization is a separate operation.'},
             {'heading': 'Commit is not push',
              'body': 'git commit records a snapshot in the local repository. git push communicates appropriate '
                      'local history to a remote. Several local commits can accumulate before one push publishes '
                      'them.'},
             {'heading': 'A remote is another repository',
              'body': 'A remote is a locally configured name for another Git repository. It might live on GitHub, '
                      'GitLab, a company server, another machine, or even another directory.'},
             {'heading': 'Origin is a convention',
              'body': 'Cloning commonly creates a remote named origin, but origin is not magical. Use git remote -v '
                      'to inspect where configured fetch and push operations actually point.'},
             {'heading': 'Local versus remote-tracking branches',
              'body': 'main is a local branch. origin/main is a local remote-tracking reference representing your '
                      "repository's knowledge of main on the remote named origin after relevant communication."},
             {'heading': 'Fetch gathers evidence',
              'body': 'git fetch contacts a remote and updates remote-tracking information and objects without '
                      'automatically integrating those changes into your checked-out branch. This gives you an '
                      'inspection point.'},
             {'heading': 'Pull fetches and integrates',
              'body': 'git pull performs a fetch followed by an integration step. The integration behavior can '
                      'depend on configuration and options, so pull can have more consequences than fetch alone.'},
             {'heading': 'Push publishes local history',
              'body': 'git push sends commits and requests a remote branch update. A command such as git push origin '
                      'main names both the remote and the local branch whose history should update the corresponding '
                      'destination.'},
             {'heading': 'Push rejection is protection',
              'body': 'If the remote has history your local branch does not contain, a normal push may be rejected. '
                      'Fetch and inspect before deciding how to integrate. Do not make force push the reflex.'},
             {'heading': 'Ahead, behind, and diverged',
              'body': 'With upstream tracking, Git can describe whether a local branch has unique commits, lacks '
                      'known remote commits, or both sides have unique history. Fetch first when freshness matters.'},
             {'heading': 'Clone creates a participating repository',
              'body': 'git clone creates a local Git repository from an existing one and normally configures origin. '
                      'It brings repository history and objects, not merely a folder of current files.'},
             {'heading': 'Upstream tracking',
              'body': 'A local branch can track a remote branch. git push -u origin feature-name is a common way to '
                      'publish a branch while setting its upstream relationship for future status and '
                      'synchronization commands.'},
             {'heading': 'Multiple commits synchronize together',
              'body': 'If your Mac creates and pushes several commits, another repository can synchronize that '
                      'branch history without pulling each commit individually. Git moves through commit '
                      'relationships, not a queue of manual downloads.'},
             {'heading': 'Practice with a bare repository',
              'body': 'A bare repository has Git repository data without a normal checked-out working tree. It can '
                      'serve as a safe local stand-in for a shared remote during the lab.'},
             {'heading': "Alex's Engineering Notes",
              'body': 'Before a consequential push, verify the current branch, recent commits, remote destination, '
                      'and synchronization state. A rejected push is information about history, not permission to '
                      'bypass safeguards.'},
             {'heading': 'Takeaway',
              'body': 'Commit locally, fetch to learn, pull when you intend to fetch and integrate, and push when '
                      'you intend to publish. Treat remote state as something your local repository learns through '
                      'communication.'}],
 'diagram': {'title': 'Three repositories, one distributed history',
             'description': 'A local practice setup can model a developer machine, a shared remote, and another '
                            'machine.',
             'nodes': [{'label': 'Repository A', 'detail': 'Working repository where new local commits are created.'},
                       {'label': 'push', 'detail': 'Publishes appropriate commits to the shared repository.'},
                       {'label': 'origin.git', 'detail': 'Bare repository acting as the shared remote.'},
                       {'label': 'fetch',
                        'detail': 'Repository B updates its knowledge of the shared history without automatically '
                                  'integrating it.'},
                       {'label': 'Repository B',
                        'detail': 'A second working repository with its own local branch and origin/main reference.'},
                       {'label': 'integrate',
                        'detail': 'Pull or another deliberate integration step moves local work toward the fetched '
                                  'remote history.'}],
             'caption': 'Git collaboration is repository-to-repository synchronization. Each working repository '
                        'maintains its own local state and history.'},
 'engineer_perspective': {'title': 'A push can be a delivery event',
                          'body': 'In modern DevOps systems, updating a remote branch may trigger builds, tests, '
                                  'security scans, reviews, releases, or deployments. Pushing is therefore not '
                                  'merely backing up files; it can be an input to an automated delivery system.'},
 'try_it_yourself': {'title': "Inspect Ascend's remote state safely",
                     'intro': 'Use the real Ascend repository for read-only inspection. Do not push or pull during '
                              'this exercise.',
                     'steps': ['From ~/Projects/Ascend, run git status and record the current branch and any '
                               'ahead/behind message.',
                               'Run git remote -v and identify each configured remote name and destination.',
                               'Run git branch -vv and inspect whether the current branch has an upstream tracking '
                               'branch.',
                               'Run git log --oneline -8 and identify the newest local commits.',
                               'If origin/main exists, run git log --oneline --decorate --graph --all -12 and '
                               'compare the positions of main and origin/main.',
                               'Explain in your Journal what evidence you would want before pushing this '
                               'repository.'],
                     'takeaway': 'Never assume where a push will go or whether your remote knowledge is current. '
                                 'Inspect branch, remote, tracking, and history first.'},
 'lab': {'title': 'Build a Local Remote Workflow',
         'instructions': ['Create a Journal entry titled “Lesson 1.6 — Remotes Lab.”',
                          'Create a temporary practice directory containing a bare repository named origin.git with '
                          'git init --bare.',
                          'Create a working repository named repo-a, make an initial commit on main, and add the '
                          'bare repository as remote origin.',
                          'Run git remote -v and verify the destination before publishing anything.',
                          'Push main to origin and establish upstream tracking. Run git status and git branch -vv '
                          'afterward.',
                          'Clone origin.git into a second working directory named repo-b. Inspect its configured '
                          'remote and history.',
                          'In repo-a, create three separate focused commits without pushing after each one. Record '
                          'git log --oneline.',
                          'Push repo-a once. Explain why one push can publish multiple commits.',
                          'In repo-b, run git log --oneline before synchronization, then git fetch origin.',
                          'Without pulling yet, inspect git status, git branch -vv, and git log --oneline --graph '
                          '--decorate --all. Identify the difference between local main and origin/main.',
                          'Integrate the fetched history into repo-b using the workflow taught in the lesson, then '
                          'verify that all three commits are present.',
                          'Create and push one new commit from repo-a. In repo-b, observe that its remote knowledge '
                          'remains stale until another fetch or pull communicates with origin.',
                          'Optional challenge: create a local commit in repo-b while origin advances from repo-a. '
                          'Fetch and inspect the diverged histories. Do not force-push.',
                          'If you attempt a normal push from a stale or diverged branch and Git rejects it, copy the '
                          'message into your Journal and explain what history Git is protecting.',
                          'Finish with a pre-push checklist covering current branch, status, recent commits, remote '
                          'destination, synchronization state, tests, and intentional destination.']},
 'quiz': [{'question': 'What does git commit do compared with git push?',
           'choices': ['Commit records local history; push communicates appropriate history to a remote',
                       'Commit uploads files; push creates local history',
                       'They are identical operations',
                       'Push only renames commits'],
           'correct': 0},
          {'question': 'What is origin?',
           'choices': ['A conventional name for a configured remote repository',
                       "Git's mandatory cloud provider",
                       'The first commit in every repository',
                       'A special branch that cannot move'],
           'correct': 0},
          {'question': 'What does origin/main normally represent locally?',
           'choices': ["Your local repository's knowledge of main on the remote named origin",
                       'A live terminal connected to the server',
                       'A second copy of your working tree',
                       'The password for remote main'],
           'correct': 0},
          {'question': 'What is a key property of git fetch?',
           'choices': ['It updates remote knowledge without automatically integrating it into the current branch',
                       'It always merges into main',
                       'It deletes local commits',
                       'It force-pushes local history'],
           'correct': 0},
          {'question': 'At a high level, what does git pull do?',
           'choices': ['Fetches and then performs an integration step',
                       'Only lists remotes',
                       'Only creates a commit',
                       'Deletes the upstream branch'],
           'correct': 0},
          {'question': 'Why might a normal push be rejected?',
           'choices': ['The remote branch may contain history your local branch does not contain',
                       'Git forbids more than one commit per push',
                       'Every remote requires force',
                       'Your branch has a name'],
           'correct': 0},
          {'question': 'What should you generally do first after a non-fast-forward push rejection?',
           'choices': ['Fetch and inspect the histories',
                       'Immediately use --force',
                       'Delete the repository',
                       'Remove origin'],
           'correct': 0},
          {'question': 'If your branch is ahead of its tracked remote reference, what does that mean?',
           'choices': ['Your local branch contains commits the known remote-tracking reference does not',
                       'The remote deleted your files',
                       'Your repository has no commits',
                       'Fetch is impossible'],
           'correct': 0},
          {'question': 'Can one push publish several local commits?',
           'choices': ['Yes, Git can send the commits needed to update the remote history',
                       'No, exactly one push is required per commit',
                       'Only on Windows',
                       'Only if every commit has the same message'],
           'correct': 0},
          {'question': 'Why is force push not a good default response to rejection?',
           'choices': ["It can rewrite remote branch history and potentially disrupt others' work",
                       'It is another name for fetch',
                       'It only changes commit messages locally',
                       'It cannot affect a remote'],
           'correct': 0}],
 'reflection': 'Explain the difference between commit, fetch, pull, and push in your own words without using their '
               'command definitions verbatim. Then describe what you would inspect if a push from your Mac were '
               'rejected because the remote had changed.'}
