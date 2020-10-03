### TODO

- [x] Need to use train-test-split
- [x] Remove the wheel-reinventing performance check
- [x] ~~Finally found the nasty bug - some of the records are not long
enough to have 44 frames. they are 41 frames long. should probably
discard those? with threshold=4 it can be seen.~~ Fixed
- [ ] Use ffmpeg, a.k.a. the swiss army knife of media processing,
to cut the raw audio. Find out how to solve the problem of continuous
keyword spotting, w/o having a pre-processed dataset.