"""Module 2, Lesson 6: Services, Logs & Evidence-Driven Troubleshooting."""

LESSON = {'id': '2-6',
 'title': 'Services, Logs & Evidence-Driven Troubleshooting',
 'summary': 'Manage and diagnose Linux services with systemd, systemctl, journalctl, log files, and a '
            'repeatable incident workflow. Move from symptom to cause, smallest safe change, and '
            'verification.',
 'duration_minutes': 75,
 'xp': 80,
 'audio_script': 'Welcome to Lesson 2.6: Services, Logs, and Evidence-Driven Troubleshooting.\n'
                 '\n'
                 'This is where the first half of Module 2 comes together.\n'
                 '\n'
                 'You know how to orient yourself on a system. You can navigate paths, inspect text, '
                 'understand permissions, and investigate processes and resources.\n'
                 '\n'
                 'Now imagine the incident message.\n'
                 '\n'
                 'Ascend is down.\n'
                 '\n'
                 'You SSH into the server.\n'
                 '\n'
                 'What happens next?\n'
                 '\n'
                 'A beginner may immediately restart the application.\n'
                 '\n'
                 'An engineer begins by preserving and gathering evidence.\n'
                 '\n'
                 'First, understand services.\n'
                 '\n'
                 'A service is long-running functionality managed by the operating system. Examples include '
                 'SSH, a web server, a database, Docker, or an application backend.\n'
                 '\n'
                 'On many modern Linux distributions, systemd is the init and service-management system.\n'
                 '\n'
                 'systemd manages units.\n'
                 '\n'
                 'A service unit commonly ends in dot service, but systemd also has socket, timer, mount, '
                 'target, path, and other unit types.\n'
                 '\n'
                 'For this lesson, service units are our focus.\n'
                 '\n'
                 'systemctl is the command-line interface you will commonly use to interact with systemd.\n'
                 '\n'
                 'systemctl status nginx shows status information for the nginx service.\n'
                 '\n'
                 'The output may include whether the service is loaded, whether it is active, its main PID, '
                 'recent log lines, and failure information.\n'
                 '\n'
                 'Learn to distinguish states.\n'
                 '\n'
                 'Active running means systemd considers the service running.\n'
                 '\n'
                 'Inactive means it is not currently running.\n'
                 '\n'
                 'Failed means an operation failed and systemd recorded the unit in a failed state.\n'
                 '\n'
                 'Activating or deactivating means a transition is in progress.\n'
                 '\n'
                 "A service can also be active and still unhealthy from the user's perspective. A process "
                 'may be running while returning errors, waiting on a broken dependency, or serving the '
                 'wrong configuration.\n'
                 '\n'
                 'That is why status is evidence, not final proof.\n'
                 '\n'
                 'systemctl start starts a service.\n'
                 '\n'
                 'stop stops it.\n'
                 '\n'
                 'restart stops and starts it.\n'
                 '\n'
                 'reload asks a service to reload configuration when the service supports that behavior.\n'
                 '\n'
                 'enable configures a service to start automatically according to its unit relationships, '
                 'commonly at boot.\n'
                 '\n'
                 'Disable removes that automatic-start configuration.\n'
                 '\n'
                 'A crucial distinction: enable does not necessarily start a service right now, and start '
                 'does not necessarily enable it for future boots.\n'
                 '\n'
                 'Now the operational warning.\n'
                 '\n'
                 'Restart is a change.\n'
                 '\n'
                 'A restart may temporarily restore service, but it can also erase useful transient '
                 'evidence, interrupt users, trigger a failure loop, or make the root cause harder to '
                 'reproduce.\n'
                 '\n'
                 'Sometimes restarting is absolutely the correct action. But you should know why you are '
                 'doing it and what evidence you gathered first.\n'
                 '\n'
                 'So if status says failed, inspect logs.\n'
                 '\n'
                 'systemd includes a journal for structured system and service logs.\n'
                 '\n'
                 'journalctl queries that journal.\n'
                 '\n'
                 'journalctl dash u nginx filters to a unit.\n'
                 '\n'
                 'journalctl dash u nginx dash n fifty asks for a recent subset.\n'
                 '\n'
                 'journalctl dash u nginx dash f follows new entries.\n'
                 '\n'
                 'journalctl dash u nginx dash since quote ten minutes ago quote constrains the time '
                 'window.\n'
                 '\n'
                 'Time windows are incredibly useful during incidents.\n'
                 '\n'
                 'If the outage began at ten fifteen, evidence from six hours earlier may be noise. Align '
                 'logs with the event timeline.\n'
                 '\n'
                 'You can also combine journalctl with grep, using the shell skills from Lesson 2.3, but '
                 "first learn the journal's own filtering options. Native filters often preserve context "
                 'better than piping everything through text filters.\n'
                 '\n'
                 'Not every application logs only to the systemd journal.\n'
                 '\n'
                 'Traditional log files commonly live under slash var slash log, and applications may have '
                 'their own paths.\n'
                 '\n'
                 'A reverse proxy might log requests and errors to files.\n'
                 '\n'
                 'A containerized application may write logs to standard output and standard error so the '
                 'container runtime can collect them.\n'
                 '\n'
                 'A cloud platform may forward logs into a centralized service.\n'
                 '\n'
                 'The location changes. The principle does not.\n'
                 '\n'
                 'Find the evidence source associated with the failing component.\n'
                 '\n'
                 "Now let's construct a troubleshooting workflow.\n"
                 '\n'
                 'Step one: define the symptom.\n'
                 '\n'
                 'Do not begin with, quote, nginx is broken, end quote, unless you have evidence.\n'
                 '\n'
                 'Begin with what users observe.\n'
                 '\n'
                 'For example: requests to the Ascend site return HTTP 502 starting at ten fifteen.\n'
                 '\n'
                 'Step two: establish scope and context.\n'
                 '\n'
                 'Which environment? Which host? Which service? All users or some? One endpoint or the whole '
                 'application? What changed?\n'
                 '\n'
                 'Step three: inspect current state.\n'
                 '\n'
                 'systemctl status for the relevant service.\n'
                 '\n'
                 'Process evidence.\n'
                 '\n'
                 'Resource evidence.\n'
                 '\n'
                 'Network evidence later in the curriculum.\n'
                 '\n'
                 'Step four: inspect logs aligned with the incident window.\n'
                 '\n'
                 'Look for the first meaningful error, not merely the loudest repeated symptom.\n'
                 '\n'
                 'Step five: form a hypothesis.\n'
                 '\n'
                 'Perhaps the backend cannot read its environment file.\n'
                 '\n'
                 'Perhaps the port is already in use.\n'
                 '\n'
                 'Perhaps the disk is full.\n'
                 '\n'
                 'Perhaps a deployment introduced invalid configuration.\n'
                 '\n'
                 'Step six: test the hypothesis with the least invasive evidence available.\n'
                 '\n'
                 'Inspect permissions.\n'
                 '\n'
                 'Check the file.\n'
                 '\n'
                 'Check disk.\n'
                 '\n'
                 'Validate configuration.\n'
                 '\n'
                 'Compare the deployment.\n'
                 '\n'
                 'Step seven: choose the smallest safe action that addresses the supported cause.\n'
                 '\n'
                 'Correct one ownership error.\n'
                 '\n'
                 'Restore one configuration value.\n'
                 '\n'
                 'Free appropriate disk space.\n'
                 '\n'
                 'Roll back a bad deployment.\n'
                 '\n'
                 'Restart or reload only the affected service if that is required.\n'
                 '\n'
                 'Step eight: verify at multiple layers.\n'
                 '\n'
                 'systemctl status may say active.\n'
                 '\n'
                 'That is not enough.\n'
                 '\n'
                 'Check logs for fresh errors.\n'
                 '\n'
                 'Test the application endpoint.\n'
                 '\n'
                 'Confirm users can perform the action that failed.\n'
                 '\n'
                 'Watch briefly for recurrence.\n'
                 '\n'
                 'Step nine: preserve what you learned.\n'
                 '\n'
                 'Record timeline, cause, change, verification, and follow-up.\n'
                 '\n'
                 'That turns an incident into organizational knowledge.\n'
                 '\n'
                 'This is the same Evidence Before Action principle from Module 0, now expressed as an '
                 'operational Linux workflow.\n'
                 '\n'
                 "Let's examine common service failures.\n"
                 '\n'
                 'Permission denied.\n'
                 '\n'
                 'You now know to identify the service user and inspect ownership plus path permissions.\n'
                 '\n'
                 'No space left on device.\n'
                 '\n'
                 'You now know to inspect df and then locate consumption carefully.\n'
                 '\n'
                 'Address already in use.\n'
                 '\n'
                 'Another process may already own the port. Networking tools come later, but the process '
                 'conflict is part of your hypothesis.\n'
                 '\n'
                 'Configuration syntax error.\n'
                 '\n'
                 "The service's own validation command, documentation, or logs may identify the exact file "
                 'and line.\n'
                 '\n'
                 'Executable not found.\n'
                 '\n'
                 'PATH, unit configuration, package state, or deployment contents may be involved.\n'
                 '\n'
                 'Environment variable missing.\n'
                 '\n'
                 "The service manager's environment may differ from your interactive shell. A command "
                 'working manually does not prove the service receives the same environment.\n'
                 '\n'
                 'Dependency unavailable.\n'
                 '\n'
                 'The application process may be healthy while a database, DNS target, API, or other '
                 'dependency is not.\n'
                 '\n'
                 'This is why troubleshooting requires systems thinking.\n'
                 '\n'
                 'Now consider unit files.\n'
                 '\n'
                 'systemctl cat service-name can display the unit definition and drop-in configuration on '
                 'many systems.\n'
                 '\n'
                 'systemctl show exposes detailed properties.\n'
                 '\n'
                 'systemctl list-units can list loaded units.\n'
                 '\n'
                 'systemctl list-unit-files describes installed unit files and enablement states.\n'
                 '\n'
                 'You do not need to memorize every systemctl command. Start with status, logs, and the '
                 'specific question you need to answer.\n'
                 '\n'
                 'There is also daemon-reload.\n'
                 '\n'
                 'When systemd unit files or drop-ins change, systemctl daemon-reload tells the systemd '
                 'manager to reload unit definitions.\n'
                 '\n'
                 'Do not confuse daemon-reload with restarting the application service. One reloads '
                 "systemd's configuration view; the other changes the running service.\n"
                 '\n'
                 'Again, precise language matters.\n'
                 '\n'
                 'What if a service repeatedly restarts?\n'
                 '\n'
                 'Do not simply keep restarting it.\n'
                 '\n'
                 "Inspect the unit's restart policy and logs. A restart loop can flood logs, consume "
                 'resources, and hide the original first failure among repeated attempts.\n'
                 '\n'
                 'Find the earliest relevant error in the incident window.\n'
                 '\n'
                 "Now let's discuss log quality.\n"
                 '\n'
                 'An ERROR line is not automatically the root cause.\n'
                 '\n'
                 'One failure can create hundreds of downstream errors.\n'
                 '\n'
                 'For example, a database connection failure might cause API requests to fail, health checks '
                 'to fail, a reverse proxy to report upstream errors, and monitoring to fire alerts.\n'
                 '\n'
                 'The root cause may be the earliest database authentication or network failure, not the '
                 'final HTTP error users see.\n'
                 '\n'
                 'Build a timeline.\n'
                 '\n'
                 'Time is one of your strongest troubleshooting tools.\n'
                 '\n'
                 'For the lab, you will practice this workflow without intentionally breaking a production '
                 'service.\n'
                 '\n'
                 'If you have a Linux environment with systemd, inspect a harmless existing service such as '
                 'SSH or another service you recognize. Do not stop, restart, disable, or modify it.\n'
                 '\n'
                 'If your current environment does not run systemd, use the supplied scenario and command '
                 'reasoning portion. Containers often do not run systemd as PID one, and macOS uses launchd '
                 'rather than systemd. That difference itself is useful evidence about your environment.\n'
                 '\n'
                 'The goal is to learn the workflow, not force systemctl to work where systemd is absent.\n'
                 '\n'
                 'Here is the takeaway.\n'
                 '\n'
                 'systemd manages units.\n'
                 '\n'
                 'systemctl lets you inspect and control them.\n'
                 '\n'
                 "journalctl queries systemd's journal.\n"
                 '\n'
                 'Status is evidence, not proof of user-facing health.\n'
                 '\n'
                 'Restart is a change, not a diagnostic reflex.\n'
                 '\n'
                 'Logs need timeline and context.\n'
                 '\n'
                 'A good incident flow is symptom, context, state, logs, hypothesis, test, smallest safe '
                 'change, verification, and documentation.\n'
                 '\n'
                 'By the end of this lesson, you have the core pieces needed to walk into a Linux service '
                 'incident and investigate it methodically.\n'
                 '\n'
                 'Next, we will learn SSH and remote administration, which is how you often reach these '
                 'Linux systems in the first place.\n'
                 '\n'
                 'Keep climbing.',
 'objectives': ['Explain systemd units and the roles of systemctl and journalctl.',
                'Distinguish service state, enablement, and user-facing application health.',
                'Use status and time-bounded logs as evidence before restarting a service.',
                'Apply a repeatable troubleshooting workflow from symptom through hypothesis, smallest safe '
                'change, and verification.',
                'Recognize common service failure patterns involving permissions, storage, configuration, '
                'environment, processes, and dependencies.'],
 'content': [{'heading': 'systemd manages units',
              'body': 'On many Linux distributions, systemd is the init/service manager. Service units '
                      'commonly end in .service, while other unit types include sockets, timers, mounts, '
                      'paths, and targets.'},
             {'heading': 'systemctl status is an investigation starting point',
              'body': 'Status can show loaded state, active/failed state, the main PID, and recent messages. '
                      'It tells you what systemd currently knows; it does not prove the application is '
                      'healthy for users.'},
             {'heading': 'Start, stop, restart, reload, enable, and disable are different actions',
              'body': 'start changes current runtime state. enable configures automatic activation '
                      'relationships for future starts/boots. restart interrupts and starts again. reload '
                      'asks supported software to reread configuration. Use the action that matches the '
                      'intent.'},
             {'heading': 'A restart is a change',
              'body': 'Restarting may restore availability, but it can destroy transient evidence, interrupt '
                      'work, or hide the cause. Gather enough evidence to justify the action whenever '
                      'circumstances allow.'},
             {'heading': 'journalctl turns service history into a timeline',
              'body': 'journalctl -u SERVICE focuses on one unit. Options such as -n, -f, and --since help '
                      'narrow evidence to recent or live events. Align log windows with the reported '
                      'incident time.'},
             {'heading': 'Logs can live in multiple places',
              'body': 'Traditional files often live under /var/log, applications may choose custom paths, '
                      'containers commonly emit stdout/stderr, and platforms may centralize logs. Find the '
                      'evidence source for the component you are investigating.'},
             {'heading': 'The first error can matter more than the loudest error',
              'body': 'One root failure can create many downstream messages. Build a timeline and look for '
                      'the earliest meaningful event around the incident rather than assuming the most '
                      'repeated ERROR line is the cause.'},
             {'heading': 'Service environment can differ from your shell',
              'body': 'A command working interactively does not prove a service receives the same PATH, '
                      "working directory, user, environment variables, or permissions. Inspect the service's "
                      'actual execution context.'},
             {'heading': 'Verification must cross layers',
              'body': 'After a fix, check service state, fresh logs, and the user-facing application '
                      'behavior. An active process that still returns 500 errors is not a recovered '
                      'service.'},
             {'heading': 'Document the incident after recovery',
              'body': 'Record symptom, timeline, evidence, root cause, action, verification, and follow-up. '
                      'Good incident notes turn troubleshooting into reusable engineering knowledge.'}],
 'diagram': {'title': 'Evidence-driven Linux incident loop',
             'description': 'Use a repeatable sequence so pressure does not turn into random changes.',
             'nodes': [{'label': 'Symptom', 'detail': 'State what users or monitoring actually observe.'},
                       {'label': 'Context & state',
                        'detail': 'Confirm host, environment, service, process, and resource state.'},
                       {'label': 'Logs & timeline',
                        'detail': 'Inspect evidence around when the symptom began.'},
                       {'label': 'Hypothesis', 'detail': 'Propose a cause that explains the evidence.'},
                       {'label': 'Smallest safe change',
                        'detail': 'Address the supported cause with minimal blast radius.'},
                       {'label': 'Verify & record',
                        'detail': 'Test service state, logs, user behavior, and document what happened.'}],
             'caption': 'Restart can be one action inside this loop, but it is not a substitute for the '
                        'loop.'},
 'engineer_perspective': {'title': 'Active is not the same as healthy',
                          'body': 'systemctl can report a process as active while users still receive '
                                  'failures. Operations requires verification at the service-manager, '
                                  'application, dependency, and user-facing layers. Recovery is a '
                                  'demonstrated outcome, not a green word in one command.'},
 'try_it_yourself': {'title': 'Read a service incident before touching it',
                     'intro': 'If you have systemd, inspect a harmless known service read-only. Otherwise '
                              'use the scenario steps conceptually.',
                     'steps': ['Run systemctl status SERVICE for a service you recognize. Do not stop or '
                               'restart it.',
                               'Identify loaded state, active state, and main PID if present.',
                               'Run journalctl -u SERVICE -n 20 --no-pager and identify the newest '
                               'timestamp.',
                               'If permitted, run systemctl cat SERVICE and identify the ExecStart command '
                               'or equivalent.',
                               'Write one statement that status proves and one thing it does not prove.',
                               'Write what you would verify at the application layer before declaring '
                               'recovery.'],
                     'takeaway': 'Service-manager state is one evidence source. Combine it with logs and '
                                 'user-facing verification.'},
 'lab': {'title': 'Work the incident: Ascend API unavailable',
         'instructions': ['Create a Journal entry titled “Lesson 2.6 — Service Incident.”',
                          'Scenario: At 10:15 users begin receiving HTTP 502 from Ascend. The reverse proxy '
                          'is reachable, but the backend appears unavailable. Write only the confirmed '
                          'symptom; do not name a root cause yet.',
                          'List the first five pieces of context you would establish after connecting to the '
                          'host.',
                          'Write the systemctl status command you would use for a hypothetical '
                          'ascend-api.service and list the fields you would inspect.',
                          'Write a journalctl command that requests ascend-api.service logs beginning around '
                          '10:10. Explain why the time boundary matters.',
                          'Evidence arrives: the service log says it cannot open /etc/ascend/app.env because '
                          'permission is denied. Use Lesson 2.4 to list the identity, ownership, and '
                          'path-permission evidence you would gather before changing anything.',
                          'Additional evidence shows the service runs as user ascend and app.env was '
                          'accidentally changed to root:root mode 600 during a deployment. Form a root-cause '
                          'hypothesis and propose the smallest safe ownership/permission correction based on '
                          "the application's intended design. Do not choose chmod 777.",
                          'Describe whether a restart or reload would be required after correcting file '
                          'access and what evidence would determine that choice.',
                          'Write a verification plan covering systemctl state, new journal entries, '
                          'direct/backend health if available, and the user-facing Ascend request.',
                          'Finish an incident note with: symptom, start time, evidence, root cause, change, '
                          'verification, and one prevention idea for the deployment process.']},
 'quiz': [{'question': 'What is systemd?',
           'choices': ['A common Linux init and service-management system',
                       'A text editor',
                       'A Git branch type',
                       'A file permission'],
           'correct': 0},
          {'question': 'What does systemctl status primarily provide?',
           'choices': ['Current service/unit state and related evidence',
                       'A guarantee of user-facing health',
                       'Automatic root-cause repair',
                       'Only disk usage'],
           'correct': 0},
          {'question': 'What is the difference between systemctl start and enable?',
           'choices': ['start changes current runtime state; enable configures automatic activation for '
                       'future boots/targets',
                       'They are always identical',
                       'enable immediately kills the service',
                       'start changes file permissions'],
           'correct': 0},
          {'question': 'Why should restart not be the automatic first troubleshooting action?',
           'choices': ['It is a change that may destroy evidence or hide the cause',
                       'Linux services cannot restart',
                       'Restart never restores availability',
                       'Only developers may restart services'],
           'correct': 0},
          {'question': 'What does journalctl -u ascend-api.service do?',
           'choices': ['Queries journal entries associated with that unit',
                       'Changes the service owner',
                       'Deletes application logs',
                       'Enables the service'],
           'correct': 0},
          {'question': 'Why use --since or another time filter during an incident?',
           'choices': ['To align evidence with the incident timeline and reduce unrelated noise',
                       'To change the system clock',
                       'To grant log permissions',
                       'To restart only recent processes'],
           'correct': 0},
          {'question': 'A service is active but users receive HTTP 500. What should you conclude?',
           'choices': ['Process state alone does not prove application health',
                       'The incident is automatically resolved',
                       'The logs can be deleted',
                       'systemd must be broken'],
           'correct': 0},
          {'question': 'Which sequence best reflects Evidence Before Action?',
           'choices': ['Symptom → state/logs → hypothesis → smallest safe change → verify',
                       'Restart → guess → delete logs',
                       'sudo → chmod 777 → reboot',
                       'Kill process → investigate later'],
           'correct': 0},
          {'question': 'Why can the earliest meaningful log error be valuable?',
           'choices': ['A root failure can generate many later downstream errors',
                       'Only the first log line is ever correct',
                       'Later logs are always corrupted',
                       'systemd sorts by severity only'],
           'correct': 0},
          {'question': 'What should happen after a service fix?',
           'choices': ['Verify service state, fresh logs, and user-facing behavior',
                       'Assume success if the command returned',
                       'Immediately delete the incident notes',
                       'Disable monitoring'],
           'correct': 0}],
 'reflection': 'Describe the difference between restoring availability and understanding root cause. During '
               'a real incident, how would you balance the urgency to recover service with the need to '
               'preserve enough evidence to prevent recurrence?'}
