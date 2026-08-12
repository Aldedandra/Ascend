"""Module 1, Lesson 8: Git Troubleshooting & Recovery."""

LESSON = {'id': '1-8',
 'title': 'Git Troubleshooting & Recovery',
 'summary': 'Recover from Git mistakes without guessing. Diagnose repository state first, then choose the smallest '
            'safe action for untracked, modified, staged, committed, or shared work.',
 'duration_minutes': 70,
 'xp': 75,
 'audio_script': 'Welcome back to Module 1 of Ascend: Git and Collaborative Source Control.\n'
                 '\n'
                 'So far, Git has mostly been presented as a tool for creating useful history. But Git becomes '
                 'especially valuable when something goes wrong.\n'
                 '\n'
                 'You edited the wrong file. You staged something by mistake. A commit contains a problem. You '
                 'switched branches and became confused about where you are. A branch appears to have disappeared. '
                 'You need to undo a change that has already been shared.\n'
                 '\n'
                 'These situations feel dangerous when every Git command looks like an undo button.\n'
                 '\n'
                 'They become much more manageable when you begin with one principle:\n'
                 '\n'
                 'Evidence Before Action.\n'
                 '\n'
                 'Before attempting recovery, determine what state the work is actually in.\n'
                 '\n'
                 'Is the change untracked?\n'
                 '\n'
                 'Is it modified in the working tree?\n'
                 '\n'
                 'Is it staged?\n'
                 '\n'
                 'Is it committed only in your local repository?\n'
                 '\n'
                 'Has it already been pushed and shared with other people?\n'
                 '\n'
                 'Does the commit still exist but no branch currently points to it?\n'
                 '\n'
                 'The correct recovery technique depends on the answer.\n'
                 '\n'
                 'This is why git status should often be your first command.\n'
                 '\n'
                 'Status tells you the current branch and reports untracked, modified, and staged work.\n'
                 '\n'
                 'It does not solve the problem for you.\n'
                 '\n'
                 'It establishes evidence.\n'
                 '\n'
                 'Then inspect the diff.\n'
                 '\n'
                 'Plain git diff normally shows unstaged changes in tracked files.\n'
                 '\n'
                 'Git diff dash dash staged shows changes currently staged for the next commit.\n'
                 '\n'
                 'Git log shows recorded history.\n'
                 '\n'
                 'Git branch shows branch references.\n'
                 '\n'
                 'Git reflog can reveal recent movements of references such as HEAD, including commits that may no '
                 'longer be visible in ordinary branch history.\n'
                 '\n'
                 'Each command answers a different question.\n'
                 '\n'
                 'Recovery begins by asking the right question.\n'
                 '\n'
                 'Let us start with one of the safest cases: a file was staged accidentally.\n'
                 '\n'
                 'Staging is not committing.\n'
                 '\n'
                 'If a file is staged but you want to keep its edits, you usually want to remove it from the staging '
                 'area without deleting the working copy.\n'
                 '\n'
                 'Modern Git provides git restore dash dash staged followed by the file name for this purpose.\n'
                 '\n'
                 'The important mental model is that you are changing what is selected for the next commit.\n'
                 '\n'
                 'You are not necessarily discarding the file edits.\n'
                 '\n'
                 'Now consider an unwanted modification in a tracked file.\n'
                 '\n'
                 'Perhaps you changed a configuration file while experimenting and you truly want to return that '
                 'file to its recorded state.\n'
                 '\n'
                 'Git restore can restore working-tree content from a known source.\n'
                 '\n'
                 'But this deserves caution.\n'
                 '\n'
                 'If the only copy of valuable work exists as an uncommitted modification, restoring over it can '
                 'discard that work.\n'
                 '\n'
                 'Inspect first.\n'
                 '\n'
                 'If you are uncertain, preserve the file somewhere or create a safe commit or branch before '
                 'destructive recovery.\n'
                 '\n'
                 'The goal is not to memorize which command can erase something.\n'
                 '\n'
                 'The goal is to understand what copy of the data you are replacing and whether another copy '
                 'exists.\n'
                 '\n'
                 'Now consider untracked files.\n'
                 '\n'
                 'Git does not yet have committed history for an untracked file.\n'
                 '\n'
                 'That means Git cannot magically restore content it never recorded.\n'
                 '\n'
                 'Git status may show the file, but if you delete the only copy, repository history may not be able '
                 'to recover it.\n'
                 '\n'
                 'This is a crucial distinction.\n'
                 '\n'
                 'Tracked history provides recovery options.\n'
                 '\n'
                 'Untracked work may not have that protection.\n'
                 '\n'
                 'Now let us discuss commits.\n'
                 '\n'
                 'Suppose your most recent local commit has the wrong message or is missing one small file.\n'
                 '\n'
                 'If the commit has not been shared, rewriting local history may be reasonable.\n'
                 '\n'
                 'Git commit dash dash amend can replace the most recent commit with a new version.\n'
                 '\n'
                 'But amend is not editing a commit in place.\n'
                 '\n'
                 'Conceptually, Git creates a new commit.\n'
                 '\n'
                 'That means the commit identifier changes.\n'
                 '\n'
                 'If the old commit was already pushed and other people may depend on it, rewriting it can create '
                 'collaboration problems.\n'
                 '\n'
                 'Local and shared history have different risk profiles.\n'
                 '\n'
                 'This brings us to reset.\n'
                 '\n'
                 'Git reset is powerful because it can move a branch reference and can also affect the staging area '
                 'or working tree depending on the mode.\n'
                 '\n'
                 'That flexibility is exactly why beginners should not reach for reset reflexively.\n'
                 '\n'
                 'Before using reset, ask what you are trying to move and what data must remain.\n'
                 '\n'
                 'A soft reset, mixed reset, and hard reset do not have the same consequences.\n'
                 '\n'
                 'You do not need to memorize every mode today.\n'
                 '\n'
                 'You do need to recognize that git reset dash dash hard can overwrite working-tree and staging '
                 'state.\n'
                 '\n'
                 'Treat destructive reset commands as precision tools, not generic undo buttons.\n'
                 '\n'
                 'Now compare reset with revert.\n'
                 '\n'
                 'Git revert is designed to record a new commit that reverses the effect of an earlier commit.\n'
                 '\n'
                 'Instead of pretending the earlier commit never happened, the history records both the original '
                 'change and the reversal.\n'
                 '\n'
                 'That makes revert especially useful when a problematic commit has already been shared.\n'
                 '\n'
                 'Imagine a deployment commit reaches main and causes a production problem.\n'
                 '\n'
                 'If teammates and automation have already consumed that history, rewriting the shared branch may '
                 'create a second problem.\n'
                 '\n'
                 'A revert can preserve the shared history while introducing an explicit corrective commit.\n'
                 '\n'
                 'This is a fundamental professional Git distinction:\n'
                 '\n'
                 'Rewriting private history can be appropriate.\n'
                 '\n'
                 'Correcting shared history often favors additive history.\n'
                 '\n'
                 'Now let us discuss detached HEAD.\n'
                 '\n'
                 'Normally, HEAD refers through a branch to the commit you currently have checked out.\n'
                 '\n'
                 'But Git can also check out a specific commit directly.\n'
                 '\n'
                 'In that state, HEAD is detached.\n'
                 '\n'
                 'Detached HEAD is not automatically an emergency.\n'
                 '\n'
                 'It can be useful for inspecting an earlier version, running a test, or exploring history.\n'
                 '\n'
                 'The risk appears when you create valuable commits while detached and then move away without '
                 'creating a branch reference to preserve them.\n'
                 '\n'
                 'If that happens, do not panic.\n'
                 '\n'
                 'The commit may still exist.\n'
                 '\n'
                 'This is where reflog becomes important.\n'
                 '\n'
                 'Git reflog records recent updates to references in your local repository.\n'
                 '\n'
                 'It can often show commits that appear to have vanished after a reset, branch movement, or '
                 'detached-HEAD experiment.\n'
                 '\n'
                 'You can inspect the reflog, identify the desired commit, verify it with git show, and then create '
                 'a branch pointing to it.\n'
                 '\n'
                 'That sequence matters.\n'
                 '\n'
                 'Inspect.\n'
                 '\n'
                 'Identify.\n'
                 '\n'
                 'Verify.\n'
                 '\n'
                 'Preserve.\n'
                 '\n'
                 'Only then continue.\n'
                 '\n'
                 'Reflog is not a permanent backup system.\n'
                 '\n'
                 'Entries expire, and it is local to a repository.\n'
                 '\n'
                 'But it is an extremely useful recovery source when recent local history has moved.\n'
                 '\n'
                 'Now consider a deleted branch.\n'
                 '\n'
                 'Deleting a branch removes a reference.\n'
                 '\n'
                 'It does not necessarily erase the underlying commits immediately.\n'
                 '\n'
                 'If another branch or tag points to those commits, they remain normally reachable.\n'
                 '\n'
                 'Even if no current branch points to a recent commit, reflog may help you find it.\n'
                 '\n'
                 'This reveals an important Git concept:\n'
                 '\n'
                 'Branches are movable names pointing into the commit graph.\n'
                 '\n'
                 'The commit and the branch name are not the same thing.\n'
                 '\n'
                 'Understanding that makes branch recovery far less mysterious.\n'
                 '\n'
                 'Now let us look at merge conflicts and interrupted operations.\n'
                 '\n'
                 'Sometimes Git tells you that a merge, rebase, or other operation is in progress.\n'
                 '\n'
                 'Do not stack random commands on top of an unfinished operation.\n'
                 '\n'
                 'Read git status.\n'
                 '\n'
                 'Git often tells you exactly what state the repository is in and whether you should resolve files '
                 'and continue or abort the operation.\n'
                 '\n'
                 'An abort command is not a universal escape key.\n'
                 '\n'
                 'It applies to a specific operation and attempts to return the repository to an earlier state.\n'
                 '\n'
                 'Again, state determines action.\n'
                 '\n'
                 'Now consider stash.\n'
                 '\n'
                 'Git stash can temporarily record certain working-tree changes so you can return to a cleaner state '
                 'and reapply them later.\n'
                 '\n'
                 'It can be useful, but it should not become a drawer where unexplained work disappears for months.\n'
                 '\n'
                 'A stash is another piece of repository state that must be understood and managed.\n'
                 '\n'
                 'Before stashing, inspect what you have.\n'
                 '\n'
                 'After stashing, verify the working tree.\n'
                 '\n'
                 'Before applying or popping a stash, inspect the stash list and understand which entry you are '
                 'using.\n'
                 '\n'
                 'Recovery tools are safer when they remain observable.\n'
                 '\n'
                 'Now let us connect this to remote collaboration.\n'
                 '\n'
                 'Suppose you pushed a bad commit to your feature branch.\n'
                 '\n'
                 'If nobody else depends on the branch and team policy permits rewriting it, you may have options '
                 'that involve rewriting and a carefully controlled force push.\n'
                 '\n'
                 'But never treat force push as routine cleanup.\n'
                 '\n'
                 "If a branch is shared, rewriting its history can invalidate another person's local assumptions.\n"
                 '\n'
                 'If the problematic commit is on a protected shared branch such as main, a revert is often the '
                 'safer model.\n'
                 '\n'
                 "Your team's workflow and branch protections matter.\n"
                 '\n'
                 'The command is only one part of the decision.\n'
                 '\n'
                 'This is why professional troubleshooting starts by defining the scope of impact.\n'
                 '\n'
                 'Is the problem only on your machine?\n'
                 '\n'
                 'Only on your private branch?\n'
                 '\n'
                 'On a shared feature branch?\n'
                 '\n'
                 'Already merged into main?\n'
                 '\n'
                 'Already deployed?\n'
                 '\n'
                 'The farther a change has traveled, the more recovery becomes an operational decision rather than a '
                 'local Git trick.\n'
                 '\n'
                 'Now let us build a recovery ladder.\n'
                 '\n'
                 'First, stop changing things.\n'
                 '\n'
                 'Second, run git status.\n'
                 '\n'
                 'Third, inspect relevant diffs.\n'
                 '\n'
                 'Fourth, inspect recent history with git log.\n'
                 '\n'
                 'Fifth, inspect branches and remotes if location is unclear.\n'
                 '\n'
                 'Sixth, use reflog when a recent commit or branch position appears lost.\n'
                 '\n'
                 'Seventh, identify whether the work is untracked, modified, staged, committed, or shared.\n'
                 '\n'
                 'Eighth, preserve anything valuable before using a destructive command.\n'
                 '\n'
                 'Ninth, choose the smallest recovery action that addresses the actual state.\n'
                 '\n'
                 'Tenth, verify afterward with status, diff, log, and tests as appropriate.\n'
                 '\n'
                 'This is deliberately slower than copying the first reset command from a search result.\n'
                 '\n'
                 'It is also much safer.\n'
                 '\n'
                 'Now consider a real Ascend-style example.\n'
                 '\n'
                 'Imagine you are updating a lesson and accidentally stage Lesson dot JSX along with the lesson '
                 'content.\n'
                 '\n'
                 'You do not want the UI file in the commit, but you do want to keep your local UI experiment.\n'
                 '\n'
                 'Deleting the file would be wrong.\n'
                 '\n'
                 'Restoring the entire working tree would be wrong.\n'
                 '\n'
                 'The problem is staging state.\n'
                 '\n'
                 'So you inspect status and staged diff, then unstage only Lesson dot JSX while preserving its '
                 'working-tree edits.\n'
                 '\n'
                 'That is precise recovery.\n'
                 '\n'
                 'Another example:\n'
                 '\n'
                 'Imagine you make two local commits, then realize the second commit is experimental and should not '
                 'be part of the branch.\n'
                 '\n'
                 'Before doing anything, you verify that the commits have not been pushed.\n'
                 '\n'
                 'Because the history is private, you have more freedom to reorganize it.\n'
                 '\n'
                 'If it had already been shared, the decision would change.\n'
                 '\n'
                 'One more example:\n'
                 '\n'
                 "Imagine you reset a branch and think yesterday's commit is gone.\n"
                 '\n'
                 'Do not immediately recreate the work from memory.\n'
                 '\n'
                 'Inspect reflog.\n'
                 '\n'
                 'If the old commit identifier is there, inspect it with git show.\n'
                 '\n'
                 'Then create a recovery branch pointing to it.\n'
                 '\n'
                 'You have turned a frightening situation into an evidence-driven procedure.\n'
                 '\n'
                 'That is the larger lesson.\n'
                 '\n'
                 'Git recovery is not about becoming fearless with destructive commands.\n'
                 '\n'
                 'It is about making destructive commands less necessary because you understand repository state.\n'
                 '\n'
                 'The best engineers are not the people who never make Git mistakes.\n'
                 '\n'
                 'They are the people who can establish what happened, preserve evidence, choose a recovery action '
                 'proportional to the problem, and verify the result.\n'
                 '\n'
                 'Your lab for this lesson will use a disposable repository.\n'
                 '\n'
                 'You will intentionally create several recoverable problems: accidental staging, an unwanted '
                 'tracked-file edit, an amended local commit, a detached HEAD commit, and a branch reference that '
                 'needs recovery.\n'
                 '\n'
                 'Because the repository is disposable, you can practice without risking Ascend.\n'
                 '\n'
                 'You will record the state before each recovery and the evidence afterward.\n'
                 '\n'
                 'The point is not speed.\n'
                 '\n'
                 'The point is to build a troubleshooting habit.\n'
                 '\n'
                 'Here is the takeaway for Lesson 1.8.\n'
                 '\n'
                 'Git gives you multiple copies and multiple layers of state: working tree, staging area, commits, '
                 'branches, remote history, and recent reference movements.\n'
                 '\n'
                 'Recovery becomes safer when you identify which layer contains the problem.\n'
                 '\n'
                 'Use status and diffs before changing state.\n'
                 '\n'
                 'Distinguish untracked work from recorded history.\n'
                 '\n'
                 'Distinguish private commits from shared commits.\n'
                 '\n'
                 'Prefer additive correction such as revert when shared history should remain stable.\n'
                 '\n'
                 'Use reflog as evidence when recent local references have moved.\n'
                 '\n'
                 'And never use a destructive command merely because its name sounds like undo.\n'
                 '\n'
                 'Evidence before action is not only a troubleshooting principle.\n'
                 '\n'
                 'In Git, it is a recovery strategy.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Diagnose a Git problem by distinguishing working-tree, staging, local-history, branch, and '
                'shared-history state.',
                'Explain safe uses of restore, amend, revert, reset concepts, stash, and reflog without treating '
                'them as interchangeable undo commands.',
                'Distinguish recovery strategies for private history from strategies for commits that have already '
                'been shared.',
                'Recover recent commits or branch positions by inspecting reflog and preserving the desired commit '
                'with a reference.',
                'Apply an Evidence Before Action recovery workflow and verify repository state after corrective '
                'action.'],
 'content': [{'heading': 'Recovery starts with state',
              'body': 'Before running an undo command, determine whether the problem is untracked, modified, staged, '
                      'committed locally, or already shared. Different states require different recovery '
                      'techniques.'},
             {'heading': 'Status and diffs are diagnostic tools',
              'body': 'git status establishes branch and file state. git diff normally exposes unstaged tracked '
                      'changes, while git diff --staged exposes what is selected for the next commit. Diagnose '
                      'before changing state.'},
             {'heading': 'Unstaging is not discarding',
              'body': 'If a file was staged accidentally but its edits are valuable, git restore --staged <file> can '
                      'remove it from the staging area while preserving the working-tree edits. The problem is '
                      'selection for the commit, not the file content.'},
             {'heading': 'Restoring a tracked file can discard work',
              'body': 'git restore can replace working-tree content from a recorded source. Inspect first: if the '
                      'uncommitted version is the only valuable copy, overwriting it may destroy work Git cannot '
                      'reconstruct from history.'},
             {'heading': 'Untracked files have no Git history yet',
              'body': 'An untracked file has not been recorded in a commit. Git may report it in status, but '
                      'repository history cannot restore content that was never committed.'},
             {'heading': 'Amend rewrites the latest local commit',
              'body': 'git commit --amend creates a replacement commit. This can be useful for private local '
                      'history, but the commit ID changes, so rewriting a commit that others already use can create '
                      'collaboration problems.'},
             {'heading': 'Reset is not a generic undo button',
              'body': 'git reset can move references and, depending on mode, alter staging or working-tree state. '
                      'Because modes have different consequences, especially --hard, use reset only after '
                      'identifying what must move and what data must remain.'},
             {'heading': 'Revert adds corrective history',
              'body': 'git revert creates a new commit that reverses an earlier commit. This is often a better model '
                      'for shared history because it preserves the original event and records the correction instead '
                      'of rewriting what collaborators already consumed.'},
             {'heading': 'Detached HEAD is a state, not a disaster',
              'body': 'HEAD can point directly to a commit instead of through a branch. Exploration is safe, but '
                      'valuable commits created while detached should be given a branch or other reference before '
                      'moving away.'},
             {'heading': 'Reflog can reveal recently moved history',
              'body': 'git reflog records recent local reference movements. When a commit seems lost after reset, '
                      'checkout, or branch movement, inspect reflog, verify the candidate with git show, and '
                      'preserve it with a branch.'},
             {'heading': 'A branch name is a reference',
              'body': 'Deleting or moving a branch changes a name pointing into the commit graph; it does not '
                      'necessarily erase the commits immediately. This mental model makes branch recovery easier to '
                      'reason about.'},
             {'heading': 'Interrupted operations have explicit state',
              'body': 'During a merge or rebase, git status often explains whether conflicts remain and whether the '
                      'operation can continue or abort. Do not stack unrelated commands onto an unfinished '
                      'operation.'},
             {'heading': 'Stash is temporary state, not a junk drawer',
              'body': 'git stash can preserve certain working changes temporarily. Inspect before stashing, verify '
                      'afterward, and inspect the stash list before applying an entry so temporary work remains '
                      'understandable.'},
             {'heading': 'Shared history changes the recovery decision',
              'body': 'A private branch may permit history rewriting. A shared branch or protected main branch has a '
                      'larger blast radius. Once others, automation, or deployment depend on history, recovery '
                      'becomes a collaboration and operations decision.'},
             {'heading': 'Use a recovery ladder',
              'body': 'Stop, inspect status, inspect diffs and history, determine the affected layer, preserve '
                      'valuable work, choose the smallest corrective action, then verify with status, diff, log, and '
                      'relevant tests.'},
             {'heading': 'Takeaway',
              'body': 'Git recovery is safest when you understand which layer of repository state is wrong. Evidence '
                      'Before Action turns recovery from command guessing into controlled engineering.'}],
 'diagram': {'title': 'The Git recovery decision ladder',
             'description': 'Identify where the unwanted state lives before choosing a corrective operation.',
             'nodes': [{'label': 'Untracked',
                        'detail': 'No committed Git copy exists yet; preserve valuable content before deletion.'},
                       {'label': 'Working tree',
                        'detail': 'Inspect unstaged changes before restoring recorded content over them.'},
                       {'label': 'Staging area',
                        'detail': 'Unstage selected content without confusing staging with file deletion.'},
                       {'label': 'Local commit',
                        'detail': 'Private history may allow amend or deliberate rewriting after verification.'},
                       {'label': 'Shared commit',
                        'detail': 'Prefer collaborative correction such as revert when history should remain '
                                  'stable.'},
                       {'label': 'Moved reference',
                        'detail': 'Use reflog and git show to locate and verify recent commits, then preserve them '
                                  'with a branch.'}],
             'caption': 'The same word—undo—can describe very different operations. Repository state determines the '
                        'safe recovery path.'},
 'engineer_perspective': {'title': 'The blast radius grows as history travels',
                          'body': 'An unpushed mistake may affect only your local branch. The same mistake after '
                                  'merge and deployment can affect teammates, automation, and users. Recovery should '
                                  'account for how far the change has propagated, not only which Git command can '
                                  'reverse it.'},
 'try_it_yourself': {'title': 'Diagnose before you recover',
                     'intro': 'Use the Ascend repository only for read-only observation. Do not run restore, reset, '
                              'clean, amend, revert, or checkout recovery commands here.',
                     'steps': ['From ~/Projects/Ascend, run git status and classify any reported files as untracked, '
                               'modified, or staged.',
                               'Run git diff and describe exactly which layer of state its output represents.',
                               'Run git diff --staged and compare its meaning with plain git diff.',
                               'Run git log --oneline -8 and identify the current HEAD commit.',
                               'Run git reflog -8 and compare reflog entries with ordinary log history.',
                               'Write a recovery hypothesis for one imaginary mistake, but do not execute it in '
                               'Ascend.'],
                     'takeaway': 'The first recovery skill is not changing the repository. It is correctly '
                                 'identifying the state that would need to change.'},
 'lab': {'title': 'Build a Disposable Git Recovery Lab',
         'instructions': ['Create a Journal entry titled “Lesson 1.8 — Git Recovery Lab.”',
                          'Create a disposable repository outside Ascend, initialize it, and make a clean baseline '
                          'commit.',
                          'Create a tracked file, modify it, and record what git status and git diff show before '
                          'doing anything else.',
                          'Stage that file, inspect git diff --staged, then use git restore --staged to unstage it '
                          'while preserving the working-tree edit. Verify both facts.',
                          'Commit the file, modify it again with disposable content, inspect the diff, then practice '
                          'restoring the tracked file to its committed state. Record what was lost and why this '
                          'would be dangerous with valuable uncommitted work.',
                          'Create an untracked file and explain why Git cannot restore its contents from commit '
                          'history if the only copy is deleted.',
                          'Make a local commit with an intentionally poor message, verify it has not been shared, '
                          'then amend the message. Compare the old and new commit identifiers.',
                          'Create another commit and use git revert to reverse it. Inspect log and explain how '
                          'revert differs from rewriting history.',
                          'Check out an earlier commit to enter detached HEAD, make a small commit, and record its '
                          'identifier.',
                          'Move back to your main branch, use git reflog to locate the detached commit, verify it '
                          'with git show, and create a recovery branch pointing to it.',
                          'Create and inspect a stash with disposable edits. Verify the working tree before and '
                          'after applying the stash.',
                          'Write a short explanation of why git reset --hard deserves extra caution. You do not need '
                          'to use it to complete the lab.',
                          'For each exercise, classify the problem layer: untracked, working tree, staging area, '
                          'local commit, shared history, or moved reference.',
                          'Finish with your own Evidence Before Action recovery checklist.']},
 'quiz': [{'question': 'What should usually happen before attempting Git recovery?',
           'choices': ['Determine the repository state with evidence',
                       'Run git reset --hard',
                       'Delete the repository',
                       'Force-push immediately'],
           'correct': 0},
          {'question': 'A file is staged accidentally, but you want to keep its edits. What state needs changing?',
           'choices': ['The staging selection', 'The file must be deleted', 'Remote history', 'The Git installation'],
           'correct': 0},
          {'question': 'Why are untracked files different during recovery?',
           'choices': ['Git has not recorded their contents in commit history',
                       'They are always backed up remotely',
                       'They cannot be edited',
                       'They are already staged'],
           'correct': 0},
          {'question': 'What does git commit --amend conceptually do?',
           'choices': ['Creates a replacement latest commit',
                       'Edits a remote server in place',
                       'Deletes every earlier commit',
                       'Only renames a branch'],
           'correct': 0},
          {'question': 'Why should git reset --hard be treated cautiously?',
           'choices': ['It can overwrite staging and working-tree state',
                       'It only displays history',
                       'It cannot affect files',
                       'It always creates a backup branch'],
           'correct': 0},
          {'question': 'Why is git revert often useful for shared history?',
           'choices': ['It records a new corrective commit without erasing the original shared event',
                       'It secretly deletes remote history',
                       'It detaches HEAD permanently',
                       'It removes Git metadata'],
           'correct': 0},
          {'question': 'What is detached HEAD?',
           'choices': ['HEAD points directly to a commit rather than through a branch',
                       'The repository has no commits',
                       'The remote is offline',
                       'The staging area is corrupt'],
           'correct': 0},
          {'question': 'What can git reflog help you find?',
           'choices': ['Recent local reference movements and commits that may no longer appear in ordinary branch '
                       'history',
                       "Other users' passwords",
                       'Deleted files that Git never recorded',
                       'Cloud billing data'],
           'correct': 0},
          {'question': 'What changes when a bad commit has already been shared?',
           'choices': ['The recovery decision must account for collaborators and downstream consumers',
                       'Nothing; private and shared history are identical',
                       'Git disables all recovery',
                       'The commit becomes untracked'],
           'correct': 0},
          {'question': 'What is the goal of the recovery ladder?',
           'choices': ['Choose the smallest corrective action after identifying and preserving relevant state',
                       'Memorize the most destructive command',
                       'Avoid using git status',
                       'Rewrite every mistake'],
           'correct': 0}],
 'reflection': 'Describe a Git mistake that would have felt intimidating before this lesson. Walk through how you '
               'would diagnose it now: what evidence would you collect, which layer of state would you identify, '
               'what would you preserve, and how would your decision change if the commit had already been shared or '
               'deployed?'}
