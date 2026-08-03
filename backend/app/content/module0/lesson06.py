"""Module 0, Lesson 0.6."""

LESSON = {'id': '0-6',
 'title': 'Reliability, Automation & Feedback',
 'summary': 'Learn why reliable systems are designed for failure, how observability makes behavior visible, '
            'how automation reduces variation, and how feedback turns incidents into improvement.',
 'duration_minutes': 80,
 'xp': 80,
 'audio_script': 'Welcome back to Ascend. This is Lesson 0.6: Reliability, Automation and Feedback.\n'
                 '\n'
                 'Imagine that it is two seventeen in the morning and your phone buzzes. The message is '
                 'short: Forge is not saving workouts.\n'
                 '\n'
                 'You open the application. The dashboard loads. Old data is visible. But when you try to '
                 'save a new workout, the request fails.\n'
                 '\n'
                 'At that moment, reliability stops being an abstract word. It becomes the difference '
                 'between a system you can understand and recover, and a system that leaves you guessing in '
                 'the dark.\n'
                 '\n'
                 'A reliable system is not a system that never fails. Every useful system eventually '
                 'experiences failure. Hardware breaks. Networks become unavailable. certificates expire. '
                 'dependencies change. disks fill. processes crash. people make mistakes. deployments '
                 'introduce unexpected behavior.\n'
                 '\n'
                 'Reliability is the ability of a system and the people responsible for it to continue '
                 'delivering an acceptable outcome, detect when that outcome is at risk, recover within a '
                 'reasonable amount of time, and learn enough to reduce the chance or impact of the same '
                 'failure later.\n'
                 '\n'
                 'That definition includes technology, process, and people.\n'
                 '\n'
                 'Consider Ascend. The backend container being marked as running is not the outcome you care '
                 'about. The outcome is that you can open the application, load a lesson, submit a quiz, '
                 'save completion, and continue learning. A green container is evidence about one component. '
                 "It is not proof that the service is reliable from the learner's point of view.\n"
                 '\n'
                 'This distinction is central to reliability engineering. Components support outcomes. The '
                 'outcome is what matters.\n'
                 '\n'
                 'Now think back to the Ascend backend restart loop. Docker kept restarting the backend '
                 'container. The visible behavior looked like an operations problem. But the logs showed '
                 'that Python could not import ACHIEVEMENTS from the content module. Docker was doing '
                 'exactly what it had been configured to do: restart a failed process. The application '
                 'contract was broken, so the process exited.\n'
                 '\n'
                 'Reliability came from several things working together. Docker made the failure visible '
                 'through repeated restarts. Logs preserved the traceback. You inspected the evidence '
                 'instead of repeatedly rebuilding at random. The missing contract was restored. The backend '
                 'was rebuilt. Then the actual application workflow was verified.\n'
                 '\n'
                 'That incident illustrates the first major principle of this lesson: reliability begins '
                 'with visibility.\n'
                 '\n'
                 'Troubleshooting a system without visibility is like walking into a dark room with no '
                 'windows and no flashlight. You may know something is wrong, but you cannot see where the '
                 'obstacle is or whether your movement is making the situation better.\n'
                 '\n'
                 "Observability is the ability to understand a system's internal state by examining the "
                 'signals it produces.\n'
                 '\n'
                 'Three common observability signals are logs, metrics, and traces.\n'
                 '\n'
                 'Logs describe events. A log may say that a process started, a request failed, '
                 'authentication was denied, a database connection timed out, or an import could not be '
                 'completed. Logs are often the best place to understand a specific event in detail.\n'
                 '\n'
                 'Metrics describe quantities over time. Request count, error rate, response time, CPU '
                 'usage, memory consumption, disk space, queue depth, and container restart count are '
                 'metrics. Metrics help you see trends, compare normal and abnormal behavior, and determine '
                 'whether a problem is isolated or growing.\n'
                 '\n'
                 'Traces follow a single unit of work across boundaries. In a distributed application, one '
                 'user request may pass through a proxy, frontend, API, identity provider, database, and '
                 'external service. A trace connects those steps so you can see where time was spent and '
                 'where the request failed.\n'
                 '\n'
                 'Your current home applications may not yet have a full tracing platform, and that is fine. '
                 'The important concept is learning to think in correlated events. A browser request at two '
                 'seventeen and four seconds, a FastAPI log at two seventeen and four seconds, and a '
                 'database error at two seventeen and five seconds may all belong to the same workflow.\n'
                 '\n'
                 'Health checks are another visibility tool. A liveness check asks whether a process is '
                 'alive enough that it should continue running. A readiness check asks whether it is '
                 'prepared to receive useful work. Those are different questions.\n'
                 '\n'
                 'A FastAPI process may be alive while its database connection is unavailable. It may pass a '
                 'simple liveness check but fail readiness because it cannot fulfill requests. This is why a '
                 'single green light can be misleading.\n'
                 '\n'
                 'Good monitoring begins with a clear question. What user outcome are we protecting? Which '
                 'signals provide early warning that the outcome is degrading? What threshold deserves '
                 'attention? Who should respond? What action should they take?\n'
                 '\n'
                 'Monitoring without purpose creates noise. If every minor fluctuation generates an alert, '
                 'people learn to ignore alerts. That is called alert fatigue. A useful alert should be '
                 'actionable. It should tell the responder that something meaningful may require attention '
                 'and provide enough context to begin safely.\n'
                 '\n'
                 'For Forge, an alert that the backend container restarted once during a planned deployment '
                 'may not matter. An alert that workout save requests have failed for ten minutes while the '
                 'frontend remains available is much closer to a user-impact signal.\n'
                 '\n'
                 'Reliability also requires recovery.\n'
                 '\n'
                 'Mean time to recovery, often shortened to M T T R, describes how long it takes to restore '
                 'an acceptable service after a failure. You do not need to memorize the acronym yet. Focus '
                 'on the idea: when failure occurs, how quickly can the team detect it, understand it, '
                 'choose a safe response, restore service, and verify the result?\n'
                 '\n'
                 'Fast recovery depends on preparation. Do you know which logs to inspect? Is there a '
                 'documented restart or rollback process? Can you identify the currently deployed version? '
                 'Is data backed up? Can a previous container image be redeployed? Do you know what healthy '
                 'behavior looks like?\n'
                 '\n'
                 'Recovery is not the same as root-cause analysis. During an urgent incident, restoring '
                 'service may come first. A rollback can be the correct action even before the exact cause '
                 'is known. But preserve evidence when possible and return afterward to understand what '
                 'happened.\n'
                 '\n'
                 'This leads to automation.\n'
                 '\n'
                 'People sometimes describe automation as a way to save time or avoid repetitive work. That '
                 'is true, but it is not the most important benefit.\n'
                 '\n'
                 'Automation reduces variation.\n'
                 '\n'
                 'A manual process depends on memory, timing, environment, interpretation, and attention. '
                 'Two people may perform the same written procedure differently. The same person may perform '
                 'it differently when tired or under pressure. A script or pipeline executes declared steps '
                 'consistently and creates a record of what happened.\n'
                 '\n'
                 'Your Docker Compose files are a form of automation. Instead of manually starting a '
                 'database, configuring a network, remembering ports, starting a backend, and starting a '
                 'frontend, Compose declares the desired services and relationships. One command can move '
                 'the environment toward that declared state.\n'
                 '\n'
                 'Your build commands are also automation. Vite creates a repeatable frontend bundle. '
                 'Dockerfiles describe image construction. Capacitor sync copies web assets and updates the '
                 'native project. Git preserves the exact source changes that produced a version.\n'
                 '\n'
                 'Automation should be designed with safety in mind. A fast automated mistake can cause harm '
                 'at scale. Safe automation should validate inputs, fail clearly, limit permissions, be '
                 'observable, support dry runs when appropriate, and provide a recovery path.\n'
                 '\n'
                 'Idempotence is a useful concept here. An idempotent operation can be applied more than '
                 'once without producing unintended additional changes after the desired state is reached. '
                 'For example, a configuration task that ensures a directory exists should succeed whether '
                 'the directory is missing or already present. Idempotence makes retries safer.\n'
                 '\n'
                 'Automation also creates feedback.\n'
                 '\n'
                 'A continuous integration pipeline can tell you within minutes that code does not compile, '
                 'tests fail, formatting changed, or a dependency contains a known vulnerability. That '
                 'feedback arrives while the change is still small and familiar.\n'
                 '\n'
                 'The earlier feedback arrives, the cheaper it usually is to act on.\n'
                 '\n'
                 'A syntax error caught in the editor is cheaper than one caught during a Docker build. A '
                 'failed automated test is cheaper than a user reporting broken behavior. A staging failure '
                 'is cheaper than a production outage. A capacity trend is cheaper than a completely full '
                 'disk.\n'
                 '\n'
                 'This is why DevOps emphasizes short feedback loops.\n'
                 '\n'
                 'The loop is simple: make a small change, observe the result, learn, and adjust.\n'
                 '\n'
                 'You already use this pattern with Forge. You deploy a feature, use it on your phone, '
                 'notice friction, improve the interface, rebuild, and test again. The real-world use of the '
                 'application is feedback. The goal is not to avoid discovering problems. The goal is to '
                 'discover them quickly enough that improvement remains safe and manageable.\n'
                 '\n'
                 'Feedback comes from technical systems and from people. Logs, metrics, test results, and '
                 'alerts are technical feedback. Support tickets, employee comments, failed workflows, '
                 'analytics, and conversations are human feedback.\n'
                 '\n'
                 'At TruHearing, a user saying that OneDrive remains on Signing in is a signal. It is '
                 'incomplete, but it enters the feedback loop. You gather device details, sign-in state, '
                 'client version, network conditions, service health, and logs. The evidence improves the '
                 'response. If the same pattern occurs repeatedly, the organization may improve '
                 'documentation, detection, automation, or configuration.\n'
                 '\n'
                 'Reliable teams do not stop at fixing the immediate incident. They ask what should change '
                 'so the next incident is less likely, less harmful, easier to detect, or faster to recover '
                 'from.\n'
                 '\n'
                 'That is the purpose of a post-incident review.\n'
                 '\n'
                 'A useful review reconstructs the timeline, describes impact, identifies contributing '
                 'conditions, explains detection and response, and creates concrete follow-up actions. It '
                 "avoids reducing a complex system failure to one person's mistake.\n"
                 '\n'
                 'Blameless does not mean nobody is accountable. It means the investigation focuses on how '
                 'the system of work allowed an action or condition to create harm. People operate inside '
                 'tools, permissions, documentation, deadlines, interfaces, and incentives. Improve those '
                 'conditions and reliability improves.\n'
                 '\n'
                 'Consider the replacement-project-folder problem in Ascend. Replacing the complete folder '
                 'worked, but it removed the hidden Git metadata and complicated commits. The lesson was not '
                 'simply that someone copied the wrong thing. The workflow itself made a risky action easy. '
                 'The process improved when changes became focused ZIPs applied inside the existing '
                 'repository.\n'
                 '\n'
                 'That is reliability through process design.\n'
                 '\n'
                 'Consider the stale Tailscale address in Forge. The source code on the Mac did not contain '
                 'the old address, but the running frontend still called it. The system had several version '
                 'boundaries: source, build output, container image, deployed container, and installed '
                 'client. The improvement is not only remembering to rebuild. It is making version state '
                 'visible and the deployment path repeatable.\n'
                 '\n'
                 'That is reliability through delivery design.\n'
                 '\n'
                 'Consider your home server. It supports Forge and Ascend, but it is still one physical '
                 'host. A power loss, disk failure, Windows update, Docker failure, or network problem can '
                 'affect both applications. Reliability thinking does not require immediately building an '
                 'expensive highly available cluster. It begins by identifying the risk and choosing '
                 'proportional controls: backups, restart policies, documented recovery, versioned images, '
                 'health checks, and verification steps.\n'
                 '\n'
                 'Reliability is always a tradeoff. Greater redundancy, monitoring, testing, and automation '
                 'require time and money. The right level depends on impact. A personal learning app does '
                 'not need the same architecture as a hospital system. But both benefit from knowing what '
                 'failure matters and how recovery will work.\n'
                 '\n'
                 'This is sometimes expressed through service objectives. A service level indicator is a '
                 'measurement of behavior, such as the percentage of successful requests. A service level '
                 'objective is a target for that measurement, such as ninety-nine point five percent '
                 'successful lesson loads during a month. You do not need to implement formal objectives '
                 'today, but the mindset is useful: define reliability in measurable user terms.\n'
                 '\n'
                 'Notice how much stronger that is than saying, the server should be reliable.\n'
                 '\n'
                 'A measurable objective creates a shared definition. It also helps balance reliability work '
                 'and feature work. If the service is comfortably meeting its objective, the team may accept '
                 'some change risk. If reliability is below the objective, stabilizing the system may become '
                 'the priority.\n'
                 '\n'
                 'Reliability, automation, and feedback reinforce each other.\n'
                 '\n'
                 'Observability creates evidence. Evidence reveals repeated problems. Automation removes '
                 'fragile manual steps. Automated validation creates earlier feedback. Faster feedback makes '
                 'smaller changes possible. Smaller changes are easier to understand and recover. Incidents '
                 'create learning. Learning improves the system.\n'
                 '\n'
                 'This is a reinforcing loop.\n'
                 '\n'
                 "The engineer's perspective is simple: reliable systems are not the ones that never fail. "
                 'They are the ones whose failures are visible, understandable, recoverable, and useful as '
                 'feedback.\n'
                 '\n'
                 'As you move into the lab, you will deliberately interrupt an Ascend or Forge service in a '
                 'controlled environment. Your goal is not merely to restart it. Your goal is to observe the '
                 'user impact, collect signals, recover safely, verify the original workflow, and identify '
                 'one improvement that would make the next recovery easier.\n'
                 '\n'
                 'This is the final preparation before the Module 0 capstone. In the next lesson, you will '
                 'receive a realistic incident and use the entire foundation: engineering questions, '
                 'evidence, request tracing, application anatomy, DevOps flow, observability, automation, '
                 'recovery, and learning.\n'
                 '\n'
                 'For now, remember the operating principle of Lesson 0.6: design for failure, automate for '
                 'consistency, observe for understanding, recover for the user, and turn every outcome into '
                 'feedback.',
 'content': [{'heading': 'Learning objectives',
              'body': 'By the end of this lesson, you should be able to define reliability in terms of user '
                      'outcomes; distinguish logs, metrics, traces, liveness, and readiness; explain why '
                      'automation improves consistency; describe recovery and feedback loops; and propose '
                      'proportional reliability improvements for Ascend, Forge, your home server, or a '
                      'TruHearing workflow.'},
             {'heading': 'Reliability is not the absence of failure',
              'body': 'Every meaningful system eventually experiences failure. Reliability is the ability to '
                      'continue delivering an acceptable outcome, detect degradation, recover within a '
                      'reasonable time, and learn enough to reduce future impact. The goal is not '
                      'perfection. The goal is controlled, understandable, recoverable behavior.'},
             {'heading': 'Start with the user outcome',
              'body': 'A running container is not the final outcome. For Ascend, the outcome is that a '
                      'learner can load a lesson, submit a quiz, save progress, and continue later. For '
                      'Forge, the outcome is that a user can record and retrieve health or workout data. '
                      'Component health supports those outcomes but does not replace end-to-end '
                      'verification.'},
             {'heading': 'Observability makes internal behavior visible',
              'body': 'Observability is the ability to infer what is happening inside a system from the '
                      'signals it produces. It turns a vague report into inspectable behavior. Without '
                      'visibility, troubleshooting becomes guesswork. With useful signals, engineers can '
                      'locate the first boundary where expected behavior stopped.'},
             {'heading': 'Logs explain events',
              'body': 'Logs record discrete events and context: process startup, request failures, '
                      'authentication decisions, exceptions, timeouts, and dependency errors. The Ascend '
                      'restart loop became understandable because the Python traceback identified the '
                      'missing ACHIEVEMENTS import. Useful logs include timestamps, severity, component, and '
                      'enough context to connect the event to a workflow.'},
             {'heading': 'Metrics reveal trends and scale',
              'body': 'Metrics are numeric measurements collected over time. Error rate, response latency, '
                      'CPU, memory, disk space, request volume, and restart count can show whether a problem '
                      'is isolated, persistent, or growing. Metrics are especially valuable for comparing '
                      'current behavior to a known baseline.'},
             {'heading': 'Traces connect one request across services',
              'body': 'A trace follows one unit of work across boundaries. A single action may cross a '
                      'proxy, API, identity provider, database, and external dependency. Even without a '
                      'formal tracing platform, correlate browser requests, backend logs, and dependency '
                      'events by time and request context to reconstruct the path.'},
             {'heading': 'Liveness and readiness answer different questions',
              'body': 'Liveness asks whether a process is alive enough to keep running. Readiness asks '
                      'whether it can currently accept useful work. A FastAPI process can be alive while '
                      'PostgreSQL is unavailable. A strong health model checks the dependencies required for '
                      'the user outcome instead of relying on one green process indicator.'},
             {'heading': 'Monitoring and alerting need purpose',
              'body': 'Monitoring observes signals over time. Alerting calls attention to conditions that '
                      'may require action. Alerts should be tied to meaningful impact, actionable, and '
                      'supported by context or a runbook. Too many low-value alerts create alert fatigue and '
                      'teach responders to ignore the system.'},
             {'heading': 'Recovery is an engineering capability',
              'body': 'Recovery includes detection, diagnosis, safe action, restoration, and verification. '
                      'Mean time to recovery describes how quickly an acceptable service is restored after '
                      'failure. Recovery becomes faster when versions are identifiable, logs are accessible, '
                      'backups exist, rollback steps are known, and healthy behavior is documented.'},
             {'heading': 'Automation reduces variation',
              'body': 'The greatest value of automation is consistency. Docker Compose, Dockerfiles, Vite '
                      'builds, Capacitor sync, scripts, and CI pipelines replace memory-dependent steps with '
                      'declared repeatable behavior. Automation creates evidence and makes the process '
                      'easier to review, repeat, and improve.'},
             {'heading': 'Safe automation needs guardrails',
              'body': 'Automation can repeat mistakes quickly, so it should validate inputs, use least '
                      'privilege, fail clearly, expose progress, support dry runs where useful, and provide '
                      'recovery. Idempotent operations are safer to retry because repeated execution '
                      'converges on the desired state rather than producing unintended duplicate changes.'},
             {'heading': 'Short feedback loops reduce risk',
              'body': 'Feedback should arrive while a change is small and familiar. Editor errors, tests, '
                      'builds, staging checks, production signals, user reports, and support tickets all '
                      'provide feedback at different times. Earlier feedback is generally cheaper to act on '
                      'and makes smaller, safer changes practical.'},
             {'heading': 'Incidents should improve the system',
              'body': 'A post-incident review reconstructs impact, timeline, contributing conditions, '
                      'detection, response, and follow-up actions. A blameless approach examines the system '
                      'of work instead of stopping at an individual mistake. The goal is to make recurrence '
                      'less likely, impact smaller, detection faster, or recovery easier.'},
             {'heading': 'Reliability should match the risk',
              'body': 'A personal home-server app does not require the same controls as a clinical or '
                      'financial service. Reliability investment should be proportional to impact. For '
                      'Ascend and Forge, backups, restart policies, versioned releases, health checks, '
                      'focused monitoring, and a tested recovery path may provide the right next level.'},
             {'heading': 'Measure outcomes, not vague intentions',
              'body': 'A service level indicator measures behavior, such as successful lesson loads or '
                      'workout-save latency. A service level objective sets a target for that measurement. '
                      'Even without formal SLOs, define reliability in measurable user terms. “The server '
                      'should be reliable” is weaker than “lesson requests should succeed at least 99.5 '
                      'percent of the time.”'},
             {'heading': 'The reinforcing loop',
              'body': 'Observability creates evidence. Evidence reveals recurring weakness. Automation '
                      'removes fragile manual variation. Automated validation produces earlier feedback. '
                      'Small changes are easier to recover. Incidents generate learning. Learning improves '
                      'the next design. Reliability, automation, and feedback are not separate topics; they '
                      'form one continuous improvement loop.'},
             {'heading': "Alex's Engineering Notes",
              'body': 'Do not ask only, “Is the container running?” Ask, “Can the user complete the '
                      'outcome?” Do not automate a process you do not understand. First make the process '
                      'visible and safe, then automate the repeatable parts. And after recovery, capture the '
                      'lesson before urgency erases it.'},
             {'heading': 'Takeaway',
              'body': 'Design for failure. Automate for consistency. Observe for understanding. Recover for '
                      'the user. Turn every outcome into feedback.'}],
 'diagram': {'title': 'The reliability improvement loop',
             'description': 'Reliable delivery improves through a repeating cycle rather than one permanent '
                            'fix.',
             'nodes': [{'label': 'User outcome',
                        'detail': 'Define the workflow that must remain useful: load, save, authenticate, '
                                  'learn, or complete a task.'},
                       {'label': 'Observe',
                        'detail': 'Collect logs, metrics, traces, health signals, timestamps, and user '
                                  'reports.'},
                       {'label': 'Detect and scope',
                        'detail': 'Recognize degradation and identify who, what, where, and how much is '
                                  'affected.'},
                       {'label': 'Recover',
                        'detail': 'Use the smallest safe action, rollback, restart, repair, or failover that '
                                  'restores the outcome.'},
                       {'label': 'Verify',
                        'detail': 'Repeat the original workflow and check for side effects instead of '
                                  'trusting component status alone.'},
                       {'label': 'Learn',
                        'detail': 'Reconstruct the timeline, contributing conditions, and detection or '
                                  'response gaps.'},
                       {'label': 'Improve and automate',
                        'detail': 'Add guardrails, tests, monitoring, documentation, backups, or repeatable '
                                  'automation.'},
                       {'label': 'Feedback',
                        'detail': 'Use the next deployment, incident, and user experience to evaluate '
                                  'whether the improvement worked.'}],
             'caption': 'The goal is not to eliminate every failure. It is to make failures less surprising, '
                        'less harmful, easier to understand, and faster to recover from.'},
 'engineer_perspective': {'title': 'Reliable systems fail well',
                          'body': 'A system that never appears to fail may simply be hiding its failures. '
                                  'Engineers value systems that expose meaningful signals, degrade '
                                  'predictably, preserve data, support recovery, and teach the team how to '
                                  'improve. Reliability is a designed capability, not a lucky streak.'},
 'try_it_yourself': {'title': 'Observe a controlled service interruption',
                     'intro': 'Use Ascend or Forge in your local environment. Do not perform this exercise '
                              'on a work production system.',
                     'steps': ['Open the application and complete one normal workflow. Record the expected '
                               'result.',
                               'Run docker compose ps and record the current state of the frontend, backend, '
                               'and database.',
                               'Follow the backend logs in one terminal with docker compose logs -f backend.',
                               'Stop only the backend service with docker compose stop backend.',
                               'Repeat the original workflow and record exactly what the user sees, '
                               'including the browser Network result if available.',
                               'Compare the user symptom, Docker state, and logs. Identify which signals '
                               'were useful and which were missing.',
                               'Start the backend again with docker compose start backend and watch the '
                               'recovery.',
                               'Repeat the original workflow to verify the outcome, not just the container '
                               'state.',
                               'Write one improvement that would make detection or recovery faster next '
                               'time.'],
                     'takeaway': 'A controlled failure turns reliability from theory into evidence. The '
                                 'recovery is complete only when the original user workflow succeeds again.'},
 'lab': {'title': 'Run a controlled reliability exercise and mini postmortem',
         'instructions': ['Choose Ascend or Forge in a safe local environment and define one user workflow '
                          'to protect.',
                          'Record the baseline: timestamp, application version or Git commit, Docker service '
                          'state, and successful workflow result.',
                          'Create a simple reliability hypothesis: predict the user symptom and system '
                          'signals you expect if one selected service stops.',
                          'Open logs or browser developer tools before introducing the failure so evidence '
                          'is preserved.',
                          'Stop exactly one non-database service. Do not delete containers, volumes, or '
                          'data.',
                          'Repeat the protected workflow and record the observed user impact, HTTP status or '
                          'network behavior, container state, and relevant logs.',
                          'Restore the service using the smallest reversible action and record how long '
                          'recovery takes.',
                          'Verify the original workflow under the same conditions and check one related '
                          'workflow for side effects.',
                          'Write a mini postmortem with impact, timeline, detection, contributing '
                          'conditions, recovery, and at least three follow-up improvements.',
                          'Classify each improvement as observability, automation, documentation, '
                          'resilience, testing, or process, then rank it by value and effort.']},
 'quiz': [{'question': 'Which definition best describes reliability?',
           'choices': ['A system never experiences any failure',
                       'Every container remains green at all times',
                       'The system delivers an acceptable user outcome, detects degradation, recovers, and '
                       'learns from failure',
                       'The application has the largest possible server'],
           'correct': 2},
          {'question': 'Ascend backend is running, but quiz submissions fail. What is the strongest '
                       'conclusion?',
           'choices': ['The service is fully reliable because the container is running',
                       'Component health does not prove the end-to-end user outcome works',
                       'The frontend must be deleted',
                       'Docker restart policies are unnecessary'],
           'correct': 1},
          {'question': 'Which observability signal is best suited to showing error rate over the last 24 '
                       'hours?',
           'choices': ['A metric',
                       'A single source-code comment',
                       'A deployment password',
                       'A screenshot of the home page'],
           'correct': 0},
          {'question': 'What is the primary difference between liveness and readiness?',
           'choices': ['Liveness checks the database while readiness checks the frontend color',
                       'Liveness asks whether the process should remain running; readiness asks whether it '
                       'can accept useful work',
                       'They are identical terms',
                       'Readiness applies only to mobile apps'],
           'correct': 1},
          {'question': 'Why can excessive low-value alerts reduce reliability?',
           'choices': ['They make servers use no CPU',
                       'They create alert fatigue and responders may ignore meaningful signals',
                       'They automatically delete logs',
                       'They prevent Docker images from building'],
           'correct': 1},
          {'question': 'What is the most important reliability benefit of automation?',
           'choices': ['It always eliminates all human involvement',
                       'It makes every system free',
                       'It reduces process variation and creates repeatable evidence',
                       'It guarantees no deployment can fail'],
           'correct': 2},
          {'question': 'Which characteristic makes an automated operation safer to retry?',
           'choices': ['It is undocumented',
                       'It is idempotent',
                       'It uses maximum permissions',
                       'It changes several environments at once'],
           'correct': 1},
          {'question': 'When is recovery verified?',
           'choices': ['When the restart command returns successfully',
                       'When the original user workflow succeeds again and related behavior is checked',
                       'When CPU usage is zero',
                       'When the incident message is deleted'],
           'correct': 1},
          {'question': 'What is the goal of a blameless post-incident review?',
           'choices': ['Avoid all accountability',
                       'Identify one person to punish',
                       'Understand system conditions and create improvements that reduce future impact',
                       'Prove the system was already perfect'],
           'correct': 2},
          {'question': 'Which is the best example of a short feedback loop?',
           'choices': ['Discovering a syntax error three months after release',
                       'Running automated validation immediately after a small code change',
                       'Waiting for users to report every failure',
                       'Changing several services before checking results'],
           'correct': 1}],
 'reflection': 'Choose a real failure from Ascend, Forge, your home server, or a TruHearing workflow. Define '
               'the user outcome, the signals you had, the signals you wished you had, the recovery action, '
               'and how you verified success. Then propose one observability improvement, one automation '
               'improvement, and one process improvement. Explain which one you would implement first and '
               'why.'}
