# Issue tracker: GitHub

Repository: `naufalahmadfauz/cognigy-grab`.

Issues and specs live in GitHub Issues. Use the `gh` CLI from this repo.

Before the first tracker write each session, run `gh repo view --json nameWithOwner` and check that it matches the repository above. If it resolves elsewhere, explicitly target this repository with `--repo`.

## Conventions

- Create: `gh issue create --title "..." --body-file <path>`. Use `--body "..."` for short bodies.
- Read: `gh issue view <number> --json number,title,body,labels,comments`.
- List: `gh issue list --state open --json number,title,body,labels,comments`. Adjust `--state`, `--label`, and `--limit` for the query.
- Edit the body: `gh issue edit <number> --body-file <path>`.
- Comment: `gh issue comment <number> --body "..."`, or use `--body-file <path>`.
- Apply/remove labels: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`. Read `triage-labels.md` for the role mapping.
- Close: post the explanation with `gh issue comment`, then run `gh issue close <number>`. Post explanations separately even when the issue is already closed.

## Parent issues and blockers

- Create a sub-issue with `gh issue create --parent <parent> ...`, or link an existing child with `gh issue edit <parent> --add-sub-issue <child>`.
- Record native dependencies with `gh issue create --blocked-by <number>,<number> ...` or `gh issue edit <child> --add-blocked-by <blocker>`.
- Inspect blockers with `gh issue view <number> --json blockedBy`. A ticket is unblocked when every blocker is closed; closed blockers do not prevent starting.
- If native sub-issues are unavailable, put `Part of #<parent>` at the top of each child and link children in a task list in the parent.
- If native dependencies are unavailable, use `Blocked by: #<number>, #<number>` at the top of the issue body.

## Pull requests as a triage surface

**PRs as a request surface: no.**

## Skill operations

- "Publish to the issue tracker": create a GitHub issue.
- "Fetch the relevant ticket": read the referenced issue with its labels and comments.

## Wayfinding operations

Used by `/wayfinder`. The map is one issue with child issues as tickets.

- Map: an issue labelled `wayfinder:map`, holding Notes / Decisions-so-far / Fog.
- Child: a sub-issue of the map, labelled `wayfinder:<type>` where type is `research`, `prototype`, `grilling`, or `task`. Use the parent-link fallback above when needed.
- Blocking: use the dependency conventions above.
- Frontier: inspect the map's open children, exclude those with open blockers or an assignee, and choose the first eligible ticket in map order.
- Claim: `gh issue edit <number> --add-assignee "@me"` before beginning work.
- Resolve: comment with the answer, close the child, then append a context pointer (gist + link) to the map's Decisions-so-far.
