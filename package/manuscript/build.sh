#!/usr/bin/env bash
set -euo pipefail

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
source_md="$script_dir/determinant_lines_character_lattices.md"
bibliography="$script_dir/references.bib"
header="$script_dir/pandoc-header.tex"
output_tex="$script_dir/determinant_lines_character_lattices.tex"
output_pdf="$script_dir/determinant_lines_character_lattices.pdf"

for required in "$source_md" "$bibliography" "$header"; do
  if [[ ! -f "$required" ]]; then
    echo "FAIL missing manuscript input: $required" >&2
    exit 1
  fi
done

pandoc_bin="${PANDOC:-pandoc}"
if ! command -v "$pandoc_bin" >/dev/null 2>&1; then
  echo "FAIL pandoc is unavailable: $pandoc_bin" >&2
  exit 1
fi

xelatex_bin="${XELATEX:-}"
if [[ -z "$xelatex_bin" ]]; then
  if command -v xelatex >/dev/null 2>&1; then
    xelatex_bin="$(command -v xelatex)"
  elif command -v pdflatex >/dev/null 2>&1; then
    tex_bin_dir="$(dirname -- "$(readlink "$(command -v pdflatex)")")"
    xelatex_bin="$tex_bin_dir/xelatex"
  fi
fi
if [[ -z "$xelatex_bin" || ! -x "$xelatex_bin" ]]; then
  echo "FAIL XeLaTeX is unavailable; set XELATEX to its executable" >&2
  exit 1
fi

build_dir="$(mktemp -d "${TMPDIR:-/tmp}/dlcl-manuscript.XXXXXX")"
cleanup() {
  rm -rf -- "$build_dir"
}
trap cleanup EXIT

sed '/^lang: /d' "$source_md" |
  "$pandoc_bin" - \
    --from markdown+tex_math_single_backslash+tex_math_double_backslash+tex_math_dollars \
    --to latex \
    --citeproc \
    --bibliography "$bibliography" \
    --standalone \
    -V documentclass=article \
    -V papersize=a4 \
    -V geometry:margin=1in \
    -V fontsize=11pt \
    -V mainfont='Songti TC' \
    -V mainfontoptions='ItalicFont=Songti TC' \
    -V mainfontoptions='BoldItalicFont=Songti TC Bold' \
    -H "$header" \
    -o "$build_dir/determinant_lines_character_lattices.tex"

for pass in 1 2; do
  "$xelatex_bin" \
    -interaction=nonstopmode \
    -halt-on-error \
    -output-directory="$build_dir" \
    "$build_dir/determinant_lines_character_lattices.tex" \
    >"$build_dir/xelatex-pass-$pass.stdout"
done

log_file="$build_dir/determinant_lines_character_lattices.log"
if grep -E 'Citation .* undefined|There were undefined references|Overfull \\hbox|LaTeX Font Warning' "$log_file" >/dev/null; then
  grep -E 'Citation .* undefined|There were undefined references|Overfull \\hbox|LaTeX Font Warning' "$log_file" >&2
  echo "FAIL manuscript log contains unresolved layout or reference warnings" >&2
  exit 1
fi

cp "$build_dir/determinant_lines_character_lattices.tex" "$output_tex"
cp "$build_dir/determinant_lines_character_lattices.pdf" "$output_pdf"

echo "PASS manuscript built"
echo "tex=$output_tex"
echo "pdf=$output_pdf"
