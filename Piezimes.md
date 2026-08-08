
# Uzdevums 01 – Repozitorija un uzdevumu izveide.

GitHub repozitorijā atveru sadaļu: **Issues → New issue**.

![alt text](Pielikumi/atteli/attels001.png)

## Izveidoju šādus 4 Issues.

Issue 1: **Izveidot funkciju saskaitit**

![alt text](Pielikumi/atteli/attels002.png)

![alt text](Pielikumi/atteli/attels003.png)

Issue 2: Uzrakstīt unittest testus

![alt text](Pielikumi/atteli/attels004.png)

Issue 3: **Iestatīt GitHub Actions CI**

![alt text](Pielikumi/atteli/attels005.png)

Issue 4: **Atjaunināt README un Definition of Done**

![alt text](Pielikumi/atteli/attels006.png)

## Izveidoju GitHub Project ar Kanban kolonām

Izmantoju GitHub Projects, lai vieglāk parādīt, ka uzdevumi tiek pārvietoti starp statusiem.

GitHub repozitorijā atveru: **Projects → New project**

![alt text](Pielikumi/atteli/attels007.png)

Izvēlējos: **Board**

![alt text](Pielikumi/atteli/attels008.png)

![alt text](Pielikumi/atteli/attels009.png)

## Pievienoju Issues projektam

visus 4 Issues ievietotas kolonnā: **To Do** tas parāda, ka visi darbi vēl nav sākti.

# Sasaistīju lokālo mapi ar GitHub

```powershell
git init
git branch -M main
git remote add origin https://github.com/ArtursSimkuns/PB1_PD18_Simkuns_Arturs.git
```

pievienoju sākotnējo struktūru:
```powershell
New-Item -ItemType Directory -Force -Path ".github\workflows"
New-Item -ItemType File -Force -Path "README.md"
New-Item -ItemType File -Force -Path "kalkulators.py"
New-Item -ItemType File -Force -Path "test_kalkulators.py"
New-Item -ItemType File -Force -Path "ci_refleksija.md"
```

```powershell
git add .
git commit -m "Izveidota sākotnējā projekta struktūra"
git push -u origin main
```

Rezultāts:
Repozitorijā ir redzami vismaz 4 Issues. Projekta Kanban dēlī ir izveidotas kolonnas `To Do`, `In Progress`, `Done`, un uzdevumu statuss tiek mainīts atbilstoši darba progresam.

# Uzdevums 02 – Programmas realizācija

Izveido failu `kalkulators.py` ar funkciju.

## Atjaunoju GitHub Project / Issue statuss
pirms darba sākšanas pārvieto šo Issue uz `In Progress`

![alt text](Pielikumi/atteli/attels010.png)

Izmantoju pilnīgāku variantu, pievienoju docstring un if __name__ == "__main__": pārbaudes daļu. Tas ļauj funkciju importēt testos bez liekas programmas izpildes.
Teorijā bija skaidrots, ka aprēķinu funkcijai jābūt atdalītai no tiešas ievades/izvades, lai to varētu viegli pārbaudīt un importēt citos failos.

## Pārbaudīju, vai programma darbojas

PowerShell terminālī projekta saknē palaidu:
```powershell
python .\kalkulators.py
```

Izvade:
```powershell
Rezultāts: 15
```

Papildu pārbaude, vai funkciju var importēt:
```powershell
python -c "from kalkulators import saskaitit; print(saskaitit(2, 3))"
```

Izvade:
```powershell
5
```

Tā kā abas komandas izpildās bez kļūdām, Uzdevums 02 ir izpildīts.

## Pievienoju izmaiņas Git

```powershell
git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   Pielikumi/atteli/attels010.png
        modified:   Piezimes.md
        modified:   kalkulators.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Piezimes.md
        modified:   kalkulators.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
```

Pievienoju failus Git kontrolei
```powershell
git add . 
git commit -m "Pievienota saskaitisanas funkcija"
git push
```

GitHub Project dēlī Issue **“Izveidot funkciju saskaitit”** pārvietoju uz **Done**.

![alt text](Pielikumi/atteli/attels011.png)

# Uzdevums 03 – Testa izveide

Svarīgi: testa faila nosaukumam jāsākas ar `test_`, jo tad `unittest discover` un vēlāk arī CI to automātiski atradīs.

GitHub Project / Issue statuss: pirms darba sākšanas pārvietoju šo Issue:
![alt text](Pielikumi/atteli/attels012.png)

Failā `test_kalkulators.py` uzrakstīju pārbaudes kodu.

Šis tests importē funkciju no `kalkulators.py` un pārbauda, vai tā dažādos gadījumos atgriež pareizu summu. Teorijā par Python struktūru skaidrots, ka funkciju atdalīšana atsevišķā modulī ļauj šo funkciju importēt un pārbaudīt citos failos.

## Pārbaudīju testu lokāli

```powershell
python -m unittest discover
```

divos veidos:
```powershell
python test_kalkulators.py
```

```powershell
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

Tests ir izpildīts veiksmīgi. Lokāli testi iziet bez kļūdām, un terminālī redzams rezultāts `OK`.

## Pievienoju izmaiņas Git

```powershell
git status
git add .
git commit -m "Pievienota funkcija un unittest testi"
git push
```

Issue **“Uzrakstīt unittest testus”** pārvietoju uz **Done**, jo tests lokāli izpildās ar `OK`.

![alt text](Pielikumi/atteli/attels013.png)

---
---

# Uzdevums 04 – CI konfigurēšana

Uzdevuma prasība: jāizveido GitHub Actions konfigurācijas fails `.github/workflows/main.yml`, kas aktivizējas pēc `push`, iestata Python vidi un palaiž testus ar komandu `python -m unittest discover`. Pēc `git push` GitHub Actions sadaļā jābūt redzamam CI izpildes procesam, un korekta testa gadījumā CI statusam jābūt zaļam.

Pirms darba sākšanas pārvietoju Issue Github Projects:

![alt text](Pielikumi/atteli/attels014.png)

Izveidoju failu: `.github/workflows/main.yml` un ievietoju konfigurāciju.

Komandas `on: [push]` nozīmē, ka CI sāk darboties pēc katra `git push`, `actions/checkout` ielādē projekta kodu, bet `python -m unittest` palaiž testus.

## Pārbaudu testus lokāli pirms `push` uz GitHub

```powershell
python -m unittest discover
```

```powershell
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

Tests iziets lokāli. Ja lokāli tests neiziet, GitHub Actions arī būs sarkans.

## Pievienoju izmaiņas Git un nosūtu uz GitHub

```powershell
git status
