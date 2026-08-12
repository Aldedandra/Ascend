"""Module 1, Lesson 9: Git Workflow Capstone: Project Relay."""

LESSON = {'id': '1-9',
 'title': 'Git Workflow Capstone: Project Relay',
 'summary': 'Prove your Module 1 skills in a realistic end-to-end Git scenario: inspect an unfamiliar repository, '
            'make a focused change, synchronize remote history, resolve a conflict, prepare a review, recover a '
            'mistake, and verify the final state.',
 'duration_minutes': 90,
 'xp': 100,
 'audio_script': 'Welcome to the Module 1 Git Capstone.\n'
                 '\n'
                 'You have spent this module learning how Git records change, how files move through repository '
                 'states, how commits create meaningful history, how branches isolate work, how merges integrate '
                 'histories, how remotes connect repositories, how collaborative review adds evidence, and how '
                 'recovery depends on understanding state before acting.\n'
                 '\n'
                 'Now the structure changes.\n'
                 '\n'
                 'This capstone will not walk you through every command.\n'
                 '\n'
                 'You are going to receive an engineering objective, a repository with several conditions to '
                 'investigate, and a set of evidence requirements.\n'
                 '\n'
                 'Your job is to decide what to inspect, what to change, how to preserve history, and how to prove '
                 'that the final repository state is correct.\n'
                 '\n'
                 'This is deliberate.\n'
                 '\n'
                 'Real engineering work rarely says, run git status now, then run git diff, then type exactly this '
                 'commit command.\n'
                 '\n'
                 'Instead, you receive a problem.\n'
                 '\n'
                 'You gather evidence.\n'
                 '\n'
                 'You build a mental model.\n'
                 '\n'
                 'You choose an action.\n'
                 '\n'
                 'You verify the result.\n'
                 '\n'
                 'That is what this capstone measures.\n'
                 '\n'
                 'The scenario is called Project Relay.\n'
                 '\n'
                 'Imagine that you have joined a small internal engineering team.\n'
                 '\n'
                 'A service repository contains a simple application, documentation, and deployment configuration.\n'
                 '\n'
                 'The team asks you to make a small feature change and prepare it for review.\n'
                 '\n'
                 'That sounds straightforward.\n'
                 '\n'
                 'But the repository has several details you must notice.\n'
                 '\n'
                 'There may be uncommitted work.\n'
                 '\n'
                 'There may be an untracked file that does not belong in history.\n'
                 '\n'
                 'The local branch may not match your first assumption.\n'
                 '\n'
                 'The remote may contain newer history.\n'
                 '\n'
                 'A feature branch must be created.\n'
                 '\n'
                 'A focused change must be committed.\n'
                 '\n'
                 'A later synchronization step may create divergent history or a merge conflict.\n'
                 '\n'
                 'And at one point, you may need to recover from an intentional Git mistake.\n'
                 '\n'
                 'Nothing in the capstone requires destructive experimentation in Ascend itself.\n'
                 '\n'
                 'Use a disposable repository created specifically for the exercise.\n'
                 '\n'
                 'The goal is not to prove that you can remember every Git command.\n'
                 '\n'
                 'The goal is to demonstrate that you can reason about Git state.\n'
                 '\n'
                 'Before you begin, create a Journal entry titled Module 1 Git Capstone — Project Relay.\n'
                 '\n'
                 'Your Journal is part of the evidence.\n'
                 '\n'
                 'Record assumptions before acting.\n'
                 '\n'
                 'Record important command output.\n'
                 '\n'
                 'Record why you chose a particular action.\n'
                 '\n'
                 'Record verification after the action.\n'
                 '\n'
                 'This may feel slower than normal terminal work.\n'
                 '\n'
                 'That is intentional.\n'
                 '\n'
                 'You are practicing the discipline that makes fast terminal work safe later.\n'
                 '\n'
                 'The first phase is repository intake.\n'
                 '\n'
                 'You have been handed a repository you did not create.\n'
                 '\n'
                 'Before changing anything, determine where you are.\n'
                 '\n'
                 'What branch is checked out?\n'
                 '\n'
                 'Is the working tree clean?\n'
                 '\n'
                 'Which files are modified, staged, or untracked?\n'
                 '\n'
                 'What does recent history show?\n'
                 '\n'
                 'Is a remote configured?\n'
                 '\n'
                 'Does the current branch track an upstream branch?\n'
                 '\n'
                 'Do not fix anything during intake.\n'
                 '\n'
                 'Produce an evidence report first.\n'
                 '\n'
                 'This separates observation from action.\n'
                 '\n'
                 'The second phase is change design.\n'
                 '\n'
                 'The assignment asks you to update a service message and add a short operations note.\n'
                 '\n'
                 'Those changes belong to one feature.\n'
                 '\n'
                 'Temporary debugging output does not.\n'
                 '\n'
                 'Create a focused branch with a meaningful name.\n'
                 '\n'
                 'Make the requested change.\n'
                 '\n'
                 'Inspect the diff.\n'
                 '\n'
                 'Stage only the intended files.\n'
                 '\n'
                 'Inspect the staged diff.\n'
                 '\n'
                 'Then create a commit whose message explains the purpose.\n'
                 '\n'
                 'You should be able to answer one question before committing:\n'
                 '\n'
                 'If another engineer saw only this commit, would the snapshot and message tell one coherent story?\n'
                 '\n'
                 'The third phase is remote synchronization.\n'
                 '\n'
                 'A second repository will act as another engineer.\n'
                 '\n'
                 'That repository will publish a change to the shared remote.\n'
                 '\n'
                 'Your local feature work now exists while the remote history has also advanced.\n'
                 '\n'
                 'Do not blindly pull.\n'
                 '\n'
                 'First update your knowledge of the remote.\n'
                 '\n'
                 'Inspect how the histories relate.\n'
                 '\n'
                 'Decide how to integrate the change according to the capstone instructions.\n'
                 '\n'
                 'The important skill is not the exact command.\n'
                 '\n'
                 'The important skill is recognizing whether you are ahead, behind, or diverged and understanding '
                 'which branch you are integrating into which.\n'
                 '\n'
                 'The fourth phase is conflict resolution.\n'
                 '\n'
                 'Both sides will intentionally modify the same configuration line.\n'
                 '\n'
                 'Git should stop and ask for human judgment.\n'
                 '\n'
                 'When that happens, use the response pattern you practiced.\n'
                 '\n'
                 'Stop.\n'
                 '\n'
                 'Run git status.\n'
                 '\n'
                 'Identify the conflicted file.\n'
                 '\n'
                 'Read both sides.\n'
                 '\n'
                 'Determine the intended final content from the scenario requirements.\n'
                 '\n'
                 'Remove the markers.\n'
                 '\n'
                 'Stage the resolution.\n'
                 '\n'
                 'Verify the merge state.\n'
                 '\n'
                 'Complete the integration.\n'
                 '\n'
                 'Then test the resulting file content and inspect the commit graph.\n'
                 '\n'
                 'A conflict is not complete when the red warning disappears.\n'
                 '\n'
                 'It is complete when the integrated repository contains the intended result and the history makes '
                 'sense.\n'
                 '\n'
                 'The fifth phase is review preparation.\n'
                 '\n'
                 'Imagine you are about to open a pull request or merge request.\n'
                 '\n'
                 'Write a title and description.\n'
                 '\n'
                 'Explain what changed.\n'
                 '\n'
                 'Explain why.\n'
                 '\n'
                 'Explain how you validated it.\n'
                 '\n'
                 'Identify risk.\n'
                 '\n'
                 'List the automated checks you would want.\n'
                 '\n'
                 'Then perform your own review of the diff before asking another engineer to spend time on it.\n'
                 '\n'
                 'Look for unrelated changes.\n'
                 '\n'
                 'Look for debug output.\n'
                 '\n'
                 'Look for secrets.\n'
                 '\n'
                 'Look for generated files.\n'
                 '\n'
                 'Look for unclear commit history.\n'
                 '\n'
                 'The capstone is testing whether you treat review as evidence, not ceremony.\n'
                 '\n'
                 'The sixth phase is recovery.\n'
                 '\n'
                 'The exercise will intentionally create a local history mistake.\n'
                 '\n'
                 'You may move a branch reference or create a commit in a location you did not intend.\n'
                 '\n'
                 'Do not recreate the work from memory.\n'
                 '\n'
                 'Use repository evidence.\n'
                 '\n'
                 'Inspect status.\n'
                 '\n'
                 'Inspect the graph.\n'
                 '\n'
                 'Inspect reflog.\n'
                 '\n'
                 'Locate the desired commit.\n'
                 '\n'
                 'Verify it.\n'
                 '\n'
                 'Preserve it with a branch or another safe reference.\n'
                 '\n'
                 'Then explain why your recovery choice would be different if the commit had already been shared on '
                 'a protected branch.\n'
                 '\n'
                 'This is where Module 1 comes together.\n'
                 '\n'
                 'Git recovery is not a separate topic from commits, branches, remotes, and collaboration.\n'
                 '\n'
                 'Recovery depends on understanding all of them.\n'
                 '\n'
                 'The final phase is verification.\n'
                 '\n'
                 'At the end of the capstone, your repository should satisfy a set of conditions.\n'
                 '\n'
                 'The working tree should be in the expected state.\n'
                 '\n'
                 'The intended feature should exist.\n'
                 '\n'
                 'Temporary files should not be tracked.\n'
                 '\n'
                 'The history should contain coherent commits.\n'
                 '\n'
                 'The branch graph should make sense.\n'
                 '\n'
                 'The remote relationship should be understood.\n'
                 '\n'
                 'The conflict resolution should contain the required final value.\n'
                 '\n'
                 'The recovered commit should be reachable by an intentional branch reference.\n'
                 '\n'
                 'Your Journal should explain not only what you did, but why.\n'
                 '\n'
                 'There is no bonus for using the most advanced Git command.\n'
                 '\n'
                 'There is no penalty for pausing to inspect.\n'
                 '\n'
                 'The strongest solution is the one that is understandable, reproducible, and verified.\n'
                 '\n'
                 'If you become stuck, use progressive hints.\n'
                 '\n'
                 'Hint level one should remind you which concept to inspect.\n'
                 '\n'
                 'Hint level two may suggest a family of commands.\n'
                 '\n'
                 'Hint level three may give a more direct path.\n'
                 '\n'
                 'Try not to jump immediately to the strongest hint.\n'
                 '\n'
                 'Struggle is useful when it remains structured.\n'
                 '\n'
                 'This capstone also has a safety boundary.\n'
                 '\n'
                 'Do not use git reset dash dash hard, git clean dash f, or force push unless the capstone '
                 'explicitly instructs you to and you understand exactly what disposable state is at risk.\n'
                 '\n'
                 'You do not need those commands to demonstrate mastery.\n'
                 '\n'
                 'A professional Git workflow is not measured by how comfortable you are deleting state.\n'
                 '\n'
                 'It is measured by how well you understand state.\n'
                 '\n'
                 'When you finish, read your Journal from beginning to end.\n'
                 '\n'
                 'You should be able to see a pattern.\n'
                 '\n'
                 'Assumption.\n'
                 '\n'
                 'Evidence.\n'
                 '\n'
                 'Decision.\n'
                 '\n'
                 'Action.\n'
                 '\n'
                 'Verification.\n'
                 '\n'
                 'That pattern is bigger than Git.\n'
                 '\n'
                 'It will appear again in Linux, networking, containers, cloud infrastructure, CI/CD, Terraform, '
                 'Kubernetes, and incident response.\n'
                 '\n'
                 'Module 1 has taught Git.\n'
                 '\n'
                 'The capstone is testing engineering behavior.\n'
                 '\n'
                 'If you can enter an unfamiliar repository, establish its state, make a focused change, create '
                 'meaningful history, synchronize safely, resolve a conflict, prepare the work for review, recover a '
                 'recent mistake, and prove the final state, then you have achieved the goal of this module.\n'
                 '\n'
                 'You are no longer memorizing Git commands.\n'
                 '\n'
                 'You are operating a version-controlled system deliberately.\n'
                 '\n'
                 'Complete the evidence report.\n'
                 '\n'
                 'Complete the repository workflow.\n'
                 '\n'
                 'Complete the final verification.\n'
                 '\n'
                 'Then mark Module 1 finished.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Establish the state of an unfamiliar repository before making changes.',
                'Create focused branch-based work with deliberate staging and meaningful commit history.',
                'Synchronize with remote history and reason correctly about ahead, behind, and diverged states.',
                'Resolve a real merge conflict and verify both repository history and resulting content.',
                'Prepare a professional pull or merge request evidence package and recover a recent Git mistake '
                'using reflog.'],
 'content': [{'heading': 'Capstone rules',
              'body': 'This capstone gives you objectives and evidence requirements rather than a command-by-command '
                      'recipe. Use a disposable repository, document assumptions, gather evidence before action, and '
                      'verify each consequential change.'},
             {'heading': 'Scenario: Project Relay',
              'body': 'You have joined an internal team maintaining a small service repository. You must make a '
                      'feature change, synchronize with another contributor, resolve competing configuration '
                      'changes, prepare the work for review, and recover an intentional local-history mistake.'},
             {'heading': 'Phase 1 — Repository intake',
              'body': 'Inspect the repository before changing it. Determine current branch, working-tree state, '
                      'staged and untracked files, recent history, remote configuration, and upstream tracking. '
                      'Record an evidence report before fixing anything.'},
             {'heading': 'Phase 2 — Focused feature work',
              'body': 'Create a purposefully named feature branch. Implement the requested service-message and '
                      'operations-note change while excluding temporary debugging output. Inspect unstaged and '
                      'staged diffs before committing.'},
             {'heading': 'Phase 3 — Remote synchronization',
              'body': 'A second working repository will advance the shared remote. Update your local knowledge, '
                      'inspect branch relationships, and integrate deliberately instead of treating pull as a '
                      'reflex.'},
             {'heading': 'Phase 4 — Conflict resolution',
              'body': 'Both histories will modify the same configuration line. Use status, inspect both sides, '
                      'resolve the required final value, stage the resolution, complete integration, and verify both '
                      'file content and commit graph.'},
             {'heading': 'Phase 5 — Review preparation',
              'body': 'Prepare a pull or merge request title, description, validation evidence, risk statement, and '
                      'desired automated checks. Self-review the full branch diff before declaring the work ready.'},
             {'heading': 'Phase 6 — Recovery',
              'body': 'Recover an intentionally misplaced recent commit using repository evidence rather than '
                      'recreating the work. Reflog, git show, and a new intentional branch reference should form the '
                      'core of the recovery reasoning.'},
             {'heading': 'Phase 7 — Final verification',
              'body': 'Verify working-tree state, feature content, ignore behavior, branch history, remote '
                      'relationship, conflict resolution, and recovered history. Your Journal should make the full '
                      'workflow understandable to another engineer.'},
             {'heading': 'Progressive hints',
              'body': 'Use hints gradually. Level 1 identifies the concept to inspect. Level 2 suggests a command '
                      'family. Level 3 gives a more direct path. Do not skip immediately to the strongest hint '
                      'unless you are genuinely blocked.'},
             {'heading': 'Safety boundary',
              'body': 'You do not need destructive reset, clean, or force-push operations to complete this capstone. '
                      'If a command can destroy the only copy of work, stop and preserve evidence before '
                      'continuing.'},
             {'heading': 'Evidence requirements',
              'body': 'Capture status at major transitions, relevant diffs before commits, compact history views, '
                      'remote information, conflict evidence, review notes, reflog evidence during recovery, and '
                      'final verification.'},
             {'heading': 'What mastery looks like',
              'body': 'Mastery is not perfect command recall. It is the ability to establish state, choose a '
                      'proportional action, explain why, and verify the result without losing useful history.'},
             {'heading': 'Connection to DevOps',
              'body': 'The same Assumption → Evidence → Decision → Action → Verification pattern will reappear in '
                      'Linux, networking, containers, cloud, CI/CD, infrastructure as code, and incident response.'},
             {'heading': "Alex's Engineering Notes",
              'body': 'If you feel tempted to type a powerful Git command because the repository feels confusing, '
                      'stop. Confusion is evidence that your mental model is incomplete. Gather state until the '
                      'intended action becomes specific.'},
             {'heading': 'Takeaway',
              'body': 'Completing this capstone means you can operate Git through a realistic engineering workflow '
                      'rather than merely recognize Git commands.'}],
 'diagram': {'title': 'Project Relay — end-to-end Git workflow',
             'description': 'The capstone connects every major Module 1 skill into one evidence-driven engineering '
                            'loop.',
             'nodes': [{'label': 'Intake',
                        'detail': 'Inspect repository, branch, files, history, remote, and upstream.'},
                       {'label': 'Feature branch',
                        'detail': 'Make a focused change and create coherent local history.'},
                       {'label': 'Remote change', 'detail': 'Another repository advances shared history.'},
                       {'label': 'Integration', 'detail': 'Fetch, inspect divergence, and integrate deliberately.'},
                       {'label': 'Conflict', 'detail': 'Resolve competing intent and verify the resulting history.'},
                       {'label': 'Review', 'detail': 'Prepare diff, validation, risk, comments, and checks.'},
                       {'label': 'Recovery',
                        'detail': 'Use reflog and references to preserve a recent misplaced commit.'},
                       {'label': 'Verification',
                        'detail': 'Prove the final repository state satisfies every requirement.'}],
             'caption': 'Module 1 mastery means using Git as an observable system from intake through recovery—not '
                        'executing isolated commands.'},
 'engineer_perspective': {'title': 'Professional Git is controlled change',
                          'body': 'The valuable skill is not knowing the most commands. It is being able to enter a '
                                  'repository you did not create, preserve useful evidence, make a change with a '
                                  'small blast radius, integrate safely, and explain the resulting history to '
                                  'another engineer.'},
 'try_it_yourself': {'title': 'Capstone readiness check',
                     'intro': 'Before starting Project Relay, answer these without running destructive commands.',
                     'steps': ['Explain the difference between working-tree, staged, local-commit, and '
                               'remote-tracking state.',
                               'Explain why git fetch is useful before deciding how to integrate remote changes.',
                               'Explain what a branch and HEAD represent.',
                               'State your conflict-response sequence beginning with git status.',
                               'Explain when revert is generally safer than rewriting history.',
                               'Explain what reflog can help you recover.',
                               'Write your pre-commit and pre-push evidence checklists from memory.'],
                     'takeaway': 'If you can explain the state model, you are ready to solve the capstone without a '
                                 'command recipe.'},
 'lab': {'title': 'Project Relay — Module 1 Git Capstone',
         'instructions': ['Create a Journal entry titled “Module 1 Git Capstone — Project Relay.”',
                          'Create a disposable workspace containing a bare remote repository and two working clones '
                          'named relay-a and relay-b.',
                          'Seed the repository with README.md, service.txt, config.env.example, and .gitignore. '
                          'Commit and publish the baseline from relay-a, then clone relay-b.',
                          'In relay-a, intentionally create one modified tracked file, one staged file, and one '
                          'untracked debug.log. Before fixing anything, produce a repository intake report using '
                          'status, diff, staged diff, branch, log, remote, and upstream evidence.',
                          'Return relay-a to a deliberate clean baseline without tracking debug.log. Record why each '
                          'action addressed the specific state you observed.',
                          'Create a feature branch named feature/relay-status-message.',
                          "Change service.txt so the service message reads 'Project Relay: ready for review.' Add "
                          'ops-notes.md explaining how to verify the message. Create temporary debug output as well, '
                          'but do not include it in feature history.',
                          'Inspect the working-tree diff, stage only the coherent feature files, inspect the staged '
                          'diff, and create a meaningful commit.',
                          'In relay-b, update config.env.example so DEPLOY_ENV=production and add team-notes.md. '
                          'Commit and push the changes to main.',
                          'Back in relay-a, update your knowledge of the remote without automatically integrating '
                          'it. Record whether your feature branch is ahead, behind, or diverged relative to the '
                          'relevant shared history.',
                          'Integrate the updated main history into your feature branch using a deliberate workflow. '
                          'Record the branch you are on and the direction of integration before running it.',
                          'Create the intentional conflict: before integration is finalized, ensure the feature '
                          'branch also changes DEPLOY_ENV in config.env.example to staging. Resolve the conflict so '
                          "the final value is DEPLOY_ENV=production, because Project Relay's review environment "
                          'requirement says production for this scenario.',
                          'During the conflict, capture git status and the conflict-marker section before editing. '
                          'After resolving, stage the file, verify status, complete integration, and inspect git log '
                          '--oneline --graph --decorate --all.',
                          'Self-review the complete feature branch against main. Confirm debug.log is not tracked '
                          'and no unrelated files are included.',
                          'Write a pull/merge request title and description containing purpose, scope, validation, '
                          'risk, and desired automated checks.',
                          'Write three review comments as if you were another engineer: one question, one '
                          'evidence-based positive observation, and one actionable improvement.',
                          'Respond to the actionable comment with one focused follow-up commit on the feature '
                          'branch.',
                          'Create a recovery exercise by checking out the parent of the current feature tip in '
                          'detached HEAD, creating recovery-note.md, and committing it while detached.',
                          'Return to the feature branch so the detached commit is no longer the checked-out tip. Use '
                          'reflog to locate the detached commit, verify it with git show, and create a branch named '
                          'recovery/relay-note pointing to it.',
                          'Explain why reflog-based recovery is preferable to recreating the lost-looking work from '
                          'memory.',
                          'Explain how your recovery decision would change if the problematic commit had already '
                          'been merged into a protected main branch and deployed.',
                          'Perform final verification: clean or intentionally understood status, feature message '
                          'correct, DEPLOY_ENV=production, debug.log untracked or ignored, expected commits visible, '
                          'feature history understandable, remote configuration correct, and recovery/relay-note '
                          'points to the recovered commit.',
                          "Finish the Journal with a section titled 'Assumption → Evidence → Decision → Action → "
                          "Verification' and summarize one example from each major capstone phase."]},
 'quiz': [{'question': 'What is the capstone primarily measuring?',
           'choices': ['Ability to reason about Git state through an end-to-end workflow',
                       'Ability to memorize every Git flag',
                       'Typing speed',
                       'Knowledge of GitHub pricing'],
           'correct': 0},
          {'question': 'What should happen during repository intake?',
           'choices': ['Observe and record state before fixing anything',
                       'Immediately clean every file',
                       'Force-push main',
                       'Delete untracked files'],
           'correct': 0},
          {'question': 'Why is fetch preferred before integration in the capstone?',
           'choices': ['It updates remote knowledge while preserving an inspection point',
                       'It always resolves conflicts automatically',
                       'It deletes local commits',
                       'It creates a pull request'],
           'correct': 0},
          {'question': 'What is the required final conflict resolution value?',
           'choices': ['DEPLOY_ENV=production',
                       'DEPLOY_ENV=staging',
                       'Delete the configuration line',
                       'Keep both conflict markers'],
           'correct': 0},
          {'question': 'What should the feature commit exclude?',
           'choices': ['Temporary debug output unrelated to the coherent feature',
                       'service.txt',
                       'ops-notes.md',
                       'Meaningful history'],
           'correct': 0},
          {'question': 'What does self-review compare?',
           'choices': ['The proposed branch diff and stated intent before requesting review',
                       'Only branch names',
                       'Only remote URLs',
                       'Only file sizes'],
           'correct': 0},
          {'question': 'What is the key recovery evidence source for the detached commit?',
           'choices': ['git reflog', 'git clean', 'git reset --hard', 'git push --force'],
           'correct': 0},
          {'question': 'Why create recovery/relay-note?',
           'choices': ['To give the recovered commit an intentional reachable reference',
                       'To delete the commit',
                       'To replace reflog permanently',
                       'To merge into main automatically'],
           'correct': 0},
          {'question': 'What changes when a bad commit has already reached protected main and deployment?',
           'choices': ['Recovery becomes a shared operational decision with a larger blast radius',
                       'Nothing changes',
                       'The commit becomes untracked',
                       'Git disables revert'],
           'correct': 0},
          {'question': 'What pattern should appear throughout the Journal?',
           'choices': ['Assumption → Evidence → Decision → Action → Verification',
                       'Action → Guess → Force → Delete',
                       'Commit → Force push → Hope',
                       'Clone → Delete → Restart'],
           'correct': 0}],
 'reflection': 'Which capstone phase required the most reasoning: intake, focused change, synchronization, conflict '
               'resolution, review, or recovery? Explain what evidence changed your decision in that phase. Then '
               'describe how the same evidence-driven behavior could apply outside Git in Linux, Docker, cloud '
               'infrastructure, or incident response.'}
