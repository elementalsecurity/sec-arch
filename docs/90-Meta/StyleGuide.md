# Style Guide

This document defines conventions for writing, formatting, and naming within this repository.

## File and Folder Naming
- Use **CamelCase** for folder and file names (e.g., `ZeroTrust`, `IdentityBroker.md`).
- Avoid spaces and special characters, only letters, numbers, and hyphens within Markdown files.

## Markdown Formatting
- Use `#`, `##`, `###` for headings.  
- Use hyphens (`-`) for lists and horizontal rules (`---`).  
- Avoid long em dashes; use simple hyphens or en dashes when needed.

## Code Blocks
- Fenced code blocks with triple backticks and language identifier.
- For Mermaid diagrams, use `````mermaid` at the start and end.

## Diagrams
- Use Mermaid C4-lite notation.  
- Always include `%%{init: {'theme': 'default'}}%%` at top for consistency.

## Tables
- Align columns with pipes (`|`).  
- Use header row with dashes under each column header.

## Commit Messages
- Use imperative tense, short summary (50 characters max), optional body.  
- Example: `Add AzureLandingZoneBicep implementation guide`

## Pull Requests
- Title should follow commit message style.
- Description must include motivation and summary of changes.
- Link to issue or roadmap phase if applicable.

## CI and Testing
- Ensure Markdown lint and docs build pass before merging.
- For IaC examples, include CI checks for Bicep/CDK/YAML syntax.

