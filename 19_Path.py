from pathlib import Path

guia = Path(Path.home(),"Europa")


for txt in Path(guia).glob("**/*.txt"):
    print(txt)