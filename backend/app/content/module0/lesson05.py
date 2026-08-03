"""Module 0, Lesson 0.5."""

LESSON = {'id': '0-5',
 'title': 'What DevOps Actually Connects',
 'summary': 'Understand DevOps as a system of shared ownership, automation, fast feedback, and reliable '
            'delivery that connects an idea in Git to a useful outcome for real people.',
 'duration_minutes': 75,
 'xp': 75,
 'audio_script': 'Welcome back to Ascend. This is Lesson 0.5: What DevOps Actually Connects.\n'
                 '\n'
                 'You have already learned how engineers think, why evidence should come before action, how '
                 'computers communicate, and how a modern application is assembled from many cooperating '
                 'parts.\n'
                 '\n'
                 'Now we can ask the question at the center of this course: what does DevOps actually '
                 'connect?\n'
                 '\n'
                 'Many people first encounter DevOps as a list of tools. Docker. GitHub Actions. Jenkins. '
                 'Terraform. Kubernetes. AWS. Monitoring dashboards. Those tools matter, and you will learn '
                 'many of them. But a list of tools does not explain why DevOps exists.\n'
                 '\n'
                 'DevOps exists because useful software has to travel through an entire system before it '
                 'creates value.\n'
                 '\n'
                 'An idea begins with a need. Someone changes code. That code must be reviewed, tested, '
                 'built, configured, deployed, secured, observed, supported, and improved. Real users then '
                 'interact with the result. Their experience produces feedback, incidents, questions, and '
                 'new requirements. That feedback must travel back to the people who can improve the '
                 'system.\n'
                 '\n'
                 'DevOps connects that loop.\n'
                 '\n'
                 'The word combines development and operations, but the connection is broader than two '
                 'departments. It links product goals, software development, testing, security, '
                 'infrastructure, deployment, operations, support, and user feedback. The goal is not to '
                 'make everyone do the same job. The goal is to make the entire path visible, reliable, and '
                 'shared.\n'
                 '\n'
                 'Consider Forge. A feature begins as an idea, perhaps adding a better workout card or '
                 'improving HealthKit data. You change React code on your Mac. The code enters Git, where '
                 'the change can be reviewed and preserved. A frontend build turns source files into '
                 'deployable assets. Docker packages those assets into an image. Docker Compose describes '
                 'how the frontend, FastAPI backend, and PostgreSQL database should run together. The image '
                 'reaches your home server. Containers start. Ports and Tailscale make the service '
                 'reachable. You open Forge on your iPhone and verify the actual workflow. Then real use '
                 'tells you what to improve next.\n'
                 '\n'
                 'That is a delivery system.\n'
                 '\n'
                 'If any handoff is unclear, manual, or invisible, risk increases. The source code can be '
                 'correct while the server runs an old image. The image can be current while the iPhone '
                 'still contains a stale Capacitor bundle. The containers can be healthy while one API '
                 'workflow fails. A deployment can succeed technically while users cannot complete the task '
                 'that matters.\n'
                 '\n'
                 'DevOps tries to reduce those gaps.\n'
                 '\n'
                 'Historically, software teams often organized work into silos. Developers wrote code and '
                 'handed it to an operations team. Operations received the release and tried to run it '
                 'safely. Testers, security teams, support teams, and business stakeholders might enter at '
                 'separate checkpoints. Each group optimized its own responsibility, but the overall flow '
                 'could remain slow and fragile.\n'
                 '\n'
                 'A developer might say, “It works on my machine.” Operations might say, “The application '
                 'does not meet production requirements.” Security might discover a problem just before '
                 'release. Support might learn about a confusing behavior only after users complained. '
                 'Everyone could be working hard while the system of work produced delays and conflict.\n'
                 '\n'
                 'The problem was not that development or operations lacked effort. The problem was that the '
                 'feedback arrived too late and responsibility was fragmented.\n'
                 '\n'
                 'DevOps responds by moving collaboration and feedback earlier. Developers consider how '
                 'software will run. Operations contributes reliability and deployment knowledge while the '
                 'system is being designed. Security becomes part of the delivery process instead of a final '
                 'gate. Tests run automatically and frequently. Infrastructure and configuration become '
                 'reviewable code. Monitoring shows how the deployed system behaves. Incidents create '
                 'learning that improves the next release.\n'
                 '\n'
                 'This is often described as breaking down silos, but that does not mean eliminating '
                 'specialties. A database engineer, software developer, systems administrator, security '
                 'engineer, and support technician still bring different expertise. DevOps creates better '
                 'interfaces between those specialties and encourages shared ownership of the user outcome.\n'
                 '\n'
                 'Shared ownership is important. If a developer is responsible only until code is merged, '
                 "the running behavior can become someone else's problem. If operations is responsible only "
                 "for keeping servers alive, application failures can be dismissed as someone else's code. "
                 'DevOps asks a stronger question: is the complete service delivering the intended outcome '
                 'reliably?\n'
                 '\n'
                 'This connects directly to what you learned in Lesson 0.4. A modern application has '
                 'clients, frontends, APIs, backends, databases, identity, infrastructure, configuration, '
                 'delivery mechanisms, and observability. DevOps connects the work required to change and '
                 'operate all of those layers safely.\n'
                 '\n'
                 'Git is one of the first connections. Git links individual changes to shared history. It '
                 'provides evidence of what changed, who changed it, and why. Branches and pull requests '
                 'create a place for collaboration. Commits create checkpoints. Tags identify releases. '
                 'Reverting creates a recovery path.\n'
                 '\n'
                 'But Git alone does not deliver software.\n'
                 '\n'
                 'Continuous integration connects code changes to automated validation. When a change is '
                 'pushed, a pipeline can install dependencies, run tests, check formatting, scan for known '
                 'issues, and build an artifact. The important idea is not the name of the tool. The '
                 'important idea is that feedback arrives quickly and consistently.\n'
                 '\n'
                 'If a change breaks the build, you want to know while the change is still small and fresh '
                 'in your mind. Fast feedback is cheaper than discovering the problem during a late-night '
                 'deployment.\n'
                 '\n'
                 'Continuous delivery connects validated code to a repeatable release process. The same '
                 'artifact that passed testing can move through environments with controlled configuration. '
                 'Deployment steps become documented and automated. Approvals can still exist, but the '
                 'mechanics are reliable rather than improvised.\n'
                 '\n'
                 'Automation is not valuable merely because it removes typing. It creates consistency. A '
                 'manual deployment can vary depending on who performs it, which commands they remember, and '
                 'what state the environment is already in. An automated pipeline performs the same declared '
                 'steps and leaves a history of what happened.\n'
                 '\n'
                 'Infrastructure as Code extends that idea to servers, networks, permissions, and cloud '
                 'resources. Instead of configuring an environment only through clicks and memory, teams '
                 'describe the desired infrastructure in version-controlled files. Changes can be reviewed, '
                 'tested, repeated, and compared.\n'
                 '\n'
                 'Containers provide another connection. A Docker image packages an application with the '
                 'runtime and dependencies it expects. This reduces differences between environments. It '
                 'does not eliminate every environmental problem, but it creates a clearer contract between '
                 'development and operations: this image is the version we intend to run.\n'
                 '\n'
                 'Docker Compose gives you a small-scale example of orchestration. It connects services, '
                 'networks, ports, volumes, environment variables, and startup behavior in one definition. '
                 'Your Forge and Ascend Compose files are not merely convenience scripts. They are '
                 'executable documentation of how the applications run.\n'
                 '\n'
                 'Configuration connects one artifact to different environments. The same code might use a '
                 'local backend during development and a Tailscale address on your home server. Database '
                 'credentials, API URLs, feature flags, and ports should be managed deliberately. When '
                 'configuration is hidden or manually changed, the delivery path becomes difficult to '
                 'reproduce.\n'
                 '\n'
                 'Secrets require special care. DevOps connects speed with security, not speed at the '
                 'expense of security. Passwords, tokens, certificates, and keys should not be committed to '
                 'source control. A reliable delivery system provides those secrets securely to the '
                 'application that needs them and limits access according to least privilege.\n'
                 '\n'
                 'Observability connects running software back to the people responsible for it. Logs '
                 'explain events. Metrics show trends and quantities. Traces connect work across multiple '
                 'services. Health checks answer focused questions about readiness or liveness. Dashboards '
                 'summarize important behavior. Alerts call attention to conditions that need action.\n'
                 '\n'
                 'Without observability, deployment is the end of the story. With observability, deployment '
                 'begins the learning phase.\n'
                 '\n'
                 'Imagine you deploy an Ascend lesson update. The container starts successfully. That is '
                 'useful evidence, but it is not enough. Can the API return the new lesson? Does the Modules '
                 'page list it? Does the iPhone app render every tab? Can the quiz submit? Does completion '
                 'tracking still work? The user workflow is the real definition of success.\n'
                 '\n'
                 'That is why DevOps connects technical signals to user outcomes.\n'
                 '\n'
                 'Feedback comes from more than monitoring. Support tickets, employee questions, application '
                 'analytics, failed workflows, and direct conversations all reveal how the system behaves in '
                 'reality. At TruHearing, a user reporting that OneDrive stays on “Signing in” is part of an '
                 'operational feedback loop. Browser network errors in the directory portal are feedback. A '
                 'manager asking for a different export is product feedback. DevOps helps move that '
                 'information to the right place quickly enough to improve the system.\n'
                 '\n'
                 'The loop can be summarized like this: plan, build, test, release, deploy, operate, '
                 'observe, learn, and plan again.\n'
                 '\n'
                 'It is a loop rather than a straight line because software is never truly finished. '
                 'Conditions change. Dependencies update. Users discover new needs. Security risks emerge. '
                 'Infrastructure fails. Teams learn. The quality of the loop determines how safely and '
                 'quickly the system can adapt.\n'
                 '\n'
                 'Speed is often associated with DevOps, but speed by itself is not the goal. A team that '
                 'deploys quickly and breaks production repeatedly is not succeeding. A team that moves '
                 'carefully but requires three months for a tiny safe change is also constrained. DevOps '
                 'aims for sustainable flow: small changes, fast feedback, reliable automation, clear '
                 'recovery, and shared learning.\n'
                 '\n'
                 'Small changes are easier to understand, test, review, deploy, and reverse. This is one '
                 'reason our development workflow for Ascend has improved as we moved away from replacing '
                 'entire project folders. A focused lesson file is safer than a giant content replacement. A '
                 'small commit provides a clear history. A backend-only rebuild limits the affected surface. '
                 'Test, commit, and continue is a DevOps-shaped workflow.\n'
                 '\n'
                 'Recovery is another essential connection. Every release process should answer not only '
                 '“How do we deploy?” but also “How do we recover?” Recovery may involve reverting a commit, '
                 'redeploying a previous image, restoring data, disabling a feature flag, or applying a '
                 'forward fix. Confidence grows when teams know that failure is detectable and recoverable.\n'
                 '\n'
                 'Blameless learning connects incidents to improvement. The purpose of a post-incident '
                 'review is not to find the person who made a mistake. It is to understand why the system '
                 'allowed the mistake to produce harm and how detection, process, tooling, documentation, or '
                 'design can improve.\n'
                 '\n'
                 'Your recent Ascend backend restart loop offers a simple example. Docker repeatedly '
                 'restarted the backend. The visible symptom existed in operations, but the cause was in '
                 'application content: main.py imported ACHIEVEMENTS, and the replacement content file did '
                 'not define it. The resolution required reading logs, understanding the Python import '
                 'boundary, restoring the expected contract, rebuilding, and verifying the service.\n'
                 '\n'
                 'That incident crossed development, packaging, deployment, runtime operation, and '
                 'troubleshooting. Calling it only a Docker problem or only a Python problem would miss the '
                 'system.\n'
                 '\n'
                 'Now consider the content-engine refactor you just completed. The motivation was '
                 'maintainability. You changed one giant content.py into a package with individual lesson '
                 'files. Git now shows focused changes. Future lessons can be added without modifying '
                 'unrelated content. The API contract remains the same because content/__init__.py still '
                 'exports MODULES and ACHIEVEMENTS. Docker rebuilds the backend. Ascend verifies that the '
                 'user experience is unchanged.\n'
                 '\n'
                 'That is DevOps thinking in practice: improve the internal system while preserving the '
                 'external outcome, make changes small and reviewable, automate the repeatable work, verify '
                 'with evidence, and keep a recovery path.\n'
                 '\n'
                 'DevOps also connects business goals to technical decisions. A pipeline is not valuable '
                 'because pipelines are fashionable. It is valuable because it helps deliver improvements '
                 'safely. Monitoring is not valuable because dashboards look professional. It is valuable '
                 'because it protects availability and reduces the time users are affected. Infrastructure '
                 'as Code is not valuable because configuration files are impressive. It is valuable because '
                 'environments become repeatable and changes become auditable.\n'
                 '\n'
                 'Always ask what outcome the tool supports.\n'
                 '\n'
                 'This protects you from tool-first learning. Kubernetes may be powerful, but a single home '
                 'server running two Compose applications may not need Kubernetes. A sophisticated CI/CD '
                 'platform may be unnecessary before basic tests and a reliable build exist. DevOps '
                 'engineers select practices and tools that improve the current system rather than adding '
                 'complexity for its own sake.\n'
                 '\n'
                 'Another misconception is that DevOps is a job title only. Organizations do hire DevOps '
                 'engineers, platform engineers, site reliability engineers, cloud engineers, and build '
                 'engineers. Their responsibilities differ. But DevOps is also a way of designing work. A '
                 'person can practice DevOps principles while writing application code, administering '
                 'Microsoft 365, supporting users, managing cloud infrastructure, or maintaining a home '
                 'lab.\n'
                 '\n'
                 'You are already practicing parts of it. You use Git to preserve changes. You package '
                 'applications with Docker. You describe multi-service environments with Compose. You host '
                 'applications on a server. You use Tailscale for secure access. You inspect logs when '
                 'containers fail. You test native iOS bundles. You collect feedback from real usage and '
                 'improve the applications.\n'
                 '\n'
                 'The purpose of Ascend is to make those experiences deliberate. You will learn the '
                 'vocabulary, tools, and deeper engineering practices behind what you are already building.\n'
                 '\n'
                 'Before we close, remember five connections.\n'
                 '\n'
                 'First, DevOps connects people. Shared goals and clear communication reduce destructive '
                 'handoffs.\n'
                 '\n'
                 'Second, DevOps connects code to running systems. Git, tests, builds, artifacts, '
                 'configuration, and deployments form a traceable path.\n'
                 '\n'
                 'Third, DevOps connects operations to development through observability and feedback. '
                 'Running behavior informs future design.\n'
                 '\n'
                 'Fourth, DevOps connects speed to safety. Small changes, automation, security, validation, '
                 'and recovery make frequent delivery sustainable.\n'
                 '\n'
                 'Fifth, DevOps connects technical work to human outcomes. The system succeeds when people '
                 'can reliably do what they need to do.\n'
                 '\n'
                 'In the next lesson, we will focus on three properties that make this loop effective: '
                 'reliability, automation, and feedback. You will learn why reliable systems are not systems '
                 'that never fail, why automation needs guardrails, and why feedback determines whether a '
                 'team learns faster than its problems grow.\n'
                 '\n'
                 'For now, carry this definition with you: DevOps is the practice of connecting people, '
                 'processes, and technology so useful changes can move from idea to operation safely, '
                 'repeatedly, and with fast learning.',
 'content': [{'heading': 'Learning objectives',
              'body': 'By the end of this lesson, you should be able to explain why DevOps exists; '
                      'distinguish DevOps principles from specific tools; trace a change from idea through '
                      'Git, testing, build, deployment, operation, and feedback; explain shared ownership, '
                      'CI/CD, Infrastructure as Code, observability, and recovery; and identify where Forge, '
                      'Ascend, your home server, and TruHearing workflows already demonstrate DevOps '
                      'practices.'},
             {'heading': 'DevOps is a connection system',
              'body': 'DevOps connects the complete path that turns an idea into a reliable user outcome. '
                      'That path includes planning, development, testing, security, infrastructure, '
                      'configuration, deployment, operations, support, and feedback. Tools enable the path, '
                      'but the path and its outcomes are the reason DevOps exists.'},
             {'heading': 'Why silos create friction',
              'body': 'Traditional handoffs can separate the people who build software from the people who '
                      'run and support it. Each group may optimize its local responsibility while delays, '
                      'misunderstandings, and late surprises accumulate between teams. DevOps improves the '
                      'interfaces between specialties and aligns them around the behavior of the complete '
                      'service.'},
             {'heading': 'Shared ownership does not erase specialties',
              'body': 'Developers, operations engineers, security specialists, database administrators, '
                      'testers, and support teams still contribute different expertise. Shared ownership '
                      "means that no group treats the final user outcome as somebody else's problem. The "
                      'team collectively cares whether the service can be changed, operated, recovered, and '
                      'improved.'},
             {'heading': 'The delivery loop',
              'body': 'A useful DevOps model is plan → build → test → release → deploy → operate → observe → '
                      'learn → plan. It is a loop because deployed software creates new evidence. '
                      'Monitoring, incidents, support requests, analytics, and user experience influence the '
                      'next decision.'},
             {'heading': 'Git connects change to history',
              'body': 'Git records what changed and creates checkpoints for collaboration and recovery. '
                      'Commits, branches, pull requests, reviews, and tags turn individual edits into a '
                      'traceable change history. Git is the beginning of a delivery path, not the entire '
                      'path.'},
             {'heading': 'Continuous integration creates fast feedback',
              'body': 'Continuous integration automatically validates small changes through repeatable '
                      'checks such as dependency installation, tests, formatting, static analysis, security '
                      'scanning, and builds. The value is early, consistent feedback while the change '
                      'remains easy to understand and repair.'},
             {'heading': 'Continuous delivery makes releases repeatable',
              'body': 'Continuous delivery connects validated code to a controlled release process. The same '
                      'tested artifact can move through environments using declared configuration and '
                      'automation. A human approval may still exist, but the mechanics should be dependable '
                      'and recorded.'},
             {'heading': 'Infrastructure and configuration are part of the product',
              'body': 'Applications depend on networks, ports, hosts, permissions, environment variables, '
                      'secrets, volumes, and external services. Infrastructure as Code and configuration '
                      'management make those dependencies reviewable and repeatable instead of relying on '
                      'undocumented clicks or memory.'},
             {'heading': 'Containers define a runtime contract',
              'body': 'A Docker image packages an application with its expected runtime and dependencies. '
                      'Docker Compose connects several services, networks, volumes, ports, and configuration '
                      'values. This reduces environmental drift and makes the operational shape of Ascend '
                      'and Forge visible in code.'},
             {'heading': 'Observability closes the loop',
              'body': 'Logs, metrics, traces, health checks, dashboards, and alerts reveal how the deployed '
                      'system behaves. A successful deployment command is not proof of a successful service. '
                      'Observability connects runtime evidence to developers and operators so they can '
                      'verify outcomes and learn from failures.'},
             {'heading': 'DevOps connects speed with safety',
              'body': 'The goal is not maximum deployment speed. The goal is sustainable flow: small '
                      'changes, automated validation, secure handling of secrets, repeatable deployment, '
                      'clear monitoring, and tested recovery. Frequent delivery becomes safe when failure is '
                      'limited, visible, and reversible.'},
             {'heading': 'Forge and Ascend are delivery systems',
              'body': 'A Forge or Ascend change moves from source code on your Mac into Git, frontend or '
                      'backend builds, Docker images, Compose services on the home server, Tailscale access, '
                      'and native iOS bundles. Each boundary can hold a different version. DevOps practices '
                      'make that path explicit and verifiable.'},
             {'heading': 'TruHearing feedback is operational evidence',
              'body': 'Employee reports, Microsoft 365 incidents, browser network errors, Graph API '
                      'behavior, and requests for portal improvements all feed the delivery loop. Good '
                      'evidence moves quickly from users and support teams to the people who can change the '
                      'system, while status and resolution information moves back.'},
             {'heading': 'Recovery is part of delivery',
              'body': 'A mature release process answers how to recover from a bad change. Reverting a '
                      'commit, redeploying a previous image, restoring data, disabling a feature, or '
                      'applying a controlled forward fix should be understood before an emergency. Recovery '
                      'confidence supports safer experimentation.'},
             {'heading': 'DevOps is not tool collecting',
              'body': 'A tool should solve a specific problem in the flow. Kubernetes, Terraform, Jenkins, '
                      'and cloud platforms can be valuable, but adding complexity without a need does not '
                      'make a system more DevOps. Start with the outcome, identify the constraint, and '
                      'choose the smallest practice or tool that improves it.'},
             {'heading': "Engineer's takeaway",
              'body': 'DevOps connects people, code, infrastructure, operations, feedback, and business '
                      'outcomes. It helps useful changes move from idea to operation safely, repeatedly, and '
                      'with fast learning.'}],
 'lab': {'title': 'Map the DevOps loop for Ascend',
         'instructions': ["Create a journal entry titled 'Lesson 0.5 - Ascend Delivery Loop.'",
                          'Choose one recent Ascend change, such as the content-engine refactor, a lesson '
                          'update, the workspace switcher, or the native iOS build.',
                          'Draw the complete path from the original need through planning, source changes, '
                          'Git, build, Docker deployment, iOS synchronization if relevant, verification, and '
                          'feedback.',
                          'At each step, identify the person, tool, artifact, and evidence involved. Include '
                          'source files, commits, images, containers, ports, URLs, logs, and user workflows '
                          'where applicable.',
                          'Mark every manual handoff. For each one, describe the risk of variation, '
                          'forgotten steps, stale versions, or missing evidence.',
                          'Identify at least five opportunities for automated validation or delivery. Do not '
                          'assume every opportunity should be implemented immediately; rank them by value '
                          'and effort.',
                          'Add a recovery path for a failed backend change and a separate recovery path for '
                          'a stale native iOS bundle.',
                          'Define three technical success signals and three user-outcome signals for the '
                          'deployment.',
                          'Write a short incident example showing how feedback from logs, Docker, the '
                          'browser, or your iPhone would travel back into a code or process improvement.',
                          'Finish by proposing the smallest next DevOps improvement for Ascend and explain '
                          'which constraint it addresses.']},
 'quiz': [{'question': 'Which description best captures DevOps?',
           'choices': ['A collection of cloud and container tools',
                       'A practice that connects people, processes, and technology to deliver and operate '
                       'useful changes reliably',
                       'A replacement for software development',
                       'A job limited to server administration'],
           'correct': 1},
          {'question': 'What is the primary problem with siloed handoffs?',
           'choices': ['Specialists learn too much about other roles',
                       'Each group can optimize locally while delays and failures grow between groups',
                       'Git cannot be used by multiple teams',
                       'Operations teams are unable to run applications'],
           'correct': 1},
          {'question': 'What does continuous integration primarily provide?',
           'choices': ['Automatic production access for every developer',
                       'Fast, repeatable validation of small code changes',
                       'A replacement for user testing',
                       'Permanent protection from defects'],
           'correct': 1},
          {'question': 'Why are small changes generally safer?',
           'choices': ['They require no review',
                       'They are easier to understand, test, deploy, and reverse',
                       'They never affect databases',
                       'They eliminate the need for monitoring'],
           'correct': 1},
          {'question': 'What is the strongest proof that an Ascend deployment succeeded?',
           'choices': ['The Docker build completed',
                       'The backend container is running',
                       'The intended lesson workflow works for the user and relevant signals are healthy',
                       'Git shows a clean working tree'],
           'correct': 2},
          {'question': 'What does observability connect?',
           'choices': ['Only frontend code to CSS',
                       'Running-system behavior back to the people responsible for understanding and '
                       'improving it',
                       'Docker images to Git branches automatically',
                       'User passwords to application logs'],
           'correct': 1},
          {'question': 'Why is recovery planning part of DevOps?',
           'choices': ['Every deployment must fail',
                       'Knowing how to detect and reverse harm makes change safer',
                       'Recovery replaces testing',
                       'Only operations teams need recovery procedures'],
           'correct': 1},
          {'question': 'Which statement about shared ownership is correct?',
           'choices': ['Everyone must perform the same job',
                       'Specialties disappear',
                       'Different specialists share responsibility for the complete service outcome',
                       'Developers become responsible only for infrastructure'],
           'correct': 2},
          {'question': 'Which is the best reason to adopt a DevOps tool?',
           'choices': ['It is popular',
                       'It appears in job descriptions',
                       'It addresses a known constraint in delivery, operation, security, or feedback',
                       'It makes the architecture more complicated'],
           'correct': 2},
          {'question': 'What did the Ascend content-engine refactor demonstrate?',
           'choices': ['Large files are always faster',
                       'Internal architecture can improve while the external API and user behavior remain '
                       'stable',
                       'Docker requires all Python content in one file',
                       'Refactoring removes the need for verification'],
           'correct': 1}],
 'diagram': {'title': 'The DevOps learning and delivery loop',
             'description': 'Useful software moves through a loop that connects intent, change, operation, '
                            'and learning.',
             'nodes': [{'label': 'Need and plan',
                        'detail': 'A user, business, reliability, or learning goal defines the desired '
                                  'outcome.'},
                       {'label': 'Build and collaborate',
                        'detail': 'Code, content, configuration, review, and Git turn the idea into a '
                                  'traceable change.'},
                       {'label': 'Validate',
                        'detail': 'Tests, checks, builds, and security controls provide fast evidence.'},
                       {'label': 'Release and deploy',
                        'detail': 'Artifacts, images, configuration, infrastructure, and approvals move the '
                                  'change into service.'},
                       {'label': 'Operate',
                        'detail': 'People and automation keep the service available, secure, and '
                                  'recoverable.'},
                       {'label': 'Observe and support',
                        'detail': 'Logs, metrics, traces, health checks, tickets, and user behavior reveal '
                                  'reality.'},
                       {'label': 'Learn and improve',
                        'detail': 'Feedback, incidents, and outcomes shape the next plan.'}],
             'caption': 'DevOps shortens and strengthens this loop. It does not end at deployment.'},
 'engineer_perspective': {'title': 'Optimize the whole path, not one team',
                          'body': 'A local improvement can damage the overall system. Developers can produce '
                                  'code faster than it can be reviewed. Operations can create a stable '
                                  'environment that is too difficult to change. Security can add a late gate '
                                  'that discovers problems only after expensive work is complete. DevOps '
                                  'looks at flow from idea to reliable user outcome and improves the '
                                  'constraint that limits the whole path.'},
 'try_it_yourself': {'title': 'Trace one commit into a running service',
                     'intro': 'Use the Ascend content-engine refactor to connect Git history with runtime '
                              'evidence.',
                     'steps': ['Run git log -3 --oneline and identify the commit that contains the refactor.',
                               'Run git show --stat <commit> and identify which files entered or left the '
                               'content package.',
                               'Run docker compose ps and record the running backend image and container.',
                               'Run docker compose logs backend --tail=30 and identify evidence that FastAPI '
                               'started successfully.',
                               'Open Lessons 0.1 and 0.4 and verify that the API contract still returns the '
                               'expected content.',
                               'Write down which evidence belongs to source control, build, deployment, '
                               'runtime health, and user outcome.'],
                     'takeaway': 'No single signal proves the entire delivery succeeded. Confidence comes '
                                 'from connected evidence across the path.'},
 'reflection': 'Explain DevOps in your own words without naming a specific tool. Then choose Forge, Ascend, '
               'or the TruHearing portal and describe how a change moves from idea to a real user outcome. '
               'Where are the manual handoffs, delayed feedback, stale-version risks, and recovery gaps? '
               'Identify one improvement that would shorten the feedback loop without adding unnecessary '
               'complexity.'}
