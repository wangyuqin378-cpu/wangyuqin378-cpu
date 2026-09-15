# Profile design

## Direction

**Small apps. Real life.** The profile connects Yuqin's two strands of work: noticing more of daily life, and building tools that make AI work easier to continue.

The signature is one drawn line joining a photo observation, a folded city map and a saved-task bookmark. These motifs come from Jianwei, City Copy and Context Continuity. They are illustrations, not simulated product screenshots. Real app previews stay adjacent to the project they describe.

- Palette: blue paper `#E6EFF4`, ink `#17384A`, coral `#C44832`, peach `#F3CFB9`, sage `#C7DCD2`, sky `#B6CEE5`.
- Typography: Avenir Next with familiar sans-serif fallbacks for the maker name and labels; Georgia italic for the short personal headline; GitHub's native typography for all explanatory copy.
- Layout: compact identity image → native introduction/navigation → paired product previews → continuity workflow → compact experiments → live updates.
- Dark mode uses separate SVG colors selected by `<picture>`. The image is a small part of the page; descriptions, status, links and updates remain selectable native text.

## References reviewed on 2026-09-16

- [oil-oil](https://github.com/oil-oil): a direct personal introduction and product destinations. The account overview is simple; its personality also comes from the avatar and project pages.
- [beautify-github-readme](https://github.com/oil-oil/beautify-github-readme): a project-specific visual opening paired with readable Markdown. The useful principle is to derive visuals from what the project does.
- [Wolfcha](https://github.com/oil-oil/wolfcha): product atmosphere and a clear first action precede technical setup.
- [Anthony Fu](https://github.com/antfu): compact navigation; [Simon Willison](https://github.com/simonw): genuine recent work with source links.

The artwork and copy here are original. Reference artwork, characters and logos are not reused. An initial generic cream-paper direction was discarded in favor of blue observation notes and motifs tied to the actual three featured projects.

## Editing

Run `python3 scripts/design_assets.py` to regenerate the six self-contained SVGs. The workflow has a vertical variant below 600px so its labels remain readable. There are no external fonts, scripts, embedded images or tracking requests in them. Keep the matching native text and alternative text accurate when changing the art. Product screenshots retain their original bytes; see [asset provenance](assets/README.md).

Keep the update marker pairs in both READMEs intact. Weekly automation owns only the content between those markers.
