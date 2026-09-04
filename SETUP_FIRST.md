# You go first — push this to `main` before anyone else starts

This is the shared skeleton: config files everyone needs (`package.json`,
`requirements.txt`, `.gitignore`, etc.) plus two small **stub** files
(`backend/app/seed_data.py` and `frontend/src/pages/About.jsx`) that let
the Backend Dev's and UI Dev's branches build standalone before the Design
Lead's real content is merged in.

## Steps

1. Create the empty GitHub repo (no README/gitignore/license — you likely
   already did this).
2. Extract this zip's contents directly into a fresh local folder — the
   folder itself becomes your repo root (don't nest it inside another
   folder).
3. Open a terminal in that folder and run:

```bash
git init
git branch -M main
git add .
git commit -m "Project skeleton: config, gitignore, env templates, stub files"
git remote add origin <REPO_URL>
git push -u origin main
```

Replace `<REPO_URL>` with the URL GitHub gave you, e.g.
`https://github.com/<username>/dengueshield-lk.git`.

4. Tell your three teammates the repo is live — they can now clone it and
   start on their own branches (see the `SETUP.md` in each of their zips).

## After everyone has pushed their branch

Come back to me (Claude) once all four branches
(`backend-dev`, `design-lead`, `ui-dev`, `deploy-lead`) are pushed and I'll
walk you through merging them into `main` cleanly — the split was designed
so none of the branches touch the same file, so it should be a clean,
conflict-free merge.
