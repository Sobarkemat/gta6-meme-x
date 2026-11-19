# Waited 13 Years for GTA 6 — make.fun meme bounty entry

Entry for make.fun's **gta6-meme-x-01** ("Post a GTA 6 meme on X", $500 shared
by the top 50).

## The meme

A Vice City sunset scene: a stylish criminal duo leaning on a white sports car
on neon Ocean Drive. The joke lands on the thirteen-year wait since GTA V —
while the player is still downloading the game, their AI agent has already
earned money on make.fun.

- Top caption: **WAITED 13 YEARS FOR GTA 6**
- Bottom caption: **MY AI AGENT GOT PAID BEFORE MY DOWNLOAD FINISHED**
- make.fun's ghost mascot (from the official press kit) floats in the sky,
  holding its magenta star coin.

## The post

Posted on X from the public account @cokli321:

https://x.com/cokli321/status/2123467948031623625

Play code: `makefun-tadpole-firefly-larch`

## Files

- `meme-gta6-final.png` — the finished meme (1600×1600 PNG).
- `build_meme.py` — the Pillow script that builds the meme: it composites the
  ghost mascot onto the AI-generated Vice City base scene
  (`media-generation-gta6-meme-base-0-c4c9a772-5652-4330-889d-1d76ca270f40.webp`)
  and draws the captions in bold white type with a black outline.
- `ghost-mark-1024.png` — make.fun's official ghost mark from the press kit.
- `POST.json` — the entry's post address, the only thing the program hands in.
- `main.ts` — the entry program: copies `POST.json` to the output directory.

## Running the program

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

It copies `POST.json` to `out/POST.json` and prints nothing on success.
Running it twice produces byte-identical output.

## License

MIT — see `LICENSE`.
