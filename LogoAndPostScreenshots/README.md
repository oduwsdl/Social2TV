## Files
| File | Description | 
|------|---------|
| `gold_standard_images_cnn.csv` | CNN Gold Standard - Inclusive|
| `gold_standard_images_foxnews.csv` | Fox News Gold Standard - Inclusive |
| `gold_standard_images_msnbc.csv` | MSNBC Gold Standard - Inclusive |
| `gold_standard_images_foxnews_static.csv` | Fox News Gold Standard - Static-only|

**CNN and MSNBC have no video-post rows in this set, so there is only one gold standard file per channel.** Fox News is the only channel with video-post screenshots, so it has two files: inclusive and static-only.

### Inclusive vs static (Fox)
- **`gold_standard_images_foxnews.csv`** — Fox News Main Gold Standard. Screenshot Yes includes played platform **video** posts (~355 rows where `notes` contains `video`; Screenshot Yes = 538).
- **`gold_standard_images_foxnews_static.csv`** — same rows, but screenshot labels on those video-post rows are set to `No` / blank type (Screenshot Yes = 188). Use for static-screenshot-only evaluation; logo labels are unchanged.
