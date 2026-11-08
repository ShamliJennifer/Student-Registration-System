# Test cases and expected behaviour

| Test | Input / action | Expected result |
|---|---|---|
| Valid record | Name, valid 10-digit phone, valid email | Record accepted |
| Empty name | Blank name | Rejected |
| Short phone | Fewer than 10 digits | Rejected |
| Invalid phone prefix | Phone starts outside 6–9 | Rejected |
| Invalid email | Missing domain dot or multiple @ symbols | Rejected |
| Duplicate phone | Register a phone already in the list | Rejected |
| Duplicate email | Register an email already in the list | Rejected |
| Search | Search by part of a name or email | Matching record displayed |
| Update | Supply an existing phone and valid new details | Record updated |
| Delete | Supply an existing phone | Record removed |
| Save | Choose Save and exit | Current records written to students_clean.csv |

Run automated validation tests from the project root:

```bash
python3 -m unittest discover -s tests -v
```

These are documented test cases; capture your own terminal screenshots after running the program if your coursework requires execution evidence.
