"""Module 1, Lesson 5: Merging Branches & Resolving Conflicts."""

LESSON = {'id': '1-5',
 'title': 'Merging Branches & Resolving Conflicts',
 'summary': 'Learn how Git combines branch histories, why conflicts happen, and how to resolve them calmly using '
            'status, conflict markers, deliberate staging, verification, and merge abort.',
 'duration_minutes': 65,
 'xp': 70,
 'audio_script': 'Welcome back to Module 1 of Ascend: Git and Collaborative Source Control.\n'
                 '\n'
                 'In Lesson 1.4, you learned that branches are movable references to commits. You created two lines '
                 'of history and watched the working tree change as you switched between them. Now we are ready for '
                 'the next question: how do we bring those lines of work back together?\n'
                 '\n'
                 'That process is called merging.\n'
                 '\n'
                 'A merge asks Git to combine histories. Sometimes the combination is simple. Sometimes the '
                 'histories have diverged but their changes do not compete, so Git can still integrate them '
                 'automatically. And sometimes both sides changed the same content in incompatible ways. In that '
                 'case, Git stops and asks a human to decide.\n'
                 '\n'
                 'That pause is not Git failing. It is Git refusing to invent intent.\n'
                 '\n'
                 'Begin with the simplest case. Imagine main points to commit C. You create feature-notes from C and '
                 'make commit D on that feature branch. Main has not changed. If you switch back to main and merge '
                 'feature-notes, Git can often perform a fast-forward merge. Main simply moves forward to D. No '
                 'separate merge commit is required because the history is still a straight line.\n'
                 '\n'
                 'Now imagine both branches advance. Feature-notes receives commit D while main receives commit E. '
                 'The histories have diverged. Git must combine two lines of work.\n'
                 '\n'
                 'If feature-notes adds feature.txt while main adds main-notes.txt, the changes do not compete. Git '
                 'can normally combine them automatically.\n'
                 '\n'
                 'But suppose both branches edit the same line in README differently. Main says, Deployment target: '
                 'production. Feature-notes says, Deployment target: staging.\n'
                 '\n'
                 'Which value is correct?\n'
                 '\n'
                 'Git cannot know the engineering decision. Both changes are valid history. So Git reports a merge '
                 'conflict.\n'
                 '\n'
                 'When that happens, your first move should be familiar: git status.\n'
                 '\n'
                 'Do not immediately reach for reset commands, delete files, or click random conflict-resolution '
                 'buttons. git status tells you that a merge is in progress and identifies the files that need human '
                 'attention.\n'
                 '\n'
                 'This is Evidence Before Action.\n'
                 '\n'
                 'Open the conflicted file. Git commonly inserts conflict markers. One section is labeled with HEAD, '
                 'another represents the incoming branch, and marker lines separate the competing content.\n'
                 '\n'
                 'Those markers are temporary evidence. They do not belong in the final file.\n'
                 '\n'
                 'HEAD usually represents the content from the branch you had checked out when you started the '
                 'merge. The other section represents the incoming change.\n'
                 '\n'
                 'Do not automatically keep one side because it appears first.\n'
                 '\n'
                 'Read both sides. Ask what the final content should actually be.\n'
                 '\n'
                 'Sometimes the correct answer is the current version. Sometimes it is the incoming version. '
                 'Sometimes both must be combined. Sometimes neither is correct and the final content should be '
                 'rewritten.\n'
                 '\n'
                 'A conflict is not a multiple-choice question. The engineer owns the resolution.\n'
                 '\n'
                 'After editing the file into the intended final state and removing all conflict markers, run git '
                 'status again. Git still knows a conflict occurred.\n'
                 '\n'
                 'Stage the resolved file with git add. That tells Git that the working copy now represents the '
                 'resolution you intend.\n'
                 '\n'
                 'Then complete the merge commit if the merge requires one.\n'
                 '\n'
                 'Afterward, verify.\n'
                 '\n'
                 'Run git status. Inspect the file. Run relevant tests. Then inspect history with git log dash dash '
                 'oneline dash dash graph dash dash decorate dash dash all.\n'
                 '\n'
                 'Do not stop just because the conflict markers are gone.\n'
                 '\n'
                 'Resolved does not automatically mean correct.\n'
                 '\n'
                 'Git can tell whether the repository is still in a conflicted state. It cannot always tell whether '
                 'your business logic, configuration, or application behavior is right.\n'
                 '\n'
                 'Now let us discuss merge abort.\n'
                 '\n'
                 'If you begin a merge and discover you are on the wrong branch, the repository state is not what '
                 'you expected, or you need more information before continuing, git merge dash dash abort can often '
                 'return the repository to its pre-merge state.\n'
                 '\n'
                 'Use it deliberately.\n'
                 '\n'
                 'First run git status. Confirm a merge is in progress. Understand whether other local work matters. '
                 'Abort because you have decided the current merge attempt should not continue, not because the '
                 'conflict message looks frightening.\n'
                 '\n'
                 'Merge direction also matters.\n'
                 '\n'
                 'If you are on main and run git merge feature-message, you are asking Git to integrate '
                 'feature-message into main.\n'
                 '\n'
                 'If you are on feature-message and run git merge main, you are asking Git to integrate main into '
                 'feature-message.\n'
                 '\n'
                 'The command is interpreted relative to the branch currently checked out.\n'
                 '\n'
                 'Before every merge, identify the branch with git status and state your intent in plain language.\n'
                 '\n'
                 'I am on main, and I want to merge feature-message into main.\n'
                 '\n'
                 'If you cannot say that confidently, do not run the merge yet.\n'
                 '\n'
                 'Now let us connect this to collaboration.\n'
                 '\n'
                 'On GitHub, teams often integrate branches with pull requests. On GitLab, the comparable workflow '
                 'is usually called a merge request.\n'
                 '\n'
                 'Those platforms add review, discussion, approvals, automated checks, and branch protections around '
                 'the underlying Git histories.\n'
                 '\n'
                 'The Git mechanics do not disappear. The platform is helping humans manage the integration '
                 'process.\n'
                 '\n'
                 'This is why understanding local merging matters even if most professional merges happen through a '
                 'web interface.\n'
                 '\n'
                 'Now consider conflict prevention.\n'
                 '\n'
                 'You cannot eliminate every merge conflict, and trying to avoid all conflict is not a useful goal.\n'
                 '\n'
                 'But you can reduce unnecessary conflicts.\n'
                 '\n'
                 'Keep branches focused. Integrate regularly rather than letting branches drift for months. '
                 'Communicate when several people are editing the same sensitive area. Avoid mixing giant formatting '
                 'changes with feature work. Keep commits coherent.\n'
                 '\n'
                 'These practices reduce the amount of unrelated change humans must reconcile.\n'
                 '\n'
                 'There is also a DevOps connection.\n'
                 '\n'
                 'A merge is a repository event. It does not prove the integrated application works.\n'
                 '\n'
                 'CI systems may respond to a branch update or merge by building the software, running tests, '
                 'linting code, scanning dependencies, or performing security checks.\n'
                 '\n'
                 'Git answers, can these histories be integrated into a repository state?\n'
                 '\n'
                 'Testing and automation answer, does that integrated state behave as expected?\n'
                 '\n'
                 'Those are different questions.\n'
                 '\n'
                 'Your lab will intentionally create both a clean merge and a conflict.\n'
                 '\n'
                 'First, you will create changes on separate files so Git can combine them automatically.\n'
                 '\n'
                 'Then you will create two branches that edit the same README line differently.\n'
                 '\n'
                 'You will predict the conflict, run the merge, stop when Git reports it, inspect git status, read '
                 'both sides, resolve the content deliberately, stage the result, complete the merge, and inspect '
                 'the graph.\n'
                 '\n'
                 'Then you will repeat a conflict only far enough to practice git merge dash dash abort.\n'
                 '\n'
                 'The goal is to create a calm response pattern.\n'
                 '\n'
                 'When a merge conflicts:\n'
                 '\n'
                 'Stop.\n'
                 '\n'
                 'Run git status.\n'
                 '\n'
                 'Identify the conflicted files.\n'
                 '\n'
                 'Inspect both sides.\n'
                 '\n'
                 'Decide the intended final content.\n'
                 '\n'
                 'Remove the conflict markers.\n'
                 '\n'
                 'Stage the resolution.\n'
                 '\n'
                 'Verify status.\n'
                 '\n'
                 'Complete the merge.\n'
                 '\n'
                 'Test the result.\n'
                 '\n'
                 'Inspect history.\n'
                 '\n'
                 'Here is the takeaway for Lesson 1.5.\n'
                 '\n'
                 'Merging combines lines of history.\n'
                 '\n'
                 'A fast-forward merge can simply move a branch pointer when history has not diverged.\n'
                 '\n'
                 'Diverged branches can often be combined automatically when their changes do not compete.\n'
                 '\n'
                 'A conflict occurs when Git cannot safely infer the intended combination.\n'
                 '\n'
                 'That is not failure. It is a request for human judgment.\n'
                 '\n'
                 'Resolve the intent, not just the markers.\n'
                 '\n'
                 'And remember: a completed merge proves that Git accepted the history. Verification proves that the '
                 'integrated system actually works.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain fast-forward merges and merges of diverged histories.',
                'Predict when Git can merge automatically and when human judgment may be required.',
                'Use git status and conflict markers to understand an in-progress merge.',
                'Resolve, stage, complete, and verify a merge conflict safely.',
                'Use git merge --abort deliberately when a merge attempt should be abandoned.'],
 'content': [{'heading': 'Merging combines histories',
              'body': 'A merge integrates another line of history into the currently checked-out branch. The result '
                      'depends on how the histories relate and whether their changes compete.'},
             {'heading': 'Fast-forward merges',
              'body': 'If the target branch has not advanced since the feature branch was created, Git can often '
                      'move the target branch pointer forward without creating a separate merge commit.'},
             {'heading': 'Diverged branches',
              'body': 'When both branches contain unique commits after their shared base, they have diverged. Git '
                      'can still merge automatically when their changes do not conflict.'},
             {'heading': 'Why conflicts happen',
              'body': 'A conflict appears when Git cannot safely infer how competing changes should be combined. Git '
                      'preserves both histories and asks a human to decide the intended result.'},
             {'heading': 'Status before resolution',
              'body': 'Run git status immediately after a conflict. It identifies the merge state and conflicted '
                      'paths without changing anything.'},
             {'heading': 'Conflict markers are evidence',
              'body': 'Conflicted files can contain markers separating HEAD content from incoming content. These '
                      'markers are temporary evidence and must be removed from the final file.'},
             {'heading': 'Resolve intent, not labels',
              'body': 'Do not automatically keep current or incoming content. The correct result may be either side, '
                      'both sides, or a new version based on engineering intent.'},
             {'heading': 'Stage the resolution',
              'body': 'After editing the conflicted file into the correct final state, git add <path> tells Git that '
                      'the path is resolved and ready for the merge result.'},
             {'heading': 'Resolved does not mean correct',
              'body': 'A completed merge only proves Git accepted the repository state. Tests, inspection, and '
                      'application verification determine whether the integrated behavior is actually correct.'},
             {'heading': 'Abort deliberately',
              'body': 'git merge --abort can often restore the pre-merge state. Use it after confirming a merge is '
                      'in progress and deciding the attempt should be abandoned.'},
             {'heading': 'Merge direction matters',
              'body': 'git merge <branch> integrates the named branch into the branch currently checked out. Confirm '
                      'the current branch and state the intended direction before merging.'},
             {'heading': 'Reduce unnecessary conflict',
              'body': 'Focused branches, regular integration, clear communication, coherent commits, and avoiding '
                      'unrelated formatting churn reduce needless merge complexity.'},
             {'heading': 'Merge requests build on Git',
              'body': 'GitHub pull requests and GitLab merge requests add review, checks, approvals, and '
                      'collaboration around branch integration. The underlying history remains Git.'},
             {'heading': 'Git integration versus CI validation',
              'body': 'Git can combine histories; CI can build, test, lint, and scan the integrated result. A '
                      'successful merge and a successful application are separate facts.'},
             {'heading': "Alex's Engineering Notes",
              'body': 'When a conflict appears, do not optimize for making the warning disappear. Optimize for '
                      'understanding both changes and producing the correct integrated result.'},
             {'heading': 'Takeaway',
              'body': 'A merge conflict is a request for human judgment. Establish state, understand both sides, '
                      'resolve deliberately, stage, complete, and verify.'}],
 'diagram': {'title': 'Diverge, then merge',
             'description': 'Two branches can share a base, advance independently, and later be integrated.',
             'nodes': [{'label': 'Shared base', 'detail': 'Both branches begin from the same commit.'},
                       {'label': 'main advances', 'detail': 'Main receives a unique commit.'},
                       {'label': 'feature advances',
                        'detail': 'The feature branch receives a different unique commit.'},
                       {'label': 'Merge attempt', 'detail': 'Git compares both histories and their changes.'},
                       {'label': 'Automatic or conflict',
                        'detail': 'Non-competing changes merge automatically; competing changes may require human '
                                  'judgment.'},
                       {'label': 'Integrated history',
                        'detail': 'After resolution and verification, both histories are represented in the '
                                  'result.'}],
             'caption': 'A conflict is about combining content, not losing history. Git stops when it cannot safely '
                        'infer the intended final state.'},
 'engineer_perspective': {'title': 'Conflict is often a design conversation',
                          'body': 'Two engineers changing the same line may be expressing two valid but competing '
                                  'assumptions. Good resolution can require understanding requirements, '
                                  'configuration, or runtime behavior—not simply choosing whichever side an editor '
                                  'labels first.'},
 'try_it_yourself': {'title': 'Inspect merge history in Ascend',
                     'intro': 'Use the real Ascend repository for read-only inspection only.',
                     'steps': ['Run git status and identify the current branch.',
                               'Run git log --oneline --graph --decorate --all -25.',
                               'Look for visible branch divergence or merge commits. If none appear, record that '
                               'observation rather than inventing one.',
                               'Choose a commit and run git show --no-patch --pretty=raw <commit>. Inspect its '
                               'parent information.',
                               'If you find a merge commit with multiple parents, explain what that suggests about '
                               'the history.',
                               'Write the direction of a hypothetical merge in plain language before writing its Git '
                               'command.'],
                     'takeaway': 'Before integration, identify where you are and which history you intend to bring '
                                 'into the current branch.'},
 'lab': {'title': 'Create, Resolve, and Abort a Merge Conflict',
         'instructions': ['Create a Journal entry titled “Lesson 1.5 — Merge Conflict Lab.”',
                          'Use a disposable repository with main and a committed README.md. Begin with a clean git '
                          'status.',
                          'Create clean-feature, add clean-feature.txt, and commit it. Return to main, add '
                          'main-only.txt, and commit it.',
                          'Merge clean-feature into main and inspect the graph. Record whether Git required human '
                          'resolution.',
                          'Create feature-message from the current main state.',
                          "On feature-message, change one README line to 'Deployment target: staging.' and commit.",
                          "Switch to main, change that exact line to 'Deployment target: production.' and commit.",
                          'Predict whether the next merge will conflict, then run git merge feature-message.',
                          'When Git stops, run git status before editing anything.',
                          'Open README.md and identify the HEAD side, incoming side, and conflict markers.',
                          "Resolve the line to 'Deployment target: choose by environment configuration.' Remove all "
                          'conflict markers.',
                          'Run git diff, stage README.md, and run git status again. Explain the state change.',
                          'Complete the merge commit and verify README.md, git status, and git log --oneline --graph '
                          '--decorate --all.',
                          'Create another temporary one-line conflict, begin the merge, verify the conflict with git '
                          'status, then run git merge --abort.',
                          'Verify the repository returned to the expected pre-merge state.',
                          "Finish with your personal conflict-response checklist beginning with 'Stop and run git "
                          "status.'"]},
 'quiz': [{'question': 'What does a Git merge fundamentally do?',
           'choices': ['Combines lines of repository history',
                       'Deletes every feature commit',
                       'Uploads a repository to GitHub',
                       'Creates a new operating-system user'],
           'correct': 0},
          {'question': 'When can a fast-forward merge occur?',
           'choices': ["When the target branch can simply move forward to the other branch's commit",
                       'Only when there is a conflict',
                       'Only on remotes',
                       'Whenever the same line changed twice'],
           'correct': 0},
          {'question': 'Why does Git stop with a merge conflict?',
           'choices': ['It cannot safely infer how competing changes should be combined',
                       'There are too many commits',
                       'Merging requires internet',
                       'All merges require manual editing'],
           'correct': 0},
          {'question': 'What should be your first low-risk command after a merge conflict?',
           'choices': ['git status', 'git reset --hard', 'git clean -fd', 'git push --force'],
           'correct': 0},
          {'question': 'What are conflict markers?',
           'choices': ['Temporary indicators showing competing content',
                       'Permanent Git syntax',
                       'Encrypted branch names',
                       'Remote errors'],
           'correct': 0},
          {'question': 'After editing a conflicted file correctly, what normally marks that path resolved?',
           'choices': ['git add <path>', 'git init', 'git remote -v', 'git branch -D main'],
           'correct': 0},
          {'question': 'Why is a completed merge not proof the application is correct?',
           'choices': ['Git can integrate history without understanding all runtime or business behavior',
                       'Git never stores merged files',
                       'Merge commits cannot be tested',
                       'Conflicts always corrupt repos'],
           'correct': 0},
          {'question': 'What does git merge --abort do in an appropriate in-progress merge?',
           'choices': ['Attempts to return to the pre-merge state',
                       'Deletes the remote',
                       'Forces the merge',
                       'Rewrites every commit'],
           'correct': 0},
          {'question': 'If you are on main and run git merge feature-message, what are you asking Git to do?',
           'choices': ['Integrate feature-message into main',
                       'Integrate main into feature-message',
                       'Delete feature-message',
                       'Push main'],
           'correct': 0},
          {'question': 'What reduces unnecessary merge conflicts?',
           'choices': ['Focused branches and regular integration',
                       'Months of divergence',
                       'Mixing formatting with feature work',
                       'Skipping status'],
           'correct': 0}],
 'reflection': 'How did you react the first time you saw conflict markers? Explain how status → inspect both sides → '
               'choose intended content → stage → verify changes the experience. Then explain why a conflict may '
               'represent competing engineering intent rather than simply a Git problem.'}
