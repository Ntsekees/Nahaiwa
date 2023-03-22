
import re

def proceed():
  with open("../description", "r", encoding = "utf-8") as tf:
    with open("../description-md.md", "w", encoding='utf-8') as mdf:
      mdf.write(as_md(tf.read()))

def as_md(s):
  s = re.sub("═+", "---", s)
  s = s.replace("\n§§§§", "\n####")
  s = s.replace("\n§§§", "\n###")
  s = s.replace("\n§§", "\n##")
  s = s.replace("\n§", "\n#")
  s = re.sub("\n( *)┌", "\n```\n\\1┌", s)
  s = s.replace("┘\n", "┘\n```\n")
  s = s.replace("└─\n", "└─\n```\n")
  s = s.replace("\n", "  \n")
  return s

proceed()


