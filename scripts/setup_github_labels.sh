#!/usr/bin/env bash
# Requires GitHub CLI (gh) installed and authenticated
# Run: chmod +x setup_github_labels.sh && ./setup_github_labels.sh

echo "Setting up OSEF GitHub Labels..."

# Types (Red/Orange/Blue)
gh label create "bug" --color "d73a4a" --description "Something isn't working" --force
gh label create "feature" --color "0366d6" --description "New feature or request" --force
gh label create "enhancement" --color "a2eeef" --description "New feature or request" --force
gh label create "docs" --color "0075ca" --description "Improvements or additions to documentation" --force
gh label create "security" --color "b60205" --description "Security vulnerabilities and improvements" --force
gh label create "testing" --color "fbca04" --description "Test coverage or CI additions" --force
gh label create "architecture" --color "5319e7" --description "Architectural changes and ADRs" --force
gh label create "governance" --color "0052cc" --description "Policy, processes, and community standards" --force

# Priorities (Red -> Yellow)
gh label create "critical" --color "b60205" --description "Highest priority. Drop everything." --force
gh label create "high" --color "d93f0b" --description "High priority. Handle soon." --force
gh label create "medium" --color "fbca04" --description "Normal priority." --force
gh label create "low" --color "fef2c0" --description "Low priority. Whenever possible." --force

# Status (Grey/Green/Yellow)
gh label create "triage" --color "e4e669" --description "Needs assessment from maintainers" --force
gh label create "in progress" --color "cccccc" --description "Actively being worked on" --force
gh label create "blocked" --color "000000" --description "Cannot proceed at this time" --force
gh label create "review" --color "1d76db" --description "Pending review" --force
gh label create "ready to merge" --color "0e8a16" --description "Approved and ready for main" --force

# Area (Purple/Pink)
gh label create "cli" --color "d4c5f9" --description "Command Line Interface" --force
gh label create "sdk" --color "d4c5f9" --description "Python SDK" --force
gh label create "plugin" --color "d4c5f9" --description "Plugin system" --force
gh label create "graph" --color "bfdadc" --description "Engineering Knowledge Graph" --force
gh label create "parser" --color "bfdadc" --description "AST and artifact parsing" --force
gh label create "intelligence" --color "bfdadc" --description "Repository Intelligence" --force

echo "Labels created successfully!"
