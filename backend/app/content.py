ACHIEVEMENTS = []

MODULES = [{'id': 'module-0',
  'number': 0,
  'title': 'DevOps Foundations and Systems Thinking',
  'subtitle': 'Build the mindset before learning the tools.',
  'status': 'active',
  'lessons': [{'id': '0-1',
               'title': 'How Engineers Think',
               'summary': 'Learn to reduce uncertainty, see connected systems, and form testable hypotheses '
                          'before making changes.',
               'duration_minutes': 50,
               'xp': 50,
               'audio_script': 'Welcome to The Journey, and welcome to Lesson 0.1: How Engineers Think.\n'
                               '\n'
                               'Imagine that it is the middle of a normal workday when a message arrives: '
                               '“Forge is down.” That sentence sounds useful, but it is not yet a diagnosis. '
                               'It may not even describe the problem accurately. The person could mean that '
                               'the page will not open, that login fails, that one button does nothing, that '
                               'data is loading slowly, or that the application works on Wi-Fi but not '
                               'through Tailscale.\n'
                               '\n'
                               'A common first reaction is to act. Restart the container. Reboot the server. '
                               'Clear the browser cache. Redeploy the application. Those actions feel '
                               'productive because they are visible. But activity is not the same as '
                               'progress. A change made before the problem is understood can hide evidence, '
                               'introduce a second problem, or make it impossible to learn what actually '
                               'happened.\n'
                               '\n'
                               'Experienced engineers do something that can look slower at first: they '
                               'pause. They ask what the report really means. They identify what is known, '
                               'what is unknown, and what assumptions are already forming in their minds. '
                               'Then they reduce uncertainty one question and one test at a time.\n'
                               '\n'
                               'That is the central idea of this lesson: engineers do not solve problems '
                               'because they know every answer. They solve problems because they know how to '
                               'ask better questions.\n'
                               '\n'
                               'You already use part of this mindset in IT support. When a user says '
                               'something is broken, you may ask when it last worked, whether anyone else is '
                               'affected, what they were doing, whether an error appeared, and whether the '
                               'behavior can be reproduced. Those are not merely help-desk questions. They '
                               'are engineering questions. DevOps expands the same reasoning into '
                               'applications, containers, networks, deployment pipelines, cloud '
                               'infrastructure, authentication systems, and databases.\n'
                               '\n'
                               'The tools will change. The thought process remains remarkably consistent.\n'
                               '\n'
                               'Let us begin with the difference between a symptom and a cause. “The page is '
                               'blank” is a symptom. “The frontend JavaScript crashed because it received an '
                               'unexpected response” is a possible cause. “The API returned a five-hundred '
                               'error because the database schema was missing a column” is a deeper cause. '
                               'Engineers avoid stopping at the first explanation that sounds believable. '
                               'They keep tracing the system until the evidence supports a useful '
                               'conclusion.\n'
                               '\n'
                               'Now consider Forge. To a user, Forge may appear to be one application. From '
                               'an engineering perspective, it is a system made of interacting parts. The '
                               'iPhone or browser must reach the host. The frontend must load. The frontend '
                               'must call the correct backend address. The backend container must be '
                               'running. FastAPI must process the request. PostgreSQL must be reachable. The '
                               'requested data must exist. Docker networking, host ports, firewall rules, '
                               'Tailscale routing, and environment variables can all influence the result.\n'
                               '\n'
                               'This is systems thinking: seeing behavior as the result of relationships '
                               'between components rather than treating each component as an isolated '
                               'object.\n'
                               '\n'
                               'Systems thinking does not mean memorizing every component before you begin. '
                               'It means building a useful map. When something fails, ask: what path did the '
                               'request take, and at what boundary did expected behavior stop?\n'
                               '\n'
                               'A practical request path might look like this: user, browser, network, '
                               'frontend, backend API, database, backend response, frontend rendering, user. '
                               'Each arrow represents a conversation. Each boundary gives you a place to '
                               'test.\n'
                               '\n'
                               'Suppose Forge opens normally, but saving a workout fails. That observation '
                               'immediately narrows the problem. The phone can reach the host. The frontend '
                               'files can load. The browser can render the application. The failure is more '
                               'likely somewhere along the save path: form validation, frontend request '
                               'construction, the backend endpoint, database access, or response handling.\n'
                               '\n'
                               'Notice what happened. We did not identify the answer. We reduced the size of '
                               'the unknown space. That is progress.\n'
                               '\n'
                               'This leads to one of the most valuable engineering habits: reduce scope '
                               'before changing anything.\n'
                               '\n'
                               'Scope means the boundaries of the problem. Ask who is affected, what action '
                               'fails, where it fails, when it began, and under which conditions it occurs. '
                               'Does it affect one user or every user? One device or every device? One '
                               'browser or all browsers? One page or the entire application? Local network '
                               'access or Tailscale access? A newly deployed version or an older stable '
                               'version?\n'
                               '\n'
                               'Each answer eliminates possibilities.\n'
                               '\n'
                               'For example, if Forge works from the Windows host but not from your iPhone, '
                               'the application itself may still be healthy. The difference between the two '
                               'tests becomes important: device, network path, hostname, port, TLS, or '
                               'firewall. If the frontend loads on the iPhone but API calls fail, then basic '
                               'reachability exists and the investigation can move toward the API address, '
                               'CORS configuration, backend port exposure, or proxy behavior.\n'
                               '\n'
                               'This is why experienced engineers sometimes appear to solve incidents '
                               'quickly. They are not guessing faster. They are narrowing possibilities '
                               'faster.\n'
                               '\n'
                               'The next habit is separating observations from assumptions.\n'
                               '\n'
                               'An observation is something you can directly verify. “The backend container '
                               'restarted six times in ten minutes” is an observation. “Docker is broken” is '
                               'an assumption. “The browser received a 502 response” is an observation. “The '
                               'database is down” is an assumption. “The request works through localhost but '
                               'times out through the Tailscale IP” is an observation. “Tailscale is the '
                               'problem” is still an assumption.\n'
                               '\n'
                               'Assumptions are not bad. Every investigation needs possible explanations. '
                               'The danger comes when an assumption is treated as fact before it has been '
                               'tested.\n'
                               '\n'
                               'A useful way to protect yourself from that mistake is to write hypotheses.\n'
                               '\n'
                               'A hypothesis is a specific, testable explanation for the observed behavior. '
                               'A good hypothesis predicts what evidence you should find if it is true.\n'
                               '\n'
                               'For example: “The backend is unreachable from the phone because port 8001 is '
                               'blocked on the Windows host.” That hypothesis predicts that the frontend may '
                               'load while direct requests to port 8001 fail from another device. You could '
                               'test the port from the network, inspect the Windows firewall, verify Docker '
                               'port publishing, and compare local versus remote access.\n'
                               '\n'
                               'Another hypothesis might be: “The frontend is calling localhost instead of '
                               'the server hostname.” That predicts that the browser developer tools will '
                               'show requests going to localhost on the phone, where localhost refers to the '
                               'phone itself rather than the Windows server.\n'
                               '\n'
                               'Both explanations are plausible. Evidence decides which one deserves '
                               'confidence.\n'
                               '\n'
                               'Good engineers also try to disprove their favorite hypothesis. This matters '
                               'because people naturally notice information that supports what they already '
                               'believe. That tendency is called confirmation bias. If you become convinced '
                               'that the network is responsible, every timeout will feel like proof, while '
                               'evidence pointing toward the application may be ignored.\n'
                               '\n'
                               'A stronger question is: what result would show that my hypothesis is wrong?\n'
                               '\n'
                               'If you believe the backend container is down, but Docker shows it healthy '
                               'and a direct API request succeeds from another machine, that hypothesis '
                               'becomes less likely. You have learned something, even though you have not '
                               'solved the incident yet.\n'
                               '\n'
                               'That brings us to controlled testing. A useful test changes or examines one '
                               'meaningful variable at a time. If you restart the frontend, backend, '
                               'database, host computer, router, and Tailscale all at once, and the '
                               'application starts working, you do not know which action mattered. You '
                               'restored service, but you learned very little.\n'
                               '\n'
                               'There are times when restoring service quickly is the priority. During a '
                               'real outage, a restart may be appropriate. Engineering judgment includes '
                               'balancing recovery speed with investigation quality. But even during urgent '
                               'incidents, record what you observed before making the change when possible. '
                               'Capture logs. Note timestamps. Identify the affected version. Preserve '
                               'enough evidence to investigate afterward.\n'
                               '\n'
                               'This is where documentation becomes part of engineering rather than an '
                               'administrative chore. A short incident timeline can be extremely valuable: '
                               '10:02, user reports failure; 10:05, frontend loads but API request returns '
                               '500; 10:08, backend log shows database connection refused; 10:12, database '
                               'container found stopped; 10:15, container restored; 10:17, request '
                               'succeeds.\n'
                               '\n'
                               'That timeline tells a story supported by evidence. It also makes '
                               'communication easier. Instead of saying, “It looks like Docker had an '
                               'issue,” you can say, “The frontend remained available, but API requests '
                               'failed because the backend could not connect to the stopped database '
                               'container. The database was restored at 10:15, and successful requests were '
                               'confirmed at 10:17.”\n'
                               '\n'
                               'Clear communication is one of the differences between troubleshooting '
                               'privately and engineering professionally. During an incident, other people '
                               'need to know the impact, current understanding, actions taken, and next '
                               'checkpoint. Confidence should match the evidence. Say “We are investigating '
                               'the database connection” when that is what you know. Do not say “The '
                               'database caused it” until the evidence supports that conclusion.\n'
                               '\n'
                               'Your experience at TruHearing gives you a strong foundation here. Think '
                               'about the portal refresh issue. The screen did not visibly change, so one '
                               'possible reaction would have been to keep rewriting the button. Instead, you '
                               'inspected the browser console and network activity. You confirmed that '
                               'requests were being sent, watched their responses, and narrowed the problem '
                               'to the behavior actually occurring. Once the buttons visibly spun and the '
                               'network calls succeeded, you had evidence that the flow was working.\n'
                               '\n'
                               'Think about the Forge backend restart loop. The container repeatedly '
                               'restarted. Rather than treating Docker as a black box, you read the backend '
                               'logs and followed the Python traceback. The container behavior was a '
                               'symptom. The logs exposed where the application startup failed.\n'
                               '\n'
                               'Think about the Tailscale and Remote Desktop investigation. You checked '
                               'whether devices appeared in Tailscale, tested ping, inspected port 3389, '
                               'reviewed Windows services, and compared local and remote behavior. Even '
                               'though the issue was frustrating, the process was engineering: test the '
                               'path, locate boundaries, and eliminate possibilities.\n'
                               '\n'
                               'These examples matter because they show that you are not beginning at zero. '
                               'The Journey is going to formalize habits you already use, strengthen the '
                               'weak spots, and apply the same reasoning to increasingly complex systems.\n'
                               '\n'
                               'Now let us build a reusable troubleshooting loop.\n'
                               '\n'
                               'First, observe. Describe the actual behavior without explaining it yet. '
                               'Include exact error messages, timestamps, affected users, and reproducible '
                               'steps.\n'
                               '\n'
                               'Second, define scope. Determine who, what, where, when, and under which '
                               'conditions.\n'
                               '\n'
                               'Third, map the system. Trace the request or workflow through the components '
                               'that must cooperate.\n'
                               '\n'
                               'Fourth, form multiple hypotheses. List plausible causes without committing '
                               'too early.\n'
                               '\n'
                               'Fifth, choose the cheapest high-value test. Look for a test that can '
                               'eliminate a large number of possibilities with low risk. Checking container '
                               'state or browser network requests is usually cheaper and safer than '
                               'redeploying the whole application.\n'
                               '\n'
                               'Sixth, collect evidence and update your beliefs. A hypothesis can become '
                               'more likely, less likely, or remain uncertain.\n'
                               '\n'
                               'Seventh, make one controlled change when a change is justified. Measure the '
                               'result.\n'
                               '\n'
                               "Eighth, verify from the user's perspective. A healthy container does not "
                               'prove the user can complete the task. Repeat the original action.\n'
                               '\n'
                               'Ninth, document what happened and what should improve. The best incident is '
                               'not merely fixed; it makes the system or the team stronger.\n'
                               '\n'
                               'There is another important idea here: engineers work with incomplete '
                               'information. You will often begin without access to every log, without full '
                               'cloud permissions, or without deep knowledge of the code. Engineering is not '
                               'the absence of uncertainty. It is disciplined progress despite uncertainty.\n'
                               '\n'
                               'That should be encouraging. You do not need to know every AWS service, Linux '
                               'command, or Kubernetes object before you can think like an engineer. Those '
                               'tools will give you more places to observe and more ways to act, but the '
                               'foundation begins now.\n'
                               '\n'
                               'Before finishing, remember three practical principles.\n'
                               '\n'
                               'First: never confuse activity with progress. Restarting five services feels '
                               'active. Finding the one failed dependency is progress.\n'
                               '\n'
                               'Second: the first explanation is a candidate, not a conclusion. Give your '
                               'ideas names such as hypothesis one and hypothesis two. That small wording '
                               'change protects your thinking.\n'
                               '\n'
                               'Third: verify the complete user outcome. Infrastructure can look healthy '
                               'while the actual workflow remains broken.\n'
                               '\n'
                               'Here is the takeaway for Lesson 0.1: great engineers do not begin with '
                               'answers. They begin with better questions.\n'
                               '\n'
                               'As you move into the lab, your job is not to fix the scenario immediately. '
                               'Your job is to make the problem smaller, build a map, and design an '
                               'investigation that produces reliable evidence. That is how The Journey '
                               'begins.',
               'content': [{'heading': 'Why this lesson matters',
                            'body': 'Tools change constantly, but disciplined engineering habits remain '
                                    'useful across support, software, infrastructure, cloud, and DevOps. '
                                    'Your first responsibility is not to make a change. It is to understand '
                                    'what the system is doing, what it should be doing, and where those two '
                                    'behaviors diverge.'},
                           {'heading': 'Engineers reduce uncertainty',
                            'body': "A vague report such as 'Forge is down' contains many possible problems. "
                                    'An engineer turns that vague report into smaller questions: Can the '
                                    'page load? Who is affected? Which action fails? Does it work locally? '
                                    'What changed? Each verified answer removes possibilities and guides the '
                                    'next test.'},
                           {'heading': 'Everything is a connected system',
                            'body': 'An application is a chain of cooperating components. A typical Forge '
                                    'request may travel from the iPhone to the network, frontend, FastAPI '
                                    'backend, PostgreSQL database, and back again. The visible symptom may '
                                    'appear in one layer even when the cause exists in another. Systems '
                                    'thinking means tracing those relationships instead of treating the '
                                    'application as one indivisible object.'},
                           {'heading': 'Reduce the scope before acting',
                            'body': 'Determine who, what, where, when, and under which conditions the '
                                    'failure occurs. Compare working and failing cases. One user versus '
                                    'everyone, local access versus Tailscale, one endpoint versus the entire '
                                    'application, and old version versus new deployment are all high-value '
                                    'comparisons. Experienced engineers often appear fast because they '
                                    'eliminate possibilities efficiently.'},
                           {'heading': 'Separate observations from assumptions',
                            'body': "An observation is directly verified: 'the API returned HTTP 500 at "
                                    "10:14.' An assumption interprets it: 'the database is broken.' "
                                    'Assumptions are useful as possible explanations, but they become '
                                    'dangerous when treated as facts. Record what you can prove before '
                                    'explaining why it happened.'},
                           {'heading': 'Build testable hypotheses',
                            'body': 'A useful hypothesis explains the observation and predicts evidence. '
                                    "Example: 'The frontend is calling localhost from the iPhone.' If true, "
                                    'browser network requests should show localhost in the API URL. Maintain '
                                    'more than one plausible hypothesis and ask what evidence would disprove '
                                    'each one.'},
                           {'heading': 'Run controlled, high-value tests',
                            'body': 'Choose the safest test that can eliminate the most possibilities. '
                                    'Inspecting the browser Network tab, checking container state, or '
                                    'calling a health endpoint usually provides more learning and less risk '
                                    'than restarting every service. Change one meaningful variable at a time '
                                    'so the result can be interpreted.'},
                           {'heading': 'Verify the user outcome',
                            'body': 'A green container, successful deployment, or healthy server metric is '
                                    'not the final proof. Repeat the exact workflow that failed and confirm '
                                    "it from the user's point of view. Engineering success is restored "
                                    'capability, not merely healthy components.'},
                           {'heading': "Alex's Engineering Notes",
                            'body': 'Never confuse activity with progress. Restarting five services feels '
                                    'productive; reading one log line that identifies the failed dependency '
                                    'is productive. Also remember that the first explanation is a candidate, '
                                    'not a conclusion. Let evidence earn your confidence.'},
                           {'heading': 'Takeaway',
                            'body': 'Great engineers do not begin with answers. They begin with better '
                                    'questions.'}],
               'lab': {'title': 'Your first engineering investigation',
                       'instructions': ["Create a journal entry titled 'Lesson 0.1 - Forge Investigation "
                                        "Plan.'",
                                        "Start with this report: 'Forge is down on my iPhone.' Do not "
                                        'propose a fix yet.',
                                        'Write two columns or sections: Observations and Assumptions. The '
                                        'report itself is an observation; list at least five assumptions you '
                                        'might accidentally make.',
                                        'Write at least eight scope questions covering who, what, where, '
                                        'when, and conditions. Include local Wi-Fi versus Tailscale and '
                                        'frontend versus backend behavior.',
                                        'Map the expected request path: iPhone → network or Tailscale → '
                                        'Windows host → frontend container → backend container → PostgreSQL '
                                        '→ response.',
                                        'For every component in the path, list one possible failure and one '
                                        'piece of evidence that could confirm or weaken it.',
                                        'Create at least three testable hypotheses. For each one, write: '
                                        'prediction, safest first test, evidence that supports it, and '
                                        'evidence that disproves it.',
                                        'Order your first five investigation steps from lowest risk and '
                                        "highest information value to higher risk. Do not use 'restart "
                                        "everything' as an early step.",
                                        'Write a two-sentence status update suitable for a coworker: one '
                                        'sentence for confirmed impact and one for the next investigation '
                                        'step. Do not claim a root cause you have not proven.',
                                        'Finish with a short reflection: Which step in your plan reduced the '
                                        'most uncertainty, and why?']},
               'quiz': [{'question': "A user reports, 'Forge is down.' What is the strongest first response?",
                         'choices': ['Restart every container immediately',
                                     'Ask targeted questions and reproduce the exact failing workflow',
                                     'Assume the latest deployment caused it',
                                     'Clear the database'],
                         'correct': 1},
                        {'question': 'Which statement is an observation rather than an assumption?',
                         'choices': ['The network is broken',
                                     'Docker caused the outage',
                                     'The browser received HTTP 502 at 10:14 AM',
                                     'The database must be overloaded'],
                         'correct': 2},
                        {'question': 'Forge loads on the Windows host but not on an iPhone through '
                                     'Tailscale. What does that evidence suggest?',
                         'choices': ['The entire application is definitely down',
                                     'The database has lost all data',
                                     'The difference in device or network path should be investigated',
                                     'The frontend code must be rewritten'],
                         'correct': 2},
                        {'question': 'What makes an engineering hypothesis useful?',
                         'choices': ['It sounds confident',
                                     'It names the most complicated component',
                                     'It is specific, testable, and predicts evidence',
                                     'It requires a restart'],
                         'correct': 2},
                        {'question': 'Why is changing several services at once a weak troubleshooting test?',
                         'choices': ['It is always slower',
                                     'You cannot tell which change affected the result',
                                     'Containers cannot restart together',
                                     'It prevents users from reporting issues'],
                         'correct': 1},
                        {'question': 'The frontend loads, but saving a workout returns an API error. Which '
                                     'conclusion is best supported?',
                         'choices': ['The phone cannot reach the server at all',
                                     'The failure is likely in the save request path rather than initial '
                                     'frontend loading',
                                     'The entire network is offline',
                                     'The user entered the wrong password'],
                         'correct': 1},
                        {'question': 'What is confirmation bias during troubleshooting?',
                         'choices': ['Testing every hypothesis equally',
                                     'Preferring evidence that supports the explanation you already favor',
                                     'Documenting a timeline',
                                     "Verifying the user's workflow"],
                         'correct': 1},
                        {'question': 'When is an incident truly verified as resolved?',
                         'choices': ['When Docker shows every container as running',
                                     'When the server has low CPU usage',
                                     'When the original user workflow succeeds under the conditions that '
                                     'previously failed',
                                     'When a deployment command exits without an error'],
                         'correct': 2},
                        {'question': 'Why can an early restart be harmful during an investigation?',
                         'choices': ['Restarts are never allowed in production',
                                     'It may erase evidence and restore service without revealing the cause',
                                     'It permanently disables logging',
                                     'It always corrupts the database'],
                         'correct': 1},
                        {'question': 'Which status update demonstrates appropriate engineering confidence?',
                         'choices': ['The database caused the outage, although we have not checked it yet',
                                     'Everything is broken and we are restarting the server',
                                     'We confirmed workout saves fail while the frontend remains available; '
                                     'we are now checking the backend response and logs',
                                     'It is probably Tailscale, so no further testing is needed'],
                         'correct': 2}],
               'reflection': 'What troubleshooting habits do you already use well? Identify one time you '
                             'acted before gathering enough evidence, explain what uncertainty existed, and '
                             'rewrite your approach using observe, scope, map, hypothesize, test, verify, '
                             'and document. Then explain in your own words why great engineers begin with '
                             'better questions rather than immediate answers.'},
              {'id': '0-2',
               'title': 'Evidence Before Action',
               'summary': 'Turn vague symptoms into reliable evidence, test one hypothesis at a time, and '
                          'make changes only when the facts justify them.',
               'duration_minutes': 55,
               'xp': 50,
               'audio_script': 'Welcome to Ascend, Lesson 0.2: Evidence Before Action.\n'
                               '\n'
                               'Imagine opening Forge on your iPhone and seeing that workout data will not '
                               'load. The fastest emotional response is to restart Docker, reboot the '
                               'server, or rebuild the app. Those actions may work, but they may also erase '
                               'the very evidence that could tell you why the failure happened.\n'
                               '\n'
                               'Evidence before action does not mean standing still. It means choosing '
                               'actions that reduce uncertainty. Begin with the user experience. What exact '
                               'step failed? What message appeared? When did it happen? Does the same '
                               'workflow fail on Wi-Fi, through Tailscale, and directly on the server?\n'
                               '\n'
                               'Next, separate observations from interpretations. “The browser requested an '
                               'old Tailscale address” is an observation. “React is broken” is an '
                               'interpretation. Observations can be shared and verified. Interpretations '
                               'must earn confidence through testing.\n'
                               '\n'
                               'Now form a hypothesis that makes a prediction. If the deployed frontend '
                               'contains an old backend address, the browser Network tab should show '
                               'requests going there even when your current source code does not. That is '
                               'exactly the kind of evidence that once helped us understand a Forge '
                               'connection problem. The browser showed what the running system was actually '
                               'doing, not what we expected it to be doing.\n'
                               '\n'
                               'Work from the outside in. Trace the path from the iPhone, through Wi-Fi or '
                               'Tailscale, to the Windows host, the frontend container, FastAPI, PostgreSQL, '
                               'and back again. Every confirmed working layer shrinks the problem.\n'
                               '\n'
                               'When you test, change one meaningful variable. If you restart five services '
                               'at once and the application recovers, you know that something changed, but '
                               'not which change mattered. A controlled test preserves learning.\n'
                               '\n'
                               'This principle applies at TruHearing too. A report that OneDrive is stuck is '
                               'only the beginning. Which user? Which device? Which client version? Which '
                               'network? Is authentication complete? What do the logs and service health '
                               'show? Better evidence creates better escalations and safer fixes.\n'
                               '\n'
                               'Finally, communicate what you know without pretending to know more. Say what '
                               'is confirmed, what remains unknown, and what you are testing next. '
                               'Engineering confidence is not loud certainty. It is disciplined honesty '
                               'supported by evidence.\n'
                               '\n'
                               'Your operating rule is simple: observe before changing, predict before '
                               'testing, change one variable when possible, and verify the original workflow '
                               'after the fix.',
               'content': [{'heading': 'Activity is not the same as progress',
                            'body': 'When a system fails, restarting services can feel decisive. But an '
                                    'unplanned change may erase logs, hide a temporary condition, or '
                                    'introduce a second variable. Engineering begins by preserving the scene '
                                    'long enough to learn from it. The goal is not to avoid action; it is to '
                                    'make the next action earn its risk.'},
                           {'heading': 'Separate observations from interpretations',
                            'body': 'An observation is something you can point to: an HTTP 502 response, a '
                                    'container marked unhealthy, a request that takes 29 seconds, or Forge '
                                    'working locally but failing through Tailscale. An interpretation '
                                    'explains the observation: the backend is down, the network is broken, '
                                    'or the database is slow. Write them separately so assumptions do not '
                                    'quietly become facts.'},
                           {'heading': 'Build an evidence ladder',
                            'body': 'Start with evidence that is fast, safe, and close to the user: '
                                    'reproduce the workflow, record the exact message and time, compare '
                                    'devices or networks, and inspect the browser Network and Console tabs. '
                                    'Then move inward through application logs, container state, resource '
                                    'usage, database health, and external dependencies. Each rung should '
                                    'narrow the search area.'},
                           {'heading': 'Use predictions to test hypotheses',
                            'body': 'A useful hypothesis predicts what you should observe. If an old '
                                    'Tailscale address is embedded in the frontend build, the browser should '
                                    'attempt requests to that address while the backend remains healthy at '
                                    'its current address. If the prediction fails, weaken or reject the '
                                    'hypothesis. This prevents troubleshooting from becoming a search for '
                                    'evidence that agrees with your first guess.'},
                           {'heading': 'Change one meaningful variable',
                            'body': 'A controlled test changes one thing and measures the result. Restarting '
                                    'the frontend, backend, database, host, and network together may restore '
                                    'service, but it destroys attribution. Prefer the smallest reversible '
                                    'test that distinguishes between competing explanations. Record the '
                                    'before state, the action, and the after state.'},
                           {'heading': 'Read the system from the outside in',
                            'body': 'For Ascend or Forge, trace the request path: iPhone or browser → Wi-Fi '
                                    'or Tailscale → Windows host → frontend container → FastAPI backend → '
                                    'PostgreSQL or another dependency → response. A working layer is '
                                    'evidence too. If the page shell loads but saving fails, initial '
                                    'frontend delivery works and the investigation should focus on the save '
                                    'request path.'},
                           {'heading': 'Real-world example: the stale Tailscale address',
                            'body': 'Forge once appeared unreliable from another device while the current '
                                    'code on the Mac contained no reference to the old address. Browser '
                                    'evidence showed the deployed frontend was still calling 100.105.129.14. '
                                    'That observation shifted the investigation away from React source code '
                                    'and toward the deployed build and synchronization path. The lesson was '
                                    'not simply “push the code”; it was that the browser’s actual request is '
                                    'stronger evidence than what we believe was deployed.'},
                           {'heading': 'Evidence at TruHearing',
                            'body': 'The same method applies to Microsoft 365 and internal support. '
                                    '“OneDrive is stuck” becomes: which user, device, tenant, client '
                                    'version, sign-in state, network, and timestamp? “The directory is slow” '
                                    'becomes: which page, which API request, server duration, Graph '
                                    'response, cache state, and affected population? Clear evidence produces '
                                    'safer changes, better escalations, and explanations coworkers can '
                                    'trust.'},
                           {'heading': 'Communicate confidence honestly',
                            'body': 'During an incident, state what is confirmed, what remains unknown, and '
                                    'what you are testing next. “We confirmed the frontend loads but workout '
                                    'saves return 500 responses; we are checking the backend logs for that '
                                    'request” is more useful than “the database is down.” Precision is not '
                                    'hesitation. It is how engineers protect trust while knowledge is '
                                    'incomplete.'},
                           {'heading': 'The operating rule',
                            'body': 'Observe before changing. Preserve evidence before restarting. Predict '
                                    'before testing. Change one variable when possible. Verify the original '
                                    'workflow after the fix. Document what the evidence taught you so the '
                                    'next incident starts with more knowledge than the last one.'}],
               'lab': {'title': 'Investigate a failure without guessing',
                       'instructions': ['Choose Forge, Ascend, or the TruHearing directory application and '
                                        'define one realistic failure scenario.',
                                        'Write the exact user report, then rewrite it as a reproducible '
                                        'workflow with device, network, timestamp, expected result, and '
                                        'actual result.',
                                        'Create two lists labeled Observations and Interpretations. Add at '
                                        'least five items to each.',
                                        'Draw the request path from the user interface to every service or '
                                        'dependency involved and back to the user.',
                                        'For each layer, name one low-risk piece of evidence that would show '
                                        'whether the request reached or passed that layer.',
                                        'Create three competing hypotheses. For each, write a prediction '
                                        'that must be true if the hypothesis is correct.',
                                        'Design the safest first test for each hypothesis. Each test should '
                                        'change no more than one meaningful variable.',
                                        'Rank your tests by information value, reversibility, and risk. '
                                        'Explain why your first test comes first.',
                                        'Write a short incident update containing confirmed impact, current '
                                        'evidence, remaining uncertainty, and the next test.',
                                        'Write a final verification plan that repeats the original workflow '
                                        'and checks for side effects after the fix.']},
               'quiz': [{'question': 'Which statement is direct evidence?',
                         'choices': ['Docker is probably broken',
                                     'The browser received HTTP 500 from /api/workouts at 9:14 PM',
                                     'The database must be slow',
                                     'The latest deployment caused it'],
                         'correct': 1},
                        {'question': 'Why should observations and interpretations be recorded separately?',
                         'choices': ['Interpretations are never useful',
                                     'It prevents assumptions from being treated as confirmed facts',
                                     'Observations only matter to managers',
                                     'It makes incidents take longer'],
                         'correct': 1},
                        {'question': 'What makes a troubleshooting hypothesis testable?',
                         'choices': ['It identifies a complicated component',
                                     'It includes a prediction that evidence can support or contradict',
                                     'It recommends restarting the server',
                                     'It agrees with the first report'],
                         'correct': 1},
                        {'question': 'Forge loads locally but fails through Tailscale. What is the best '
                                     'conclusion?',
                         'choices': ['PostgreSQL is definitely corrupted',
                                     'The entire app is down',
                                     'The differing network path is an important investigation variable',
                                     'React must be rewritten'],
                         'correct': 2},
                        {'question': 'Why is restarting every service at once a weak diagnostic test?',
                         'choices': ['It can restore service without revealing which change mattered',
                                     'Docker forbids it',
                                     'It always deletes logs',
                                     'Users cannot reconnect afterward'],
                         'correct': 0},
                        {'question': 'The page shell loads, but saving returns a 500 response. Which layer '
                                     'is already partly verified?',
                         'choices': ['Initial frontend delivery to the browser',
                                     'Every backend dependency',
                                     'The database write',
                                     'The full user workflow'],
                         'correct': 0},
                        {'question': 'Which test should usually come first?',
                         'choices': ['The most disruptive test',
                                     'The fastest test regardless of risk',
                                     'A low-risk reversible test that best distinguishes hypotheses',
                                     'A production redeployment'],
                         'correct': 2},
                        {'question': 'What should a useful incident update include?',
                         'choices': ['Only a confident root cause',
                                     'Confirmed impact, current evidence, unknowns, and next step',
                                     'Every command ever run',
                                     'A promise that the issue is fixed'],
                         'correct': 1},
                        {'question': 'When is a repair verified?',
                         'choices': ['When containers are green',
                                     'When CPU usage falls',
                                     'When the original failing workflow succeeds under the same conditions '
                                     'and side effects are checked',
                                     'When the restart command completes'],
                         'correct': 2},
                        {'question': 'What did the stale Tailscale address example demonstrate?',
                         'choices': ['Source code always reflects the deployed application',
                                     'Browser request evidence can reveal a mismatch between expected and '
                                     'deployed behavior',
                                     'Tailscale addresses never change',
                                     'Rebuilding is always the first step'],
                         'correct': 1}],
               'reflection': 'Describe a time when you changed something before collecting enough evidence. '
                             'What observation did you have, what interpretation did you treat as fact, and '
                             'what evidence would have produced a safer first action? Then write the status '
                             'update you would give today using confirmed impact, evidence, uncertainty, and '
                             'next test.'},
              {'id': '0-3',
               'title': 'The Internet Is Computers Talking',
               'summary': 'Trace requests as conversations through DNS, networks, servers, applications, and '
                          'dependencies.',
               'duration_minutes': 30,
               'xp': 30,
               'audio_script': 'Welcome back to The Journey.\n'
                               '\n'
                               'The internet can feel mysterious, but at its core it is computers having '
                               'structured conversations.\n'
                               '\n'
                               'When you enter a website address, the browser first needs to learn where '
                               'that name lives. DNS provides an IP address. The browser then establishes a '
                               'connection, negotiates security, and asks a server for a resource. The '
                               'server may ask an application, database, authentication provider, or '
                               'external API for additional information before returning a response.\n'
                               '\n'
                               'When an application does not load, ask which conversation failed. Did DNS '
                               'resolve the name? Could the browser reach the server? Did TLS succeed? Did '
                               'the reverse proxy route the request? Did the application respond? Did the '
                               'application reach its database or external dependency?\n'
                               '\n'
                               'Thinking in conversations lets you trace a request in order instead of '
                               'jumping randomly between components.\n'
                               '\n'
                               'Your task is to map the login flow for your Directory App from the browser '
                               'through authentication and finally to the home page.',
               'content': [{'heading': 'Names and addresses',
                            'body': 'DNS translates a human-readable name into an IP address that a computer '
                                    'can connect to.'},
                           {'heading': 'Connections',
                            'body': 'The browser connects to a server over a network and may negotiate TLS '
                                    'before sending an HTTP request.'},
                           {'heading': 'Routing',
                            'body': 'A reverse proxy or load balancer can receive the request and route it '
                                    'to the correct application service.'},
                           {'heading': 'Dependencies',
                            'body': 'The application may depend on authentication, databases, caches, or '
                                    'external APIs before it can answer.'},
                           {'heading': 'Engineer principle',
                            'body': 'When a system fails, identify which conversation stopped succeeding.'}],
               'lab': {'title': 'Map the login conversation',
                       'instructions': ['Start with the user entering the application URL.',
                                        'Include DNS, browser, server, frontend, authentication provider, '
                                        'backend, and external APIs.',
                                        'Write what each component asks and what it returns.',
                                        'Mark at least five possible failure points.']},
               'quiz': [{'question': 'What is DNS primarily responsible for?',
                         'choices': ['Rendering React components',
                                     'Translating names into IP addresses',
                                     'Storing user passwords',
                                     'Building Docker images'],
                         'correct': 1},
                        {'question': "Why is the 'conversation' model useful?",
                         'choices': ['It eliminates the need for logs',
                                     'It helps trace failures in order through the system',
                                     'It proves every problem is DNS',
                                     'It replaces networking knowledge'],
                         'correct': 1},
                        {'question': 'Which component commonly routes incoming web requests to an '
                                     'application service?',
                         'choices': ['Reverse proxy', 'Text editor', 'Monitor', 'Package manager'],
                         'correct': 0}],
               'reflection': 'Which part of a web request path feels most familiar, and which part do you '
                             'most want to understand better?'}]},
 {'id': 'module-1',
  'number': 1,
  'title': 'Git and Collaborative Source Control',
  'subtitle': 'Repositories, commits, branches, merges, pull requests, tags, and recovery.',
  'status': 'locked',
  'lessons': []},
 {'id': 'module-2',
  'number': 2,
  'title': 'Linux and the Command Line',
  'subtitle': 'Filesystems, users, permissions, processes, services, logs, SSH, and shell fundamentals.',
  'status': 'locked',
  'lessons': []},
 {'id': 'module-3',
  'number': 3,
  'title': 'Networking and Web Fundamentals',
  'subtitle': 'DNS, TCP/IP, HTTP, TLS, ports, routing, proxies, and firewalls.',
  'status': 'locked',
  'lessons': []},
 {'id': 'module-4',
  'number': 4,
  'title': 'Docker and Containers',
  'subtitle': 'Images, containers, Dockerfiles, Compose, volumes, networks, registries, tags, and rollback.',
  'status': 'locked',
  'lessons': []},
 {'id': 'module-5',
  'number': 5,
  'title': 'CI/CD Pipelines',
  'subtitle': 'Automated testing, builds, artifacts, deployment strategies, and pipeline troubleshooting.',
  'status': 'locked',
  'lessons': []},
 {'id': 'module-6',
  'number': 6,
  'title': 'AWS and Cloud Fundamentals',
  'subtitle': 'IAM, billing safety, EC2, S3, VPC, RDS, CloudWatch, ECS, and application deployment.',
  'status': 'locked',
  'lessons': []},
 {'id': 'module-7',
  'number': 7,
  'title': 'Infrastructure as Code',
  'subtitle': 'Terraform fundamentals, state, modules, environments, and safe infrastructure changes.',
  'status': 'locked',
  'lessons': []},
 {'id': 'module-8',
  'number': 8,
  'title': 'Monitoring, Logging, and Reliability',
  'subtitle': 'Metrics, logs, traces, health checks, dashboards, alerts, incidents, and postmortems.',
  'status': 'locked',
  'lessons': []},
 {'id': 'module-9',
  'number': 9,
  'title': 'Security and Secrets',
  'subtitle': 'Least privilege, secret management, patching, vulnerability awareness, HTTPS, and secure '
              'delivery.',
  'status': 'locked',
  'lessons': []},
 {'id': 'module-10',
  'number': 10,
  'title': 'Capstone Deployment',
  'subtitle': 'Build, deploy, monitor, document, and recover a complete production-style application.',
  'status': 'locked',
  'lessons': []}]
