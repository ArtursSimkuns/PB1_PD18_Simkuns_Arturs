# CI refleksija

## 1. Kas notika, kad tests bija kļūdains?

Kad testā apzināti nomainīju pareizo sagaidāmo vērtību uz nepareizu, lokālā testu palaišana parādīja kļūdu. Pēc `git push` arī GitHub Actions sadaļā CI statuss kļuva sarkans. Tas parādīja, ka automatizētā pārbaude atrod kļūdu arī tad, ja kods jau ir nosūtīts uz GitHub.

## 2. Kāpēc CI palīdz ātri pamanīt kļūdas?

CI palīdz ātri pamanīt kļūdas, jo testi tiek palaisti automātiski pēc katra `git push`. Nav jāatceras manuāli pārbaudīt katru izmaiņu. Ja kāds tests neiziet, GitHub Actions uzreiz parāda kļūdu un neļauj uzskatīt darbu par pilnībā pabeigtu.

## 3. Kā DoD palīdz komandai?

Definition of Done palīdz komandai vienoties, kad uzdevumu drīkst uzskatīt par pabeigtu. Tas samazina pārpratumus, jo nepietiek tikai uzrakstīt kodu. Uzdevums ir pabeigts tikai tad, ja funkcija darbojas, tests iziet, CI ir zaļš un Issue ir pārvietots uz `Done`.

## 4. Kā mainījās tava attieksme pret `git push`?

Pēc CI eksperimenta `git push` vairs neuztveru tikai kā koda nosūtīšanu uz GitHub. Tas ir arī pārbaudes sākšanas brīdis. Pēc `push` ir jāpaskatās GitHub Actions statuss, jo tikai zaļš CI apliecina, ka pēdējās izmaiņas ir pārbaudītas.