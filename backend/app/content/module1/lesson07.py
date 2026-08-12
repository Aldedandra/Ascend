"""Module 1, Lesson 7: Pull Requests, Reviews & Collaborative Git."""

LESSON = {'id': '1-7',
 'title': 'Pull Requests, Reviews & Collaborative Git',
 'summary': 'Turn branches into a team workflow. Learn how pull and merge requests combine diffs, review, automated '
            'checks, approvals, and branch protection before integration.',
 'duration_minutes': 65,
 'xp': 70,
 'audio_script': 'Welcome back to Module 1 of Ascend: Git and Collaborative Source Control.\n'
                 '\n'
                 'You now understand local history, branches, merges, conflicts, and remotes. The next step is '
                 'collaboration.\n'
                 '\n'
                 'In many professional teams, engineers do not push a feature branch directly into main and '
                 'immediately call the work finished. Instead, they open a pull request or merge request so the '
                 'proposed change can be reviewed before integration.\n'
                 '\n'
                 'GitHub commonly uses the term pull request. GitLab commonly uses the term merge request.\n'
                 '\n'
                 'The names differ, but the core idea is similar: compare one branch with another, discuss the '
                 'proposed change, run checks, and decide whether the work should be integrated.\n'
                 '\n'
                 'A pull request is not a replacement for Git. It is a collaboration process built around Git '
                 'branches and commits.\n'
                 '\n'
                 'Everything you learned in the previous lessons still applies. The source branch points to commits. '
                 'The target branch points to another line of history. The hosting platform compares them. Reviewers '
                 'inspect the diff. Automation may run against the proposed state. If the work is approved and '
                 'integrated, Git history changes according to the chosen merge strategy.\n'
                 '\n'
                 'Let us begin with the purpose of review.\n'
                 '\n'
                 'Code review is not primarily about proving that one engineer is smarter than another. Good review '
                 'improves the change and spreads understanding.\n'
                 '\n'
                 'A reviewer may notice a bug, missing test, risky configuration, unclear name, security issue, or '
                 'operational consequence. They may also ask a question because the intent is not obvious.\n'
                 '\n'
                 'That question is useful evidence.\n'
                 '\n'
                 'If a change is difficult for another engineer to understand, that may indicate the code, '
                 'documentation, commit structure, or pull request description needs more context.\n'
                 '\n'
                 'Review is also a knowledge-sharing mechanism. If only one person understands a critical deployment '
                 'script, the team has a reliability risk. When others review and discuss that script, knowledge '
                 'becomes less concentrated.\n'
                 '\n'
                 'Now consider the pull request description.\n'
                 '\n'
                 'A weak description might say, fixed things.\n'
                 '\n'
                 'A useful description tells reviewers what changed, why it changed, how it was tested, and what '
                 'risks or follow-up work matter.\n'
                 '\n'
                 'For example: this change adds Gold Master audio routing for Module 1 lessons. It updates the '
                 'lesson player to resolve audio by module number. Tested on web, iPad, and iPhone. No database '
                 'changes.\n'
                 '\n'
                 'That description helps a reviewer orient before reading the diff.\n'
                 '\n'
                 'The diff still matters. Descriptions can be wrong or incomplete. Evidence comes from both the '
                 'stated intent and the actual change.\n'
                 '\n'
                 'A strong review compares them.\n'
                 '\n'
                 'Does the diff match the description? Are unrelated changes included? Do the tests support the '
                 'claimed behavior? Are there files that should not be present? Does the branch contain debugging '
                 'output or secrets? Do commit messages make the history understandable?\n'
                 '\n'
                 'This is Evidence Before Action applied to collaborative review.\n'
                 '\n'
                 'Now let us discuss comments.\n'
                 '\n'
                 'Review comments should be specific and actionable.\n'
                 '\n'
                 'Saying, this is bad, gives little useful direction.\n'
                 '\n'
                 'A stronger comment might say, this function now retries forever if the API remains unavailable. '
                 'Should we cap retries and surface an error after the third attempt?\n'
                 '\n'
                 'That comment identifies the behavior, risk, and a possible direction.\n'
                 '\n'
                 'Review comments can also be questions.\n'
                 '\n'
                 'What happens if this value is missing? Is this path valid on iOS as well as web? Why is this '
                 'permission required? Could this configuration be moved to an environment variable?\n'
                 '\n'
                 'Questions are valuable when they expose assumptions.\n'
                 '\n'
                 'Now consider the author receiving feedback.\n'
                 '\n'
                 'Do not treat every comment as an instruction that must be obeyed without thought.\n'
                 '\n'
                 'Clarify the concern. Provide evidence. Update the code when the feedback improves the change. '
                 'Explain respectfully when another approach is intentional.\n'
                 '\n'
                 'The goal is a better engineering decision, not winning an argument.\n'
                 '\n'
                 'Healthy review is collaborative reasoning.\n'
                 '\n'
                 'Now let us connect review to commits.\n'
                 '\n'
                 'Suppose you open a pull request and a reviewer requests a change. You modify the branch and create '
                 'another commit.\n'
                 '\n'
                 'Because the pull request compares branch history, the new commit normally becomes part of the '
                 'proposed change automatically after it is pushed to the remote branch.\n'
                 '\n'
                 'The pull request evolves as the branch evolves.\n'
                 '\n'
                 'Focused commits can make that evolution easier to understand.\n'
                 '\n'
                 'Now we need to discuss automated checks.\n'
                 '\n'
                 'Repository hosting platforms can run CI workflows when a pull request or merge request is opened '
                 'or updated.\n'
                 '\n'
                 'Checks may build the application, run tests, lint code, scan dependencies, validate infrastructure '
                 'configuration, or perform security analysis.\n'
                 '\n'
                 'These checks provide evidence before integration.\n'
                 '\n'
                 'But green checks do not prove everything is correct.\n'
                 '\n'
                 'Automation only tests what it is configured to test.\n'
                 '\n'
                 'A passing unit test suite may not catch a broken CarPlay interaction. A successful build may not '
                 'prove a database migration is safe. A security scan may not understand the business logic.\n'
                 '\n'
                 'Human review and automation complement each other.\n'
                 '\n'
                 'Now let us talk about branch protection.\n'
                 '\n'
                 'Teams often protect important branches such as main.\n'
                 '\n'
                 'A protected branch can require changes to arrive through a pull request, require approvals, '
                 'require status checks to pass, prevent force pushes, or restrict who can update the branch.\n'
                 '\n'
                 'These rules make the desired workflow enforceable.\n'
                 '\n'
                 'Remember the lesson from branches: main is not safe because it is named main. Main becomes safer '
                 'because the organization builds controls around how changes reach it.\n'
                 '\n'
                 'Branch protection is one of those controls.\n'
                 '\n'
                 'Now consider approval.\n'
                 '\n'
                 'An approval should mean more than, I glanced at the title.\n'
                 '\n'
                 'A reviewer should understand enough of the change to accept responsibility for the review.\n'
                 '\n'
                 'That does not mean every reviewer must understand every line equally deeply. Teams may use '
                 'specialized reviewers for security, database changes, infrastructure, or product behavior.\n'
                 '\n'
                 'The important idea is that approval is a signal in a process. Its value depends on the quality of '
                 'the review behind it.\n'
                 '\n'
                 'Now let us discuss merge strategies at a high level.\n'
                 '\n'
                 'Hosting platforms often offer options such as merge commit, squash merge, and rebase merge.\n'
                 '\n'
                 'A merge commit preserves the branch integration structure in history.\n'
                 '\n'
                 "A squash merge combines the pull request's changes into one commit on the target branch.\n"
                 '\n'
                 'A rebase-style integration can replay commits onto a new base to create a linear history.\n'
                 '\n'
                 'There are tradeoffs.\n'
                 '\n'
                 'A team may prefer one strategy for readability, traceability, or workflow consistency.\n'
                 '\n'
                 'Do not decide that one strategy is universally correct.\n'
                 '\n'
                 'Understand what history your team wants to preserve.\n'
                 '\n'
                 'Now let us discuss stale branches.\n'
                 '\n'
                 'A feature branch may fall behind main while review is happening.\n'
                 '\n'
                 'The platform may report that the branch is out of date or has conflicts.\n'
                 '\n'
                 'Do not blindly click update buttons without understanding what they do.\n'
                 '\n'
                 'The branch may need main merged into it, rebased onto main, or otherwise synchronized according to '
                 'team policy.\n'
                 '\n'
                 'The same mechanics from earlier lessons still apply.\n'
                 '\n'
                 'Inspect branch state. Fetch. Understand divergence. Integrate deliberately. Resolve conflicts if '
                 'required. Run tests again. Then update the remote feature branch.\n'
                 '\n'
                 'The web interface does not remove the need for a Git mental model.\n'
                 '\n'
                 'It simply exposes common operations through another interface.\n'
                 '\n'
                 'Now consider review size.\n'
                 '\n'
                 'A pull request with thousands of unrelated changed lines is difficult to review well.\n'
                 '\n'
                 'Large reviews increase cognitive load. Reviewers may miss subtle issues because they are trying to '
                 'understand too many decisions at once.\n'
                 '\n'
                 'Focused branches and coherent commits help create focused pull requests.\n'
                 '\n'
                 'This is another DevOps connection.\n'
                 '\n'
                 'Small changes improve feedback speed.\n'
                 '\n'
                 'A smaller change can often be reviewed, tested, integrated, and deployed faster. If something goes '
                 'wrong, the blast radius is easier to reason about.\n'
                 '\n'
                 'This does not mean every pull request should be tiny.\n'
                 '\n'
                 'A complete change may require several files and several commits.\n'
                 '\n'
                 'The goal is coherence.\n'
                 '\n'
                 'Can the reviewer understand the purpose? Can the author explain how it was validated? Can the team '
                 'integrate it with confidence?\n'
                 '\n'
                 'Now let us look at a practical review workflow.\n'
                 '\n'
                 'Update your local understanding of the remote.\n'
                 '\n'
                 'Create or continue work on a focused branch.\n'
                 '\n'
                 'Inspect status and diff.\n'
                 '\n'
                 'Commit coherent changes.\n'
                 '\n'
                 'Push the feature branch.\n'
                 '\n'
                 'Open a pull request or merge request with a useful title and description.\n'
                 '\n'
                 "Read the platform's diff yourself before asking someone else to review it.\n"
                 '\n'
                 'Verify automated checks.\n'
                 '\n'
                 'Respond to review feedback with evidence and focused updates.\n'
                 '\n'
                 'Re-run relevant tests after changes.\n'
                 '\n'
                 'Obtain required approvals.\n'
                 '\n'
                 "Integrate using the team's merge strategy.\n"
                 '\n'
                 'Then verify the target branch and downstream systems after integration.\n'
                 '\n'
                 'Notice that the process does not end when the merge button turns green.\n'
                 '\n'
                 'Integration is another change to a system.\n'
                 '\n'
                 'Verification still matters.\n'
                 '\n'
                 'Now let us connect this to Ascend.\n'
                 '\n'
                 'Imagine Lesson 1.7 is developed on a branch named feature slash module1-review-lesson.\n'
                 '\n'
                 'The branch contains the lesson file, module registration, and the Back to Top lesson control we '
                 'are adding.\n'
                 '\n'
                 'A good pull request would explain that it adds collaborative Git content and a reusable long-page '
                 'navigation improvement.\n'
                 '\n'
                 'The author would inspect the diff to ensure no unrelated project files were included.\n'
                 '\n'
                 'Automated checks could build the frontend and compile the backend content files.\n'
                 '\n'
                 'A reviewer could verify that the Back to Top button appears only after scrolling and that the '
                 'lesson content renders correctly.\n'
                 '\n'
                 'Then the change could be integrated.\n'
                 '\n'
                 'This is how a Git feature becomes a team delivery workflow.\n'
                 '\n'
                 'Your lab will simulate this process without requiring a real GitHub or GitLab account.\n'
                 '\n'
                 'You will create a feature branch in a disposable repository, make focused commits, compare it with '
                 'main, and write a pull request description in your Journal.\n'
                 '\n'
                 'Then you will play both roles.\n'
                 '\n'
                 'As the author, explain the change and evidence.\n'
                 '\n'
                 'As the reviewer, inspect the diff and write specific review comments.\n'
                 '\n'
                 'Finally, make one review-driven update to the branch and inspect how the branch comparison '
                 'changes.\n'
                 '\n'
                 'The goal is not to imitate a website.\n'
                 '\n'
                 'The goal is to practice the engineering reasoning that the website supports.\n'
                 '\n'
                 'Here is the takeaway for Lesson 1.7.\n'
                 '\n'
                 'Pull requests and merge requests are structured conversations around Git history.\n'
                 '\n'
                 'The branch contains the work.\n'
                 '\n'
                 'The diff exposes the proposed change.\n'
                 '\n'
                 'The description explains intent.\n'
                 '\n'
                 'Reviewers challenge assumptions and improve shared understanding.\n'
                 '\n'
                 'Automation gathers repeatable evidence.\n'
                 '\n'
                 'Branch protections enforce important policy.\n'
                 '\n'
                 'And approval is meaningful only when it reflects an informed review.\n'
                 '\n'
                 'Collaboration is not an extra layer after Git.\n'
                 '\n'
                 'It is where Git history becomes a team decision.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain pull requests and merge requests as collaboration workflows built around Git branches and '
                'commits.',
                'Write a useful change description that communicates intent, validation, risk, and scope.',
                'Review a proposed change by comparing stated intent with the actual diff and test evidence.',
                'Explain how automated checks, approvals, and protected branches reduce integration risk.',
                'Recognize common merge strategies and explain why review size and branch freshness affect delivery '
                'quality.'],
 'content': [{'heading': 'Pull requests are built on Git',
              'body': 'GitHub pull requests and GitLab merge requests compare branch histories and wrap that '
                      'comparison in collaboration features. The branch, commits, diff, and merge mechanics remain '
                      'Git.'},
             {'heading': 'Review improves code and understanding',
              'body': 'Good review can find defects, unclear assumptions, missing tests, security risks, and '
                      'operational consequences. It also spreads knowledge so critical systems are not understood by '
                      'only one person.'},
             {'heading': 'Describe the change before asking for review',
              'body': 'A useful request explains what changed, why, how it was tested, and relevant risks or '
                      'follow-up work. Reviewers still verify the diff; the description provides orientation rather '
                      'than replacing evidence.'},
             {'heading': 'Compare intent with the diff',
              'body': 'A reviewer should ask whether the actual changed files match the stated purpose. Unrelated '
                      'edits, debug output, secrets, generated files, or missing tests are easier to catch when '
                      'scope is explicit.'},
             {'heading': 'Write actionable review comments',
              'body': 'Specific comments identify behavior, risk, or an unanswered question. A concrete question '
                      'creates a productive engineering conversation; vague criticism does not.'},
             {'heading': 'Respond with reasoning, not reflex',
              'body': 'Authors should understand the concern, update the change when feedback improves it, and '
                      'explain intentional decisions with evidence when another approach is appropriate.'},
             {'heading': 'A request evolves with the branch',
              'body': 'When the author pushes new commits to the source branch, the proposed change normally '
                      'updates. Focused follow-up commits can make review-driven changes easier to understand.'},
             {'heading': 'Automated checks gather repeatable evidence',
              'body': 'CI can build, test, lint, scan, or validate a proposed change before integration. Green '
                      'checks are valuable, but they only prove what the configured checks actually cover.'},
             {'heading': 'Protected branches enforce policy',
              'body': 'A protected main branch can require reviews, passing checks, approved users, or other '
                      'controls. Main is made trustworthy by process and enforcement, not by its branch name.'},
             {'heading': 'Approval should mean informed review',
              'body': 'An approval is a process signal. Its value depends on whether the reviewer understood enough '
                      'of the change and evidence to accept the review responsibility.'},
             {'heading': 'Merge strategies shape history',
              'body': 'Merge commits, squash merges, and rebase-style integration produce different histories. Teams '
                      'choose policies based on traceability, readability, and workflow needs rather than a '
                      'universal rule.'},
             {'heading': 'Keep the branch current deliberately',
              'body': 'A reviewed branch can fall behind main. Fetch and inspect before updating it. The required '
                      'integration method depends on team policy and can introduce new conflicts or test results.'},
             {'heading': 'Review size affects review quality',
              'body': 'Very large, mixed pull requests increase cognitive load and make subtle issues easier to '
                      'miss. Focused changes create faster feedback and easier troubleshooting without forcing '
                      'artificial fragmentation.'},
             {'heading': 'The merge button is not the finish line',
              'body': 'After integration, verify the target branch, build, deployment, or user workflow as '
                      'appropriate. A successful platform merge proves history was integrated, not that every '
                      'downstream behavior is correct.'},
             {'heading': "Alex's Engineering Notes",
              'body': 'Before requesting review, review your own diff first. If you cannot explain the scope, test '
                      "evidence, and risk clearly, the change may not be ready for someone else's time."},
             {'heading': 'Takeaway',
              'body': 'Collaborative Git turns branch history into a team decision. Diff, description, review, '
                      'automation, policy, approval, integration, and verification all contribute evidence.'}],
 'diagram': {'title': 'From feature branch to reviewed integration',
             'description': 'A collaborative workflow adds evidence and human judgment around the Git branch before '
                            'it reaches main.',
             'nodes': [{'label': 'Feature branch', 'detail': 'Focused commits represent the proposed work.'},
                       {'label': 'Pull / merge request',
                        'detail': 'The platform compares the source branch with the target branch.'},
                       {'label': 'Self-review', 'detail': 'The author checks scope, diff, tests, and description.'},
                       {'label': 'Automation', 'detail': 'CI builds, tests, lints, scans, or validates the change.'},
                       {'label': 'Human review',
                        'detail': 'Reviewers inspect intent, implementation, risk, and evidence.'},
                       {'label': 'Integration',
                        'detail': "Approved work reaches the protected target branch using the team's merge "
                                  'strategy.'},
                       {'label': 'Verification',
                        'detail': 'The team confirms the integrated system behaves as expected.'}],
             'caption': 'Review does not replace Git mechanics. It adds structured human and automated evidence '
                        'before branch integration.'},
 'engineer_perspective': {'title': 'Small changes improve the feedback loop',
                          'body': 'A focused pull request can be understood, tested, reviewed, and integrated more '
                                  'quickly than a giant mixed change. Faster review shortens the time between an '
                                  'engineering decision and useful feedback.'},
 'try_it_yourself': {'title': 'Read a real project change like a reviewer',
                     'intro': 'Use the Ascend repository for read-only inspection. Choose a recent focused commit as '
                              'a stand-in for a proposed change.',
                     'steps': ['From ~/Projects/Ascend, run git log --oneline -12 and choose a recent focused '
                               'commit.',
                               'Run git show --stat <commit> and predict the purpose of the change from the message '
                               'and file list.',
                               'Run git show <commit> and inspect the actual patch.',
                               'Write a two-sentence pull request description: what changed and why.',
                               'Write how you would test or validate that change before integration.',
                               'Write one reviewer question that would improve confidence without inventing a '
                               'problem.'],
                     'takeaway': 'A good reviewer compares intent, actual change, and validation evidence rather '
                                 'than reviewing the title alone.'},
 'lab': {'title': 'Simulate a Pull Request Review',
         'instructions': ['Create a Journal entry titled “Lesson 1.7 — Collaborative Git Review Lab.”',
                          'Use a disposable repository with a clean main branch.',
                          'Create a feature branch named feature/review-lab.',
                          'Make two focused commits: one adding feature.txt and one adding docs.md that explains the '
                          'feature.',
                          'Run git diff main...feature/review-lab and inspect the complete proposed change.',
                          'Write a pull request title and description containing purpose, scope, validation, and '
                          'risk.',
                          'As the reviewer, inspect git log main..feature/review-lab --oneline and the branch diff.',
                          'Write at least three review comments: one question, one positive observation tied to '
                          'evidence, and one actionable improvement.',
                          'Return to the author role and make one focused commit that responds to your actionable '
                          'review comment.',
                          'Inspect the branch comparison again and explain how the proposed change evolved.',
                          'Write the automated checks you would want before integrating this change into main.',
                          'Decide whether you would approve the request and justify the decision using evidence.',
                          'Without performing the merge, describe what a protected-main policy might require before '
                          'integration.',
                          'Compare merge commit, squash merge, and rebase-style integration at a high level.',
                          'Finish with a pre-review checklist you could use before asking a teammate to spend time '
                          'reviewing your work.']},
 'quiz': [{'question': 'What is a pull request or merge request fundamentally built around?',
           'choices': ['A collaboration workflow around Git branches and commits',
                       'A replacement for Git repositories',
                       'A cloud backup with no history',
                       'A Linux package manager'],
           'correct': 0},
          {'question': 'What should a useful change description communicate?',
           'choices': ['Intent, scope, validation, and relevant risk',
                       'Only the branch name',
                       "The author's password",
                       'Every unchanged file'],
           'correct': 0},
          {'question': 'What should a reviewer compare with the stated description?',
           'choices': ['The actual diff and validation evidence',
                       "Only the author's title",
                       'The repository size',
                       'The laptop age'],
           'correct': 0},
          {'question': 'Which review comment is most actionable?',
           'choices': ['This is bad',
                       'Why did you do this?',
                       'This retry loop has no limit; should we cap attempts and surface an error?',
                       'No'],
           'correct': 2},
          {'question': 'What do green automated checks prove?',
           'choices': ['Only that the configured checks passed for what they test',
                       'The application can never fail',
                       'Every business requirement is correct',
                       'No human review is needed'],
           'correct': 0},
          {'question': 'Why protect main?',
           'choices': ['To enforce policies such as review and required checks before important updates',
                       'Because Git deletes protected branches',
                       'To prevent history from being read',
                       'Because main cannot contain commits otherwise'],
           'correct': 0},
          {'question': 'What is one risk of extremely large mixed pull requests?',
           'choices': ['Higher cognitive load can reduce review quality',
                       'Git stops storing commits',
                       'They cannot contain tests',
                       'They automatically force-push'],
           'correct': 0},
          {'question': 'Why might a feature branch need updating during review?',
           'choices': ['Main may have advanced and the branch may need deliberate synchronization',
                       'Pull requests delete history',
                       'Reviews only work on empty branches',
                       'Branch names expire'],
           'correct': 0},
          {'question': 'What does a squash merge generally emphasize?',
           'choices': ['Combining the proposed change into a single target-branch commit',
                       'Preserving every branch pointer forever',
                       'Deleting the target branch',
                       'Avoiding review'],
           'correct': 0},
          {'question': 'What should happen after successful integration?',
           'choices': ['Verify relevant downstream behavior',
                       'Delete all tests',
                       'Force-push main',
                       'Ignore deployment results'],
           'correct': 0}],
 'reflection': 'Think about a change you recently made in Ascend or Forge. If you had to ask another engineer to '
               'review it, what context would they need before opening the diff? Describe how you would prove the '
               'change is ready for review and what kind of feedback would increase your confidence before '
               'integration.'}
