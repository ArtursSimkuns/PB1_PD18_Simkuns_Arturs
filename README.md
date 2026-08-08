# PB1_PD18 - Kalkulators ar CI

Šis projekts demonstrē vienkāršu Python kalkulatora funkciju, automātisku testēšanu ar `unittest` un GitHub Actions CI izmantošanu.

## Projekta faili

- `kalkulators.py` - satur funkciju `saskaitit(a, b)`;
- `test_kalkulators.py` - satur funkcijas testus;
- `.github/workflows/main.yml` - GitHub Actions CI konfigurācija;
- `ci_refleksija.md` - refleksija par CI eksperimentu.

## Kā palaist programmu lokāli

Terminālī projekta saknē izpilda komandu:

```bash
python kalkulators.py
```

## Kā palaist testus lokāli

Terminālī projekta saknē izpilda komandu:

```bash
python -m unittest discover
```

Ja testi ir korekti, terminālī redzams rezultāts `OK`.

## CI process

Pēc katra `git push` GitHub Actions automātiski palaiž testus ar komandu:

```bash
python -m unittest discover
```

Ja tests ir veiksmīgs, GitHub Actions statuss ir zaļš. Ja tests kļūdās, CI statuss kļūst sarkans.

## Definition of Done

Uzdevums ir pabeigts, ja:

- funkcija darbojas;
- tests iziet;
- CI ir zaļš;
- Issue pārvietots uz `Done`.