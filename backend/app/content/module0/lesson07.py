"""Module 0, Lesson 0.7."""

LESSON = {'id': '0-7',
 'title': 'Engineering Foundations Capstone',
 'summary': 'Apply the entire Module 0 mindset to a realistic Forge production incident: gather evidence, '
            'trace the request, identify ownership boundaries, recover safely, and write a blameless '
            'postmortem.',
 'duration_minutes': 90,
 'xp': 100,
 'audio_script': 'Welcome back to Ascend. This is Lesson 0.7: Engineering Foundations Capstone.\n'
                 '\n'
                 'This lesson is different.\n'
                 '\n'
                 'There is no new tool to memorize. There is no long list of definitions waiting for you. '
                 'Instead, you are going to step into a realistic incident and use the engineering habits '
                 'you have built throughout Module 0.\n'
                 '\n'
                 'It is two seventeen in the morning. Your phone buzzes with a short message: Forge users '
                 'cannot save workouts.\n'
                 '\n'
                 'That report is urgent, but it is incomplete. You do not yet know whether every user is '
                 'affected, whether the failure began after a deployment, whether the frontend is sending '
                 'the request correctly, whether FastAPI is returning an error, or whether PostgreSQL '
                 'rejected a write.\n'
                 '\n'
                 'Your first responsibility is not to fix the system. Your first responsibility is to reduce '
                 'uncertainty without destroying evidence.\n'
                 '\n'
                 'You open Forge. The dashboard loads. Existing workout history appears. Authentication '
                 'works. You start a new workout and tap Save. The application waits, then reports that the '
                 'save failed.\n'
                 '\n'
                 'Those observations matter.\n'
                 '\n'
                 'The dashboard loading tells you the phone can reach the application. Existing history '
                 'loading tells you at least one read path through the frontend, backend, and database is '
                 'functioning. Authentication working tells you the identity path is not completely '
                 'unavailable. Saving failing narrows the problem toward a write-specific path.\n'
                 '\n'
                 'Notice what you have not concluded. You have not declared that Docker is broken. You have '
                 'not blamed PostgreSQL. You have not restarted the server. You have translated a vague '
                 'report into a smaller problem.\n'
                 '\n'
                 'You open the browser or application network evidence. The save request reaches the Forge '
                 'backend endpoint and returns HTTP five hundred. The response arrives quickly. That means '
                 'the client reached the backend and the backend responded, even though it failed.\n'
                 '\n'
                 'You check Docker. The frontend, backend, and database containers are running. The backend '
                 'has not restarted. Again, that is useful, but it does not prove the workflow is healthy.\n'
                 '\n'
                 'You inspect the backend logs around the exact timestamp of the failed request. The '
                 'traceback shows that the workout insert attempted to write a field named effort_score. '
                 'PostgreSQL reports that the effort_score column does not exist.\n'
                 '\n'
                 'Now you have evidence that connects the user symptom to a specific application boundary.\n'
                 '\n'
                 'The frontend sent a save request. FastAPI accepted it. The backend attempted a database '
                 'write. The database rejected the statement because the deployed application expected a '
                 'schema change that the running database did not have.\n'
                 '\n'
                 'The immediate technical cause is a mismatch between the deployed backend code and the '
                 'database schema.\n'
                 '\n'
                 'But a capstone investigation does not stop at the first technical cause.\n'
                 '\n'
                 'Why did the mismatch reach the running environment? Perhaps the backend image was deployed '
                 'without the database migration. Perhaps the migration existed but the deployment process '
                 'did not run it. Perhaps the migration failed and the release continued. Perhaps there was '
                 'no automated validation proving that a fresh database could reach the expected schema.\n'
                 '\n'
                 'This is where DevOps thinking becomes visible.\n'
                 '\n'
                 'The developer changed the application contract. Operations ran the application '
                 'environment. The database represented persistent state. The deployment process connected '
                 'all three. The failure happened at the boundary between them.\n'
                 '\n'
                 'Your recovery decision should be deliberate.\n'
                 '\n'
                 'One option is to apply the missing migration. Another is to roll the backend back to the '
                 'previous compatible image. The safest choice depends on what has been verified: whether '
                 'the migration is reversible, whether it has been tested, whether data changes are '
                 'involved, whether the previous image is available, and how urgent restoration is.\n'
                 '\n'
                 'For this scenario, imagine that the migration is small, reviewed, and already tested in '
                 'development. You preserve the logs and record the deployed image version. You back up the '
                 'database. You apply the migration. Then you repeat the original save workflow.\n'
                 '\n'
                 'The workout saves successfully.\n'
                 '\n'
                 'You do not stop there.\n'
                 '\n'
                 'You reload workout history and confirm the new entry appears. You check an existing '
                 'workout. You verify that authentication still works. You inspect backend logs for new '
                 'errors. You confirm the database is healthy. Recovery is proven through the user outcome, '
                 'not through the success message from one command.\n'
                 '\n'
                 'Now you communicate.\n'
                 '\n'
                 'A useful status update might say: We confirmed that Forge workout saves failed because the '
                 'deployed backend expected a database column that had not been applied to the production '
                 'schema. The migration was applied after preserving evidence and backing up the database, '
                 'and save plus history workflows are now verified. We are reviewing the deployment process '
                 'to prevent application and schema versions from diverging again.\n'
                 '\n'
                 'That statement distinguishes impact, cause, recovery, verification, and follow-up.\n'
                 '\n'
                 'Next comes the postmortem.\n'
                 '\n'
                 'A blameless postmortem is not a search for the person who forgot a step. It is an '
                 'investigation into why the system allowed one missed or failed step to become user '
                 'impact.\n'
                 '\n'
                 'Ask what detection existed. Did any health check verify a write operation? Did the '
                 'deployment pipeline validate migration state? Did the application expose its expected '
                 'schema version? Was the deployed image version visible? Could the release have stopped '
                 'automatically when migration validation failed?\n'
                 '\n'
                 'Ask what reduced impact. Existing reads continued to work. Logs identified the database '
                 'error quickly. A tested migration existed. The previous image remained available. Those '
                 'are strengths worth preserving.\n'
                 '\n'
                 'Ask what made the incident harder. There was no alert on save error rate. The deployment '
                 'process did not enforce schema compatibility. The first user report was vague. Those are '
                 'system opportunities, not reasons for blame.\n'
                 '\n'
                 'Then create follow-up work.\n'
                 '\n'
                 'A high-value improvement might be adding a deployment step that runs migrations and fails '
                 'the release if they do not complete. Another might be a startup readiness check that '
                 'verifies the expected schema version. A third might be a synthetic test that saves and '
                 'deletes a test workout after deployment. A fourth might be displaying the backend build '
                 'and schema versions in an internal health endpoint.\n'
                 '\n'
                 'Each improvement tightens the feedback loop.\n'
                 '\n'
                 'Now step back and notice how every Module 0 lesson participated.\n'
                 '\n'
                 'How Engineers Think taught you to reduce uncertainty and map the system.\n'
                 '\n'
                 'Evidence Before Action taught you to preserve the scene, separate observations from '
                 'interpretations, and form testable hypotheses.\n'
                 '\n'
                 'The Internet Is Computers Talking taught you to trace the request through network and '
                 'application conversations.\n'
                 '\n'
                 'Anatomy of a Modern Application taught you the roles of client, frontend, API, backend, '
                 'database, configuration, and infrastructure.\n'
                 '\n'
                 'What DevOps Actually Connects taught you that the failure crossed development, delivery, '
                 'operations, and feedback boundaries.\n'
                 '\n'
                 'Reliability, Automation and Feedback taught you to care about user outcomes, '
                 'observability, repeatability, recovery, and learning.\n'
                 '\n'
                 'The capstone is not about knowing the answer in advance. It is about building a defensible '
                 'path from symptom to evidence, from evidence to action, and from recovery to improvement.\n'
                 '\n'
                 'That is engineering.\n'
                 '\n'
                 'Before you complete this lesson, work through the incident yourself. Do not simply copy '
                 'the conclusion. Build your own timeline. Name competing hypotheses. Explain why each piece '
                 'of evidence strengthens or weakens them. Choose a recovery plan and defend it. Write the '
                 'communication update. Then write the postmortem actions you would actually prioritize.\n'
                 '\n'
                 'When you finish, Module 0 will be complete.\n'
                 '\n'
                 'You will not know every DevOps tool. You are not supposed to.\n'
                 '\n'
                 'But you will have something more important: a foundation for approaching unfamiliar '
                 'systems without panic, gathering evidence without guessing, understanding how components '
                 'cooperate, connecting delivery to operations, and improving reliability through feedback.\n'
                 '\n'
                 'That foundation will support every module that follows.\n'
                 '\n'
                 'Git will give you controlled history and collaboration.\n'
                 '\n'
                 'Linux will help you understand the operating environment beneath applications.\n'
                 '\n'
                 'Networking will deepen the conversations you traced here.\n'
                 '\n'
                 'Docker will teach you how applications are packaged and run consistently.\n'
                 '\n'
                 'CI and CD will automate the delivery loop.\n'
                 '\n'
                 'AWS, Terraform, Kubernetes, monitoring, and security will expand the scale and capability '
                 'of the systems you manage.\n'
                 '\n'
                 'The tools will become more advanced. The mindset remains the same.\n'
                 '\n'
                 'Observe. Scope. Map. Hypothesize. Test. Recover. Verify. Communicate. Improve.\n'
                 '\n'
                 'You have reached the summit of Engineering Foundations.\n'
                 '\n'
                 'The next climb begins with Git and collaborative source control.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Convert a vague production report into verified observations and a precise impact '
                'statement.',
                'Trace a failing user workflow across client, network, frontend, API, backend, and database '
                'boundaries.',
                'Create and rank competing hypotheses using prediction, evidence, risk, and information '
                'value.',
                'Choose a safe recovery action, verify the complete user outcome, and communicate with '
                'appropriate confidence.',
                'Write a blameless postmortem and propose observability, automation, testing, and process '
                'improvements.'],
 'content': [{'heading': 'Capstone briefing',
              'body': 'At 2:17 AM, Forge users report that workout entries will not save. The dashboard '
                      'loads, authentication succeeds, and existing workout history is visible. Both the '
                      'mobile app and web interface reproduce the failure. Your task is to investigate, '
                      'restore the workflow safely, explain what happened, and design improvements.'},
             {'heading': 'Start with impact, not explanation',
              'body': 'The initial report is not a root cause. Define the affected capability, population, '
                      'conditions, and time. A precise impact statement might be: authenticated Forge users '
                      'can read existing workout data but cannot create new workout entries from either '
                      'client. That statement is useful even before the cause is known.'},
             {'heading': 'Preserve the scene',
              'body': 'Record timestamps, deployed versions, container state, request details, and relevant '
                      'logs before restarting or redeploying. Urgent recovery may eventually justify a '
                      'change, but preserving enough evidence protects the investigation and makes later '
                      'learning possible.'},
             {'heading': 'Use working behavior as evidence',
              'body': 'A loading dashboard proves several boundaries are functioning. Existing history '
                      'loading suggests a read path reaches the backend and database. Authentication '
                      'succeeding weakens hypotheses involving a total identity outage. Saving alone failing '
                      'focuses attention on the write workflow and anything unique to it.'},
             {'heading': 'Trace the failing conversation',
              'body': 'Follow the request in order: user action → client validation → network request → '
                      'Forge API endpoint → backend logic → database write → response → client rendering. At '
                      'each boundary, ask what evidence proves the request arrived, what it attempted, and '
                      'what it returned.'},
             {'heading': 'Build competing hypotheses',
              'body': 'Plausible explanations include a client payload defect, expired authorization, '
                      'backend validation failure, database unavailability, schema mismatch, or deployment '
                      'configuration error. Do not choose a favorite too early. Write the prediction each '
                      'hypothesis makes and the cheapest evidence that would distinguish it from the '
                      'others.'},
             {'heading': 'Interpret the incident evidence',
              'body': 'The save request reaches the backend and returns HTTP 500. Containers remain running. '
                      'Backend logs show PostgreSQL rejecting an insert because the effort_score column does '
                      'not exist. This evidence weakens client reachability, authentication, and total '
                      'database outage hypotheses while strongly supporting application-to-schema '
                      'incompatibility.'},
             {'heading': 'Find the ownership boundary',
              'body': 'The backend code expects one data contract while the database provides another. That '
                      'boundary connects development, deployment, operations, and persistent state. Treating '
                      'the event as only a coding mistake or only an operations mistake hides the system '
                      'condition that allowed incompatible versions to run together.'},
             {'heading': 'Choose recovery deliberately',
              'body': 'Possible recovery paths include applying the missing migration or rolling back the '
                      'backend to a compatible version. Evaluate urgency, reversibility, data risk, testing '
                      'evidence, backup state, and availability of the previous image. The smallest safe '
                      'action that restores the user outcome is preferable to broad uncontrolled changes.'},
             {'heading': 'Verify beyond the command',
              'body': 'A successful migration command is not proof of recovery. Repeat the original save '
                      'workflow, reload history, inspect the new record, test a related workflow, review '
                      'logs, and confirm database health. Verification should match the conditions that '
                      'originally failed.'},
             {'heading': 'Communicate what is known',
              'body': 'A professional update separates confirmed impact, supported cause, recovery action, '
                      'verification, remaining risk, and next checkpoint. Avoid vague claims such as “Docker '
                      'broke” or certainty beyond the evidence. Precise language protects trust during '
                      'uncertainty.'},
             {'heading': 'Write a blameless postmortem',
              'body': 'The postmortem should describe impact, timeline, detection, technical cause, '
                      'contributing system conditions, recovery, what went well, what made response harder, '
                      'and concrete follow-up actions. The purpose is not to remove accountability; it is to '
                      'improve the system rather than stopping at individual blame.'},
             {'heading': 'Improve the delivery contract',
              'body': 'Application code and database schema must evolve together. Useful controls include '
                      'automated migrations, schema-version checks, deployment gates, rollback-ready images, '
                      'compatibility tests, and an internal health endpoint exposing build and schema '
                      'versions.'},
             {'heading': 'Improve detection',
              'body': 'Container health alone would not detect this partial failure. Better signals include '
                      'workout-save error rate, synthetic write tests, structured database exceptions, '
                      'request correlation IDs, and alerts tied to user-impact thresholds.'},
             {'heading': 'Close the feedback loop',
              'body': 'The incident creates value only when learning changes the system. Prioritize '
                      'follow-up work, assign ownership, define completion evidence, and review whether the '
                      'improvement worked during the next deployment or controlled test.'},
             {'heading': 'Module 0 in one operating loop',
              'body': 'Observe the real behavior. Define scope. Map the system. Form testable hypotheses. '
                      'Select high-value tests. Make a controlled change. Verify the user outcome. '
                      'Communicate clearly. Document and improve. This loop is the foundation you will carry '
                      'into every DevOps tool and environment.'},
             {'heading': "Alex's Engineering Notes",
              'body': 'You do not need to recognize every failure immediately. Your advantage comes from '
                      'making uncertainty smaller without creating unnecessary risk. During pressure, return '
                      'to the loop: evidence before action, one boundary at a time, complete verification, '
                      'honest communication.'},
             {'heading': 'Takeaway',
              'body': 'Engineering maturity is not knowing every answer. It is producing a reliable path '
                      'from an unclear symptom to an evidence-supported recovery and a stronger system.'}],
 'diagram': {'title': 'Forge Incident Investigation Path',
             'nodes': [{'label': 'User report', 'detail': 'Workout entries fail to save.'},
                       {'label': 'Scope',
                        'detail': 'Reads and authentication work; writes fail on mobile and web.'},
                       {'label': 'Request evidence', 'detail': 'POST reaches backend and returns HTTP 500.'},
                       {'label': 'Backend evidence',
                        'detail': 'Traceback shows PostgreSQL rejected effort_score.'},
                       {'label': 'System cause',
                        'detail': 'Backend and database schema versions are incompatible.'},
                       {'label': 'Recovery',
                        'detail': 'Back up, apply tested migration or roll back safely.'},
                       {'label': 'Verification',
                        'detail': 'Save, reload, related workflow, logs, and database health pass.'},
                       {'label': 'Improvement',
                        'detail': 'Automate migrations, compatibility checks, synthetic writes, and version '
                                  'visibility.'}],
             'caption': 'A defensible incident response connects every conclusion to evidence and every '
                        'recovery to verification.'},
 'engineer_perspective': {'title': 'The capstone is the method, not the answer',
                          'body': 'A less experienced responder may be proud of guessing the schema problem '
                                  'quickly. A stronger engineer can explain how the evidence ruled out '
                                  'alternatives, why the recovery was safe, how the user outcome was '
                                  'verified, and what system changes will prevent recurrence. Repeatable '
                                  'reasoning scales better than intuition alone.'},
 'try_it_yourself': {'title': 'Run the tabletop incident before touching a system',
                     'intro': 'Use the scenario as a paper exercise first. This is safe to complete anywhere '
                              'and does not require breaking Forge.',
                     'steps': ['Write the initial impact statement using only the confirmed facts in the '
                               'scenario.',
                               'List at least five observations and five interpretations, keeping them '
                               'separate.',
                               'Draw the full workout-save request path from the user to PostgreSQL and '
                               'back.',
                               'Create four competing hypotheses and a prediction for each.',
                               'Rank five tests by information value, risk, and reversibility.',
                               'After reading the supplied evidence, explain which hypotheses weaken and '
                               'why.',
                               'Choose migration or rollback as your recovery and document the conditions '
                               'required to make it safe.',
                               'Write a verification checklist that proves the user outcome and checks for '
                               'side effects.',
                               'Write a three-sentence incident update for a technical stakeholder and a '
                               'nontechnical stakeholder.',
                               'Propose four follow-up actions and rank them by value versus effort.'],
                     'takeaway': 'A tabletop exercise lets you practice incident judgment without creating '
                                 'production risk. The skill is building a chain of reasoning another '
                                 'engineer can review.'},
 'lab': {'title': 'Incident 001 — Forge workout saves are failing',
         'instructions': ['Create a journal entry titled “Module 0 Capstone — Incident 001.” Record the '
                          'incident start time, initial report, and a precise impact statement.',
                          'Build an evidence table with columns for timestamp, source, observation, '
                          'interpretation, and confidence. Add at least twelve entries from the scenario.',
                          'Draw the end-to-end request path and mark every boundary that is already proven '
                          'working, still uncertain, or proven failing.',
                          'Create at least four competing hypotheses. For each, document its prediction, '
                          'supporting evidence, contradicting evidence, safest first test, and risk.',
                          'Write the first six investigation actions in exact order and justify why each '
                          'action comes before the next.',
                          'Use the supplied HTTP 500, stable container state, and PostgreSQL missing-column '
                          'traceback to update the confidence of every hypothesis.',
                          'Design two recovery plans: apply the migration and roll back the backend. Include '
                          'prerequisites, risks, rollback path, and verification for each. Choose one and '
                          'defend it.',
                          'Write a recovery verification checklist covering save, read-after-write, existing '
                          'data, authentication, logs, database health, and one related workflow.',
                          'Write an incident communication package: initial acknowledgement, investigation '
                          'update, recovery update, and final resolution statement.',
                          'Complete a blameless postmortem with impact, timeline, detection, root cause, '
                          'contributing conditions, what went well, what did not, and at least five '
                          'follow-up actions.',
                          'Classify the follow-up actions as observability, automation, testing, delivery, '
                          'documentation, resilience, or process. Assign priority, owner role, and '
                          'completion evidence.',
                          'Finish with a personal reflection explaining which Module 0 habit changed your '
                          'investigation most and how you will use it in your next real technical problem.']},
 'quiz': [{'question': 'Forge dashboard and workout history load, but saving a workout fails. What is the '
                       'strongest conclusion?',
           'choices': ['The entire application is unreachable',
                       'The read and initial delivery paths work, while the write path requires '
                       'investigation',
                       'PostgreSQL has definitely lost all data',
                       'Authentication is completely unavailable'],
           'correct': 1},
          {'question': 'The save request returns HTTP 500 from the Forge API. Which boundary is directly '
                       'proven?',
           'choices': ['The client reached the backend and received a server error',
                       'The database write succeeded',
                       'The frontend never sent a request',
                       'The network is completely offline'],
           'correct': 0},
          {'question': 'All Docker containers are running during the incident. What does that prove?',
           'choices': ['Every user workflow is healthy',
                       'The schema is correct',
                       'The processes are running, but end-to-end capability still requires verification',
                       'No application error can exist'],
           'correct': 2},
          {'question': 'Backend logs show PostgreSQL rejected effort_score because the column does not '
                       'exist. Which hypothesis is best supported?',
           'choices': ['A total Tailscale outage',
                       'A backend-to-database schema mismatch',
                       'An iPhone display defect',
                       'A DNS lookup failure'],
           'correct': 1},
          {'question': 'What is the best reason to maintain several hypotheses early in the incident?',
           'choices': ['It makes the incident report longer',
                       'It prevents the first plausible explanation from becoming an unsupported conclusion',
                       'It guarantees every hypothesis is correct',
                       'It removes the need for evidence'],
           'correct': 1},
          {'question': 'Which recovery choice is automatically correct?',
           'choices': ['Always migrate forward',
                       'Always restart every container',
                       'Always roll back',
                       'Neither; choose based on tested evidence, reversibility, data risk, urgency, and '
                       'available recovery paths'],
           'correct': 3},
          {'question': 'When is the incident recovery verified?',
           'choices': ['When the migration command exits successfully',
                       'When Docker Desktop shows green containers',
                       'When the original save workflow and related checks succeed under the failing '
                       'conditions',
                       'When the traceback disappears from the screen'],
           'correct': 2},
          {'question': 'What is the best postmortem question?',
           'choices': ['Who should be blamed for forgetting the step?',
                       'Why did the system allow incompatible application and schema versions to run '
                       'together?',
                       'How can we avoid writing anything down?',
                       'Which person can promise failure will never happen again?'],
           'correct': 1},
          {'question': 'Which improvement most directly prevents the same deployment mismatch?',
           'choices': ['Change the application color',
                       'Automate and gate schema migration or compatibility validation during deployment',
                       'Disable backend logs',
                       'Ask users to retry until it works'],
           'correct': 1},
          {'question': 'Which statement best summarizes Module 0?',
           'choices': ['Memorize commands before understanding the system',
                       'Act immediately whenever a user reports a problem',
                       'Use evidence, systems thinking, controlled action, verification, communication, and '
                       'feedback to improve outcomes',
                       'A running container is the final measure of success'],
           'correct': 2}],
 'reflection': 'You have completed Engineering Foundations. Describe how your troubleshooting approach has '
               'changed across Module 0. Use one real example from Forge, Ascend, your home server, or '
               'TruHearing. Explain how you would now observe, scope, map, hypothesize, test, recover, '
               'verify, communicate, and improve. Then identify the one habit you most want to make '
               'automatic before beginning Module 1.'}
