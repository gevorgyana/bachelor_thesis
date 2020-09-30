### TODO

- [x] Need to use train-test-split
- [x] Remove the wheel-reinventing performance check
- [ ] Finally found the nasty bug - some of the records are not long
enough to have 44 frames. they are 41 frames long. should probably
discard those? with threshold=4 it can be seen.