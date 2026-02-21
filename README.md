🦞 OpenClaw: The Ultimate Setup & Management Guide (Arch Linux)

This guide documents the exact process used to set up AI agent on Arch Linux using Docker. It includes definitions, architecture logic, and management workflows for daily development.

🌟 What is OpenClaw?

OpenClaw is an open-source, autonomous AI agent gateway. It acts as a bridge between powerful AI models (like GitHub Copilot, Gemini, or Claude) and your local system. Unlike a standard chatbot, OpenClaw has "hands"—it can read your files, execute terminal commands, and manage your projects autonomously via messaging apps like Telegram.

Why Docker for Isolation?

On an Arch Linux system, "Isolation" is your primary security layer.

Protection: AI can occasionally "hallucinate" or make mistakes. By running in Docker, the AI is inside a "digital jail." Even if it tries to run a destructive command, it can only affect the files inside the container, not your entire operating system.

Clean System: It keeps your host OS clean. You don't need to install hundreds of Python or Node.js dependencies on your main machine; everything stays inside the container.

Consistency: Docker ensures the AI has the exact environment it needs to function, regardless of your Arch updates.

🏗️ Phase 1: The Installation Journey

followed the Manual Onboarding path to ensure total control.

The Core Command: ./docker-setup.sh

Definition: * ./: A Linux shell instruction meaning "look in the current directory."

docker-setup.sh: The master script that builds the OpenClaw images locally on your machine.

The Process: You selected Manual mode, connected GitHub Copilot via a device code, and provided a Telegram Bot Token from @BotFather.

🐳 Phase 2: Word-Wise Docker Definitions

These are the fundamental commands used to manage the AI "Engine."

1. docker compose up -d

docker: The platform that runs software in containers.

compose: A tool to manage multiple containers (Gateway + Database) at once.

up: Create and start the entire AI system.

-d (Detached): Run in the "background." This allows you to close your terminal while the AI stays active and ready to receive Telegram messages.

2. docker compose logs -f

logs: The history of everything the AI is thinking or doing.

-f (Follow): This "sticks" the terminal to the output so you can watch live as the AI processes your requests.

🛠️ Phase 3: Essential Management Commands

Use these commands daily to maintain your agent.

🔄 How to Restart

If the bot stops responding or you change a configuration:

docker compose restart openclaw-gateway


Definition: Stops the gateway process and starts it again without losing your data.

🛑 How to Stop

To completely turn off the AI when you aren't using it:

docker compose stop


Definition: Pauses the containers. They remain on your disk but stop consuming CPU/RAM.

🧩 How to Add New Skills

Skills are the "tools" the AI uses (like GitHub, Email, or File search).

Tell the AI to install the skill config:

docker compose run --rm openclaw-cli skills install <skill-name>


Install the Linux tools needed for that skill (Inside the jail):

docker compose exec -u root openclaw-gateway apt-get install -y <tool-name>


📂 Phase 4: Project Interaction (The "Symlink" Trick)

Because the AI is Isolated, it only sees the folder /home/node/.openclaw/workspace. To let it work on projects without moving them, by create a "Bridge."

How to link a project:

ln -s /home/zen/path/to/your/project ~/.openclaw/workspace/project-name


ln -s: Creates a Symbolic Link. 

Result: The AI "thinks" the project is inside its workspace, but the real files stay safely in your personal folders.

🔐 Phase 5: Security & Verification

Pairing: We used pairing approve telegram <CODE> to "lock" the bot. This means only your Telegram account can issue commands.

Token: Your unique Gateway Token (found in ~/.openclaw/openclaw.json) is the only way to access the local web dashboard.

Localhost: The control panel only runs on 127.0.0.1:18789, meaning no one from the outside internet can reach it.

🗺️ File Map for Reference

Settings: ~/.openclaw (Contains your keys and configuration)

Storage: ~/openclaw/openclaw-db (The AI's long-term memory)

Sandbox: ~/.openclaw/workspace (The only place the AI can touch files)
