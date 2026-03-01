# 🛡️ Permissions Setup Guide

## Core Adjustments

### Ownership Fix
- Adjusted ownership to the current user:
  ```bash
  sudo chown -R $USER:$USER ~/.openclaw/workspace
  ```
  This prevents permission issues during workspace actions.

### Symlink Bridge Setup
- Linked Gmail automation bot for ease of access:
  ```bash
  ln -s /home/zen/projects/gmail-bot ~/.openclaw/workspace/Gmail-Automation-Bot
  ```

## Secure Secrets Handling

### Docker Key Injection
- Secrets securely added and environment refreshed:
  ```bash
  docker compose up -d
  ```
  This ensures `.env` variables and Docker keys are correctly injected.

### GitHub CLI Configuration
- Set up GitHub CLI for secure command-line operations. Installed tools include:
  - `gh`
  - `jq`

### Himalaya Integration
- Configured Himalaya for parsing email tasks, including Gmail App Password setup for automation workflows.

Ensure these steps are followed to maintain a seamless and secure OpenClaw environment.