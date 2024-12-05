## Release Note

#### v1.2.4
Add: you can input Phase name in mian window now, and the phase name will be added into d-list. This makes it easier to distinguish the d-list results of different phases.

Note: Default phase name is "Alpha-Fe" and needs to be manually inputted, even if importing from CIF. Ignoring phase input will not result in calculation errors, the only result is that the phase name displayed in the d-list is "Alpha Fe".

#### v1.2.3
Bug fix: Crashed while calculating angles (due to incorrect use of math.acos)

#### v1.2.2
Build exe using nuitka.

#### v1.2.1
Remove dependency on numpy, meaning a smaller bin file.

#### v1.2
Init and copy from Gitee