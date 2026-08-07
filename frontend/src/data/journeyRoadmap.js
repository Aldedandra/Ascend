export const journeyRoadmap = [
  {
    id: "linux",
    number: 1,
    title: "Operating System",
    focus: "Linux",
    moduleId: "module-2",
    description:
      "Navigate Linux confidently, inspect processes, permissions, filesystems, services, logs, disk usage, and SSH.",
    outcome: "Troubleshoot a Linux host without being afraid of the terminal.",
  },
  {
    id: "software-design",
    number: 2,
    title: "Software Design",
    focus: "Systems thinking & application architecture",
    description:
      "Understand how applications are shaped, how responsibilities are separated, and how engineers reduce uncertainty before changing a system.",
    outcome: "See an application as connected systems instead of one giant black box.",
  },
  {
    id: "programming",
    number: 3,
    title: "Programming",
    focus: "Bash / Python / Ruby concepts",
    description:
      "Build enough programming fluency to automate repetitive work, read application code, and troubleshoot delivery systems.",
    outcome: "Write small automation and confidently follow code you did not author.",
  },
  {
    id: "source-control",
    number: 4,
    title: "Source Code Management",
    focus: "Git",
    moduleId: "module-1",
    description:
      "Use repositories, commits, branches, merges, pull requests, tags, and recovery workflows safely.",
    outcome: "Treat Git as the history and collaboration layer behind every change.",
  },
  {
    id: "containerization",
    number: 5,
    title: "Containerization",
    focus: "Docker / containerd",
    moduleId: "module-4",
    description:
      "Package applications into repeatable images and run them as isolated, disposable containers.",
    outcome: "Build, inspect, run, troubleshoot, tag, and publish container images.",
  },
  {
    id: "orchestration",
    number: 6,
    title: "Orchestration",
    focus: "Kubernetes / ECS concepts",
    description:
      "Learn how containers are scheduled, scaled, networked, recovered, and operated together.",
    outcome: "Understand the control plane that keeps many containers healthy.",
  },
  {
    id: "cicd",
    number: 7,
    title: "CI/CD",
    focus: "Pipelines & automated delivery",
    moduleId: "module-5",
    description:
      "Automatically test, build, package, release, and deploy changes through repeatable pipelines.",
    outcome: "Follow a change from commit to a safe production deployment.",
  },
  {
    id: "configuration",
    number: 8,
    title: "Configuration Management",
    focus: "Ansible / Chef concepts",
    description:
      "Keep systems consistent through declared, repeatable configuration instead of manual server changes.",
    outcome: "Recognize configuration drift and replace one-off fixes with repeatable automation.",
  },
  {
    id: "cloud",
    number: 9,
    title: "Cloud",
    focus: "AWS",
    moduleId: "module-6",
    description:
      "Understand identity, compute, networking, storage, observability, containers, and deployment architecture in AWS.",
    outcome: "Reason about where an application runs and which cloud services support it.",
  },
  {
    id: "iac",
    number: 10,
    title: "Infrastructure as Code",
    focus: "Terraform / Pulumi",
    moduleId: "module-7",
    description:
      "Define infrastructure as version-controlled code so environments are reproducible, reviewable, and recoverable.",
    outcome: "Create infrastructure by changing reviewed code instead of clicking through consoles.",
  },
  {
    id: "observability",
    number: 11,
    title: "Observability & Monitoring",
    focus: "Metrics / logs / alerts",
    moduleId: "module-8",
    description:
      "Know what production is doing through health checks, metrics, logs, dashboards, alerts, and incident learning.",
    outcome: "Use evidence from production to detect, explain, and recover from problems.",
  },
];

export const ascendExtensions = [
  {
    id: "security",
    title: "Security & Secrets",
    moduleId: "module-9",
    description:
      "Apply least privilege, secure secret handling, vulnerability awareness, and safe delivery practices throughout the climb.",
  },
  {
    id: "capstone",
    title: "Capstone Deployment",
    moduleId: "module-10",
    description:
      "Bring the full path together by deploying, monitoring, documenting, breaking, and recovering a production-style application.",
  },
];
