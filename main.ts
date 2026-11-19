// gta6-meme-x-01 entry program.
//
// The house judges the X post named in POST.json, so this program's only job
// is to hand that file over: it copies POST.json from the repository
// directory into the output directory, byte for byte. It stays silent on
// success and fails loudly (non-zero exit) on any error, so a broken entry
// is never mistaken for a valid one.
//
// Environment:
//   MAKEFUN_BOT_DIR     repository directory (default: /bot)
//   MAKEFUN_OUTPUT_DIR  output directory (default: /output)
import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

// The entry names exactly one X post; refuse anything else so a typo in
// POST.json fails the run instead of submitting a dead entry.
const POST_URL_PATTERN =
  /^https:\/\/(www\.|mobile\.)?(x\.com|twitter\.com)\/[^/]+\/status\/\d+$/;

const repoDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const sourcePath = join(repoDir, "POST.json");
const targetPath = join(outputDir, "POST.json");

const entry = JSON.parse(readFileSync(sourcePath, "utf8"));
if (
  typeof entry !== "object" ||
  entry === null ||
  typeof entry.url !== "string" ||
  !POST_URL_PATTERN.test(entry.url)
) {
  throw new Error(`POST.json does not name a valid X post URL: ${sourcePath}`);
}

mkdirSync(outputDir, { recursive: true });
copyFileSync(sourcePath, targetPath);
