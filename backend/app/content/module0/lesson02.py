"""Module 0, Lesson 2: Evidence Before Action."""

LESSON = {'id': '0-2',
 'title': 'Evidence Before Action',
 'summary': 'Turn vague symptoms into reliable evidence, protect what the system can teach you, and choose '
            'the smallest safe action that meaningfully reduces uncertainty.',
 'duration_minutes': 60,
 'xp': 60,
 'audio_script': 'Welcome back to Ascend. This is Lesson 0.2: Evidence Before Action.\n'
                 '\n'
                 'In the previous lesson, you learned that engineers begin with better questions. In this '
                 'lesson, we take the next step. We learn how to gather answers without destroying the '
                 'evidence that could lead us to the truth.\n'
                 '\n'
                 'Picture this. You open Forge on your iPhone before work. The dashboard loads, but your '
                 'workout data does not appear. You tap refresh. Nothing changes. You try again. Still '
                 'nothing.\n'
                 '\n'
                 'There is an immediate temptation to do something dramatic. Restart Docker. Reboot the home '
                 'server. Rebuild the iPhone app. Change the backend address. Maybe do all four.\n'
                 '\n'
                 'That temptation is understandable. Action feels like progress. But in engineering, the '
                 'fastest-looking action is not always the fastest path to understanding.\n'
                 '\n'
                 'Before changing anything, pause and describe exactly what happened.\n'
                 '\n'
                 'The Forge application opened. The dashboard shell rendered. Some information may have '
                 'appeared. Workout data did not load. No conclusion has been earned yet.\n'
                 '\n'
                 'That description is already more useful than saying, “Forge is broken.” It tells us that '
                 'the phone can launch the app and that at least part of the frontend is functioning. The '
                 'problem may exist in a specific request path rather than the entire system.\n'
                 '\n'
                 'This is the principle of evidence before action. Preserve the system long enough to learn '
                 'from it. Observe what is true. Record what happened. Then choose an action because the '
                 'evidence justifies it, not because the action is familiar.\n'
                 '\n'
                 'Let us separate four ideas that often get mixed together: symptom, observation, '
                 'interpretation, and conclusion.\n'
                 '\n'
                 'A symptom is the user-visible problem. “My workouts will not load.”\n'
                 '\n'
                 'An observation is something directly verified. “The frontend requested slash API slash '
                 'workouts and received HTTP five hundred at 8:12 A.M.”\n'
                 '\n'
                 'An interpretation is a possible explanation. “The backend may have failed while reading '
                 'from the database.”\n'
                 '\n'
                 'A conclusion is the explanation supported by enough evidence to act with confidence. “The '
                 'backend crashed during startup because content dot py no longer defined ACHIEVEMENTS.”\n'
                 '\n'
                 'Notice how confidence increases one step at a time. Engineers do not skip from symptom to '
                 'conclusion.\n'
                 '\n'
                 'You experienced this recently with Ascend. Docker Desktop showed the backend container '
                 'restarting. It would have been easy to say Docker was malfunctioning. Instead, you opened '
                 'the container logs. The traceback showed that main dot py attempted to import ACHIEVEMENTS '
                 'from content dot py, but that name no longer existed. The restart loop was the symptom. '
                 'The Python import error was the direct cause of the startup failure.\n'
                 '\n'
                 'That incident is a perfect example of evidence changing the direction of the '
                 'investigation. Reinstalling Docker would not have repaired a missing Python variable. '
                 'Rebooting the Mac would not have repaired it either. One log message was worth more than '
                 'ten random restarts.\n'
                 '\n'
                 'Evidence has another important quality: it should be reproducible whenever possible.\n'
                 '\n'
                 'If a problem occurs once and disappears, write down the time, device, network, version, '
                 'and action. If it happens again, repeat the same workflow. A reproducible failure gives '
                 'you a stable target. A stable target allows controlled tests.\n'
                 '\n'
                 'Suppose Forge works on the home server but fails on your iPhone. That comparison matters. '
                 'Suppose it works on Wi-Fi but fails through Tailscale. That comparison matters. Suppose '
                 'the page loads but saving a workout fails. That comparison matters.\n'
                 '\n'
                 'Working cases are evidence too. Every successful boundary eliminates possibilities.\n'
                 '\n'
                 'This leads to the evidence ladder. Begin with evidence that is close to the user, '
                 'inexpensive to collect, and unlikely to alter the system.\n'
                 '\n'
                 'First, reproduce the exact workflow.\n'
                 '\n'
                 'Second, record the visible message and timestamp.\n'
                 '\n'
                 'Third, compare a working case with a failing case.\n'
                 '\n'
                 'Fourth, inspect the browser console and network activity.\n'
                 '\n'
                 'Fifth, check service and container state.\n'
                 '\n'
                 'Sixth, read application logs around the same timestamp.\n'
                 '\n'
                 'Seventh, inspect dependencies such as the database, authentication provider, or external '
                 'API.\n'
                 '\n'
                 'Only after those steps should you consider broader changes such as restarting, rebuilding, '
                 'or redeploying, unless service restoration is urgently required.\n'
                 '\n'
                 'The order is not rigid. It is a way of thinking. Move from low-risk observation toward '
                 'higher-impact action.\n'
                 '\n'
                 'Now consider the stale Tailscale address that once appeared in Forge. Your current source '
                 'code on the Mac did not contain the old address, but the browser console showed requests '
                 'going to it. The running application was telling you something the source tree could not: '
                 'the deployed build did not match your expectation.\n'
                 '\n'
                 'That is a powerful lesson. Engineers troubleshoot the system that is actually running, not '
                 'the system they believe should be running.\n'
                 '\n'
                 'A file on your laptop is not proof of what exists inside a Docker image. A successful '
                 'build is not proof that the right image is running on the home server. A green container '
                 'is not proof that the user workflow succeeds. Evidence must come from the relevant layer.\n'
                 '\n'
                 'This is also why timestamps are so valuable. Imagine that a user reports a failure at 2:14 '
                 'P.M. The backend log contains thousands of entries. Without a time window, the search is '
                 'noisy. With the timestamp, you can correlate the browser request, reverse proxy entry, '
                 'backend exception, and database event.\n'
                 '\n'
                 'Correlation means connecting evidence from different layers into one story.\n'
                 '\n'
                 'At 2:14:03, the browser sends POST slash workouts.\n'
                 '\n'
                 'At 2:14:03, the proxy forwards the request to the backend.\n'
                 '\n'
                 'At 2:14:04, FastAPI logs a database connection error.\n'
                 '\n'
                 'At 2:14:04, the browser receives HTTP five hundred.\n'
                 '\n'
                 'Now the failure path is visible.\n'
                 '\n'
                 'Good evidence also helps you form better hypotheses. A hypothesis should explain the '
                 'observations and predict what else you would expect to find.\n'
                 '\n'
                 'Hypothesis one: the backend container is not running.\n'
                 '\n'
                 'Prediction: direct requests to the backend health endpoint will fail, and Docker will show '
                 'the container stopped or restarting.\n'
                 '\n'
                 'Hypothesis two: the frontend contains an outdated API address.\n'
                 '\n'
                 'Prediction: the browser network panel will show requests going to the old address while '
                 'the backend remains healthy at the current address.\n'
                 '\n'
                 'Hypothesis three: the database is unavailable.\n'
                 '\n'
                 'Prediction: the backend will receive the request, but logs will show connection failures '
                 'when it tries to read or write data.\n'
                 '\n'
                 'Each hypothesis points to a different test. That is what makes it useful.\n'
                 '\n'
                 'A weak hypothesis says, “Something is wrong with Docker.” It is too broad and predicts '
                 'almost nothing. A strong hypothesis says, “The backend exits during startup because a '
                 'required object cannot be imported.” That predicts a traceback during application import '
                 'and a restarting container.\n'
                 '\n'
                 'You should also ask what evidence would prove your favorite idea wrong. This protects you '
                 'from confirmation bias.\n'
                 '\n'
                 'If you believe Tailscale is responsible, test the backend directly through the Tailscale '
                 'address. If that succeeds, the network path may be working and the problem may exist '
                 'higher in the application. If you believe the database is down, check whether another '
                 'database-backed endpoint succeeds. One successful query weakens the broad claim that the '
                 'database is completely unavailable.\n'
                 '\n'
                 'The next principle is controlled change.\n'
                 '\n'
                 'A controlled change is small, reversible, and connected to a prediction. You record the '
                 'state before the change, make one meaningful adjustment, and compare the result '
                 'afterward.\n'
                 '\n'
                 'For example, replacing the missing ACHIEVEMENTS definition is a controlled change. It '
                 'addresses the exact import error. Rebuilding only the backend limits the scope. Reading '
                 'the logs afterward verifies the result.\n'
                 '\n'
                 'By contrast, deleting every container, image, network, and volume would be uncontrolled '
                 'and dangerous. It could erase data and introduce additional failures without addressing '
                 'the original cause.\n'
                 '\n'
                 'There are moments when you must prioritize restoration over diagnosis. If an important '
                 'service is unavailable, restarting a failed process may be the right decision. Evidence '
                 'before action does not mean refusing to restore service. It means capturing what you '
                 'reasonably can first and being honest about what the recovery action did and did not '
                 'prove.\n'
                 '\n'
                 'For example: “Restarting the backend restored service. The original cause is still '
                 'unknown. Logs were preserved for follow-up.”\n'
                 '\n'
                 'That is a professional statement. It separates recovery from root-cause analysis.\n'
                 '\n'
                 'At TruHearing, the same discipline applies even when the system is Microsoft 365 rather '
                 'than Docker. “OneDrive is broken” is not enough. Which user? Which device? Which client '
                 'version? Is the user signed in? Is the issue limited to one library? Is Microsoft '
                 'reporting a service incident? What error code appears? What do sync logs show?\n'
                 '\n'
                 'A strong escalation includes evidence another engineer can use. It should contain impact, '
                 'exact reproduction steps, timestamps, error messages, device and software details, tests '
                 'already performed, results, and remaining uncertainty.\n'
                 '\n'
                 'That is far more useful than a list of random fixes.\n'
                 '\n'
                 'Evidence also improves communication during an incident. Use three categories.\n'
                 '\n'
                 'Confirmed: what you directly know.\n'
                 '\n'
                 'Suspected: what the current evidence suggests.\n'
                 '\n'
                 'Next: what you will test or change next.\n'
                 '\n'
                 'For example: “Confirmed: the Ascend frontend loads, but the backend container restarts '
                 'before accepting requests. Suspected: application startup is failing during a Python '
                 'import. Next: inspect the first traceback and verify the imported names in content dot '
                 'py.”\n'
                 '\n'
                 'That update is calm, precise, and useful.\n'
                 '\n'
                 'Finally, always verify from the user’s perspective. The backend staying up is good '
                 'evidence, but it is not the finish line. Open Ascend. Load the dashboard. Switch '
                 'workspaces. Open Lesson 0.2. Submit a quiz. Repeat the workflow that was broken.\n'
                 '\n'
                 'A component can be healthy while the product remains unusable.\n'
                 '\n'
                 'Here is the complete loop for this lesson.\n'
                 '\n'
                 'Observe the actual behavior.\n'
                 '\n'
                 'Preserve evidence.\n'
                 '\n'
                 'Define the scope.\n'
                 '\n'
                 'Compare working and failing cases.\n'
                 '\n'
                 'Build multiple hypotheses.\n'
                 '\n'
                 'Choose the safest high-value test.\n'
                 '\n'
                 'Make one controlled change.\n'
                 '\n'
                 'Verify the original user workflow.\n'
                 '\n'
                 'Document what was learned.\n'
                 '\n'
                 'Your takeaway is simple: before you ask, “What should I change?” ask, “What evidence would '
                 'help me understand this system?”\n'
                 '\n'
                 'In the next lesson, we will follow that evidence through the conversations computers use '
                 'to communicate. You will trace a request from your iPhone, through DNS, IP addresses, '
                 'ports, Tailscale, Docker, FastAPI, and PostgreSQL, and then back to the screen. The '
                 'internet will stop feeling like magic. It will become a path you can inspect.',
 'content': [{'heading': 'Learning objectives',
              'body': 'By the end of this lesson, you should be able to distinguish symptoms, observations, '
                      'interpretations, and conclusions; preserve useful evidence before changing a system; '
                      'compare working and failing cases; form hypotheses that predict evidence; choose '
                      'controlled low-risk tests; communicate confidence honestly; and verify the complete '
                      'user workflow after a repair.'},
             {'heading': 'Why evidence comes before action',
              'body': 'A fast change can restore service, but it can also erase logs, hide a temporary '
                      'condition, or introduce a second problem. Evidence before action means preserving the '
                      'system long enough to learn from it and selecting actions because they reduce '
                      'uncertainty. It does not prohibit urgent recovery; it separates restoration from '
                      'diagnosis.'},
             {'heading': 'Symptom, observation, interpretation, conclusion',
              'body': 'A symptom is the user-visible problem. An observation is directly verified. An '
                      'interpretation is a possible explanation. A conclusion is an explanation supported by '
                      'enough evidence to guide action. “Ascend is unavailable” is a symptom. “The backend '
                      'container restarts and logs an ImportError for ACHIEVEMENTS” is an observation. '
                      '“content.py no longer defines a required constant” is an interpretation that can be '
                      'verified by inspecting the file.'},
             {'heading': 'Preserve the scene',
              'body': 'Record the time, exact workflow, device, network, application version, visible error, '
                      'and affected scope before restarting or redeploying. Capture browser requests, '
                      'console messages, container state, and relevant logs. A short evidence snapshot may '
                      'be the only record of a transient failure.'},
             {'heading': 'Build an evidence ladder',
              'body': 'Move from low-risk evidence near the user toward deeper system evidence: reproduce '
                      'the workflow; compare working and failing cases; inspect the browser Network and '
                      'Console tools; check container state; correlate application logs by timestamp; '
                      'inspect database, authentication, and external dependencies. Each rung should narrow '
                      'the problem before the next action.'},
             {'heading': 'Working cases are evidence',
              'body': 'A successful boundary eliminates possibilities. If the Ascend page shell loads, '
                      'initial frontend delivery works. If the backend health endpoint responds through '
                      'Tailscale, basic routing and port reachability work. If one database-backed endpoint '
                      'succeeds, a complete database outage becomes less likely. Compare what works with '
                      'what fails.'},
             {'heading': 'Troubleshoot the running system',
              'body': 'Source code on a laptop does not prove what is inside the deployed image. A completed '
                      'build does not prove the correct image is running. A green container does not prove '
                      'the user workflow succeeds. The stale Forge Tailscale address demonstrated that the '
                      'browser’s actual request was stronger evidence than the source code we expected to be '
                      'deployed.'},
             {'heading': 'Form hypotheses that make predictions',
              'body': 'A useful hypothesis explains observations and predicts additional evidence. “The '
                      'backend exits during startup because a required name cannot be imported” predicts a '
                      'Python traceback before the server begins accepting requests. Write at least two '
                      'competing hypotheses and identify what would support or disprove each one.'},
             {'heading': 'Choose controlled tests',
              'body': 'Prefer the smallest reversible test that distinguishes between explanations. Record '
                      'the before state, perform one meaningful change, and measure the after state. '
                      'Replacing a missing constant and rebuilding only the backend is controlled. Deleting '
                      'all containers, images, and volumes is not.'},
             {'heading': 'Correlate evidence across layers',
              'body': 'Use timestamps and request identifiers to connect the browser, proxy, backend, and '
                      'database into one incident story. A browser request at 2:14:03, a FastAPI exception '
                      'at 2:14:04, and an HTTP 500 response at 2:14:04 are stronger together than any one '
                      'line alone.'},
             {'heading': 'Communicate confidence honestly',
              'body': 'Separate updates into Confirmed, Suspected, and Next. State impact and evidence '
                      'without presenting a hypothesis as fact. Example: “Confirmed: the frontend loads, but '
                      'workout saves return HTTP 500. Suspected: the backend is failing during the database '
                      'write. Next: correlate the request timestamp with backend and database logs.”'},
             {'heading': 'Real-world practice at TruHearing',
              'body': 'A useful escalation replaces “OneDrive is broken” with user, device, client version, '
                      'sign-in state, network, timestamp, exact error, service-health status, reproduction '
                      'steps, tests already completed, and results. The same evidence discipline improves '
                      'Microsoft 365 support, Graph API troubleshooting, and internal application '
                      'incidents.'},
             {'heading': 'Verify the user outcome',
              'body': 'A repaired component is not the same as a repaired product. Repeat the exact workflow '
                      'that failed, under the same conditions, and check nearby workflows for side effects. '
                      'For Ascend that may include loading the dashboard, switching workspaces, opening the '
                      'lesson, submitting a quiz, and confirming progress persists.'},
             {'heading': 'Takeaway and bridge',
              'body': 'Before asking what to change, ask what evidence would reduce uncertainty. Preserve, '
                      'observe, compare, predict, test, verify, and document. Next, you will trace where '
                      'that evidence appears as computers talk through names, addresses, ports, protocols, '
                      'applications, and dependencies.'}],
 'lab': {'title': 'Build an evidence-first incident record',
         'instructions': ['Choose a realistic failure in Forge, Ascend, the home server, or the TruHearing '
                          'directory application.',
                          'Write the original user report exactly as it might arrive, then rewrite it as a '
                          'reproducible workflow containing device, network, timestamp, expected result, and '
                          'actual result.',
                          'Create four labeled sections: Symptoms, Observations, Interpretations, and '
                          'Conclusions. Do not place an item in Conclusions until the evidence supports it.',
                          'Draw the request path involved in the failure. Include the user interface, '
                          'network boundary, application services, and dependencies.',
                          'List at least two working cases and two failing cases. Explain what each '
                          'comparison eliminates or makes less likely.',
                          'Create an evidence ladder with at least eight checks ordered from low risk and '
                          'high information value toward higher-impact actions.',
                          'Write three competing hypotheses. For each, include the prediction, supporting '
                          'evidence, disconfirming evidence, and safest first test.',
                          'Choose one controlled change. Record the before state, exact change, rollback '
                          'plan, expected result, and verification step.',
                          'Write an incident update using Confirmed, Suspected, and Next.',
                          'Finish with a user-perspective verification checklist and a short note describing '
                          'what should be documented or automated to make the next incident easier.']},
 'quiz': [{'question': 'Which statement is an observation rather than an interpretation?',
           'choices': ['Docker is broken',
                       'The backend container restarted seven times and logged ImportError: cannot import '
                       'name ACHIEVEMENTS',
                       'The database probably caused the outage',
                       'The latest deployment must be bad'],
           'correct': 1},
          {'question': 'Why can restarting a service too early weaken an investigation?',
           'choices': ['Restarts are never allowed',
                       'It may erase transient evidence or restore service without revealing the cause',
                       'It always damages the database',
                       'It prevents Docker from building images'],
           'correct': 1},
          {'question': 'Which sequence shows increasing confidence?',
           'choices': ['Conclusion, symptom, observation, guess',
                       'Symptom, observation, interpretation, supported conclusion',
                       'Observation, restart, assumption, deletion',
                       'Hypothesis, conclusion, symptom, evidence'],
           'correct': 1},
          {'question': 'Ascend loads its frontend but API calls fail. What is already partly verified?',
           'choices': ['The complete application',
                       'Initial frontend delivery to the client',
                       'Every backend dependency',
                       'The database write path'],
           'correct': 1},
          {'question': 'What makes a hypothesis useful during troubleshooting?',
           'choices': ['It names a complicated component',
                       'It predicts evidence that can support or contradict it',
                       'It recommends the fastest restart',
                       'It agrees with the first guess'],
           'correct': 1},
          {'question': 'Why was the stale Forge Tailscale address strong evidence?',
           'choices': ['It proved Tailscale never changes',
                       'It showed what the deployed browser was actually requesting',
                       'It proved the source code was wrong',
                       'It eliminated the need to inspect deployment state'],
           'correct': 1},
          {'question': 'Which action is the most controlled?',
           'choices': ['Delete all containers and volumes',
                       'Restart the host, router, and every service',
                       'Add the missing imported constant, rebuild only the backend, and verify logs',
                       'Reinstall Docker Desktop'],
           'correct': 2},
          {'question': 'What is the value of timestamps during an incident?',
           'choices': ['They make logs shorter',
                       'They help correlate evidence across browser, proxy, backend, and dependencies',
                       'They prove the first hypothesis',
                       'They replace reproduction steps'],
           'correct': 1},
          {'question': 'Which incident update uses appropriate confidence?',
           'choices': ['The database is down, although we have not checked it',
                       'Confirmed: the frontend loads and saves return 500; suspected: the backend write '
                       'path; next: correlate request and backend logs',
                       'Everything is broken; we are restarting everything',
                       'The issue is fixed because Docker is green'],
           'correct': 1},
          {'question': 'When is a repair fully verified?',
           'choices': ['When the changed file saves',
                       'When the container remains running',
                       'When the original user workflow succeeds under the failing conditions and nearby '
                       'workflows are checked',
                       'When the build command exits successfully'],
           'correct': 2}],
 'diagram': {'title': 'The evidence-first troubleshooting loop',
             'description': 'Use this loop to reduce uncertainty before making a risky change.',
             'nodes': [{'label': 'Observe',
                        'detail': 'Capture the exact symptom, timestamp, and affected workflow.'},
                       {'label': 'Scope',
                        'detail': 'Compare users, devices, networks, versions, and working cases.'},
                       {'label': 'Map', 'detail': 'Trace the request through each component and dependency.'},
                       {'label': 'Hypothesize',
                        'detail': 'Write competing explanations that predict evidence.'},
                       {'label': 'Test',
                        'detail': 'Choose the lowest-risk test with the highest information value.'},
                       {'label': 'Verify',
                        'detail': 'Repeat the original user workflow and check nearby behavior.'},
                       {'label': 'Document',
                        'detail': 'Record what happened, what fixed it, and what should improve.'}],
             'caption': 'The loop is intentionally evidence-driven. A restart may still be the right action, '
                        'but it should follow observation whenever time and impact allow.'},
 'engineer_perspective': {'title': 'A fix without understanding is only a temporary victory',
                          'body': 'A junior troubleshooter may ask, “What command makes this work again?” An '
                                  'experienced engineer also asks, “What evidence explains why it failed, '
                                  'and how will I know the repair addressed the real cause?” Restoring '
                                  'service matters. Preserving learning makes the next incident safer and '
                                  'faster.'},
 'try_it_yourself': {'title': 'Read the running system before changing it',
                     'intro': 'Use either Forge or Ascend while it is healthy so you can practice collecting '
                              'baseline evidence before a real incident.',
                     'steps': ['Open the application and complete one normal workflow, such as loading a '
                               'lesson or opening the Forge dashboard.',
                               'Open the browser Network panel and repeat the workflow.',
                               'Record the request URL, method, status code, response time, and response '
                               'type for one API call.',
                               'Run docker compose ps and note which containers support the workflow.',
                               'Write one observation and one possible interpretation, keeping them clearly '
                               'separate.'],
                     'takeaway': 'Healthy-system evidence becomes your comparison point later. '
                                 'Troubleshooting is much easier when you know what normal looks like.'},
 'reflection': 'Describe a real situation in which action came before evidence. Separate the symptom, '
               'observations, interpretations, and eventual conclusion. Identify the evidence that would '
               'have produced a safer first test, then rewrite the incident update using Confirmed, '
               'Suspected, and Next. Finally, explain how you would verify the repair from the user’s '
               'perspective.'}
