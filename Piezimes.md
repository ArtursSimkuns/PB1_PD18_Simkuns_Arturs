
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
git add .
git commit -m "Pievienota GitHub Actions CI konfiguracija"
git push
```

## Pārbaudu GitHub Actions rezultātu

GitHub repozitorijā atveru: **Actions**

Redzams workflow ar nosaukumu: **Python CI pārbaude**

![alt text](Pielikumi/atteli/attels015.png)

Redzams zaļš statuss, tas nozīmē, ka viss ir pareizi.

![alt text](Pielikumi/atteli/attels016.png)

Pēc `git push` GitHub sadaļā Actions parādījās CI izpildes process. Tā kā testi bija korekti, CI statuss kļuva zaļš.

![alt text](Pielikumi/atteli/attels017.png)

---
---

## Uzdevums 05 – CI eksperiments

Uzdevuma mērķis ir apzināti izraisīt kļūdu testā, nosūtīt kļūdaino versiju uz GitHub, redzēt sarkanu CI statusu, pēc tam kļūdu salabot un panākt zaļu CI statusu.

Atveru failu `test_kalkulators.py`, atrodu vienu pareizu testu, apzināti nomainu pareizo sagaidāmo vērtību 5 uz nepareizu vērtību 6:

```python
    def test_saskaitit_pozitivus_skaitlus(self):
        """Pārbauda pozitīvu skaitļu saskaitīšanu."""
        self.assertEqual(saskaitit(2, 3), 6)
```

Šajā brīdī funkcija `saskaitit(2, 3)` joprojām atgriež 5, bet tests kļūdaini sagaida 6.

## Pārbaudu kļūdu lokāli

```powershell
python -m unittest discover
```

```powershell
..F
======================================================================
FAIL: test_saskaitit_pozitivus_skaitlus (test_kalkulators.TestKalkulators.test_saskaitit_pozitivus_skaitlus)
Pārbauda pozitīvu skaitļu saskaitīšanu.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\robo\Documents\BUTS\Praktiskie_darbi\05 Programmas koda rakstīšana (Kodēšana)\PB1_PD18 CI pamati un uzdevumu pārvaldība\PB1_PD18_Simkuns_Arturs\test_kalkulators.py", line 13, in test_saskaitit_pozitivus_skaitlus
    self.assertEqual(saskaitit(2, 3), 6)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
AssertionError: 5 != 6

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```

## Veicu commit un push ar kļūdaino testu
Lai GitHub Actions arī parādītu sarkanu CI statusu, kļūdainais tests jānosūta uz GitHub:

```powershell
git status
git add .
git commit -m "Apzinati sabojats tests CI eksperimentam"
git push
```

Pēc `git push` GitHub repozitorijā atveru: **Actions**

![alt text](Pielikumi/atteli/attels018.png)

Tur redzu, ka workflow izpilde ir sarkana.

![alt text](Pielikumi/atteli/attels019.png)

Tas ir salūzis CI pipeline: ja CI ir sarkans, uzdevums nav pabeigts un kļūda jālabo pirms turpināt darbu.

## Salaboju testu

Atveru `test_kalkulators.py` un nomaini nepareizo vērtību atpakaļ uz pareizo.

## Veicu commit un push ar salaboto testu

```powershell
git status
git add .
git commit -m "Salabots tests pec CI eksperimenta"
git push
```

Vēlreiz atveru GitHub: **Actions**

![alt text](Pielikumi/atteli/attels020.png)

Jaunā CI izpilde zaļa.

## Ko novēroju GitHub Actions sadaļā

Divas CI izpildes:

| CI izpilde          | Sagaidāmais statuss | Nozīme                       |
| ------------------- | ------------------- | ---------------------------- |
| Pēc sabojāta testa  | Sarkans             | CI atrada kļūdu testā        |
| Pēc testa labošanas | Zaļš                | Tests atkal iziet bez kļūdām |

Tas parāda automatizētas pārbaudes jēgu: pēc katra `git push` GitHub Actions automātiski pārbauda kodu un uzreiz parāda, vai izmaiņas ir drošas.
Teorijā CI aprakstīts kā cikls: raksti kodu, veic `commit`, veic `push`, CI palaiž testus, kļūdas gadījumā labo un atkārto procesu.

Pēc apzināti sabojāta testa GitHub Actions sadaļā bija redzams sarkans CI statuss. Pēc testa labošanas un atkārtota `push` CI statuss kļuva zaļš. Eksperiments parādīja, ka CI palīdz ātri pamanīt kļūdas pēc koda nosūtīšanas uz GitHub.

---
---

# Uzdevums 06 – Definition of Done un refleksija

`README.md` atjaunots saturs.

README sadaļā nevajag rakstīt garu atskaiti. README jābūt īsam projekta lietošanas aprakstam: kas tas ir, kā palaist programmu, kā palaist testus un kāds ir DoD.


Pievienoju izmaiņas Git un nosūtu uz GitHub.

GitHub sadaļā: **Actions** pārbaudīju, vai jaunā CI izpilde ir zaļa.

![alt text](Pielikumi/atteli/attels021.png)


Pēc šī soļa Issue **“Atjaunināt README un Definition of Done”** pārvietoju uz **Done**, jo GitHub Actions statuss ir zaļš.