#!/bin/sed -rf

s/\\documentclass\[11pt\]\{article\}/\\documentclass{scrartcl}/
s/\\OriginalVerbatim\[#1\,codes/\\OriginalVerbatim[#1,fontsize=\\small,codes/
/\\begin\{center\}\\rule\{0\.5\\linewidth\}\{0\.5pt\}\\end\{center}/d

# Remove incompatible option
s/\\usepackage\[utf8x\]\{inputenc\}/\\usepackage[utf8]{inputenc}/

# Delete titling package, messes with KOMA title page
/\\usepackage\{titling\}/d

# Make code box background somewhat lighted
s/\\definecolor\{cellbackground\}\{HTML\}\{[A-F0-9]+\}/\\definecolor{cellbackground}{HTML}{FCFCFC}/

# Deal with parskip using KOMA settings
/\\usepackage\{parskip\}/d

# Remove white space after figures
/\{ \\hspace\*\{\\fill\} \\\\\}/d

# Replace paragraphs with subsubsections
s/\\paragraph\{/\\subsubsection*{/

# Replace subparagraphs with paragraphs
s/\\subparagraph/\\paragraph/

# Add extra indent before examples
s/^[[:space:]]*\\([a-z]+)\{(Examples?):/\\vspace{1em}\\\1{\2:/

# Fix bold math for Greek letters
s/\\mathbf\{\\beta\}/\\bm\\beta/g
s/\\mathbf\{\\gamma\}/\\bm\\gamma/g
s/\\mathbf\{\\Sigma\}/\\bm\\Sigma/g

s/i\.e\.,?~/\\ie /g
s/i\.e\.,?/\\ie/g
s/e\.g\.,?~/\\eg /g
s/e\.g\.,?/\\eg/g
s/\.svg\b/.pdf/g
s/etc\.(,?)/\\etc\1/g
