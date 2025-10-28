# Outreach Message Templates

This directory contains templates for reaching out to developers affected by gatekeeping in the upstream repository.

## Automated Notification System

The repository now includes an **automated notification system** that posts issues directly to developer repositories.

### How It Works

1. **Notification Generation**: The `send_notifications.py` script generates notification message files in `generated_notifications/`
2. **Automated Posting**: The `post_notifications.py` script creates **NEW ISSUES** in each developer's repository
3. **Workflow Integration**: The `gatekeeping-automation.yml` workflow automatically runs both scripts when gatekept tools are added

### Manual Triggering

You can manually trigger notifications using the GitHub Actions workflow:

1. Go to Actions → "Post Gatekeeping Notifications to Developer Repos"
2. Click "Run workflow"
3. Choose dry run mode (for testing) or live mode
4. Review the results in the workflow logs

### Key Design Decisions

- **Issues, not comments**: Notifications are posted as NEW ISSUES in developer repositories (e.g., `schlunsen/claude-control-terminal/issues`)
- **Not spam to upstream**: We don't post comments on upstream repository issues to avoid over-notifying hesreallyhim
- **Duplicate prevention**: The script checks for existing notification issues before posting
- **Graceful failures**: If a repo has issues disabled or is private, the script continues with other repos

## Template Usage

1. **Personalize each message** - Use the developer's name and tool name
2. **Include issue number** - Reference their original submission
3. **Be respectful** - No bashing of upstream maintainer
4. **Be clear** - Explain the auto-approval system
5. **Be welcoming** - Make them feel valued

---

## Priority Contact List

See [GATEKEEPING_ANALYSIS.md](../GATEKEEPING_ANALYSIS.md) for full details.

### Critical Priority (5 developers)

1. **@schlunsen** - #228 Claude Control Terminal (locked, pay-to-play concerns)
2. **@jfpedroza** - #122 claude-code-guardian (74+ days waiting)
3. **@Atipico1** - #148 Claudable (62+ days, assigned but not approved)
4. **@cheolwanpark** - #169 Claude Agent Toolkit (46+ days)
5. **@ishaansehgal99** - #183 Omnara (41+ days)

### High Priority - Rejected (7 developers)

6. **@2mawi2** - #205 Schaltwerk
7. **@shinpr** - #175 Sub agents Starter Kit, #104 ai-coding-project-boilerplate
8. **@vaderyang** - #166 Claude Code Web Shell
9. **@aeulker** - #165 Claude Code Cheat Sheet
10. **@bartolli** - #108 Codanna

### Medium Priority - Waiting (9+ developers)

11. **@ankushdixit** - #233 Session Driven Development (11+ days)
12. **@NikiforovAll** - #238 Claude Code Handbook (9+ days)
13. **@kunwar-shah** - #242 Claude X (6+ days)
14. **@alexander-zuev** - #243 conduit8 (6+ days)
15. **@alonw0** - #244 Web Assets Generator (6+ days)
16. **@jamesrochabrun** - #252 Claw Code (4+ days)
17. **@4xian** - #253 Claude Codex Api (3+ days)
18. **@tomohiro-owada** - #259 DevRag (2+ days)
19. **@PepijnSenders** - #264 Pretty Printer (2+ days)

---

## Available Templates

- [template-rejected.md](./template-rejected.md) - For developers whose validated tools were rejected
- [template-waiting.md](./template-waiting.md) - For developers whose tools are still waiting
- [template-locked-thread.md](./template-locked-thread.md) - Special template for #228 (locked thread)

---

## Outreach Strategy

### Phase 1: Critical Contact (Week 1)
Contact developers #1-5 (most egregious cases)

### Phase 2: High Priority (Week 2)
Contact developers #6-10 (rejected tools)

### Phase 3: Medium Priority (Week 3)
Contact developers #11-19 (waiting tools)

### Timing
- Send messages 1-2 days apart
- Don't overwhelm the community
- Allow time for response before next batch

---

## Communication Channels

### Automated: GitHub Issues in Developer Repos
The notification system automatically creates issues in each developer's repository with:
- Personalized notification about their tool being featured
- Links to the fork and analysis
- Explanation of the community-driven approach

### Manual Alternative: GitHub Issue Comments
If automated posting fails or for special cases, can post a comment on their original issue in the upstream repository

### Do NOT:
- Send unsolicited direct messages
- Spam multiple channels
- Make promises we can't keep
- Over-notify the upstream repository maintainer

---

## Tracking

Keep track of outreach in a spreadsheet or issue:
- [ ] Developer contacted
- [ ] Developer responded
- [ ] Developer resubmitted
- [ ] Submission auto-approved

---

*Last Updated: October 28, 2025*
