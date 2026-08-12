"""Module 1, Lesson 4: Branches: Working Without Breaking Main."""

LESSON = {'id': '1-4',
 'title': 'Branches: Working Without Breaking Main',
 'summary': 'Understand branches as movable references to commits, learn how HEAD and branch switching affect your '
            'working tree, and build parallel lines of history safely.',
 'duration_minutes': 60,
 'xp': 65,
 'audio_script': 'Welcome back to Module 1 of Ascend: Git and Collaborative Source Control.\n'
                 '\n'
                 'So far, you have learned why version control exists, how Git sees repository state, and how '
                 'deliberate staging creates meaningful history.\n'
                 '\n'
                 "Now we are ready for one of Git's most important ideas: branches.\n"
                 '\n'
                 'Branches let you develop a line of work without treating every new change as the next permanent '
                 'step on main.\n'
                 '\n'
                 'A common beginner explanation says that a branch is a copy of your code.\n'
                 '\n'
                 'That description can be useful at first, but it is not a very accurate mental model.\n'
                 '\n'
                 'In Git, a branch is better understood as a movable name that points to a commit.\n'
                 '\n'
                 'Imagine a repository with three commits in a straight line. Commit A came first. Commit B followed '
                 'it. Commit C is the newest commit.\n'
                 '\n'
                 'The branch named main points to commit C.\n'
                 '\n'
                 'When you create a new branch named feature-audio while you are on main, Git does not need to '
                 'duplicate the entire project. It creates another branch reference that initially points to the '
                 'same commit.\n'
                 '\n'
                 'At that moment, main and feature-audio can both point to commit C.\n'
                 '\n'
                 'Now switch to feature-audio and create another commit, commit D.\n'
                 '\n'
                 'The feature-audio branch moves forward to commit D. Main still points to commit C.\n'
                 '\n'
                 'The histories have begun to diverge.\n'
                 '\n'
                 'This is the foundation of branch-based development.\n'
                 '\n'
                 'Branches give names to different lines of history.\n'
                 '\n'
                 'Now we need another important term: HEAD.\n'
                 '\n'
                 'HEAD tells Git what you currently have checked out.\n'
                 '\n'
                 'In normal branch-based work, HEAD refers to the branch you are currently on.\n'
                 '\n'
                 'If HEAD is attached to main, a new commit normally advances main.\n'
                 '\n'
                 'If you switch to feature-audio, HEAD follows that branch, and a new commit advances feature-audio '
                 'instead.\n'
                 '\n'
                 'This explains something that can otherwise feel magical.\n'
                 '\n'
                 'When you switch branches, files in your working tree can change.\n'
                 '\n'
                 'Git is updating the working tree to represent the commit associated with the branch you checked '
                 'out.\n'
                 '\n'
                 'Suppose feature-audio contains a new file named audio-notes dot M D, but main does not.\n'
                 '\n'
                 'While feature-audio is checked out, the file may be present.\n'
                 '\n'
                 'Switch back to main, and the file may disappear from the working tree because main points to '
                 'history from before that file was added.\n'
                 '\n'
                 'The file was not necessarily deleted from Git history.\n'
                 '\n'
                 'You changed which history your working tree represents.\n'
                 '\n'
                 'That distinction is essential.\n'
                 '\n'
                 'Now let us look at commands.\n'
                 '\n'
                 'git branch lists local branches.\n'
                 '\n'
                 'The currently checked-out branch is normally marked in the output.\n'
                 '\n'
                 'git switch followed by a branch name switches to an existing branch.\n'
                 '\n'
                 'git switch dash c followed by a new branch name creates the branch and switches to it.\n'
                 '\n'
                 'Older tutorials often use git checkout for several different jobs, including switching branches. '
                 'You will still encounter it frequently.\n'
                 '\n'
                 'Modern Git provides git switch for branch switching and git restore for certain file-restoration '
                 'tasks, which can make intent clearer.\n'
                 '\n'
                 'You should understand that checkout exists, but in Ascend we will generally prefer git switch when '
                 'our goal is specifically to change branches.\n'
                 '\n'
                 'Now let us create a branch safely.\n'
                 '\n'
                 'In a disposable practice repository, begin from a clean main branch with at least one commit.\n'
                 '\n'
                 'Run git status.\n'
                 '\n'
                 'Before switching branches, verify the working tree is clean.\n'
                 '\n'
                 'Then run git switch dash c feature-notes.\n'
                 '\n'
                 'Run git branch.\n'
                 '\n'
                 'You should see both main and feature-notes, with feature-notes marked as current.\n'
                 '\n'
                 'Now create a file named feature dot txt, stage it, and commit it.\n'
                 '\n'
                 'Run git log dash dash oneline.\n'
                 '\n'
                 'Your new commit exists on feature-notes.\n'
                 '\n'
                 'Now switch back to main with git switch main.\n'
                 '\n'
                 'Look at the working tree.\n'
                 '\n'
                 'If feature dot txt was introduced only by the feature branch commit, it should no longer appear in '
                 'the checked-out main version.\n'
                 '\n'
                 'Run git log dash dash oneline again.\n'
                 '\n'
                 'The feature commit may no longer appear in the simple log of the current branch because main does '
                 'not contain that commit.\n'
                 '\n'
                 'But the feature branch still exists.\n'
                 '\n'
                 'Run git switch feature-notes, and the feature file and commit become visible again from that '
                 'branch.\n'
                 '\n'
                 'This is the moment branches often begin to make sense.\n'
                 '\n'
                 'You did not create two unrelated repositories.\n'
                 '\n'
                 "You created two named paths through one repository's commit graph.\n"
                 '\n'
                 'Now let us make the graph visible.\n'
                 '\n'
                 'The command git log dash dash oneline dash dash graph dash dash decorate dash dash all can show a '
                 'compact representation of commits and branch pointers.\n'
                 '\n'
                 'Do not worry about memorizing every flag immediately.\n'
                 '\n'
                 'Oneline keeps each commit compact.\n'
                 '\n'
                 'Graph draws simple branch lines.\n'
                 '\n'
                 'Decorate shows references such as branch names.\n'
                 '\n'
                 'All asks Git to include all local reference histories rather than only the current branch.\n'
                 '\n'
                 'When main and feature-notes point to different commits, this view helps you see that '
                 'relationship.\n'
                 '\n'
                 'Visual evidence is especially useful when branches become more complex.\n'
                 '\n'
                 'Why do teams use feature branches?\n'
                 '\n'
                 'One reason is isolation.\n'
                 '\n'
                 'Suppose production code on main is known to work. You need to build a new feature that will take '
                 'several commits.\n'
                 '\n'
                 'If every incomplete commit goes directly onto main, the main line may spend time in a partially '
                 'implemented state.\n'
                 '\n'
                 'A feature branch gives that work its own line of history until it is ready to integrate.\n'
                 '\n'
                 'Branches also support review.\n'
                 '\n'
                 'A team can compare a feature branch with main, discuss the changes, run automated tests, and '
                 'approve the work before integration.\n'
                 '\n'
                 'Branches also support parallel work.\n'
                 '\n'
                 'One engineer can work on an API change while another updates a user interface. Their commits can '
                 'progress independently and later be combined through a controlled integration process.\n'
                 '\n'
                 'This does not mean branches eliminate risk.\n'
                 '\n'
                 'Branches can diverge.\n'
                 '\n'
                 'Two branches may modify the same lines.\n'
                 '\n'
                 'A long-lived branch can become increasingly different from main.\n'
                 '\n'
                 'Integration can produce conflicts.\n'
                 '\n'
                 'Those are not reasons to avoid branches. They are reasons to keep work focused, integrate '
                 'regularly, and understand the history you are creating.\n'
                 '\n'
                 'We will cover merging and conflicts soon.\n'
                 '\n'
                 'For now, focus on branch identity and movement.\n'
                 '\n'
                 'There is another important safety issue: switching branches with uncommitted changes.\n'
                 '\n'
                 'Git sometimes allows you to switch branches while local modifications exist if those changes can '
                 'be carried safely into the target branch.\n'
                 '\n'
                 'Other times Git refuses because switching would overwrite work.\n'
                 '\n'
                 'A beginner can easily become confused because the modified files seem to follow them from branch '
                 'to branch.\n'
                 '\n'
                 'The safest learning habit is simple.\n'
                 '\n'
                 'Before switching branches, run git status.\n'
                 '\n'
                 'Know what is modified, staged, and untracked.\n'
                 '\n'
                 'Prefer to reach a deliberate state before switching: commit the work if it belongs in history, '
                 'stash it when you understand stashing and that is appropriate, or otherwise resolve the working '
                 'state intentionally.\n'
                 '\n'
                 'Do not treat branch switching as a way to make changes disappear.\n'
                 '\n'
                 'Evidence before action.\n'
                 '\n'
                 'Now consider branch names.\n'
                 '\n'
                 'Names should communicate purpose.\n'
                 '\n'
                 'feature/audio-resume is more useful than test2.\n'
                 '\n'
                 'fix/module1-audio-path tells you more than branch-new.\n'
                 '\n'
                 'Organizations often have conventions for prefixes such as feature, fix, hotfix, release, or '
                 'chore.\n'
                 '\n'
                 'The exact convention varies. The important principle is that branch names should help humans '
                 'understand the line of work.\n'
                 '\n'
                 'Now let us connect this to the projects you have been building.\n'
                 '\n'
                 'When a larger Forge or Ascend change is developed on a feature branch, you can make several '
                 'focused commits without immediately changing main.\n'
                 '\n'
                 'You can test the work locally.\n'
                 '\n'
                 'You can inspect the branch history.\n'
                 '\n'
                 'You can compare the branch with main.\n'
                 '\n'
                 'When the feature is ready, it can be integrated through the workflow the project uses.\n'
                 '\n'
                 'This gives main a useful role.\n'
                 '\n'
                 'Main is not magically protected by Git itself. Its stability comes from engineering practices '
                 'around it.\n'
                 '\n'
                 'Teams may use repository-hosting rules, required reviews, automated checks, protected branches, or '
                 'deployment policies.\n'
                 '\n'
                 'But the branch name alone does not guarantee quality.\n'
                 '\n'
                 'A main branch is trustworthy only when the process around it makes it trustworthy.\n'
                 '\n'
                 'This is a DevOps connection.\n'
                 '\n'
                 'Branch strategy affects delivery.\n'
                 '\n'
                 'If branches are enormous and live for months, integration becomes harder and feedback arrives '
                 'later.\n'
                 '\n'
                 'If engineers create focused changes, test continuously, and integrate frequently, the distance '
                 'between development and production can shrink.\n'
                 '\n'
                 'There is no single branching model that is correct for every organization.\n'
                 '\n'
                 'Some teams use short-lived feature branches and pull requests.\n'
                 '\n'
                 'Some use trunk-based development with very small branches or direct integration under strict '
                 'automation.\n'
                 '\n'
                 'Some products maintain release branches.\n'
                 '\n'
                 'Your goal is not to memorize one universal branch strategy.\n'
                 '\n'
                 "Your goal is to understand the Git mechanics well enough to recognize what a team's strategy is "
                 'trying to accomplish.\n'
                 '\n'
                 'Now let us discuss deleting branches.\n'
                 '\n'
                 'Once a branch has been integrated and is no longer needed, teams often delete the branch '
                 'reference.\n'
                 '\n'
                 'Deleting a branch name is not the same concept as deleting every commit that ever belonged to that '
                 'work.\n'
                 '\n'
                 'Whether commits remain reachable depends on the repository history and whether they were '
                 'integrated or referenced elsewhere.\n'
                 '\n'
                 'For now, do not practice force-deleting branches.\n'
                 '\n'
                 'Use branches to learn creation, switching, committing, and visualization. We will add cleanup when '
                 'the surrounding concepts are clear.\n'
                 '\n'
                 'Your lab will build a small commit graph.\n'
                 '\n'
                 'You will start on main, create a feature branch, add a feature-only commit, switch back to main, '
                 'create a separate main-only commit, and then inspect both lines with the graph view.\n'
                 '\n'
                 'You will not merge them yet.\n'
                 '\n'
                 'That is intentional.\n'
                 '\n'
                 'I want you to become comfortable seeing two lines of history before we teach you how to bring them '
                 'back together.\n'
                 '\n'
                 'You will also predict what files should appear before each switch.\n'
                 '\n'
                 'If your prediction is wrong, inspect git status and the graph rather than guessing.\n'
                 '\n'
                 'Here is the takeaway for Lesson 1.4.\n'
                 '\n'
                 'A branch is a movable reference to a commit.\n'
                 '\n'
                 'HEAD identifies what you currently have checked out.\n'
                 '\n'
                 'New commits advance the current branch.\n'
                 '\n'
                 'Switching branches can change the working tree because you are asking Git to represent a different '
                 'point in history.\n'
                 '\n'
                 'Feature branches isolate lines of work, support review, and allow parallel development, but they '
                 'still require disciplined integration.\n'
                 '\n'
                 'And main is not safe because it is named main.\n'
                 '\n'
                 'It is safe only when engineers and automation protect the quality of the history that reaches it.\n'
                 '\n'
                 'Observe the branch.\n'
                 '\n'
                 'Observe HEAD.\n'
                 '\n'
                 'Observe the graph.\n'
                 '\n'
                 'Then make your next move.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain a Git branch as a movable reference to a commit rather than simply a copy of a project.',
                'Explain the role of HEAD and why new commits advance the currently checked-out branch.',
                'Create, list, and switch branches with git branch and git switch.',
                'Use a graph view of history to reason about branches that point to different commits.',
                'Explain why feature branches can isolate work and why a clean, deliberate working state matters '
                'before switching branches.'],
 'content': [{'heading': 'A branch is not just a copy',
              'body': 'A useful mental model is that a Git branch is a movable name pointing to a commit. Two '
                      'branches can initially point to the same commit and later diverge as new commits advance one '
                      'branch but not the other.'},
             {'heading': 'Main is a branch too',
              'body': 'main is commonly used as the primary integration branch, but Git does not make it inherently '
                      'safer than another branch. Its trustworthiness comes from the engineering practices, reviews, '
                      'automation, and protections surrounding it.'},
             {'heading': 'HEAD tells Git what is checked out',
              'body': 'In normal branch-based work, HEAD refers to the branch you currently have checked out. A new '
                      'commit advances that current branch, which is why branch identity matters before you commit.'},
             {'heading': 'Switching branches can change files',
              'body': 'The working tree is updated to represent the checked-out history. A file introduced only on a '
                      'feature branch can appear there and disappear when you switch back to main without being lost '
                      "from the feature branch's history."},
             {'heading': 'List and switch branches',
              'body': 'git branch lists local branches. git switch <name> switches to an existing branch. git switch '
                      '-c <name> creates a new branch from the current point and switches to it.'},
             {'heading': 'Why Ascend prefers git switch',
              'body': 'Older material often uses git checkout for branch switching. Modern Git also provides git '
                      'switch for branch operations and git restore for certain restoration tasks. Using a more '
                      'specific command can make your intent clearer while you learn.'},
             {'heading': 'Watch a branch advance',
              'body': 'Create feature-notes from main and both references initially point to the same commit. Commit '
                      'feature.txt while feature-notes is checked out and feature-notes advances while main remains '
                      'at its previous commit.'},
             {'heading': 'Make the commit graph visible',
              'body': 'git log --oneline --graph --decorate --all provides a compact visualization of commits and '
                      'branch references. The flags are less important than the evidence: you can see where names '
                      'point and where histories diverge.'},
             {'heading': 'Feature branches isolate work',
              'body': 'A feature can take several commits without placing each incomplete state directly on main. '
                      'The branch can be tested and reviewed as a unit before the project integrates it.'},
             {'heading': 'Branches support parallel development',
              'body': 'Different lines of work can progress independently in the same repository. An API change and '
                      "a UI change can each have their own history and later be integrated through the team's chosen "
                      'workflow.'},
             {'heading': 'Branches do not eliminate integration risk',
              'body': 'Branches can diverge, touch the same lines, and eventually conflict. Keeping branches focused '
                      'and short-lived where practical reduces the distance that must later be reconciled.'},
             {'heading': 'Inspect before switching',
              'body': 'Uncommitted changes may sometimes follow you across branches, while Git may refuse other '
                      'switches to avoid overwriting work. Run git status first and understand your working state '
                      'rather than using branch switching to make changes disappear.'},
             {'heading': 'Name branches for humans',
              'body': 'Names such as feature/audio-resume or fix/module1-audio-path communicate purpose better than '
                      'test2. Teams use different naming conventions, but useful names make parallel work easier to '
                      'understand.'},
             {'heading': 'Branch strategy affects delivery',
              'body': 'Long-lived, highly divergent branches can delay feedback and increase integration cost. '
                      'Shorter feedback loops, focused changes, testing, and deliberate integration connect Git '
                      'branching directly to DevOps delivery practices.'},
             {'heading': "Alex's Engineering Notes",
              'body': 'Do not assume main is safe because of its name, and do not assume switching branches is '
                      'harmless when the working tree is dirty. Check git status, identify the current branch, and '
                      'inspect the graph before making consequential changes.'},
             {'heading': 'Takeaway',
              'body': 'Branches are named pointers into repository history. HEAD identifies the checked-out line of '
                      'work, commits advance that branch, and switching changes which history the working tree '
                      'represents.'}],
 'diagram': {'title': 'Two branches, one shared history',
             'description': 'A feature branch begins at the same commit as main, then advances independently when '
                            'new commits are created on it.',
             'nodes': [{'label': 'Commit A', 'detail': 'Shared earlier history.'},
                       {'label': 'Commit B', 'detail': 'Both branches include this commit.'},
                       {'label': 'Commit C', 'detail': 'main points here when the feature branch is created.'},
                       {'label': 'main', 'detail': 'Remains pointing to Commit C while feature work continues.'},
                       {'label': 'feature-notes → Commit D',
                        'detail': 'A new feature commit advances only the feature branch.'},
                       {'label': 'HEAD',
                        'detail': 'Follows the currently checked-out branch in normal branch-based work.'}],
             'caption': 'Creating a branch does not duplicate the whole repository. It creates another reference '
                        'that can move along a different line of commits.'},
 'engineer_perspective': {'title': 'Branching is a delivery decision, not just a Git trick',
                          'body': 'Branch lifetime affects feedback. A feature branch that diverges for weeks can '
                                  'accumulate integration risk, while focused work integrated through tests and '
                                  'review can surface problems earlier. Git supplies the mechanics; teams design the '
                                  'delivery policy.'},
 'try_it_yourself': {'title': "See Ascend's current branch and graph",
                     'intro': 'Use the real Ascend repository only for read-only inspection in this exercise.',
                     'steps': ['From ~/Projects/Ascend, run git status and identify the branch Git says is currently '
                               'checked out.',
                               'Run git branch and compare its current-branch marker with the status output.',
                               'Run git log --oneline --graph --decorate --all -15 and locate the current branch '
                               'name in the graph.',
                               'Identify where HEAD appears and explain what you think it is pointing to.',
                               'Look for any other local branch names. If present, identify whether they point to '
                               'the same commit as the current branch or somewhere else.',
                               'Do not switch branches in Ascend for this exercise. Record what the graph tells you '
                               'about the repository as it currently exists.'],
                     'takeaway': 'Before changing branches, learn to answer two questions from evidence: where am I '
                                 'now, and what history does each branch name point to?'},
 'lab': {'title': 'Build Two Lines of History',
         'instructions': ['Create a Journal entry titled “Lesson 1.4 — Branches Lab.”',
                          'Create a disposable Git repository with README.md committed on the primary branch. If the '
                          'initial branch is not named main, record its actual name and either use it consistently '
                          'or deliberately rename it.',
                          'Run git status, git branch, and git log --oneline --decorate. Record the evidence for '
                          'your current branch and commit.',
                          'Create and switch to feature-notes with git switch -c feature-notes.',
                          'Run git branch again and explain what changed even though no new commit has been created '
                          'yet.',
                          'Create feature.txt, stage it, commit it, and inspect git log --oneline --decorate.',
                          "Before switching back to main, predict whether feature.txt should appear in main's "
                          'working tree.',
                          'Run git status to verify a clean state, then git switch main. Check whether feature.txt '
                          "exists and compare git log with the feature branch's history.",
                          'Create main-notes.txt on main, stage it, and commit it. You now have work unique to both '
                          'branches.',
                          'Run git log --oneline --graph --decorate --all. Draw or describe the resulting commit '
                          'graph in your Journal.',
                          'Switch between main and feature-notes. Before each switch, predict which branch-only file '
                          'should be visible, then verify.',
                          'Finish by explaining why the two branches are not two separate repositories and why '
                          "neither branch has yet incorporated the other's unique commit."]},
 'quiz': [{'question': 'What is the most useful mental model for a Git branch?',
           'choices': ['A complete duplicate of the repository',
                       'A movable reference that points to a commit',
                       'A folder that Git automatically uploads',
                       'A password-protected copy of main'],
           'correct': 1},
          {'question': 'In normal branch-based work, what does HEAD identify?',
           'choices': ['The largest file in the repository',
                       'The currently checked-out branch or position',
                       'The remote server only',
                       'The oldest commit'],
           'correct': 1},
          {'question': 'You create feature-notes from main and make no commits. What is initially true?',
           'choices': ['The branches can point to the same commit',
                       'main is deleted',
                       'Git duplicates every file into another repository',
                       'The feature branch must already be ahead'],
           'correct': 0},
          {'question': 'What does git switch -c feature-notes do?',
           'choices': ['Deletes feature-notes',
                       'Creates feature-notes and switches to it',
                       'Commits every modified file',
                       'Merges feature-notes into main'],
           'correct': 1},
          {'question': 'Why can a file disappear from the working tree after switching from a feature branch to '
                       'main?',
           'choices': ['Git permanently deleted the feature history',
                       'main may point to history that does not contain that file',
                       'All branch switches erase untracked files',
                       'The remote repository rejected the file'],
           'correct': 1},
          {'question': 'Which command is useful for visualizing multiple branch histories together?',
           'choices': ['git log --oneline --graph --decorate --all',
                       'git add .',
                       'git init --delete',
                       'git ignore --everything'],
           'correct': 0},
          {'question': 'Why should you run git status before switching branches?',
           'choices': ['To understand modified, staged, or untracked work that may affect the switch',
                       'Because status automatically commits changes',
                       'Because branches cannot be switched from a clean tree',
                       'To download all remote branches'],
           'correct': 0},
          {'question': 'What makes main trustworthy in a professional workflow?',
           'choices': ['The word main itself',
                       'Engineering practices such as review, testing, automation, and branch protections',
                       'Git guarantees main contains no bugs',
                       'Main cannot receive commits'],
           'correct': 1},
          {'question': 'What is one cost of a long-lived branch that diverges heavily from main?',
           'choices': ['Git stops storing commits',
                       'Integration can become harder and feedback can arrive later',
                       'The branch automatically becomes a remote',
                       'Commit messages are erased'],
           'correct': 1},
          {'question': 'Why does this lesson intentionally stop before merging the lab branches?',
           'choices': ['Git cannot merge branches',
                       'To first understand branch identity, switching, and divergent history before learning '
                       'integration',
                       'Merging requires deleting main',
                       'Feature branches can never be combined'],
           'correct': 1}],
 'reflection': 'Before this lesson, how did you picture a Git branch? Explain how the movable-reference model '
               'changes that picture. Then describe why checking the current branch, working-tree state, and commit '
               'graph before acting could prevent a real engineering mistake.'}
