# Battle Games in Middle Earth Index

BGIME was a part-works magazine that ran in the early 2000s, which taught you how to play, paint and create scenary for the Games Workshop Lord of the Rings game. After being away from the game for many years I've finally finished my collection of magazines, but with 91 issues (plus three specials) it is quite hard to keep track of where it all is.

This github contains a contents (grouped by category) and index

## Format

The Contents are grouped by:

* Guides (The quite minimal fluff)
* Playing grouped by:
  * Rules
  * Army lists (Stats and special rules for different models)
* battle game grouped by:
  * scenarios
  * campaigns
  * battle reports
* painting models
* modelling terrain

For the playing, painting and modelling, there is a `special_` prefix to put them at the top of the list, these are for special articles which don't quite follow the regular format (e.g. painting is normally a step by step guide for a model, but there's a few special articles for general painting tips, colour pallets etc which are particular useful reference)

## Making your own changes

Tweak the `index.csv` file and then run `python convert_index.py` this will create a new version of `index.md` for the github pages.
