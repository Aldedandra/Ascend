"""Module 1, Lesson 3: Staging, Commits & Meaningful History."""

LESSON = {'id': '1-3',
 'title': 'Staging, Commits & Meaningful History',
 'summary': 'Learn to shape Git history deliberately with selective staging, staged-diff review, meaningful commit '
            'messages, commit identifiers, git log, and git show.',
 'duration_minutes': 60,
 'xp': 65,
 'audio_script': 'Welcome back to Module 1 of Ascend: Git and Collaborative Source Control.\n'
                 '\n'
                 'In Lesson 1.1, you learned why version control exists. In Lesson 1.2, you watched a repository '
                 'change state as files moved from untracked to staged to committed.\n'
                 '\n'
                 'Now we are going to focus on the quality of the history you create.\n'
                 '\n'
                 'A Git repository can contain hundreds or thousands of commits. If those commits are vague, '
                 'oversized, or unrelated, the repository may technically preserve history while still making that '
                 'history difficult to use.\n'
                 '\n'
                 'Good Git history is not created automatically. Engineers shape it.\n'
                 '\n'
                 'The first principle is simple: a commit should represent a coherent change.\n'
                 '\n'
                 "Imagine you are working on Ascend. You change Archer's display label, fix a navigation bug, "
                 'rewrite part of a Git lesson, add temporary debugging output, and update an unrelated dependency.\n'
                 '\n'
                 'If you stage everything and create one commit called updates, Git will preserve the changes, but '
                 'the history will not explain them well.\n'
                 '\n'
                 'Later, suppose the navigation fix causes a regression. Which part of that giant commit should be '
                 'reversed? Which changes were intentional? Why was the dependency updated? Was the debug output '
                 'supposed to ship?\n'
                 '\n'
                 'A large mixed commit increases the amount of reasoning required.\n'
                 '\n'
                 'Now imagine the same work as several focused commits.\n'
                 '\n'
                 "One commit changes Archer's display label.\n"
                 '\n'
                 'One fixes the navigation bug.\n'
                 '\n'
                 'One adds the lesson content.\n'
                 '\n'
                 'One updates the dependency with an explanation.\n'
                 '\n'
                 'Temporary debugging output never enters history at all.\n'
                 '\n'
                 'The repository now tells a story.\n'
                 '\n'
                 'This is what we mean by meaningful history.\n'
                 '\n'
                 'Meaningful history begins before git commit. It begins with inspection and staging.\n'
                 '\n'
                 'In Lesson 1.2, you learned that git add selects content for the next commit. Now we will use that '
                 'staging area more deliberately.\n'
                 '\n'
                 'Suppose git status shows three modified files, but only two belong to the feature you are '
                 'finishing. You can stage those two paths and leave the unrelated file unstaged.\n'
                 '\n'
                 'Then run git diff dash dash staged.\n'
                 '\n'
                 'Ask a specific question: if I commit right now, does this staged diff represent one understandable '
                 'change?\n'
                 '\n'
                 'If the answer is no, do not commit merely because the code works. Improve the proposed snapshot.\n'
                 '\n'
                 'This is one reason the staging area is powerful. It lets you separate the state of your working '
                 'tree from the history you intend to create.\n'
                 '\n'
                 'Git can be even more selective than whole files. The command git add dash p starts an interactive '
                 'patch-staging workflow that can let you choose individual hunks of a changed file.\n'
                 '\n'
                 'A hunk is a related section of a diff.\n'
                 '\n'
                 'You do not need to master patch staging today, but understand why it exists. Sometimes one file '
                 'contains two unrelated edits. Git can help you stage one change without staging the other.\n'
                 '\n'
                 'Selective staging should be used carefully. If two edits depend on each other for correctness, '
                 'splitting them into separate commits may create misleading or broken history.\n'
                 '\n'
                 'The goal is not to make commits artificially tiny. The goal is coherence.\n'
                 '\n'
                 'A useful question is: does this commit make sense as one engineering decision?\n'
                 '\n'
                 'Now let us talk about commit messages.\n'
                 '\n'
                 'A commit message is metadata attached to the snapshot. It should help another engineer, including '
                 'your future self, understand the purpose of the change.\n'
                 '\n'
                 'Compare these messages.\n'
                 '\n'
                 'Changes.\n'
                 '\n'
                 'Fix stuff.\n'
                 '\n'
                 'Update files.\n'
                 '\n'
                 'Now compare them with:\n'
                 '\n'
                 'Add Module 1 Git repository state lesson.\n'
                 '\n'
                 'Fix Gold Master audio path for Module 1.\n'
                 '\n'
                 'Preserve playback position when lesson audio resumes.\n'
                 '\n'
                 'The second group provides intent.\n'
                 '\n'
                 'A strong short commit subject is usually concise, specific, and action-oriented. Many teams prefer '
                 'an imperative style, such as add, fix, remove, update, or refactor.\n'
                 '\n'
                 'That style makes a history read almost like a sequence of actions.\n'
                 '\n'
                 'Add Archer narration support.\n'
                 '\n'
                 'Fix Module 1 audio routing.\n'
                 '\n'
                 'Refactor lesson registration.\n'
                 '\n'
                 'Remove obsolete speech fallback.\n'
                 '\n'
                 'You do not need to obsess over grammar. Clarity matters more than ritual.\n'
                 '\n'
                 'For simple changes, a good subject line may be enough.\n'
                 '\n'
                 'For a change that needs more context, Git also supports a longer commit message with a subject and '
                 'body. The body can explain why the change was necessary, important constraints, or decisions that '
                 'are not obvious from the diff.\n'
                 '\n'
                 'The diff tells you what changed.\n'
                 '\n'
                 'The commit message should often help explain why.\n'
                 '\n'
                 'This distinction matters because code rarely preserves every reason behind a decision.\n'
                 '\n'
                 'Imagine a configuration value changes from thirty to sixty. The diff proves the value changed. It '
                 'may not explain whether the reason was performance, reliability, a vendor limit, a customer '
                 'requirement, or an experiment.\n'
                 '\n'
                 'Useful history preserves context.\n'
                 '\n'
                 'Now let us inspect history.\n'
                 '\n'
                 'git log displays commits. By default it can show commit identifiers, authors, dates, and '
                 'messages.\n'
                 '\n'
                 'git log dash dash oneline provides a compact view. Each line includes an abbreviated commit '
                 'identifier and the commit subject.\n'
                 '\n'
                 "That abbreviated identifier is derived from the commit's object identifier.\n"
                 '\n'
                 'You will often hear people say commit hash or SHA. In everyday Git work, this refers to the '
                 'identifier used to name a particular commit object.\n'
                 '\n'
                 'The important mental model is that a commit can be referenced precisely.\n'
                 '\n'
                 'Instead of saying, the version from sometime Tuesday, an engineer can identify a specific commit.\n'
                 '\n'
                 'That precision is valuable in deployments, troubleshooting, reviews, and collaboration.\n'
                 '\n'
                 'You may see abbreviated identifiers such as a1b2c3d rather than a full identifier. Git commonly '
                 'allows an unambiguous prefix to refer to an object.\n'
                 '\n'
                 'Do not worry about memorizing identifiers. Use Git to inspect them.\n'
                 '\n'
                 'Now consider git show.\n'
                 '\n'
                 'If git log tells you which commits exist, git show can display information about a particular '
                 'commit, including its metadata and patch.\n'
                 '\n'
                 'For example, git show followed by a commit identifier lets you inspect what that commit actually '
                 'changed.\n'
                 '\n'
                 'This is powerful during troubleshooting.\n'
                 '\n'
                 'Suppose a bug appeared after a deployment. You identify the deployed commit, inspect recent '
                 "history, and find a suspicious change. git show lets you examine that exact snapshot's change "
                 'rather than relying on a memory of what happened.\n'
                 '\n'
                 'Again, history becomes evidence.\n'
                 '\n'
                 'Another useful command is git diff with two commit references. This can compare states across '
                 'history.\n'
                 '\n'
                 'The exact syntax will become more natural with practice, but the idea is important now: Git lets '
                 'you compare known points rather than guessing how the project evolved.\n'
                 '\n'
                 'Good commit structure makes those comparisons more useful.\n'
                 '\n'
                 'If one commit contains twenty unrelated changes, a diff around that commit contains twenty '
                 'unrelated stories.\n'
                 '\n'
                 'If a commit represents one coherent engineering decision, the evidence is easier to interpret.\n'
                 '\n'
                 'Now let us discuss something that sounds contradictory.\n'
                 '\n'
                 'Should every tiny edit be its own commit?\n'
                 '\n'
                 'No.\n'
                 '\n'
                 'A commit should be focused, not fragmented.\n'
                 '\n'
                 "Suppose you add a new lesson file and update the module's registration file so the application can "
                 'load that lesson. Those changes belong together because the feature is incomplete without both.\n'
                 '\n'
                 'Separating them purely to create smaller commits would not improve the history.\n'
                 '\n'
                 'Likewise, a bug fix may require a code change and a corresponding test. Those belong naturally in '
                 'one commit.\n'
                 '\n'
                 'The right unit is an understandable change.\n'
                 '\n'
                 'Ask: if another engineer checks out this commit, does it represent a sensible state? Can the '
                 'purpose be described clearly? Are unrelated experiments excluded?\n'
                 '\n'
                 'That is a better standard than counting files or lines.\n'
                 '\n'
                 'Now return to git status and diff.\n'
                 '\n'
                 'Before committing, a disciplined workflow might look like this.\n'
                 '\n'
                 'Run git status.\n'
                 '\n'
                 'Inspect git diff for unstaged work.\n'
                 '\n'
                 'Stage the files or hunks that belong to one change.\n'
                 '\n'
                 'Run git status again.\n'
                 '\n'
                 'Run git diff dash dash staged.\n'
                 '\n'
                 "Read the proposed commit as if you were reviewing someone else's work.\n"
                 '\n'
                 'Check for debug statements, accidental files, secrets, generated output, unrelated edits, and '
                 'incomplete changes.\n'
                 '\n'
                 'Then commit with a meaningful message.\n'
                 '\n'
                 'Afterward, run git status and inspect git log dash dash oneline.\n'
                 '\n'
                 'You are not merely confirming that Git accepted the command. You are verifying that the repository '
                 'history now matches your intent.\n'
                 '\n'
                 'This is Evidence Before Action applied to creating history.\n'
                 '\n'
                 'There is also value in reading your own history periodically.\n'
                 '\n'
                 'Look at the last ten commits in a project. Can you understand what happened without opening every '
                 'file?\n'
                 '\n'
                 'If the messages say update, more changes, fix, and stuff, the history is technically present but '
                 'operationally weak.\n'
                 '\n'
                 'If the messages describe focused changes, the log becomes a useful map.\n'
                 '\n'
                 'Your recent Ascend workflow gives us a practical example.\n'
                 '\n'
                 'When Module 0 became production-ready, a commit such as Complete Module 0 Gold Master and '
                 'integrate Archer narration describes a milestone.\n'
                 '\n'
                 'When Lesson 1.1 was added, a focused commit can identify that content separately from later Lesson '
                 '1.2 work.\n'
                 '\n'
                 'This matters when you need to answer questions later.\n'
                 '\n'
                 'When did Module 1 begin?\n'
                 '\n'
                 'Which commit added Archer to the player?\n'
                 '\n'
                 'What changed immediately before audio stopped working?\n'
                 '\n'
                 'Which lesson files were part of a particular milestone?\n'
                 '\n'
                 'Good history makes these questions easier.\n'
                 '\n'
                 'Now let us address amending commits.\n'
                 '\n'
                 'Git provides git commit dash dash amend, which can replace the most recent commit with a new one. '
                 'This can be useful if you just committed and immediately notice that the message is wrong or a '
                 'small intended change was omitted.\n'
                 '\n'
                 'But amendment changes the commit identity.\n'
                 '\n'
                 'That matters if the original commit has already been shared with other people or pushed into a '
                 'collaborative history.\n'
                 '\n'
                 'For now, treat amend as a tool whose consequences depend on whether history is private or shared. '
                 'Do not use it casually on shared work simply because you want a prettier message.\n'
                 '\n'
                 'We will explore history rewriting and recovery more deeply later.\n'
                 '\n'
                 'The same principle applies to other powerful Git commands. Understand the state and consequences '
                 'before acting.\n'
                 '\n'
                 'Your lab for this lesson will use a disposable repository again.\n'
                 '\n'
                 'You will create several changes, intentionally mix unrelated work in the working tree, and then '
                 'build focused commits from that messy state.\n'
                 '\n'
                 'You will inspect staged diffs before each commit and use git log and git show afterward to judge '
                 'the history you created.\n'
                 '\n'
                 'The goal is not to produce the maximum number of commits.\n'
                 '\n'
                 'The goal is to produce a history that another engineer could understand.\n'
                 '\n'
                 'Here is the takeaway for Lesson 1.3.\n'
                 '\n'
                 'Commits are not just checkpoints. They are units of engineering history.\n'
                 '\n'
                 'The staging area lets you design the next commit.\n'
                 '\n'
                 'Diffs let you inspect it.\n'
                 '\n'
                 'Commit messages preserve intent.\n'
                 '\n'
                 'Commit identifiers let you reference exact points in history.\n'
                 '\n'
                 'git log and git show turn that history back into evidence.\n'
                 '\n'
                 'A clean Git history is easier to review, troubleshoot, deploy, and reverse.\n'
                 '\n'
                 'Before you commit, ask one question.\n'
                 '\n'
                 'What story will this commit tell six months from now?\n'
                 '\n'
                 'Then make sure the snapshot and message tell the same story.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain why a commit should represent a coherent engineering change rather than an arbitrary '
                'collection of edits.',
                'Use the staging area and staged diffs to design and verify the next commit.',
                'Write concise commit subjects that communicate intent and know when additional context belongs in a '
                'commit body.',
                'Use git log and git show to inspect meaningful history and reference specific commits.',
                'Recognize when changes belong together, when they should be separated, and why rewriting shared '
                'history requires caution.'],
 'content': [{'heading': 'History can be preserved and still be poor',
              'body': 'Git will happily record a large mixed snapshot with a vague message. Meaningful history '
                      'requires engineers to shape commits so future readers can understand the purpose and scope of '
                      'each change.'},
             {'heading': 'A commit should be coherent',
              'body': 'A useful commit represents one understandable engineering decision. Focused does not mean one '
                      'file or one line; related code, tests, content, or registration changes may naturally belong '
                      'together.'},
             {'heading': 'Design the commit before creating it',
              'body': 'Use git status and git diff to understand the working tree, then stage only the changes that '
                      'belong to the next commit. The staging area is where you construct the snapshot you intend to '
                      'preserve.'},
             {'heading': 'Review the proposed snapshot',
              'body': 'git diff --staged shows what the next commit is currently prepared to contain. Read it as if '
                      "you were reviewing another engineer's work. Look for unrelated edits, debug output, secrets, "
                      'generated files, and omissions.'},
             {'heading': 'Selective staging',
              'body': 'Staging specific paths helps separate unrelated work. git add -p can go further by '
                      'interactively staging selected diff hunks from a file. Use selectivity to improve coherence, '
                      'not to split changes that depend on each other.'},
             {'heading': 'Commit messages preserve intent',
              'body': "Messages such as 'updates' or 'fix stuff' provide little future value. A concise message such "
                      "as 'Fix Module 1 audio routing' explains the purpose of the snapshot and makes history easier "
                      'to scan.'},
             {'heading': 'Subject and body',
              'body': 'Simple commits may need only a clear subject. More complex changes can use a body to explain '
                      'why the change was necessary, constraints, or decisions that are not obvious from the diff. '
                      'The diff shows what; the message often explains why.'},
             {'heading': 'Read history with git log',
              'body': 'git log displays repository history, while git log --oneline gives a compact view of '
                      'abbreviated commit identifiers and subjects. A readable log becomes a map of how the project '
                      'evolved.'},
             {'heading': 'Commit identifiers provide precision',
              'body': 'Each commit has an object identifier, often casually called a commit hash or SHA. Engineers '
                      "can reference a specific commit instead of saying 'the version from sometime Tuesday,' which "
                      'improves troubleshooting and deployment precision.'},
             {'heading': 'Inspect one commit with git show',
              'body': "git show <commit> can display a commit's metadata and patch. During an investigation, this "
                      'lets you inspect exactly what a suspicious or important commit changed.'},
             {'heading': 'Compare known points',
              'body': 'Git can diff commits or other references to compare known project states. Structured commits '
                      'make these comparisons more useful because each historical transition has a clearer purpose.'},
             {'heading': 'Focused does not mean fragmented',
              'body': 'A lesson file and the registration change required to load it may belong in the same commit. '
                      'A bug fix and its test may belong together. The goal is a sensible unit of change, not the '
                      'smallest possible commit.'},
             {'heading': 'Verify the history you created',
              'body': 'After committing, run git status and inspect git log --oneline. Verification checks that the '
                      'working tree and recorded history match what you intended rather than merely proving the '
                      'commit command succeeded.'},
             {'heading': 'Amending changes commit identity',
              'body': 'git commit --amend can replace the most recent commit and is useful in some private-history '
                      'situations. Because amendment changes commit identity, use caution once the original commit '
                      'has been shared with collaborators.'},
             {'heading': "Alex's Engineering Notes",
              'body': 'Before every important commit, ask whether the staged diff and commit message tell the same '
                      'story. If you cannot summarize the change clearly, the proposed commit may contain too many '
                      'unrelated decisions.'},
             {'heading': 'Takeaway',
              'body': 'Commits are units of engineering history. Deliberate staging, staged-diff review, useful '
                      'messages, and readable history make Git more valuable for reviews, troubleshooting, '
                      'deployments, and recovery.'}],
 'diagram': {'title': 'Designing a meaningful commit',
             'description': 'A useful commit is constructed deliberately rather than created from whatever happens '
                            'to be modified.',
             'nodes': [{'label': 'Working tree', 'detail': 'Several related and unrelated edits may exist at once.'},
                       {'label': 'Inspect', 'detail': 'git status and git diff establish what actually changed.'},
                       {'label': 'Select', 'detail': 'Stage the files or hunks that belong to one coherent change.'},
                       {'label': 'Review', 'detail': 'git diff --staged verifies the proposed snapshot.'},
                       {'label': 'Record',
                        'detail': 'git commit preserves the snapshot with a message explaining intent.'},
                       {'label': 'Verify',
                        'detail': 'git status, git log, and git show confirm the resulting state and history.'}],
             'caption': 'The staging area is a design surface for history: inspect, select, review, record, and '
                        'verify.'},
 'engineer_perspective': {'title': 'Repository history becomes incident evidence',
                          'body': 'When a deployment begins failing, a readable sequence of focused commits can '
                                  'narrow the investigation quickly. A giant commit containing features, '
                                  'dependencies, configuration, and cleanup forces responders to untangle several '
                                  'hypotheses at once. Commit quality can directly affect troubleshooting speed.'},
 'try_it_yourself': {'title': "Judge the story told by Ascend's history",
                     'intro': 'Use the real Ascend repository for read-only history inspection. Do not rewrite or '
                              'amend anything during this exercise.',
                     'steps': ['From ~/Projects/Ascend, run git log --oneline -10 and read the ten subjects as a '
                               'sequence.',
                               'Choose the clearest commit subject and explain what makes its intent understandable '
                               'without opening the diff.',
                               'Choose one vague or broad subject if one exists and describe what information you '
                               'would want before relying on it during troubleshooting.',
                               'Copy the abbreviated identifier of one recent commit and run git show --stat '
                               '<commit>. Identify which files were part of that change.',
                               'Run git show <commit> for a small recent commit and compare the patch with its '
                               'message. Decide whether they tell the same story.',
                               'Write a better commit subject for one hypothetical change: adding Lesson 1.3 and '
                               'registering it in Module 1.'],
                     'takeaway': 'A repository log should function as an understandable map, while git show lets you '
                                 "test whether a commit's actual change matches the story its message tells."},
 'lab': {'title': 'Build Meaningful History from a Messy Working Tree',
         'instructions': ['Create a Journal entry titled “Lesson 1.3 — Meaningful Git History Lab.”',
                          'Use a disposable Git repository. Begin from a clean committed README.md.',
                          'Create three intentionally different changes: add docs.md with documentation, add app.txt '
                          'with a small feature description, and add debug.log with temporary debug text.',
                          'Run git status and describe the mixed working-tree state before staging anything.',
                          'Stage only docs.md. Run git diff --staged and explain why this is a coherent proposed '
                          'commit.',
                          'Commit it with a specific action-oriented message, then verify with git status and git '
                          'log --oneline.',
                          'Add *.log to .gitignore. Stage app.txt and .gitignore only after inspecting their '
                          'changes. Decide whether they represent one coherent decision or should become separate '
                          'commits, and justify your choice.',
                          'Create the remaining focused commit or commits using messages that communicate intent.',
                          'Run git log --oneline and evaluate whether another engineer could understand the sequence '
                          'without opening every file.',
                          'Choose one commit identifier and run git show --stat followed by git show <commit>. '
                          'Explain what each view contributes.',
                          'Make two unrelated edits inside one tracked file. Run git diff and inspect the hunks. '
                          'Optionally explore git add -p, but do not use it unless you understand each prompt.',
                          'Finish by writing your personal pre-commit checklist, including status, diff, deliberate '
                          'staging, staged-diff review, message quality, and post-commit verification.']},
 'quiz': [{'question': 'What is the best general definition of a focused commit?',
           'choices': ['A commit containing exactly one file',
                       'The smallest commit Git will allow',
                       'A commit representing one coherent engineering change',
                       'Any commit with fewer than ten changed lines'],
           'correct': 2},
          {'question': 'Why inspect git diff --staged immediately before committing?',
           'choices': ['To see the snapshot currently prepared for the commit',
                       'To download remote history',
                       'To delete unstaged changes',
                       'To rename the current branch'],
           'correct': 0},
          {'question': 'What problem can selective staging solve?',
           'choices': ['It lets you include only changes that belong to the next coherent commit',
                       'It automatically fixes merge conflicts',
                       'It pushes only selected commits',
                       'It encrypts selected files'],
           'correct': 0},
          {'question': 'Which commit subject provides the strongest intent?',
           'choices': ['updates', 'stuff', 'Fix Module 1 audio routing', 'changes again'],
           'correct': 2},
          {'question': 'What should a commit message often explain that may not be obvious from the diff?',
           'choices': ['Why the change was made',
                       "The user's operating-system password",
                       'Every Git command ever run',
                       'The full contents of unchanged files'],
           'correct': 0},
          {'question': 'What does git log --oneline primarily provide?',
           'choices': ['A compact view of commit identifiers and subjects',
                       'A list of untracked files only',
                       'A staged diff',
                       'Remote server logs'],
           'correct': 0},
          {'question': 'Why are commit identifiers useful?',
           'choices': ['They provide a precise reference to a particular commit',
                       'They permanently replace commit messages',
                       'They guarantee the commit was deployed',
                       'They are passwords for GitHub'],
           'correct': 0},
          {'question': 'What is git show <commit> useful for?',
           'choices': ['Inspecting the metadata and change associated with a specific commit',
                       'Staging every file',
                       'Creating a remote repository',
                       'Ignoring generated files'],
           'correct': 0},
          {'question': 'Why should related changes sometimes stay in one commit?',
           'choices': ['Because every commit must contain multiple files',
                       'Because a coherent feature or fix may require several files to form one sensible state',
                       'Because Git cannot stage individual files',
                       'Because large commits are always better'],
           'correct': 1},
          {'question': 'Why should git commit --amend be used cautiously after a commit has been shared?',
           'choices': ['Amending changes the commit identity and can complicate shared history',
                       'Amend permanently disables Git',
                       'Amend always deletes the repository',
                       'Shared commits cannot contain messages'],
           'correct': 0}],
 'reflection': 'Think about the Git history you have created while building Ascend or another project. What makes a '
               'commit useful to your future self? Describe one habit you want to adopt before every commit, and '
               'explain how that habit could help during a future bug investigation or rollback.'}
