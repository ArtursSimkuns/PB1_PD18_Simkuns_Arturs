
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




