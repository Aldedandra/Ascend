export const WORKSHOP_SESSIONS = [
  {
    id: "2026-07-15-ecr",
    number: 1,
    date: "July 15, 2026",
    duration: "49 min",
    title: "From Local Docker Image to AWS ECR",
    summary:
      "Installed and configured the AWS CLI, created an ECR repository, authenticated Docker, and manually built, tagged, and pushed a container image.",
    status: "Complete",
    topics: ["AWS CLI", "IAM access keys", "Amazon ECR", "Docker", "CI/CD", "AWS regions"],
    relatedLessons: ["Module 4 — Docker and Containers", "Module 6 — AWS and Cloud Fundamentals"],
    overview: [
      {
        heading: "Session objective",
        body:
          "Move a container image from a local development machine into Amazon Elastic Container Registry (ECR), then connect those manual steps to the work performed by a CI/CD pipeline.",
      },
      {
        heading: "What happened",
        body:
          "The session began by confirming access to the AWS development account and installing the AWS CLI. After configuring command-line credentials and the default region, the group created an ECR repository, authenticated Docker to that registry, built the provided application image, applied an ECR-compatible tag, and pushed the image. The image then appeared in ECR and was ready to be consumed by a service such as ECS.",
      },
      {
        heading: "The central lesson",
        body:
          "A deployment pipeline is not magic. At a high level, it automates the same sequence performed manually in this workshop: authenticate, build, tag, and push. Understanding the manual workflow makes pipeline behavior easier to read and troubleshoot later.",
      },
    ],
    keyConcepts: [
      {
        term: "Amazon ECR",
        definition:
          "A managed AWS container registry that stores Docker and OCI container images. An ECS task can later pull a versioned image from ECR.",
      },
      {
        term: "AWS CLI",
        definition:
          "A command-line interface for AWS. It allows engineers and automation to perform work without relying exclusively on the AWS console.",
      },
      {
        term: "Image tag",
        definition:
          "A human-readable reference attached to an image. The workshop used a local image and added a new registry-qualified tag before pushing it.",
      },
      {
        term: "Registry authentication",
        definition:
          "Docker must receive a temporary login token before it can push to a private ECR repository.",
      },
      {
        term: "Region",
        definition:
          "An AWS geographic area. Resources and CLI commands must target the intended region. The discussion connected US West 2 with Oregon and US East 2 with Ohio.",
      },
      {
        term: "Availability Zone",
        definition:
          "An isolated data-center location inside a region. Multiple zones help systems avoid depending on one physical location.",
      },
      {
        term: "Hybrid environment",
        definition:
          "An architecture that connects on-premises systems and cloud resources. The session discussed private AWS access through site-to-site networking.",
      },
    ],
    commands: [
      {
        label: "Install AWS CLI on macOS",
        command: "brew install awscli",
        explanation:
          "Installs the AWS command-line client. Confirm installation with aws --version.",
      },
      {
        label: "Configure a CLI profile",
        command: "aws configure",
        explanation:
          "Prompts for an access key, secret key, default region, and output format. Never commit credentials to Git or paste them into notes.",
        warning: "Use approved credentials and follow your organization’s credential-handling policy.",
      },
      {
        label: "Verify the active AWS identity",
        command: "aws sts get-caller-identity",
        explanation:
          "A safe validation step that shows which AWS account and principal the CLI is using.",
      },
      {
        label: "Authenticate Docker to ECR",
        command:
          "aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com",
        explanation:
          "Requests a short-lived ECR token and passes it to Docker without placing the password directly in the command history.",
      },
      {
        label: "Build the local image",
        command: "docker build -t demo/test-image .",
        explanation:
          "Builds an image from the Dockerfile in the current directory and gives it a local name.",
      },
      {
        label: "List local images",
        command: "docker images",
        explanation:
          "Confirms that the build succeeded and helps verify the image name and tag before continuing.",
      },
      {
        label: "Add the ECR repository tag",
        command:
          "docker tag demo/test-image:latest <account-id>.dkr.ecr.<region>.amazonaws.com/<repository>:<tag>",
        explanation:
          "Creates another reference to the same image using the destination registry, repository, and chosen tag.",
      },
      {
        label: "Push the image",
        command:
          "docker push <account-id>.dkr.ecr.<region>.amazonaws.com/<repository>:<tag>",
        explanation:
          "Uploads the image layers to ECR. The tag must exactly match the tag created in the previous command.",
      },
    ],
    notes: [
      "ECR is where container images are stored; a running application still requires a compute service such as ECS.",
      "The build initially failed when the local Docker daemon was not running. The error was evidence about the local environment, not an AWS failure.",
      "Colima can provide a lightweight Docker-compatible runtime on macOS, but Docker Desktop was already available.",
      "The image repository incurs storage cost, although a very small test image has negligible cost.",
      "Route 53 was introduced as the DNS layer that can eventually help users reach a deployed application.",
      "Any application can follow this pattern as long as its Dockerfile correctly builds and starts the application.",
    ],
    lab: {
      title: "Repeat the container registry workflow safely",
      objective:
        "Demonstrate that you understand the relationship between a local image, an ECR tag, and the remote registry without exposing credentials.",
      prerequisites: [
        "Docker Desktop or another working Docker daemon",
        "AWS CLI installed",
        "Approved AWS development access",
        "An ECR repository you are authorized to use",
      ],
      steps: [
        "Run aws --version and docker version. Record whether both tools are available.",
        "Run aws sts get-caller-identity and confirm the expected account before making changes.",
        "Choose a small test project with a working Dockerfile. Build it with a descriptive local image name.",
        "Run docker images and record the image ID, repository name, tag, and size.",
        "Open the target ECR repository and use its push-command guidance, replacing values only where appropriate.",
        "Authenticate Docker to ECR using get-login-password and password-stdin.",
        "Tag the local image with the full ECR repository URI and a meaningful non-secret tag.",
        "Push the tagged image and verify that it appears in ECR.",
        "Explain in your own words which of these steps a CI/CD pipeline would automate.",
        "Remove only the local test tag if cleanup is appropriate. Do not delete shared cloud resources without approval.",
      ],
      evidence: [
        "Output from aws sts get-caller-identity with sensitive identifiers redacted",
        "The local docker images entry",
        "The image and tag visible in ECR",
        "A short workflow diagram: source → build → tag → push → registry",
      ],
    },
    reviewQuestions: [
      "Why must a local image be given a registry-qualified tag before it is pushed?",
      "What does ECR store, and what does it not do by itself?",
      "Why is aws sts get-caller-identity useful before running cloud commands?",
      "Which manual steps from this session would normally occur inside a pipeline?",
      "What evidence would distinguish an ECR authentication problem from a stopped Docker daemon?",
    ],
    questionsForTravis: [
      "How does our production pipeline choose image tags: commit SHA, release version, latest, or a combination?",
      "Which IAM permissions does the pipeline receive to push into ECR?",
      "How are old ECR images cleaned up and how long are they retained?",
      "What security scanning happens before an image is allowed to deploy?",
      "Where can I view one of our real GitLab build-and-push jobs?",
    ],
    actionItems: [
      "Practice the build, tag, and push sequence using a disposable development repository.",
      "Document the difference between a local Docker image, an ECR image, and a running ECS task.",
      "Review the GitLab pipeline for one containerized TruHearing application and identify the equivalent steps.",
      "Never store AWS access keys in Ascend, Git, screenshots, or workshop notes.",
    ],
    handbookEntries: [
      {
        title: "Container image delivery path",
        category: "Containers",
        summary: "Source code → Docker build → local image → registry tag → ECR push → ECS pull.",
      },
      {
        title: "ECR authentication pattern",
        category: "AWS",
        summary: "Use aws ecr get-login-password and Docker password-stdin for a temporary registry login.",
      },
      {
        title: "Docker daemon troubleshooting",
        category: "Troubleshooting",
        summary: "If docker build cannot connect to the daemon, verify the local runtime before investigating AWS.",
      },
    ],
  },
  {
    id: "2026-07-29-ecs",
    number: 2,
    date: "July 29, 2026",
    duration: "48 min",
    title: "Running an ECR Image with Amazon ECS",
    summary:
      "Created the ECS foundation for running an ECR image in the cloud, explored Fargate, task definitions, services, roles, tags, Linux fundamentals, and Terraform.",
    status: "Complete",
    topics: ["Amazon ECS", "AWS Fargate", "Task definitions", "IAM roles", "Resource tags", "Linux", "Terraform"],
    relatedLessons: ["Module 2 — Linux and the Command Line", "Module 6 — AWS and Cloud Fundamentals", "Module 7 — Infrastructure as Code"],
    overview: [
      {
        heading: "Session objective",
        body:
          "Take the image previously pushed to ECR and begin defining the AWS resources required to run it continuously in Amazon ECS.",
      },
      {
        heading: "What happened",
        body:
          "The session reviewed Linux skills and infrastructure-as-code learning before moving into ECS. The group created an ECS cluster, discussed Fargate, ECS Exec, encryption, and resource tags, then started building a task definition and service around the ECR image. The exercise exposed an important dependency: cloud workloads need correctly configured IAM roles and networking, not merely an image URI.",
      },
      {
        heading: "The central lesson",
        body:
          "ECR stores the deployable package; ECS describes and operates the running workload. A task definition tells ECS what to run, and a service tells ECS how many tasks to keep running and how to replace them.",
      },
    ],
    keyConcepts: [
      {
        term: "ECS cluster",
        definition:
          "A logical boundary where ECS services and tasks run. With Fargate, AWS manages the underlying compute rather than requiring you to manage EC2 container hosts.",
      },
      {
        term: "Task definition",
        definition:
          "A versioned blueprint for a workload: image URI, CPU, memory, container command, ports, environment variables, logging, and IAM roles.",
      },
      {
        term: "ECS service",
        definition:
          "Maintains a desired number of task instances and replaces failed tasks. It turns a task definition into a continuously managed application.",
      },
      {
        term: "AWS Fargate",
        definition:
          "A serverless compute option for containers. You define workload resources while AWS manages the host infrastructure.",
      },
      {
        term: "Task execution role",
        definition:
          "An IAM role used by ECS infrastructure for actions such as pulling an image from ECR and sending logs.",
      },
      {
        term: "Task role",
        definition:
          "An IAM role assumed by the application inside the container when it needs to call AWS services.",
      },
      {
        term: "ECS Exec",
        definition:
          "A capability for executing commands inside a running ECS container for approved operational and troubleshooting work.",
      },
      {
        term: "Resource tags",
        definition:
          "Key-value metadata used for organization, ownership, automation, and cost reporting. Consistent spelling matters.",
      },
      {
        term: "Terraform",
        definition:
          "Infrastructure as code that describes cloud resources declaratively, making environments repeatable and reviewable.",
      },
      {
        term: "Linux disk and inode checks",
        definition:
          "df -h reports filesystem capacity while df -i reports inode usage. A system can run out of file metadata entries even when storage capacity remains.",
      },
    ],
    commands: [
      {
        label: "Check filesystem capacity",
        command: "df -h",
        explanation:
          "Shows disk usage in human-readable units. Useful when a Linux host or container cannot write new data.",
      },
      {
        label: "Check inode usage",
        command: "df -i",
        explanation:
          "Shows inode consumption. A machine can have free bytes but still be unable to create files when inodes are exhausted.",
      },
      {
        label: "Inspect the ECR image URI",
        command:
          "aws ecr describe-images --repository-name <repository> --region <region>",
        explanation:
          "Lists image metadata. The ECS task definition uses the repository URI and chosen tag or digest.",
      },
      {
        label: "Describe ECS clusters",
        command: "aws ecs list-clusters --region <region>",
        explanation:
          "Lists cluster ARNs in the selected region and reinforces that AWS CLI operations are regional.",
      },
      {
        label: "Describe task definitions",
        command: "aws ecs list-task-definitions --region <region>",
        explanation:
          "Lists registered task-definition revisions that can be selected by an ECS service.",
      },
    ],
    notes: [
      "The workshop used the Ohio region already selected in the AWS console; resources must be created and inspected in the intended region.",
      "A VPC and subnet strategy is part of deploying a task. A cluster alone does not make the application reachable.",
      "Fargate removes host management, but you still define CPU, memory, ports, roles, networking, and application configuration.",
      "The task definition connects the ECR image to ECS and describes how the container should run.",
      "The service is responsible for keeping the requested number of task instances alive.",
      "A missing or incorrect IAM role can prevent ECS from pulling images or completing deployment.",
      "The Environment tag was emphasized because tagging supports later cost reporting and organization.",
      "Terraform was highlighted as an important DevOps skill because it can recreate this configuration from reviewed code.",
    ],
    lab: {
      title: "Design an ECS deployment before creating it",
      objective:
        "Create a deployment plan that clearly separates registry, task definition, service, networking, and IAM responsibilities.",
      prerequisites: [
        "An ECR image URI and tag",
        "A target AWS region",
        "A development VPC and subnet plan",
        "Approved IAM roles or a request path for creating them",
      ],
      steps: [
        "Draw the intended flow: user or client → networking entry point → ECS service → Fargate task → container image from ECR.",
        "Create a task-definition worksheet containing image URI, container name, CPU, memory, port, environment variables, secrets, logs, task execution role, and task role.",
        "Explain which values are application configuration and which are infrastructure configuration.",
        "Create a service worksheet containing cluster, task-definition revision, desired count, subnets, security groups, public-IP decision, health-check strategy, and deployment behavior.",
        "List the IAM actions needed for ECS to pull the image and publish logs. Do not invent production permissions; identify what needs approval.",
        "Add a tagging plan with Environment, Application, Owner, and Purpose.",
        "Identify at least six failure points and the evidence you would inspect for each.",
        "Describe how Terraform could represent the cluster, task definition, service, roles, networking, and tags.",
        "Write a two-sentence explanation of why the application continues running after the developer laptop is turned off.",
      ],
      evidence: [
        "Architecture diagram",
        "Task-definition worksheet",
        "Service and networking worksheet",
        "Failure-point table",
        "Terraform resource outline",
      ],
    },
    reviewQuestions: [
      "What is the difference between an ECR repository, an ECS task definition, and an ECS service?",
      "Why can an ECS deployment fail even when the image exists in ECR?",
      "What is the difference between a task role and a task execution role?",
      "What responsibility does Fargate remove, and what responsibilities remain?",
      "Why are consistent resource tags operationally important?",
      "What different problems do df -h and df -i identify?",
    ],
    questionsForTravis: [
      "Which networking pattern does our team normally use for ECS services: public subnets, private subnets with a load balancer, or another design?",
      "Can we walk through a real task execution role and task role and compare their permissions?",
      "How does our team inject secrets and environment variables into task definitions?",
      "What logging and health-check configuration is standard for our ECS services?",
      "Where is Terraform stored for an existing ECS application, and how does it reach each environment?",
      "When would our team choose ECS/Fargate instead of Kubernetes?",
    ],
    actionItems: [
      "Practice Linux navigation and resource checks, including df -h and df -i.",
      "Review one existing ECS task definition and identify image, ports, roles, resources, logs, and environment variables.",
      "Create a simple Terraform study plan focused on providers, resources, variables, state, plan, and apply.",
      "Document the relationship: ECR image → task definition → ECS service → running Fargate task.",
    ],
    handbookEntries: [
      {
        title: "ECS deployment building blocks",
        category: "AWS",
        summary: "ECR stores the image; the task definition describes it; the service keeps tasks running.",
      },
      {
        title: "Task role vs execution role",
        category: "IAM",
        summary: "Execution role supports ECS platform actions; task role grants the application AWS access.",
      },
      {
        title: "Linux disk troubleshooting",
        category: "Linux",
        summary: "Use df -h for capacity and df -i for inode exhaustion.",
      },
      {
        title: "Resource tagging",
        category: "Cloud operations",
        summary: "Consistent tags improve ownership, search, automation, and cost allocation.",
      },
    ],
  },
  {
    id: "2026-08-05-ecs-security-storage",
    number: 3,
    date: "August 5, 2026",
    duration: "34 min",
    title: "ECS Security, Volumes, and Persistent Storage",
    summary:
      "Followed a real AWS security finding through ECS task definitions, read-only root filesystems, ephemeral volumes, and EFS-backed persistent storage.",
    status: "Complete",
    topics: ["Amazon ECS", "AWS Config", "DevSecOps", "EFS", "Ephemeral volumes", "Task definitions", "CloudWatch"],
    relatedLessons: ["Module 4 — Docker and Containers", "Module 6 — AWS and Cloud Fundamentals", "Module 7 — Infrastructure as Code"],
    overview: [
      {
        heading: "Session objective",
        body:
          "Use a real security task from the DevOps queue to understand how container security controls, writable storage, and ECS task definitions fit together in a production environment.",
      },
      {
        heading: "What happened",
        body:
          "Travis opened an AWS security finding showing ECS task definitions that were not compliant with a read-only root-filesystem control. He traced the finding through AWS Config, entered running ECS containers, and explained how writable paths must be deliberately provided through volumes when the root filesystem is locked down.",
      },
      {
        heading: "The central lesson",
        body:
          "Containers should be treated as replaceable runtime environments. Persistent business data belongs outside the container, while temporary writable paths should be narrowly scoped. Security improves when a workload can write only where it genuinely needs to.",
      },
    ],
    keyConcepts: [
      {
        term: "AWS Config",
        definition:
          "An AWS service used here to evaluate resources against configuration and compliance rules and surface findings that the DevOps team reviews.",
      },
      {
        term: "DevSecOps",
        definition:
          "Security work integrated into development and operations. Travis explained that the DevOps team handles this work because there is not a separate DevSecOps function for these findings.",
      },
      {
        term: "Read-only root filesystem",
        definition:
          "An ECS container setting that prevents writes to the container root filesystem. Required writable locations are then explicitly mounted instead of leaving the entire filesystem writable.",
      },
      {
        term: "Ephemeral volume",
        definition:
          "Temporary writable storage associated with the life of an ECS task. It can support paths needed while the task runs, but it should not be treated as durable business storage.",
      },
      {
        term: "Amazon EFS",
        definition:
          "Persistent shared file storage that multiple ECS tasks can attach to. The workshop used it to explain data that must remain available even when containers stop and restart.",
      },
      {
        term: "Task definition",
        definition:
          "The ECS configuration that describes containers and runtime settings such as environment variables, secrets references, volumes, and filesystem behavior.",
      },
      {
        term: "CloudWatch agent",
        definition:
          "A component that needs specific writable directories so it can collect and send logs while the rest of the container root filesystem remains read-only.",
      },
    ],
    commands: [
      {
        label: "Read-only root filesystem setting",
        command: '"readonlyRootFilesystem": true',
        explanation:
          "The ECS container-definition setting highlighted by the security control. Writable locations must then be explicitly provided where required.",
      },
      {
        label: "Inspect a mounted path",
        command: "cd /var/www/echo/shared",
        explanation:
          "The workshop navigated into an EFS-backed shared directory to illustrate storage that survives container replacement.",
      },
      {
        label: "Temporary writable path example",
        command: "/tmp",
        explanation:
          "A temporary path can be backed by an ephemeral volume when an application needs scratch space but the root filesystem should stay read-only.",
      },
    ],
    notes: [
      "The DevOps team reviews recurring AWS security findings and prioritizes higher-impact issues rather than treating cloud security as a one-time setup task.",
      "A read-only root filesystem reduces the places an attacker could write scripts or modify files if a container were compromised.",
      "Writable exceptions should be deliberate and container-specific rather than granting write access everywhere.",
      "Ephemeral storage disappears with the task; EFS is used when data must survive task replacement or be shared by multiple tasks.",
      "Separating Sidekick and Clockwork into ECS services preserved independent scaling while shared storage reproduced behavior they previously had on one machine.",
      "Secrets in the task definition point to a secure store rather than being placed directly into plain-text configuration.",
    ],
    lab: {
      title: "Classify container storage by lifetime and purpose",
      objective:
        "Practice deciding what should remain immutable, what may be written temporarily, and what must persist independently of a container.",
      prerequisites: [
        "A containerized test application or architecture diagram",
        "Basic understanding of Docker containers and ECS tasks",
        "No production changes are required",
      ],
      steps: [
        "Choose one containerized application and list every path or category of data it may write.",
        "Classify each write as temporary, log/agent-related, or persistent business data.",
        "Mark the container root filesystem read-only in your design and identify only the paths that genuinely require write access.",
        "Assign temporary paths to ephemeral storage and persistent/shared paths to a durable storage service such as EFS where appropriate.",
        "Draw the lifecycle for a task replacement and show which data disappears and which data remains.",
        "Explain how the design reduces the impact of a compromised container.",
        "Write three checks you would perform if the application failed after enabling a read-only root filesystem.",
      ],
      evidence: [
        "Storage classification table",
        "Container → volume → persistent-storage diagram",
        "A short explanation of why container filesystems should not be the source of truth for durable data",
        "Three troubleshooting checks",
      ],
    },
    reviewQuestions: [
      "Why does a read-only root filesystem improve container security?",
      "What is the practical difference between an ephemeral volume and EFS?",
      "Why might two separate ECS services still need shared storage?",
      "What does an ECS task definition control?",
      "If a container is replaced, which kinds of data should be expected to survive?",
    ],
    questionsForTravis: [
      "Are our ECS task definitions generated from Terraform, application repositories, or both?",
      "How do we test a read-only root-filesystem change before promoting it to production?",
      "What other AWS Config findings tend to create the most valuable DevOps security projects?",
      "How do we decide between EFS, EBS, S3, or a database for persistent application data?",
      "Can we walk through how secrets referenced by an ECS task definition are stored and injected?",
    ],
    actionItems: [
      "Review the difference between container-local, ephemeral, and persistent storage.",
      "Identify one application you run locally and decide which of its files should survive container replacement.",
      "Practice reading a simple ECS task-definition JSON document and locate volumes, mounts, environment variables, and secrets references.",
      "Add read-only-root-filesystem security to the container-hardening study notes in Ascend.",
    ],
    handbookEntries: [
      {
        title: "Container storage lifetime",
        category: "Containers",
        summary: "Container filesystem = replaceable; ephemeral volume = task lifetime; EFS = durable shared storage.",
      },
      {
        title: "Read-only root filesystem",
        category: "Security",
        summary: "Lock the root filesystem and explicitly mount only the paths that truly require write access.",
      },
      {
        title: "ECS task definition",
        category: "AWS",
        summary: "Describes how ECS should run containers, including images, configuration, secrets references, volumes, and security settings.",
      },
    ],
  },
  {
    id: "2026-08-13-lambda-eventbridge",
    number: 4,
    date: "August 13, 2026",
    duration: "29 min",
    title: "AWS Lambda, EventBridge, and Serverless Automation",
    summary:
      "Explored Lambda hands-on, traced a scheduled EventBridge trigger into a Python cost-saving function, reviewed CloudWatch monitoring, and connected serverless automation to regions, permissions, configuration, and reusable code.",
    status: "Complete",
    topics: ["AWS Lambda", "EventBridge", "Serverless", "Cron", "CloudWatch", "IAM", "Environment variables", "AWS regions"],
    relatedLessons: ["Module 3 — Networking and Web Fundamentals", "Module 6 — AWS and Cloud Fundamentals", "Module 7 — Infrastructure as Code"],
    overview: [
      {
        heading: "Session objective",
        body:
          "Understand what AWS Lambda is, create or inspect a function in the AWS console, and follow a real automation from its EventBridge schedule through Python execution and CloudWatch observability.",
      },
      {
        heading: "What happened",
        body:
          "You shared your screen and navigated Lambda in the AWS development account. After reviewing function creation and runtimes, the group inspected an existing cost-saver function that automatically stops and starts development resources. The session followed its EventBridge schedule, Python code, exclusion tags, monitoring metrics, CloudWatch logs, timeout settings, and environment variables.",
      },
      {
        heading: "The central lesson",
        body:
          "Serverless automation is event-driven code. Instead of keeping a server or container running continuously, Lambda starts when an event invokes it, performs a focused job, records what happened, and then stops. The trigger, permissions, configuration, and logs are just as important as the code itself.",
      },
    ],
    keyConcepts: [
      {
        term: "AWS Lambda",
        definition:
          "Serverless compute for running focused code in response to an invocation. AWS supplies the runtime environment so a dedicated EC2 instance or continuously running container is not required for the function itself.",
      },
      {
        term: "Event payload",
        definition:
          "Data passed into a Lambda invocation. The function can inspect keys and values in the event and choose behavior based on what it receives.",
      },
      {
        term: "Amazon EventBridge",
        definition:
          "The event and scheduling layer shown in the workshop. Events or schedules can invoke a Lambda when a defined condition occurs.",
      },
      {
        term: "Cron schedule",
        definition:
          "A time-based expression used by the demonstrated EventBridge rules to determine when the cost-saving Lambda should run.",
      },
      {
        term: "Region-bound resource",
        definition:
          "Lambda functions are scoped to an AWS region. Switching from Northern Virginia to Oregon exposed a different set of functions in the console.",
      },
      {
        term: "CloudWatch logs and monitoring",
        definition:
          "Lambda metrics show invocations and duration, while CloudWatch logs preserve application output that engineers can inspect after a run or failure.",
      },
      {
        term: "Environment variable",
        definition:
          "Configuration supplied separately from code so the same function can target different environments or resources without changing the implementation.",
      },
      {
        term: "Timeout",
        definition:
          "The maximum amount of time a Lambda invocation may run before AWS stops it. Travis emphasized shorter values for request-driven work and longer values only when the job actually needs them.",
      },
    ],
    commands: [
      {
        label: "Read a Lambda environment variable in Python",
        command: 'os.getenv("<VARIABLE_NAME>")',
        explanation:
          "The pattern discussed for reading configuration from the Lambda environment instead of hard-coding environment-specific values.",
        warning: "Do not use plain environment variables as a place to store secrets unless your organization explicitly provides a secure pattern for doing so.",
      },
      {
        label: "Event payload shape",
        command: '{ "key": "value" }',
        explanation:
          "The Lambda test view can provide JSON input to a function. The function may read keys from that event and branch based on the received data.",
      },
      {
        label: "Scheduled invocation pattern",
        command: "EventBridge schedule → Lambda → AWS resources → CloudWatch",
        explanation:
          "The cost-saver workflow demonstrated in the session: a schedule invokes code, the code changes resource state, and logs/metrics provide evidence of the run.",
      },
    ],
    notes: [
      "Lambda was introduced as a good fit for focused tasks that run on demand or on a schedule rather than requiring an always-on server or container.",
      "The console showed that Lambda functions are region-bound; the same AWS account can display different functions when the selected region changes.",
      "The cost-saver automation uses EventBridge schedules to invoke Python that stops development resources after hours and starts them again before developers return.",
      "An exclusion tag allows selected ECS resources to stay running instead of being stopped by the automation.",
      "The start workflow restores the prior ECS task count using saved parameters so environments return to their previous state.",
      "CloudWatch logs were emphasized as essential evidence for understanding what a previous invocation actually did.",
      "IAM permissions affected what could be created or viewed during the hands-on walkthrough, reinforcing that access is part of cloud architecture and troubleshooting.",
      "Environment variables make code reusable across environments, but Travis explicitly warned against putting secrets directly into ordinary environment variables.",
      "The session ended with a preview of a higher-volume Lambda/Kinesis workflow that continuously processes CloudWatch/RDS data and sends it to Splunk; Travis plans to explain it in a future workshop.",
    ],
    lab: {
      title: "Design a safe scheduled Lambda automation",
      objective:
        "Model the trigger → function → resource → logs workflow from the workshop without making destructive changes to company AWS resources.",
      prerequisites: [
        "Basic Python familiarity",
        "Understanding of AWS regions and IAM permissions",
        "A local editor; AWS development read access is optional",
      ],
      steps: [
        "Draw the cost-saver flow demonstrated in the workshop: EventBridge schedule → Lambda → resource decision → CloudWatch logs.",
        "Write a local Python function that receives a small JSON-like event and prints which action it would take. Do not make AWS API calls yet.",
        "Add an EXCLUDED flag or tag value to the sample input and make the function skip that resource when the exclusion is present.",
        "Move one non-secret value, such as ENVIRONMENT, out of the code and read it with os.getenv().",
        "Add useful log output for start, decision, skipped resource, successful action, and error paths.",
        "Choose a hypothetical EventBridge schedule and describe it in plain English. You do not need to create the rule in AWS.",
        "Explain what IAM permissions the real function would require and why least privilege matters.",
        "Describe how you would verify a successful run using Lambda Monitor and CloudWatch logs.",
        "Explain when this workload is a better fit for Lambda than for an always-running ECS service.",
      ],
      evidence: [
        "Trigger-to-observability architecture diagram",
        "Local Python function or pseudocode",
        "Example input event and expected output",
        "A short IAM/least-privilege explanation",
        "Lambda-vs-ECS decision explanation",
      ],
    },
    reviewQuestions: [
      "What makes Lambda serverless from the application team's point of view?",
      "What invokes the cost-saver Lambda demonstrated in the workshop?",
      "Why did changing AWS regions change the Lambda functions visible in the console?",
      "What is the difference between a trigger, an event payload, and the Lambda code itself?",
      "Why are CloudWatch logs important even when a Lambda normally runs successfully?",
      "How do environment variables make a function more reusable?",
      "Why might an ECS service be excluded from the automatic stop/start workflow?",
    ],
    questionsForTravis: [
      "Can we walk through how our Lambda IAM execution roles are built and how permissions are kept least-privilege?",
      "Where are secrets stored for Lambda if ordinary environment variables should not contain them?",
      "Are our EventBridge schedules and Lambda functions managed through Terraform, GitLab pipelines, or directly in AWS?",
      "How does the cost-saver function persist and restore the previous ECS desired task count?",
      "What alarms do we use for Lambda failures, throttling, or unexpected duration increases?",
      "When does our team choose Lambda instead of ECS/Fargate for new backend or automation work?",
      "Can we continue with the Kinesis Data Streams and Splunk Lambda example you previewed at the end of this session?",
    ],
    actionItems: [
      "Practice reading and writing small Python functions that accept an event payload.",
      "Review EventBridge scheduling and learn how cron expressions map to human-readable schedules.",
      "Review one non-destructive Lambda in the development account and identify its trigger, runtime, timeout, environment variables, IAM role, metrics, and logs.",
      "Add Lambda vs ECS to the Ascend handbook as a workload-selection comparison.",
      "Prepare questions about the Kinesis/Splunk example for the next session.",
    ],
    handbookEntries: [
      {
        title: "Serverless automation loop",
        category: "AWS",
        summary: "Event or schedule → Lambda invocation → focused action → CloudWatch evidence.",
      },
      {
        title: "Lambda configuration vs code",
        category: "Automation",
        summary: "Keep reusable logic in code and environment-specific non-secret values in configuration rather than hard-coding them.",
      },
      {
        title: "Lambda observability",
        category: "Monitoring",
        summary: "Use invocation/duration metrics plus CloudWatch logs to prove what ran, when it ran, and what happened.",
      },
      {
        title: "AWS resources are regional",
        category: "Cloud fundamentals",
        summary: "Always verify the selected AWS region before assuming a resource is missing or before making changes.",
      },
    ],
  },
];

export const WORKSHOP_LABS = WORKSHOP_SESSIONS.map((session) => ({
  id: session.id,
  sessionNumber: session.number,
  sessionTitle: session.title,
  ...session.lab,
}));

export const WORKSHOP_QUESTIONS = WORKSHOP_SESSIONS.flatMap((session) =>
  session.questionsForTravis.map((question, index) => ({
    id: `${session.id}-question-${index + 1}`,
    sessionId: session.id,
    sessionNumber: session.number,
    sessionTitle: session.title,
    question,
  }))
);

export const WORKSHOP_HANDBOOK = WORKSHOP_SESSIONS.flatMap((session) =>
  session.handbookEntries.map((entry, index) => ({
    id: `${session.id}-handbook-${index + 1}`,
    sessionId: session.id,
    sessionNumber: session.number,
    sessionTitle: session.title,
    ...entry,
  }))
);

export function getWorkshopSession(sessionId) {
  return WORKSHOP_SESSIONS.find((session) => session.id === sessionId);
}
