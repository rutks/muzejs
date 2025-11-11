# Muzeja pārdēvēšanas skripts

Šis Python skripts automatizē partijas attēlu failu pārdēvēšanu un pārvietošanu mapē, balstoties uz atbilstībām Excel izklājlapā. Tas ir īpaši noderīgs muzejiem, arhīviem vai bibliotēkām, kam nepieciešams sinhronizēt digitālo failu vārdus ar kataloga datiem.

## Kā tas darbojas

- Sagaida, ka mapē kopā ar skriptu būs Excel fails, kurā ir vismaz viena kolonna ar jaunajiem failu nosaukumiem.
- Izvelk kodus (piemēram, `PK-20`, `ABC_123`) no mērķa failu nosaukumiem, izmantojot noteiktu šablonu.
- Atrod mapē failus, kas atbilst kodam (normalizē no `-` uz `_`) un ar atbalstītu attēlu paplašinājumu (`.jpg`, `.jpeg`, `.tif`, `.tiff`, `.png`).
- Pārvieto un pārdēvē atrastos failus uz jaunu apakšmapi `renamed/`, izmantojot precīzus nosaukumus no Excel kolonnas.
- Sagatavo pārskatu par pārdēvētajiem un atrastajiem/neatrastajiem failiem.

## Lietošanas pamācība

1. **Prasības**  
   Nepieciešams Python 3 un sekojošas bibliotēkas:
   ```sh
   pip install pandas openpyxl
   ```

2. **Sagatavo failus**  
   - Novietojiet šo skriptu tajā pašā mapē ar attēliem un vienu Excel failu.
   - Excel failā jābūt kolonnai ar nosaukumu **`Datnes nosaukums`**, kurā ir vēlamie failu nosaukumi.

3. **Palaidiet skriptu**
   ```sh
   python rename.py
   ```

4. **Rezultāts**  
   - Pārdēvētie faili tiks pārvietoti uz apakšmapi `renamed`.
   - Konsolē tiks parādīts pārdēvēto un neatrasto failu kopsavilkums.

## Konfigurācija

Jūs varat mainīt šīs opcijas `rename.py` sākumā pēc vajadzības:

- **`excel_column`**: Kolonnas nosaukums Excel failā ar mērķa failu nosaukumiem (noklusējums: `Datnes nosaukums`)
- **`search_pattern`**: Kodam meklējamā parauga regex (noklusējums: `[A-Za-z]+[-_]\d+` piemēram, `PK-20`, `ABC_123`)
- **`valid_ext`**: Atbalstīto failu paplašinājumu saraksts

## Piemērs

Pieņemsim, ka Jūsu mapē ir:
- `PK_20.jpg`
- `PK_21.jpg`
- `Renames.xlsx`, kurā kolonnā `Datnes nosaukums` ir:
    - `PK-20-foto1.jpg`
    - `PK-21-foto2.jpg`

Pēc skripta palaišanas:
- Faili tiks pārvietoti un pārdēvēti kā:
    - `renamed/PK-20-foto1.jpg` (bija `PK_20.jpg`)
    - `renamed/PK-21-foto2.jpg` (bija `PK_21.jpg`)

## Piezīmes

- Esošie faili mapē `renamed` tiks pārrakstīti bez brīdinājuma.
- Ja atbilstošs fails nav atrasts, tas tiks atzīmēts kā pazudis.
- Tikai pirmais Excel rindas kodam atbilstošais fails tiks apstrādāts.

## Licence

MIT licence. 

---

*Izstrādāts muzeju attēlu organizācijas darba vienkāršošanai.*
